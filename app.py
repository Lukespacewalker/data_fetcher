import json
from os import mkdir, path
from pathlib import Path
import win32mica
import darkdetect
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QDateEdit, QGroupBox, QVBoxLayout, QGridLayout, QLabel, QPushButton, QComboBox, QCheckBox, QTabWidget
from PySide6.QtCore import Qt, QLocale, QDate
import sys
from modules.blurwindow import GlobalBlur
from modules.fetcher import Fetcher
import stylesheet
import calendarpaint
from glob import glob

with open("config.json") as f:
    config = json.load(f)


fetcher: Fetcher = None

is_win_11 = sys.getwindowsversion().build > 20000


def createVBoxLayout(widgets: list[QWidget]):
    layout = QVBoxLayout()
    layout.setSpacing(8)
    for widget in widgets:
        layout.addWidget(widget)
    return layout


def ApplyMenuBlur(hwnd: int):
    hwnd = int(hwnd)
    if darkdetect.isDark() == True:
        GlobalBlur(hwnd, Acrylic=True, hexColor="#21212140",
                   Dark=True, smallCorners=True)
    else:
        GlobalBlur(hwnd, Acrylic=True, hexColor="#faf7f740",
                   Dark=False, smallCorners=True)


class ConnectionWidget(QWidget):
    def updateConfig(self):
        config["mysqlAddress"] = self.server_address.text()
        config["port"] = self.server_port.text()
        config["username"] = self.server_username.text()
        config["password"] = self.server_password.text()
        config["database"] = self.db_name.text()

    def saveConfig(self):
        with open("./config.json", "w") as f:
            self.updateConfig()
            json.dump(config, f)
            global fetcher
            fetcher = Fetcher(config["username"], config["password"],
                              config["mysqlAddress"], config["port"], config["database"])

    def createSetConfigDelegate(self, prop_name):
        def delegate():
            self.updateConfig()
            global fetcher
            fetcher = Fetcher(config["username"], config["password"],
                              config["mysqlAddress"], config["port"], config["database"])
        return delegate

    def __init__(self):
        super(ConnectionWidget, self).__init__()
        global fetcher
        fetcher = Fetcher(config["username"], config["password"],
                          config["mysqlAddress"], config["port"], config["database"])
        layout = QGridLayout()
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(10)

        # title = QLabel(text="การเชื่อมต่อ")
        # title.setStyleSheet(
        #    "font-size:36px")
        # layout.addWidget(title, 0, 0, 1, 3)

        save = QPushButton()
        save.setText("บันทึก")
        save.setCheckable(True)
        save.clicked.connect(self.saveConfig)
        layout.addWidget(save, 0, 2)

        label_server_address = QLabel(text="ที่อยู่ของเซิรฟเวอร์ MySQL")
        self.server_address = server_address = QLineEdit()
        server_address.setPlaceholderText("เช่น 127.0.0.1")
        server_address.setText(config["mysqlAddress"])
        server_address.editingFinished.connect(
            self.createSetConfigDelegate("mysqlAddress"))
        layout.addLayout(createVBoxLayout(
            [label_server_address, server_address]), 1, 0, 1, 2)

        label_server_port = QLabel(text="พอร์ต")
        self.server_port = server_port = QLineEdit()
        server_port.setPlaceholderText("เช่น 3306")
        server_port.setText(config["port"])
        server_port.editingFinished.connect(
            self.createSetConfigDelegate("port"))
        layout.addLayout(createVBoxLayout(
            [label_server_port, server_port]), 1, 2)

        label_db_name = QLabel(text="ชื่อฐานข้อมูล")
        self.db_name = db_name = QLineEdit()
        db_name.setPlaceholderText("เช่น hos")
        db_name.setText(config["database"])
        db_name.editingFinished.connect(
            self.createSetConfigDelegate("database"))
        layout.addLayout(createVBoxLayout(
            [label_db_name, db_name]), 2, 0)

        label_server_username = QLabel(text="ชื่อผู้ใช้")
        self.server_username = server_username = QLineEdit()
        server_username.setText(config["username"])
        server_username.editingFinished.connect(
            self.createSetConfigDelegate("username"))
        layout.addLayout(createVBoxLayout(
            [label_server_username, server_username]), 2, 1)

        label_server_password = QLabel(text="รหัสผ่าน")
        self.server_password = server_password = QLineEdit()
        server_password.setText(config["password"])
        server_password.editingFinished.connect(
            self.createSetConfigDelegate("password"))
        server_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addLayout(createVBoxLayout(
            [label_server_password, server_password]), 2, 2)

        self.setLayout(layout)


class SearchWidget(QWidget):
    def fetch(self):
        global fetcher
        self.result.setText("")
        self.search.setDisabled(True)
        self.search.setCheckable(False)
        self.search.setText("กำลังทำงาน ...")
        QApplication.processEvents()
        try:
            if self.use_end_date.isChecked():
                fname = fetcher.get_data(
                    self.cc.text(), self.start_date.date(), self.end_date.date())
            else:
                fname = fetcher.get_data(
                    self.cc.text(), self.start_date.date())
            self.result.setText(f"เรียบร้อย {fname}")
        except:
            self.result.setText("เกิดข้อผิดพลาด")

        self.search.setText("ค้นหา")
        self.search.setDisabled(False)
        pass

    def change_template(self, index):
        global fetcher
        po = self.template.itemData(index)
        fetcher.change_template(po)

    def toggle_end_date_visibility(self, state):
        self.end_date.setVisible(state)

    def toggle_search_disability(self, text):
        self.search.setDisabled(True if text.strip() == "" else False)

    def __init__(self):
        super(SearchWidget, self).__init__()
        global fetcher
        # group = QGroupBox(title="การค้นหา")

        layout = QGridLayout()
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(10)

        template_label = QLabel(text="เทมเพลต")
        self.template = template = QComboBox()
        # template.view().window().setAttribute(
        #    Qt.WidgetAttribute.WA_TranslucentBackground)
        template.view().window().setWindowFlags(
            Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        # template.setCurrentIndex(-1)
        # ApplyMenuBlur(template.view().window().winId())

        template.activated.connect(self.change_template)
        for path in glob("./templates/*"):
            po = Path(path)
            template.addItem(po.name, userData=po)
        layout.addLayout(createVBoxLayout(
            [template_label, template]), 1, 0, 1, 2)
        fetcher.change_template(template.itemData(0))

        cc_label = QLabel(text="อาการสำคัญ (Chief complaint)")
        cc_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.cc = cc = QLineEdit()
        cc.setPlaceholderText("ค้นหาการมาตรวจที่มีอาการสำคัญนี้")
        cc.textChanged.connect(self.toggle_search_disability)
        layout.addLayout(createVBoxLayout(
            [cc_label, cc]), 2, 0, 1, 2)

        start_date_label = QLabel(text="ตั้งแต่")
        start_date_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.start_date = date = QDateEdit()
        date.setCalendarPopup(True)
        date.setCalendarWidget(calendarpaint.Calendar())
        date.setLocale(QLocale.Language.English)
        date.setDate(QDate.currentDate())
        date_window = date.calendarWidget().window()
        date_window.setWindowFlags(
            Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        layout.addLayout(createVBoxLayout(
            [start_date_label, date]), 1, 2)

        self.use_end_date = use_end_date = QCheckBox()
        use_end_date.stateChanged.connect(self.toggle_end_date_visibility)
        use_end_date.setText("จนถึง")
        self.end_date = end_date = QDateEdit()
        end_date.setVisible(use_end_date.isChecked())
        end_date.setCalendarPopup(True)
        end_date.setCalendarWidget(calendarpaint.Calendar())
        end_date.setLocale(QLocale.Language.English)
        end_date.setDate(QDate.currentDate())
        end_date.calendarWidget().window().setWindowFlags(
            Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        layout.addLayout(createVBoxLayout(
            [use_end_date, end_date]), 2, 2)

        self.search = search = QPushButton()
        search.setText("ค้นหา")
        search.setDisabled(True)
        search.clicked.connect(self.fetch)
        layout.addWidget(search, 3, 0, 1, 3)

        self.result = result = QLabel()
        result.setText("")
        layout.addWidget(result, 4, 0, 1, 2)

        self.setLayout(layout)
       # self.set(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("โปรแกรมดึงข้อมูลจาก HosXP")
        screen = self.screen().availableGeometry()
        width = 600
        height = 300
        self.setGeometry(screen.center().x()-int(width/2),
                         screen.center().y()-int(height/2), width, height)

        if is_win_11:
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        is_dark = darkdetect.isDark()
        if is_dark:
            self.setStyleSheet(stylesheet.DARK)
            from icons import styledark_rc
            if is_win_11:
                win32mica.ApplyMica(self.winId(
                ), ColorMode=win32mica.MICAMODE.DARK)

        else:
            self.setStyleSheet(stylesheet.LIGHT)
            from icons import stylelight_rc
            if is_win_11:
                win32mica.ApplyMica(self.winId(
                ), ColorMode=win32mica.MICAMODE.LIGHT)

        tabs = QTabWidget()
        c = ConnectionWidget()
        s = SearchWidget()
        tabs.addTab(s, "การค้นหา")
        tabs.addTab(c, "การเชื่อมต่อ")

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not path.exists("./outputs"):
        mkdir("./outputs")
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
