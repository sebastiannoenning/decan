# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFormLayout,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

from views.resources.custom_classes.eventlistview import EventListView
from views.resources.custom_classes.qmodelcombobox import QModelComboBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QSize(800, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.navigation = QWidget(self.centralwidget)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setGeometry(QRect(0, 0, 120, 480))
        self.b_user = QPushButton(self.navigation)
        self.b_user.setObjectName(u"b_user")
        self.b_user.setGeometry(QRect(9, 30, 101, 101))
        self.b_calendar = QPushButton(self.navigation)
        self.b_calendar.setObjectName(u"b_calendar")
        self.b_calendar.setGeometry(QRect(10, 140, 101, 101))
        self.b_events = QPushButton(self.navigation)
        self.b_events.setObjectName(u"b_events")
        self.b_events.setGeometry(QRect(10, 250, 101, 101))
        self.b_settings = QPushButton(self.navigation)
        self.b_settings.setObjectName(u"b_settings")
        self.b_settings.setGeometry(QRect(10, 360, 101, 101))
        self.l_sidebar = QLabel(self.navigation)
        self.l_sidebar.setObjectName(u"l_sidebar")
        self.l_sidebar.setGeometry(QRect(10, 10, 101, 16))
        self.container = QWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(130, 10, 660, 460))
        self.pages = QStackedWidget(self.container)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 660, 460))
        self.page_usr = QWidget()
        self.page_usr.setObjectName(u"page_usr")
        self.userinfo = QStackedWidget(self.page_usr)
        self.userinfo.setObjectName(u"userinfo")
        self.userinfo.setGeometry(QRect(10, 30, 315, 420))
        self.userinfo.setAutoFillBackground(False)
        self.p_user_login = QWidget()
        self.p_user_login.setObjectName(u"p_user_login")
        self.tb_Username = QLineEdit(self.p_user_login)
        self.tb_Username.setObjectName(u"tb_Username")
        self.tb_Username.setGeometry(QRect(10, 130, 300, 24))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.tb_Username.setFont(font)
        self.tb_Username.setFrame(False)
        self.l_Login = QLabel(self.p_user_login)
        self.l_Login.setObjectName(u"l_Login")
        self.l_Login.setGeometry(QRect(10, 60, 291, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        self.l_Login.setFont(font1)
        self.l_Login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tb_Password = QLineEdit(self.p_user_login)
        self.tb_Password.setObjectName(u"tb_Password")
        self.tb_Password.setGeometry(QRect(10, 200, 274, 24))
        self.tb_Password.setFont(font)
        self.tb_Password.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText)
        self.tb_Password.setFrame(False)
        self.b_showhidebutton = QPushButton(self.p_user_login)
        self.b_showhidebutton.setObjectName(u"b_showhidebutton")
        self.b_showhidebutton.setGeometry(QRect(286, 200, 24, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_showhidebutton.sizePolicy().hasHeightForWidth())
        self.b_showhidebutton.setSizePolicy(sizePolicy)
        self.b_showhidebutton.setMinimumSize(QSize(24, 24))
        self.b_showhidebutton.setAutoFillBackground(False)
        self.l_Username = QLabel(self.p_user_login)
        self.l_Username.setObjectName(u"l_Username")
        self.l_Username.setGeometry(QRect(10, 110, 300, 20))
        self.l_Username.setFont(font)
        self.l_Username.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_Username.setMargin(0)
        self.l_Username.setIndent(-1)
        self.l_Password = QLabel(self.p_user_login)
        self.l_Password.setObjectName(u"l_Password")
        self.l_Password.setGeometry(QRect(10, 180, 300, 20))
        self.l_Password.setFont(font)
        self.l_Password.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_Password.setMargin(0)
        self.l_Password.setIndent(-1)
        self.b_confirm = QPushButton(self.p_user_login)
        self.b_confirm.setObjectName(u"b_confirm")
        self.b_confirm.setGeometry(QRect(100, 250, 100, 32))
        self.userinfo.addWidget(self.p_user_login)
        self.p_user_profile = QWidget()
        self.p_user_profile.setObjectName(u"p_user_profile")
        self.pushButton = QPushButton(self.p_user_profile)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 330, 100, 32))
        self.label = QLabel(self.p_user_profile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 120, 58, 16))
        self.label_2 = QLabel(self.p_user_profile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 160, 58, 16))
        self.userinfo.addWidget(self.p_user_profile)
        self.Profile = QLabel(self.page_usr)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setGeometry(QRect(0, 0, 330, 20))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.Profile.setFont(font2)
        self.Profile.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Select = QLabel(self.page_usr)
        self.Select.setObjectName(u"Select")
        self.Select.setGeometry(QRect(330, 0, 330, 20))
        self.Select.setFont(font2)
        self.Select.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayoutWidget = QWidget(self.page_usr)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(340, 50, 160, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.page_usr)
        self.page_cal = QWidget()
        self.page_cal.setObjectName(u"page_cal")
        self.upcomingevents = QScrollArea(self.page_cal)
        self.upcomingevents.setObjectName(u"upcomingevents")
        self.upcomingevents.setGeometry(QRect(10, 10, 340, 440))
        self.upcomingevents.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.upcomingevents.setWidgetResizable(True)
        self.scrollAreaWidgetContents = EventListView()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 322, 438))
        self.upcomingevents.setWidget(self.scrollAreaWidgetContents)
        self.b_delete = QPushButton(self.page_cal)
        self.b_delete.setObjectName(u"b_delete")
        self.b_delete.setGeometry(QRect(420, 120, 100, 32))
        self.userSelect = QModelComboBox(self.page_cal)
        self.userSelect.setObjectName(u"userSelect")
        self.userSelect.setGeometry(QRect(370, 20, 181, 32))
        self.pages.addWidget(self.page_cal)
        self.page_addevent = QWidget()
        self.page_addevent.setObjectName(u"page_addevent")
        self.eventform = QScrollArea(self.page_addevent)
        self.eventform.setObjectName(u"eventform")
        self.eventform.setGeometry(QRect(310, 0, 341, 461))
        self.eventform.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 339, 459))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 331, 385))
        self.generalcontainer = QVBoxLayout(self.verticalLayoutWidget)
        self.generalcontainer.setObjectName(u"generalcontainer")
        self.generalcontainer.setContentsMargins(0, 0, 0, 0)
        self.GenericSettings = QFormLayout()
        self.GenericSettings.setObjectName(u"GenericSettings")
        self.label_user = QLabel(self.verticalLayoutWidget)
        self.label_user.setObjectName(u"label_user")

        self.GenericSettings.setWidget(0, QFormLayout.LabelRole, self.label_user)

        self.selectuser = QComboBox(self.verticalLayoutWidget)
        self.selectuser.setObjectName(u"selectuser")

        self.GenericSettings.setWidget(0, QFormLayout.FieldRole, self.selectuser)

        self.label_title = QLabel(self.verticalLayoutWidget)
        self.label_title.setObjectName(u"label_title")

        self.GenericSettings.setWidget(1, QFormLayout.LabelRole, self.label_title)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.GenericSettings.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_st = QLabel(self.verticalLayoutWidget)
        self.label_st.setObjectName(u"label_st")

        self.GenericSettings.setWidget(2, QFormLayout.LabelRole, self.label_st)

        self.startedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.startedit.setObjectName(u"startedit")

        self.GenericSettings.setWidget(2, QFormLayout.FieldRole, self.startedit)

        self.label_et = QLabel(self.verticalLayoutWidget)
        self.label_et.setObjectName(u"label_et")

        self.GenericSettings.setWidget(3, QFormLayout.LabelRole, self.label_et)

        self.endedit = QDateTimeEdit(self.verticalLayoutWidget)
        self.endedit.setObjectName(u"endedit")

        self.GenericSettings.setWidget(3, QFormLayout.FieldRole, self.endedit)


        self.generalcontainer.addLayout(self.GenericSettings)

        self.expandusers = QPushButton(self.verticalLayoutWidget)
        self.expandusers.setObjectName(u"expandusers")

        self.generalcontainer.addWidget(self.expandusers)

        self.userview = QListView(self.verticalLayoutWidget)
        self.userview.setObjectName(u"userview")

        self.generalcontainer.addWidget(self.userview)

        self.componentsexpand = QVBoxLayout()
        self.componentsexpand.setObjectName(u"componentsexpand")
        self.expandcomponent = QPushButton(self.verticalLayoutWidget)
        self.expandcomponent.setObjectName(u"expandcomponent")

        self.componentsexpand.addWidget(self.expandcomponent)

        self.select_add = QHBoxLayout()
        self.select_add.setObjectName(u"select_add")
        self.selectcomponenttype = QComboBox(self.verticalLayoutWidget)
        self.selectcomponenttype.setObjectName(u"selectcomponenttype")

        self.select_add.addWidget(self.selectcomponenttype)

        self.addcomponent = QPushButton(self.verticalLayoutWidget)
        self.addcomponent.setObjectName(u"addcomponent")

        self.select_add.addWidget(self.addcomponent)


        self.componentsexpand.addLayout(self.select_add)

        self.dynamiccomponentsection = QVBoxLayout()
        self.dynamiccomponentsection.setObjectName(u"dynamiccomponentsection")

        self.componentsexpand.addLayout(self.dynamiccomponentsection)


        self.generalcontainer.addLayout(self.componentsexpand)

        self.addeventbutton = QPushButton(self.verticalLayoutWidget)
        self.addeventbutton.setObjectName(u"addeventbutton")

        self.generalcontainer.addWidget(self.addeventbutton)

        self.eventform.setWidget(self.scrollAreaWidgetContents_2)
        self.pages.addWidget(self.page_addevent)
        self.page_set = QWidget()
        self.page_set.setObjectName(u"page_set")
        self.table_user = QTableView(self.page_set)
        self.table_user.setObjectName(u"table_user")
        self.table_user.setGeometry(QRect(40, 20, 256, 192))
        self.table_user_profile = QTableView(self.page_set)
        self.table_user_profile.setObjectName(u"table_user_profile")
        self.table_user_profile.setGeometry(QRect(330, 20, 256, 192))
        self.table_tags = QTableView(self.page_set)
        self.table_tags.setObjectName(u"table_tags")
        self.table_tags.setGeometry(QRect(40, 240, 256, 192))
        self.table_events = QTableView(self.page_set)
        self.table_events.setObjectName(u"table_events")
        self.table_events.setGeometry(QRect(330, 240, 256, 192))
        self.pages.addWidget(self.page_set)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.userinfo.setCurrentIndex(0)
        self.b_showhidebutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_user.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.b_calendar.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.b_events.setText(QCoreApplication.translate("MainWindow", u"Events", None))
        self.b_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.l_sidebar.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.tb_Username.setText("")
        self.tb_Username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your username here", None))
        self.l_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.tb_Password.setInputMask("")
        self.tb_Password.setText("")
        self.tb_Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password here", None))
        self.b_showhidebutton.setText("")
        self.l_Username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.l_Password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.b_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.Select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.b_delete.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.userSelect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select User", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_st.setText(QCoreApplication.translate("MainWindow", u"StartDate", None))
        self.label_et.setText(QCoreApplication.translate("MainWindow", u"EndDate", None))
        self.expandusers.setText(QCoreApplication.translate("MainWindow", u"Add Users (Expand)", None))
        self.expandcomponent.setText(QCoreApplication.translate("MainWindow", u"Add Components", None))
        self.addcomponent.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.addeventbutton.setText(QCoreApplication.translate("MainWindow", u"AddEvent", None))
    # retranslateUi

