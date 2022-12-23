from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER

registry = ConnectRegistry(None, HKEY_CURRENT_USER)
key = OpenKey(
    registry, r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Explorer\\Accent')
key_value = QueryValueEx(key, 'AccentColorMenu')
accent_int = key_value[0]
accent = accent_int-4278190080
accent = str(hex(accent)).split('x')[1]
accent = accent[4:6]+accent[2:4]+accent[0:2]
accent = 'rgb'+str(tuple(int(accent[i:i+2], 16) for i in (0, 2, 4)))

DARK = '''
QMainWindow{
    background-color: rgb(30,30,30);
}

/*BACKGROUND*/
QWidget {
    color: rgb(255, 255, 255);
    font-size: 17px;
    font-family: "Segoe UI Variable Small", "Tahoma", serif;
    font-weight: 400;
}

/*LINEEDIT*/
QLineEdit {
    background-color: rgba(255, 255, 255, 16);
    border: 1px solid rgba(255, 255, 255, 13);
    font-size: 16px;
    font-family: "Segoe UI Variable Small","Tahoma", serif;
    font-weight: 500;
    border-radius: 7px;
    border-bottom: 1px solid rgba(255, 255, 255, 150);
    padding-top: 0px;
    padding-left: 5px;
    min-height: 38px;
}

QLineEdit:hover {
    background-color: rgba(255, 255, 255, 20);
    border: 1px solid rgba(255, 255, 255, 10);
    border-bottom: 1px solid rgba(255, 255, 255, 150);
}

QLineEdit:focus {
    border-bottom: 2px solid '''+accent+''';
    background-color: rgba(255, 255, 255, 5);
    border-top: 1px solid rgba(255, 255, 255, 13);
    border-left: 1px solid rgba(255, 255, 255, 13);
    border-right: 1px solid rgba(255, 255, 255, 13);
}

QLineEdit:disabled {
    color: rgb(150, 150, 150);
    background-color: rgba(255, 255, 255, 13);
    border: 1px solid rgba(255, 255, 255, 5);
}


/*PUSHBUTTON*/
QPushButton {
    background-color: rgba(255, 255, 255, 18);
    border: 1px solid rgba(255, 255, 255, 13);
    border-radius: 7px;
    min-height: 38px;
    max-height: 38px;
}

QPushButton:hover {
    background-color: rgba(255, 255, 255, 25);
    border: 1px solid rgba(255, 255, 255, 10);
}

QPushButton::pressed {
    background-color: rgba(255, 255, 255, 7);
    border: 1px solid rgba(255, 255, 255, 13);
    color: rgba(255, 255, 255, 200);
}

QPushButton::disabled {
    color: rgb(150, 150, 150);
    background-color: rgba(255, 255, 255, 13);
}

/*COMBOBOX*/
QComboBox {
    background-color: rgba(255, 255, 255, 16);
    border: 1px solid rgba(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
}

QComboBox:hover {
    background-color: rgba(255, 255, 255, 20);
    border: 1px solid rgba(255, 255, 255, 10);
}

QComboBox::pressed {
    background-color: rgba(255, 255, 255, 20);
    border: 1px solid rgba(255, 255, 255, 13);
    color: rgba(255, 255, 255, 200);
}

QComboBox::down-arrow {
    image: url(:/ComboBox/img dark/ComboBox.png);
}

QComboBox::drop-down {
    background-color: transparent;
    min-width: 50px;
}

QComboBox:disabled {
    color: rgb(150, 150, 150);
    background-color: rgba(255, 255, 255, 13);
    border: 1px solid rgba(255, 255, 255, 5);
}

QComboBox::down-arrow:disabled {
    image: url(:/ComboBox/img dark/ComboBoxDisabled.png);
}


/*DATETIMEEDIT*/
QDateTimeEdit {
    background-color: rgba(255, 255, 255, 10);
    border: 1px solid rgba(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
    min-width: 100px;
    border-bottom: 1px solid rgba(255, 255, 255, 150);
}

QDateTimeEdit:hover {
    background-color: rgba(255, 255, 255, 16);
    border: 1px solid rgba(255, 255, 255, 13);
    border-bottom: 1px solid rgba(255, 255, 255, 150);
}

QDateTimeEdit::focus {
    background-color: rgba(255, 255, 255, 5);
    border: 1px solid rgba(255, 255, 255, 13);
    color: rgba(255, 255, 255, 200);
    border-bottom: 2px solid '''+accent+''';
}

QDateTimeEdit::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::up-button:hover {
    background-color: rgba(255, 255, 255, 13);
}

QDateTimeEdit::up-button:pressed {
    background-color: rgba(255, 255, 255, 5);
}

QDateTimeEdit::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::down-button:hover {
    background-color: rgba(255, 255, 255, 13);
}

QDateTimeEdit::down-button:pressed {
    background-color: rgba(255, 255, 255, 5);
}

QDateTimeEdit::drop-down {
    background-color: transparent;
    width: 50px;
}

QDateTimeEdit:disabled {
    color: rgb(150, 150, 150);
    background-color: rgba(255, 255, 255, 13);
    border: 1px solid rgba(255, 255, 255, 5);
}

QDateTimeEdit::up-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxUpDisabled.png);
}

QDateTimeEdit::down-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxDownDisabled.png);
}



/*CALENDAR*/
QCalendarWidget {
}

QCalendarWidget QToolButton {
    height: 36px;
    font-size: 18px;
    background-color: rgba(255, 255, 255, 0);
    margin: 5px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar { 
    background-color: rgba(255, 255, 255, 0); 
    border: 1px solid rgba(255, 255, 255, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    border-bottom: none;
}

#qt_calendar_prevmonth {
    qproperty-icon: url(:/PrevNext/img dark/PrevMonth.png);
    width: 32px;
}

#qt_calendar_nextmonth {
    qproperty-icon: url(:/PrevNext/img dark/NextMonth.png);
    width: 32px;
}

#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(255, 255, 255, 16);
    border-radius: 5px;
}

#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(255, 255, 255, 10);
    border-radius: 5px;
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: white;
    margin: 5px 0px;
    padding: 0px 10px;
}

#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(255, 255, 255, 16);
    border-radius: 5px;
}

#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(255, 255, 255, 10);
    border-radius: 5px;
}

QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton {
    background-color: transparent;
}

QCalendarWidget QMenu {
    background-color : #202020;
}

QCalendarWidget QSpinBox {
    margin: 5px 0px;
}

QCalendarWidget QSpinBox::focus {
    background-color: rgba(255, 255, 255, 5);
    border: 1px solid rgba(255, 255, 255, 13);
    color: rgba(0, 0, 0, 200);
    border-bottom: 2px solid '''+accent+''';
}

QCalendarWidget QSpinBox::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::up-button:hover {
    background-color: rgba(255, 255, 255, 13);
}

QCalendarWidget QSpinBox::up-button:pressed {
    background-color: rgba(255, 255, 255, 5);
}

QCalendarWidget QSpinBox::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::down-button:hover {
    background-color: rgba(255, 255, 255, 13);
}

QCalendarWidget QSpinBox::down-button:pressed {
    background-color: rgba(255, 255, 255, 5);
}

QCalendarWidget QWidget { 
    alternate-background-color: rgba(255, 255, 255, 0); 
}

QCalendarWidget QAbstractItemView:enabled {
    color: rgb(255, 255, 255);  
    selection-background-color: '''+accent+''';
    selection-color: black;
    border: 1px solid rgba(255, 255, 255, 13);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    outline: 0;
}

QCalendarWidget QAbstractItemView:disabled {
    color: rgb(150, 150, 150);  
    selection-background-color: rgb(150, 150, 150);
    selection-color: black;
    border: 1px solid rgba(255, 255, 255, 13);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}

#qt_calendar_yearbutton:disabled, #qt_calendar_monthbutton:disabled {
    color: rgb(150, 150, 150);
}

#qt_calendar_prevmonth:disabled {
    qproperty-icon: url(:/PrevNext/img dark/PrevMonthDisabled.png);
}

#qt_calendar_nextmonth:disabled {
    qproperty-icon: url(:/PrevNext/img dark/NextMonthDisabled.png);
}

/*CHECKBOX*/
QCheckBox {
    min-height: 30px;
    max-height: 30px;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border-radius: 5px;
    border: 2px solid #848484;
    background-color: rgba(255, 255, 255, 0);
    margin-right: 5px;
}

QCheckBox::indicator:hover {
    background-color: rgba(255, 255, 255, 16);
}

QCheckBox::indicator:pressed {
    background-color: rgba(255, 255, 255, 20);
    border: 2px solid #434343;
}

QCheckBox::indicator:checked {
    background-color: '''+accent+''';
    border: 2px solid '''+accent+''';
    image: url(:/CheckBox/img dark/CheckBox.png);
}

QCheckBox::indicator:checked:pressed {
    image: url(:/CheckBox/img dark/CheckBoxPressed.png);
}

QCheckBox:disabled {
    color: rgb(150, 150, 150);
}

QCheckBox::indicator:disabled {
    border: 2px solid #646464;
    background-color: rgba(255, 255, 255, 0);
}

/*GROUPBOX*/
QGroupBox {
    background-color: rgba(50,50,50, 150);
    border-radius: 5px;
    border: 1px solid rgba(255, 255, 255, 13);
    margin-top: 36px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    background-color: rgba(255, 255, 255, 16);
    padding: 7px 15px;
    margin-left: 5px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QGroupBox::title::disabled {
    color: rgb(150, 150, 150)
}
/*TABWIDGET*/
QTabWidget {
}

QWidget {
    border-radius: 5px;
}

QTabWidget::pane {
    background-color: rgba(50,50,50, 150);
    border: 1px solid rgb(43, 43, 43);
    border-radius: 5px;
}

QTabWidget::tab-bar {
    left: 5px;
}

QTabBar::tab {
    background-color: rgba(255, 255, 255, 0);
    padding: 7px 15px;
    margin-right: 2px;
}

QTabBar::tab:hover {
    background-color: rgba(255, 255, 255, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:selected {
    background-color: rgba(255, 255, 255, 16);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:disabled {
    color: rgb(150, 150, 150)
}

/*LISTVIEW*/
QListView {
    background-color: rgba(30, 30, 30, 255);
    font-size: 17px;
    font-family: "Segoe UI Variable Small","Tahoma", serif;
    font-weight: 400;
    padding: 7px;
    border-radius: 0px;
    outline: 0;
}

QListView::item {
    height: 35px;
}

QListView::item:selected {
    background-color: rgba(255, 255, 255, 13);
    color: white;
    border-radius: 5px;
    padding-left: 0px;
}
'''

LIGHT = '''
QMainWindow{
    background-color: rgb(250,250,250);
}

/*BACKGROUND*/
QWidget {
    color: rgb(0, 0, 0);
    font-size: 17px;
    font-family: "Segoe UI Variable Small", "Tahoma", serif;
    font-weight: 400;
}

/*LINEEDIT*/
QLineEdit {
    background-color: rgba(0, 0, 0, 7);
    border: 1px solid rgba(0, 0, 0, 13);
    font-size: 16px;
    font-family: "Segoe UI Variable Small","Tahoma", serif;
    font-weight: 500;
    border-radius: 7px;
    border-bottom: 1px solid rgba(0, 0, 0, 100);
    padding-top: 0px;
    padding-left: 5px;
    min-height: 38px;
}

QLineEdit:hover {
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 13);
    border-bottom: 1px solid rgba(0, 0, 0, 100);
}

QLineEdit:focus {
    border-bottom: 2px solid '''+accent+''';
    background-color: rgba(0, 0, 0, 5);
    border-top: 1px solid rgba(0, 0, 0, 13);
    border-left: 1px solid rgba(0, 0, 0, 13);
    border-right: 1px solid rgba(0, 0, 0, 13);
}

QLineEdit:disabled {
    color: rgba(0, 0, 0, 150);
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 5);
}

/*PUSHBUTTON*/
QPushButton {
    background-color: rgba(0, 0, 0, 7);
    border: 1px solid rgba(0, 0, 0, 13);
    border-radius: 7px;
    min-height: 38px;
    max-height: 38px;
}

QPushButton:hover {
    background-color: rgba(0, 0, 0, 10);
    border: 1px solid rgba(0, 0, 0, 13);
}

QPushButton::pressed {
    color: rgba(0, 0, 0, 150);
}

QPushButton::disabled {
    color: rgba(0, 0, 0, 110);
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 5);
}

/*COMBOBOX*/
QComboBox {
    background-color: rgba(0, 0, 0, 7);
    border: 1px solid rgba(0, 0, 0, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
}

QComboBox:hover {
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 13);
}

QComboBox::pressed {
    border: 1px solid rgba(0, 0, 0, 10);
}

QComboBox::down-arrow {
    image: url(:/newPrefix/img light/ComboBox.png);
}

QComboBox::drop-down {
    background-color: transparent;
    min-width: 50px;
}

QComboBox:disabled {
    color: rgba(0, 0, 0, 110);
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 5);
}

QComboBox::down-arrow:disabled {
    image: url(:/newPrefix/img light/ComboBoxDisabled.png);
}

/*DATETIMEEDIT*/
QDateTimeEdit {
    background-color: rgba(0, 0, 0, 7);
    border: 1px solid rgba(0, 0, 0, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
    min-width: 100px;
    border-bottom: 1px solid rgba(0, 0, 0, 100);
}

QDateTimeEdit:hover {
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 13);
    border-bottom: 1px solid rgba(0, 0, 0, 100);
}

QDateTimeEdit::focus {
    background-color: rgba(0, 0, 0, 5);
    border: 1px solid rgba(0, 0, 0, 10);
    color: rgba(0, 0, 0, 200);
    border-bottom: 2px solid '''+accent+''';
}

QDateTimeEdit::up-button {
    image: url(:/SpinBox/img light/SpinBoxUp.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::up-button:hover {
    background-color: rgba(0, 0, 0, 10);
}

QDateTimeEdit::up-button:pressed {
    background-color: rgba(0, 0, 0, 5);
}

QDateTimeEdit::down-button {
    image: url(:/SpinBox/img light/SpinBoxDown.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::down-button:hover {
    background-color: rgba(0, 0, 0, 10);
}

QDateTimeEdit::down-button:pressed {
    background-color: rgba(0, 0, 0, 5);
}

QDateTimeEdit::drop-down {
    background-color: transparent;
    width: 50px;
}

QDateTimeEdit:disabled {
    color: rgba(0, 0, 0, 110);
    background-color: rgba(0, 0, 0, 13);
    border: 1px solid rgba(0, 0, 0, 5);
}

QDateTimeEdit::up-button:disabled {
    image: url(:/SpinBox/img light/SpinBoxUpDisabled.png);
}

QDateTimeEdit::down-button:disabled {
    image: url(:/SpinBox/img light/SpinBoxDownDisabled.png);
}

/*CALENDAR*/
QCalendarWidget {
}

QCalendarWidget QToolButton {
    height: 36px;
    font-size: 18px;
    background-color: rgba(0, 0, 0, 0);
    margin: 5px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar { 
    background-color: rgba(0, 0, 0, 0); 
    border: 1px solid rgba(0, 0, 0, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    border-bottom: none;
}

QCalendarWidget QMenu {
    background-color : #f3f3f3;
}

#qt_calendar_prevmonth {
    qproperty-icon: url(:/PrevNext/img light/PrevMonth.png);
    width: 32px;
}

#qt_calendar_nextmonth {
    qproperty-icon: url(:/PrevNext/img light/NextMonth.png);
    width: 32px;
}

#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(0, 0, 0, 10);
    border-radius: 5px;
}

#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(0, 0, 0, 7);
    border-radius: 5px;
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: rgb(0, 0, 0);
    margin: 5px 0px;
    padding: 0px 10px;
}

#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(0, 0, 0, 10);
    border-radius: 5px;
}

#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(0, 0, 0, 7);
    border-radius: 5px;
}

QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton {
    background-color: transparent;
}

QCalendarWidget QSpinBox {
    margin: 5px 0px;
}

QCalendarWidget QSpinBox::focus {
    background-color: rgba(0, 0, 0, 5);
    border: 1px solid rgba(0, 0, 0, 10);
    color: rgba(0, 0, 0, 200);
    border-bottom: 2px solid '''+accent+''';
}

QCalendarWidget QSpinBox::up-button {
    image: url(:/SpinBox/img light/SpinBoxUp.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::up-button:hover {
    background-color: rgba(0, 0, 0, 10);
}

QCalendarWidget QSpinBox::up-button:pressed {
    background-color: rgba(0, 0, 0, 5);
}

QCalendarWidget QSpinBox::down-button {
    image: url(:/SpinBox/img light/SpinBoxDown.png);
    background-color: rgba(0, 0, 0, 0);
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::down-button:hover {
    background-color: rgba(0, 0, 0, 10);
}

QCalendarWidget QSpinBox::down-button:pressed {
    background-color: rgba(0, 0, 0, 5);
}

QCalendarWidget QWidget { 
    alternate-background-color: rgba(0, 0, 0, 0); 
}

QCalendarWidget QAbstractItemView:enabled {
    color: rgb(0, 0, 0);  
    selection-background-color: '''+accent+''';
    selection-color: black;
    border: 1px solid rgba(0, 0, 0, 10);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    outline: 0;
}

QCalendarWidget QAbstractItemView:disabled {
    color: rgb(30, 30, 30);  
    selection-background-color: rgb(30, 30, 30);
    selection-color: black;
    border: 1px solid rgba(0, 0, 0, 13);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}

#qt_calendar_yearbutton:disabled, #qt_calendar_monthbutton:disabled {
    color: rgba(0, 0, 0, 110);
}

#qt_calendar_prevmonth:disabled {
    qproperty-icon: url(:/PrevNext/img light/PrevMonthDisabled.png);
}

#qt_calendar_nextmonth:disabled {
    qproperty-icon: url(:/PrevNext/img light/NextMonthDisabled.png);
}

/*CHECKBOX*/
QCheckBox {
    min-height: 30px;
    max-height: 30px;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border-radius: 5px;
    border: 2px solid #999999;
    background-color: rgba(0, 0, 0, 0);
    margin-right: 5px;
}

QCheckBox::indicator:hover {
    background-color: rgba(0, 0, 0, 15);
}

QCheckBox::indicator:pressed {
    background-color: rgba(0, 0, 0, 24);
    border: 2px solid #bbbbbb;
}

QCheckBox::indicator:checked {
    background-color: '''+accent+''';
    border: 2px solid '''+accent+''';
    image: url(:/CheckBox/img light/CheckBox.png);
    color: rgb(255, 255, 255);
}

QCheckBox::indicator:checked:pressed {
    image: url(:/CheckBox/img light/CheckBoxPressed.png);
}

QCheckBox:disabled {
    color: rgba(0, 0, 0, 110);
}

QCheckBox::indicator:disabled {
    border: 2px solid #bbbbbb;
    background-color: rgba(0, 0, 0, 0);
}

/*GROUPBOX*/
QGroupBox {
    background-color: rgba(250,250,250, 150);
    border-radius: 5px;
    border: 1px solid rgba(0, 0, 0, 13);
    margin-top: 36px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    background-color: rgba(0, 0, 0, 10);
    padding: 7px 15px;
    margin-left: 5px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QGroupBox::title::disabled {
    color: rgba(0, 0, 0, 150);
}

/*TABWIDGET*/
QTabWidget {
}

QWidget {
    border-radius: 5px;
}

QTabWidget::pane {
    background-color: rgba(250,250,250, 150);
    border: 1px solid rgba(0, 0, 0, 13);
    border-radius: 5px;
}

QTabWidget::tab-bar {
    left: 5px;
}

QTabBar::tab {
    background-color: rgba(0, 0, 0, 0);
    padding: 7px 15px;
    margin-right: 2px;
}

QTabBar::tab:hover {
    background-color: rgba(0, 0, 0, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:selected {
    background-color: rgba(0, 0, 0, 10);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:disabled {
    color: rgba(0, 0, 0, 150)
}

/*LISTVIEW*/
QListView {
    background-color: rgba(250, 250, 250, 255);
    font-size: 17px;
    font-family: "Segoe UI Variable Small","Tahoma", serif;
    font-weight: 400;
    padding: 7px;
    border-radius: 0px;
    outline: 0;
}

QListView::item {
    height: 35px;
}

QListView::item:selected {
    background-color: rgba(0, 0, 0, 13);
    color: black;
    border-radius: 5px;
    padding-left: 0px;
}
'''
