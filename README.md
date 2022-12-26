# โปรแกรมดึงข้อมูลจาก  HosXP

## ทดสอบบน Windows 11
Interface ของโปรแกรมอาจแสดงผลไม่ถูกต้องบน Widows 10 (ซึ่งไม่มี Windows 10 ให้ทดสอบ) และบน MacOSX และ Linux (ซึ่งไม่สนใจ)

## โหลดโปรแกรม
[v 1.00](https://github.com/Lukespacewalker/data_fetcher/releases/tag/v1)

## Build โปรแกรม
### ความต้องการ
Python 3.11
### คำสั่ง
1. `python -m venv .venv`
2. `./.venv/Scripts/Activate.ps1`
3. `pip install -r requirements.txt`
4. `pip install pyinstaller`
5. `pyinstaller app.spec`
6.  คัดลอก config.json และ templates ไปยัง dist
