import re
import sqlalchemy
from sqlalchemy.sql import text
import pandas as pd
import numpy as np
from functools import reduce
from PySide6.QtCore import QDate


def make_sorter(l):
    """
    Create a dict from the list to map to 0..len(l)
    Returns a mapper to map a series to this custom sort order
    """
    sort_order = {k: v for k, v in zip(l, range(len(l)))}
    return lambda s: s.map(lambda x: sort_order[x])


def aggreagator(x, y):
    if x == y:
        return x
    if x != y:
        if np.nan in [x]:
            return y
        if np.NaN in [y]:
            return x
        return x


def reducder(series):
    return reduce(aggreagator, series)


lab_dict = {
    981: "CBC-Hb",
    983: "CBC-Hct",
    985: "CBC-MCV",
    967: "CBC-WBCCount",
    995: "CBC-PlateletCount",
    977: "CBC-Basophils",
    975: "CBC-Eosinophils",
    971: "CBC-Lymphocytes",
    973: "CBC-Monocytes",
    969: "CBC-Neutrophils",
    1035: "CBC-RBCMorphology",
    1139: "UA-Color",
    1145: "UA-Sp.gr",
    1156: "UA-Glucose",
    1576: "UA-Protein",
    1152: "UA-Ph",
    1176: "UA-WBC",
    1172: "UA-RBC",
    1198: "UA-Sq.Epi",
    540: "Sugar-FBS",
    559: "Sugar-HbA1C",
    566: "Lipid-TC",
    568: "Lipid-HDL",
    1135: "Lipid-LDL",
    879: "Lipid-LDL",
    567: "Lipid-TG",
    538: "Kidney-BUN",
    539: "Kidney-Cr",
    1547: "Kidney-GFR",
    542: "Kidney-UricAcid",
    555: "Liver-SGOT",
    556: "Liver-SGPT",
    554: "Liver-ALP",
    # "":"Stool-RectalSwab",
    1357: "Stool-Parasite",
    1347: "Stool-WBC",
    1342: "Stool-RBC",
    # "":"Stool-OccultBlood",
}


class Fetcher:
    def __init__(self, username: str, password: str, address: str, port: str, database_name: str) -> None:
        url = f"mysql+mysqlconnector://{username}:{password}@{address}:{port}/{database_name}"
        self.engine = sqlalchemy.create_engine(url)
        self.has_gotten_key = False

    def getkey(self):
        smoking_query = '''
            SELECT smoking_type_name,smoking_type_id FROM smoking_type
        '''
        self.smoking_df = self.call_database(smoking_query)
        drinking_query = '''
            SELECT drinking_type_name,drinking_type_id FROM drinking_type
        '''
        self.drinking_df = self.call_database(drinking_query)

    def change_template(self, path):
        self.template = pd.read_excel(path)

    def call_database(self, sql):
        with self.engine.connect().execution_options(autocommit=False) as conn:
            query = conn.execute(text(sql))
            df = pd.DataFrame(query.fetchall())
            return df

    def main(self, cc: str, start_date: str, end_date: str | None = None):
        if not self.has_gotten_key:
            self.getkey()
            self.has_gotten_key = True
        end_date_query = f'AND OPD.vstdate <= "{end_date}"' if end_date is not None else ""
        main_query = f'''
            SELECT PT.pname,PT.fname,PT.lname,PT.sex,OPD.hn,PT.cid,PT.birthday,OPD.vn,OPD.vstdate,OPDILL.cc_persist_disease,OPD.smoking_type_id,OPD.drinking_type_id,OPD.bw,OPD.height,OPD.waist,OPD.bps,OPD.bpd,OPD.pulse,OPD.rr,XR.report_text,OPD.cc FROM opdscreen OPD
                INNER JOIN patient PT ON PT.hn = OPD.hn
                LEFT JOIN xray_report XR ON XR.vn = OPD.vn
                LEFT JOIN opd_ill_history OPDILL ON OPDILL.hn = OPD.hn
                WHERE OPD.vstdate >= "{start_date}" {end_date_query} AND OPD.cc LIKE "%{cc}%"
        '''
        main_df = self.call_database(main_query)

        need_to_check_xray_again_hn = main_df[pd.isna(
            main_df["report_text"])]["hn"].unique()
        if len(need_to_check_xray_again_hn) > 0:
            joined_xray_again_hn = ','.join(need_to_check_xray_again_hn)
            xray_again_query = f'''
                    SELECT OPD.hn,XR.report_text FROM opdscreen OPD
                    LEFT JOIN xray_report XR ON XR.vn = OPD.vn
                    WHERE OPD.hn IN ({joined_xray_again_hn}) AND OPD.vstdate >= "{start_date}" AND (XR.report_text LIKE "%CXR%" OR XR.report_text LIKE "%CHEST%")
            '''
            xray_again_df = self.call_database(xray_again_query)
            if not xray_again_df.empty:
                xray_again_df = xray_again_df.groupby(
                    'hn', as_index=False).agg(reducder)
                cat = pd.concat([main_df, xray_again_df], axis="index")
                main_df = cat.groupby(
                    'hn', as_index=False).agg(reducder)

        joined_hn = ','.join(main_df["hn"].unique())
        joined_vn = ','.join(main_df["vn"].unique())
        lab_query = f'''
            SELECT OPD.vn,LO.lab_items_code,LO.lab_items_name_ref,LO.lab_order_result FROM opdscreen OPD
                LEFT JOIN lab_head LH ON LH.vn = OPD.vn
                INNER JOIN lab_order LO ON LO.lab_order_number = LH.lab_order_number
                WHERE OPD.vn IN ({joined_vn}) AND LO.lab_order_result IS NOT NULL
        '''
        lab_df = self.call_database(lab_query)
        allergy_query = f'''
            SELECT hn, group_concat(agent SEPARATOR "; ") as agent FROM opd_allergy
                WHERE hn IN ({joined_hn})
                GROUP BY hn
        '''
        allergy_df = self.call_database(allergy_query)

        lab_df = lab_df.drop(lab_df[lab_df["lab_items_code"].apply(lambda c: c not in lab_dict.keys())].index, axis="rows") \
            .sort_values(by=["lab_items_code"], key=make_sorter(list(lab_dict.keys()))) \
            .replace({"lab_items_code": lab_dict})

        lab_df['lab_items_code'] = pd.Categorical(
            lab_df['lab_items_code'], ordered=True, categories=lab_df['lab_items_code'].unique())

        lab_df = lab_df.drop_duplicates(subset=["vn", "lab_items_code"]).pivot(
            index="vn", columns="lab_items_code", values="lab_order_result")

        main_df = main_df \
            .merge(self.smoking_df, on="smoking_type_id", how="left") \
            .merge(self.drinking_df, on="drinking_type_id", how="left") \
            .drop(columns=["smoking_type_id", "drinking_type_id"])
        if not allergy_df.empty:
            main_df = main_df.merge(allergy_df, on="hn", how="left")
        else:
            main_df["agent"] = np.nan
        if not lab_df.empty:
            main_df = main_df.merge(lab_df, on="vn", how="left")

        main_df = main_df.groupby('hn', as_index=False).agg(reducder)

        main_df.rename(columns={
            "pname": "Title",
            "fname": "Name",
            "lname": "Surname",
            "sex": "Gender",
            "hn": "HospitalNumber",
            "cid": "CitizenId",
            "birthday": "BirthDate",
            "vn": "VisitNumber",
            "vstdate": "VisitDate",
            "cc_persist_disease": "HX-UnderlyingDisease",
            "smoking_type_name": "HX-Smoking",
            "drinking_type_name": "HX-Alcohol",
            "agent": "HX-Allergy",
            "bw": "PE-Weight",
            "height": "PE-Height",
            "waist": "PE-Waist",
            "bps": "PE-SBP",
            "bpd": "PE-DBP",
            "pulse": "PE-Pulse",
            "rr": "PE-RR",
            "report_text": "Image-ChestXray",
        }, inplace=True)

        main_df["HX-UnderlyingDisease"] = main_df["HX-UnderlyingDisease"].str.replace(
            ",", ";").str.replace("/", ";").str.strip()
        main_df["HX-UnderlyingDisease"] = np.where(
            main_df["HX-UnderlyingDisease"] == "", np.NaN, main_df["HX-UnderlyingDisease"])
        main_df["HX-UnderlyingDisease"].fillna("-", inplace=True)
        main_df["HX-Allergy"].fillna("-", inplace=True)
        main_df["HX-Smoking"] = main_df["HX-Smoking"].str.replace(
            "ไม่เคยสูบ", "-")
        main_df["HX-Alcohol"] = main_df["HX-Alcohol"].str.replace(
            "ไม่ดื่ม", "-")
        main_df["Image-ChestXray"] = main_df["Image-ChestXray"].str.replace(
            "�", "").str.strip()
        main_df["PE-Weight"].replace(0, np.NAN, inplace=True)
        main_df["PE-Waist"].replace(0, np.NAN, inplace=True)
        main_df["PE-SBP"].replace(0, np.NAN, inplace=True)
        main_df["PE-DBP"].replace(0, np.NAN, inplace=True)
        main_df["PE-Pulse"].replace(0, np.NAN, inplace=True)
        main_df["PE-RR"].replace(0, np.NAN, inplace=True)
        if "Lipid-LDL" in main_df:
            main_df["Lipid-LDL"] = pd.to_numeric(
                main_df["Lipid-LDL"], errors='coerce')
        if "UA-Sq.Epi" in main_df:
            main_df["UA-Sq.Epi"] = np.where(pd.isna(main_df["UA-Color"]), main_df["UA-Sq.Epi"],
                                            np.where(pd.isna(main_df["UA-Sq.Epi"]), "-", main_df["UA-Sq.Epi"]))

        return main_df.fillna("")

    def get_data(self, cc: str, start_date: QDate, end_date: QDate | None = None):
        # YYYY-MM-DDout = template.copy()
        if end_date is not None:
            output = self.main(cc, start_date.addDays(-3).toString(
                "yyyy-MM-dd"), end_date.toString("yyyy-MM-dd"))
        else:
            output = self.main(
                cc, start_date.addDays(-3).toString("yyyy-MM-dd"))
        output = output[output["VisitDate"] >= 
            start_date]
        out = self.template.copy()
        for col in output.columns:
            out[col] = output[col]
        column_to_move = out.pop("cc")
        out.insert(0, "cc", column_to_move)
        name = re.sub(r"[^\u0E00-\u0E7Fa-zA-Z' \.]", "_", cc)
        end_date_string = "" if end_date is None else f"{end_date.toString('yyyy-MM-dd')}"
        fullname = f"output_{name}{start_date.toString('yyyy-MM-dd')}{end_date_string}.xlsx"
        out.sort_values(by="VisitNumber").to_excel(
            f"outputs/{fullname}")
        return fullname
