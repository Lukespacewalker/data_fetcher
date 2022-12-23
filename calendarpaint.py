from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QFrame, QProgressBar, QMainWindow, QApplication
from winreg import ConnectRegistry,OpenKey,QueryValueEx,HKEY_CURRENT_USER
import darkdetect

registry = ConnectRegistry(None,HKEY_CURRENT_USER)
key = OpenKey(registry, r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Explorer\\Accent')
key_value = QueryValueEx(key,'AccentColorMenu')
accent_int = key_value[0]
accent = accent_int-4278190080
accent = str(hex(accent)).split('x')[1]
accent = accent[4:6]+accent[2:4]+accent[0:2]

class Calendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

        self.setVerticalHeaderFormat(self.VerticalHeaderFormat.NoVerticalHeader)
        self.setHorizontalHeaderFormat(self.HorizontalHeaderFormat.ShortDayNames)
        print(self.showSelectedDate())

        if darkdetect.isDark() == True:
            for d in (QtCore.Qt.DayOfWeek.Saturday, QtCore.Qt.DayOfWeek.Sunday):
                fmt = self.weekdayTextFormat(d)
                fmt.setForeground(QtCore.Qt.GlobalColor.white)
                self.setWeekdayTextFormat(d, fmt)
        else:
            for d in (QtCore.Qt.DayOfWeek.Saturday, QtCore.Qt.DayOfWeek.Sunday):
                fmt = self.weekdayTextFormat(d)
                fmt.setForeground(QtCore.Qt.GlobalColor.black)
                self.setWeekdayTextFormat(d, fmt)

    if darkdetect.isDark() == True:
        def paintCell(self, painter, rect, date):
            if date == date.currentDate():
                painter.save()
                painter.fillRect(rect, QtGui.QColor("transparent"))
                painter.setPen(QtCore.Qt.PenStyle.NoPen)
                painter.setBrush(QtGui.QColor('#'+accent))
                r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                r.moveCenter(rect.center())
                painter.drawEllipse(r)
                painter.setPen(QtGui.QPen(QtGui.QColor("black")))
                painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                painter.restore()
            else:
                month = "{0}-{1}".format(str(self.yearShown()), str(self.monthShown()).zfill(2))
                day = str(date.toPython())
                if day.startswith(month):
                    if date != self.selectedDate(): 
                        painter.setPen(QtGui.QPen(QtGui.QColor("white")))
                        painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                    if date == self.selectedDate(): 
                        if date != date.currentDate():
                            painter.setPen(QtCore.Qt.PenStyle.NoPen)
                            painter.setBrush(QtGui.QColor(255, 255, 255, 13))
                            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                            r.moveCenter(rect.center())
                            painter.drawEllipse(r)
                            painter.setPen(QtGui.QPen(QtGui.QColor('#'+accent)))
                            painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                else:
                    painter.setPen(QtGui.QPen(QtGui.QColor(150, 150, 150)))
                    painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
    else:
        def paintCell(self, painter, rect, date):
            if date == date.currentDate():
                painter.save()
                painter.fillRect(rect, QtGui.QColor("transparent"))
                painter.setPen(QtCore.Qt.PenStyle.NoPen)
                painter.setBrush(QtGui.QColor('#'+accent))
                r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                r.moveCenter(rect.center())
                painter.drawEllipse(r)
                painter.setPen(QtGui.QPen(QtGui.QColor("white")))
                painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                painter.restore()
            else:
                month = "{0}-{1}".format(str(self.yearShown()), str(self.monthShown()).zfill(2))
                day = str(date.toPython())
                if day.startswith(month):
                    if date != self.selectedDate(): 
                        painter.setPen(QtGui.QPen(QtGui.QColor("black")))
                        painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                    if date == self.selectedDate(): 
                        if date != date.currentDate():
                            painter.setPen(QtCore.Qt.PenStyle.NoPen)
                            painter.setBrush(QtGui.QColor(0, 0, 0, 13))
                            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
                            r.moveCenter(rect.center())
                            painter.drawEllipse(r)
                            painter.setPen(QtGui.QPen(QtGui.QColor('#'+accent)))
                            painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))
                else:
                    painter.setPen(QtGui.QPen(QtGui.QColor(100, 100, 100)))
                    painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, str(date.day()))