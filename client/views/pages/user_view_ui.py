# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

from modules.touchdatetime.tdateedit import DateSelect
from modules.userlist.userlist import UserList
from . import rss_rc

class Ui_user_view(object):
    def setupUi(self, user_view):
        if not user_view.objectName():
            user_view.setObjectName(u"user_view")
        user_view.resize(635, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user_view.sizePolicy().hasHeightForWidth())
        user_view.setSizePolicy(sizePolicy)
        user_view.setMinimumSize(QSize(635, 460))
        user_view.setMaximumSize(QSize(710, 460))
        user_view.setStyleSheet(u"")
        self.user_view_option = QTabWidget(user_view)
        self.user_view_option.setObjectName(u"user_view_option")
        self.user_view_option.setGeometry(QRect(0, 0, 635, 460))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.user_view_option.setFont(font)
        self.user_view_option.setStyleSheet(u"QTabBar {\n"
"	border-bottom: 2px solid rgba(60,60,60,1); \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background: transparent;\n"
"    	border: none;\n"
"	border-top-left-radius:  4px;\n"
"	border-top-right-radius:  4px;\n"
"	padding: 4px;\n"
"    	min-width: 160px;\n"
"    	font-size: 18px;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgba(60,60,60,1); \n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"")
        self.user_view_option.setTabPosition(QTabWidget.TabPosition.North)
        self.user_view_option.setTabShape(QTabWidget.TabShape.Rounded)
        self.user_view_option.setIconSize(QSize(30, 30))
        self.user_view_option.setElideMode(Qt.TextElideMode.ElideNone)
        self.user_view_option.setUsesScrollButtons(False)
        self.user_view_option.setDocumentMode(False)
        self.user_view_option.setTabBarAutoHide(False)
        self.current_user = QWidget()
        self.current_user.setObjectName(u"current_user")
        self.current_user.setAutoFillBackground(False)
        self.current_user.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(120,120,120,1);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(30,30,30,1);\n"
"	border: 0px solid transparent;\n"
"	border-bottom: 2px solid rgba(255, 80, 80, 1);\n"
"	padding-left: 5px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QLineEdit::clear-button {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QLabel{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#current_user{\n"
"	border-radius: 0px;\n"
"}\n"
"#current_user QPushButton {\n"
"	border-bottom-right-radius: 4px; border-top-right-radius: 4px;\n"
"}\n"
"#current_user QLineEdit, #current_user QLabel {\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#current_user QPushButton {\n"
"	border-left: 1px solid white;\n"
"}\n"
"#curre"
                        "nt_user QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"}\n"
"#current_user QScrollBar::handle:horizontal {\n"
"    	background: rgba(75,150,255,1);\n"
"}")
        self.current_user_layout = QHBoxLayout(self.current_user)
        self.current_user_layout.setSpacing(0)
        self.current_user_layout.setObjectName(u"current_user_layout")
        self.current_user_layout.setContentsMargins(0, 0, 0, 0)
        self.current_spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.current_user_layout.addItem(self.current_spacer_left)

        self.log_in = QWidget(self.current_user)
        self.log_in.setObjectName(u"log_in")

        self.current_user_layout.addWidget(self.log_in)

        self.current_internal = QWidget(self.current_user)
        self.current_internal.setObjectName(u"current_internal")
        self.current_user_internal_layout = QVBoxLayout(self.current_internal)
        self.current_user_internal_layout.setSpacing(10)
        self.current_user_internal_layout.setObjectName(u"current_user_internal_layout")
        self.current_user_internal_layout.setContentsMargins(0, 10, 0, 0)
        self.header = QWidget(self.current_internal)
        self.header.setObjectName(u"header")
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setMaximumSize(QSize(380, 40))
        self.current_header = QHBoxLayout(self.header)
        self.current_header.setSpacing(0)
        self.current_header.setObjectName(u"current_header")
        self.current_header.setContentsMargins(0, 0, 0, 0)
        self.cur_user_loggedin_status = QPushButton(self.header)
        self.cur_user_loggedin_status.setObjectName(u"cur_user_loggedin_status")
        self.cur_user_loggedin_status.setEnabled(False)
        self.cur_user_loggedin_status.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(22)
        self.cur_user_loggedin_status.setFont(font1)
        self.cur_user_loggedin_status.setStyleSheet(u"border: 0px;")
        icon = QIcon()
        icon.addFile(u":/icons/user/security_slash_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/user/security_tick_green.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon.addFile(u":/icons/user/security_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon.addFile(u":/icons/user/security_tick_green.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.cur_user_loggedin_status.setIcon(icon)
        self.cur_user_loggedin_status.setIconSize(QSize(30, 30))
        self.cur_user_loggedin_status.setCheckable(True)
        self.cur_user_loggedin_status.setChecked(False)

        self.current_header.addWidget(self.cur_user_loggedin_status)

        self.cur_save_user = QPushButton(self.header)
        self.cur_save_user.setObjectName(u"cur_save_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cur_save_user.sizePolicy().hasHeightForWidth())
        self.cur_save_user.setSizePolicy(sizePolicy1)
        self.cur_save_user.setMinimumSize(QSize(0, 40))
        self.cur_save_user.setMaximumSize(QSize(16777215, 40))
        self.cur_save_user.setFont(font1)
        self.cur_save_user.setStyleSheet(u"border-radius: 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/util/tick_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/util/tick_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.cur_save_user.setIcon(icon1)
        self.cur_save_user.setIconSize(QSize(30, 30))
        self.cur_save_user.setCheckable(True)
        self.cur_save_user.setChecked(False)

        self.current_header.addWidget(self.cur_save_user)

        self.cur_change_password = QPushButton(self.header)
        self.cur_change_password.setObjectName(u"cur_change_password")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cur_change_password.sizePolicy().hasHeightForWidth())
        self.cur_change_password.setSizePolicy(sizePolicy2)
        self.cur_change_password.setMinimumSize(QSize(40, 50))
        self.cur_change_password.setMaximumSize(QSize(40, 50))
        font2 = QFont()
        font2.setPointSize(15)
        self.cur_change_password.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/util/edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon2.addFile(u":/icons/util/lock_circle_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon2.addFile(u":/icons/util/lock_circle_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon2.addFile(u":/icons/util/lock_circle_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon2.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon2.addFile(u":/icons/util/lock_circle_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon2.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.cur_change_password.setIcon(icon2)
        self.cur_change_password.setIconSize(QSize(30, 30))
        self.cur_change_password.setCheckable(True)
        self.cur_change_password.setChecked(False)

        self.current_header.addWidget(self.cur_change_password)

        self.cur_log_out = QPushButton(self.header)
        self.cur_log_out.setObjectName(u"cur_log_out")
        sizePolicy1.setHeightForWidth(self.cur_log_out.sizePolicy().hasHeightForWidth())
        self.cur_log_out.setSizePolicy(sizePolicy1)
        self.cur_log_out.setMinimumSize(QSize(0, 40))
        self.cur_log_out.setMaximumSize(QSize(16777215, 40))
        self.cur_log_out.setFont(font1)
        self.cur_log_out.setStyleSheet(u"border-radius: 0px;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/util/back_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/util/back_square1_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon3.addFile(u":/icons/util/back_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.cur_log_out.setIcon(icon3)
        self.cur_log_out.setIconSize(QSize(30, 30))
        self.cur_log_out.setCheckable(True)
        self.cur_log_out.setChecked(False)

        self.current_header.addWidget(self.cur_log_out)


        self.current_user_internal_layout.addWidget(self.header)

        self.left_pane = QWidget(self.current_internal)
        self.left_pane.setObjectName(u"left_pane")
        sizePolicy.setHeightForWidth(self.left_pane.sizePolicy().hasHeightForWidth())
        self.left_pane.setSizePolicy(sizePolicy)
        self.left_pane.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout = QVBoxLayout(self.left_pane)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.user_current_icon = QWidget(self.left_pane)
        self.user_current_icon.setObjectName(u"user_current_icon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.user_current_icon.sizePolicy().hasHeightForWidth())
        self.user_current_icon.setSizePolicy(sizePolicy3)
        self.user_current_icon.setMinimumSize(QSize(0, 110))
        self.user_current_icon_layout = QHBoxLayout(self.user_current_icon)
        self.user_current_icon_layout.setSpacing(0)
        self.user_current_icon_layout.setObjectName(u"user_current_icon_layout")
        self.user_current_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_icon_spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.user_current_icon_layout.addItem(self.cur_icon_spacer_left)

        self.cur_icon_view = QGraphicsView(self.user_current_icon)
        self.cur_icon_view.setObjectName(u"cur_icon_view")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cur_icon_view.sizePolicy().hasHeightForWidth())
        self.cur_icon_view.setSizePolicy(sizePolicy4)
        self.cur_icon_view.setMinimumSize(QSize(110, 110))
        self.cur_icon_view.setMaximumSize(QSize(110, 110))
        self.cur_icon_view.setStyleSheet(u"border: 2px solid grey;\n"
"border-radius: 4px;\n"
"padding: 2px;")

        self.user_current_icon_layout.addWidget(self.cur_icon_view)

        self.cur_icon_change_pushbutton = QPushButton(self.user_current_icon)
        self.cur_icon_change_pushbutton.setObjectName(u"cur_icon_change_pushbutton")
        sizePolicy2.setHeightForWidth(self.cur_icon_change_pushbutton.sizePolicy().hasHeightForWidth())
        self.cur_icon_change_pushbutton.setSizePolicy(sizePolicy2)
        self.cur_icon_change_pushbutton.setMinimumSize(QSize(40, 0))
        self.cur_icon_change_pushbutton.setMaximumSize(QSize(40, 16777215))
        self.cur_icon_change_pushbutton.setFont(font2)
        self.cur_icon_change_pushbutton.setStyleSheet(u"border-left: 0px;")
        self.cur_icon_change_pushbutton.setIcon(icon2)
        self.cur_icon_change_pushbutton.setIconSize(QSize(30, 30))
        self.cur_icon_change_pushbutton.setCheckable(True)
        self.cur_icon_change_pushbutton.setChecked(False)

        self.user_current_icon_layout.addWidget(self.cur_icon_change_pushbutton)

        self.cur_icon_spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.user_current_icon_layout.addItem(self.cur_icon_spacer_right)


        self.verticalLayout.addWidget(self.user_current_icon)

        self.cur_username = QWidget(self.left_pane)
        self.cur_username.setObjectName(u"cur_username")
        self.cur_username.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cur_username.sizePolicy().hasHeightForWidth())
        self.cur_username.setSizePolicy(sizePolicy)
        self.cur_username.setMinimumSize(QSize(312, 0))
        self.cur_username.setMaximumSize(QSize(350, 16777215))
        font3 = QFont()
        font3.setFamilies([u"American Typewriter"])
        font3.setPointSize(20)
        self.cur_username.setFont(font3)
        self.cur_username_layout = QVBoxLayout(self.cur_username)
        self.cur_username_layout.setSpacing(0)
        self.cur_username_layout.setObjectName(u"cur_username_layout")
        self.cur_username_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_username_view = QWidget(self.cur_username)
        self.cur_username_view.setObjectName(u"cur_username_view")
        sizePolicy.setHeightForWidth(self.cur_username_view.sizePolicy().hasHeightForWidth())
        self.cur_username_view.setSizePolicy(sizePolicy)
        self.cur_username_view.setMinimumSize(QSize(312, 50))
        self.cur_username_view.setMaximumSize(QSize(350, 50))
        self.cur_username_view.setStyleSheet(u"")
        self.cur_username_view_container = QHBoxLayout(self.cur_username_view)
        self.cur_username_view_container.setSpacing(0)
        self.cur_username_view_container.setObjectName(u"cur_username_view_container")
        self.cur_username_view_container.setContentsMargins(0, 0, 0, 0)
        self.cur_username_view_wrapper = QScrollArea(self.cur_username_view)
        self.cur_username_view_wrapper.setObjectName(u"cur_username_view_wrapper")
        self.cur_username_view_wrapper.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cur_username_view_wrapper.sizePolicy().hasHeightForWidth())
        self.cur_username_view_wrapper.setSizePolicy(sizePolicy5)
        self.cur_username_view_wrapper.setMinimumSize(QSize(272, 50))
        self.cur_username_view_wrapper.setMaximumSize(QSize(350, 50))
        self.cur_username_view_wrapper.setAutoFillBackground(False)
        self.cur_username_view_wrapper.setStyleSheet(u"#title_label_container { \n"
"	background: rgba(20,20,20,1);\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height:  2px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::groove:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height: 2px;\n"
"    margin: 0px;\n"
"}")
        self.cur_username_view_wrapper.setFrameShape(QFrame.Shape.Box)
        self.cur_username_view_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.cur_username_view_wrapper.setLineWidth(0)
        self.cur_username_view_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.cur_username_view_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.cur_username_view_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.cur_username_view_wrapper.setWidgetResizable(False)
        self.cur_username_label_container = QWidget()
        self.cur_username_label_container.setObjectName(u"cur_username_label_container")
        self.cur_username_label_container.setGeometry(QRect(0, 0, 350, 48))
        sizePolicy3.setHeightForWidth(self.cur_username_label_container.sizePolicy().hasHeightForWidth())
        self.cur_username_label_container.setSizePolicy(sizePolicy3)
        self.cur_username_label_container.setMinimumSize(QSize(350, 48))
        self.cur_username_label_container.setMaximumSize(QSize(350, 48))
        self.cur_username_label_layout = QHBoxLayout(self.cur_username_label_container)
        self.cur_username_label_layout.setSpacing(0)
        self.cur_username_label_layout.setObjectName(u"cur_username_label_layout")
        self.cur_username_label_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_username_label = QLabel(self.cur_username_label_container)
        self.cur_username_label.setObjectName(u"cur_username_label")
        sizePolicy1.setHeightForWidth(self.cur_username_label.sizePolicy().hasHeightForWidth())
        self.cur_username_label.setSizePolicy(sizePolicy1)
        self.cur_username_label.setMinimumSize(QSize(350, 48))
        self.cur_username_label.setMaximumSize(QSize(800, 48))
        self.cur_username_label.setBaseSize(QSize(212, 48))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(27)
        self.cur_username_label.setFont(font4)

        self.cur_username_label_layout.addWidget(self.cur_username_label)

        self.cur_username_view_wrapper.setWidget(self.cur_username_label_container)

        self.cur_username_view_container.addWidget(self.cur_username_view_wrapper)

        self.cur_username_edit_button = QPushButton(self.cur_username_view)
        self.cur_username_edit_button.setObjectName(u"cur_username_edit_button")
        sizePolicy2.setHeightForWidth(self.cur_username_edit_button.sizePolicy().hasHeightForWidth())
        self.cur_username_edit_button.setSizePolicy(sizePolicy2)
        self.cur_username_edit_button.setMinimumSize(QSize(40, 50))
        self.cur_username_edit_button.setMaximumSize(QSize(40, 50))
        self.cur_username_edit_button.setFont(font2)
        self.cur_username_edit_button.setIcon(icon2)
        self.cur_username_edit_button.setIconSize(QSize(30, 30))
        self.cur_username_edit_button.setCheckable(True)
        self.cur_username_edit_button.setChecked(False)

        self.cur_username_view_container.addWidget(self.cur_username_edit_button)


        self.cur_username_layout.addWidget(self.cur_username_view)

        self.cur_username_edit = QWidget(self.cur_username)
        self.cur_username_edit.setObjectName(u"cur_username_edit")
        self.cur_username_edit.setMinimumSize(QSize(312, 50))
        self.cur_username_edit.setMaximumSize(QSize(350, 50))
        self.username_edit_layout = QHBoxLayout(self.cur_username_edit)
        self.username_edit_layout.setSpacing(0)
        self.username_edit_layout.setObjectName(u"username_edit_layout")
        self.username_edit_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_username_lineedit = QLineEdit(self.cur_username_edit)
        self.cur_username_lineedit.setObjectName(u"cur_username_lineedit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cur_username_lineedit.sizePolicy().hasHeightForWidth())
        self.cur_username_lineedit.setSizePolicy(sizePolicy6)
        self.cur_username_lineedit.setMinimumSize(QSize(272, 50))
        self.cur_username_lineedit.setMaximumSize(QSize(310, 50))
        self.cur_username_lineedit.setFont(font4)
        self.cur_username_lineedit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.cur_username_lineedit.setMaxLength(32767)
        self.cur_username_lineedit.setClearButtonEnabled(True)

        self.username_edit_layout.addWidget(self.cur_username_lineedit)

        self.cur_keyboard_button = QPushButton(self.cur_username_edit)
        self.cur_keyboard_button.setObjectName(u"cur_keyboard_button")
        sizePolicy2.setHeightForWidth(self.cur_keyboard_button.sizePolicy().hasHeightForWidth())
        self.cur_keyboard_button.setSizePolicy(sizePolicy2)
        self.cur_keyboard_button.setMinimumSize(QSize(40, 50))
        self.cur_keyboard_button.setMaximumSize(QSize(40, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons/util/keyboard_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.cur_keyboard_button.setIcon(icon4)
        self.cur_keyboard_button.setIconSize(QSize(30, 30))
        self.cur_keyboard_button.setCheckable(True)

        self.username_edit_layout.addWidget(self.cur_keyboard_button)


        self.cur_username_layout.addWidget(self.cur_username_edit)


        self.verticalLayout.addWidget(self.cur_username)

        self.cur_pin = QWidget(self.left_pane)
        self.cur_pin.setObjectName(u"cur_pin")
        self.cur_pin.setEnabled(True)
        sizePolicy.setHeightForWidth(self.cur_pin.sizePolicy().hasHeightForWidth())
        self.cur_pin.setSizePolicy(sizePolicy)
        self.cur_pin.setMinimumSize(QSize(312, 0))
        self.cur_pin.setMaximumSize(QSize(350, 16777215))
        self.cur_pin.setFont(font3)
        self.cur_pin_layout = QVBoxLayout(self.cur_pin)
        self.cur_pin_layout.setSpacing(0)
        self.cur_pin_layout.setObjectName(u"cur_pin_layout")
        self.cur_pin_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_pin_view = QWidget(self.cur_pin)
        self.cur_pin_view.setObjectName(u"cur_pin_view")
        sizePolicy.setHeightForWidth(self.cur_pin_view.sizePolicy().hasHeightForWidth())
        self.cur_pin_view.setSizePolicy(sizePolicy)
        self.cur_pin_view.setMinimumSize(QSize(312, 50))
        self.cur_pin_view.setMaximumSize(QSize(350, 50))
        self.cur_pin_view.setStyleSheet(u"")
        self.cur_pin_view_layout = QHBoxLayout(self.cur_pin_view)
        self.cur_pin_view_layout.setSpacing(0)
        self.cur_pin_view_layout.setObjectName(u"cur_pin_view_layout")
        self.cur_pin_view_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_pin_view_wrapper = QScrollArea(self.cur_pin_view)
        self.cur_pin_view_wrapper.setObjectName(u"cur_pin_view_wrapper")
        self.cur_pin_view_wrapper.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.cur_pin_view_wrapper.sizePolicy().hasHeightForWidth())
        self.cur_pin_view_wrapper.setSizePolicy(sizePolicy5)
        self.cur_pin_view_wrapper.setMinimumSize(QSize(272, 50))
        self.cur_pin_view_wrapper.setMaximumSize(QSize(350, 50))
        self.cur_pin_view_wrapper.setAutoFillBackground(False)
        self.cur_pin_view_wrapper.setStyleSheet(u"#title_label_container { \n"
"	background: rgba(20,20,20,1);\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height:  2px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::groove:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height: 2px;\n"
"    margin: 0px;\n"
"}")
        self.cur_pin_view_wrapper.setFrameShape(QFrame.Shape.Box)
        self.cur_pin_view_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.cur_pin_view_wrapper.setLineWidth(0)
        self.cur_pin_view_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.cur_pin_view_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.cur_pin_view_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.cur_pin_view_wrapper.setWidgetResizable(False)
        self.cur_pin_label_container = QWidget()
        self.cur_pin_label_container.setObjectName(u"cur_pin_label_container")
        self.cur_pin_label_container.setGeometry(QRect(0, 0, 723, 48))
        sizePolicy3.setHeightForWidth(self.cur_pin_label_container.sizePolicy().hasHeightForWidth())
        self.cur_pin_label_container.setSizePolicy(sizePolicy3)
        self.cur_pin_label_container.setMinimumSize(QSize(272, 48))
        self.cur_pin_label_container.setMaximumSize(QSize(16777215, 48))
        self.cur_pin_label_layout = QHBoxLayout(self.cur_pin_label_container)
        self.cur_pin_label_layout.setSpacing(0)
        self.cur_pin_label_layout.setObjectName(u"cur_pin_label_layout")
        self.cur_pin_label_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_pin_label = QLabel(self.cur_pin_label_container)
        self.cur_pin_label.setObjectName(u"cur_pin_label")
        sizePolicy1.setHeightForWidth(self.cur_pin_label.sizePolicy().hasHeightForWidth())
        self.cur_pin_label.setSizePolicy(sizePolicy1)
        self.cur_pin_label.setMinimumSize(QSize(350, 48))
        self.cur_pin_label.setMaximumSize(QSize(800, 48))
        self.cur_pin_label.setBaseSize(QSize(212, 48))
        self.cur_pin_label.setFont(font4)

        self.cur_pin_label_layout.addWidget(self.cur_pin_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.cur_pin_view_wrapper.setWidget(self.cur_pin_label_container)

        self.cur_pin_view_layout.addWidget(self.cur_pin_view_wrapper)

        self.cur_pin_edit_button = QPushButton(self.cur_pin_view)
        self.cur_pin_edit_button.setObjectName(u"cur_pin_edit_button")
        sizePolicy2.setHeightForWidth(self.cur_pin_edit_button.sizePolicy().hasHeightForWidth())
        self.cur_pin_edit_button.setSizePolicy(sizePolicy2)
        self.cur_pin_edit_button.setMinimumSize(QSize(40, 50))
        self.cur_pin_edit_button.setMaximumSize(QSize(40, 50))
        self.cur_pin_edit_button.setFont(font2)
        self.cur_pin_edit_button.setIcon(icon2)
        self.cur_pin_edit_button.setIconSize(QSize(30, 30))
        self.cur_pin_edit_button.setCheckable(True)
        self.cur_pin_edit_button.setChecked(False)

        self.cur_pin_view_layout.addWidget(self.cur_pin_edit_button)


        self.cur_pin_layout.addWidget(self.cur_pin_view)

        self.cur_pin_edit = QWidget(self.cur_pin)
        self.cur_pin_edit.setObjectName(u"cur_pin_edit")
        self.cur_pin_edit.setMinimumSize(QSize(312, 50))
        self.cur_pin_edit.setMaximumSize(QSize(350, 50))
        self.cur_pin_edit_layout = QHBoxLayout(self.cur_pin_edit)
        self.cur_pin_edit_layout.setSpacing(0)
        self.cur_pin_edit_layout.setObjectName(u"cur_pin_edit_layout")
        self.cur_pin_edit_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_pin_lineedit = QLineEdit(self.cur_pin_edit)
        self.cur_pin_lineedit.setObjectName(u"cur_pin_lineedit")
        sizePolicy6.setHeightForWidth(self.cur_pin_lineedit.sizePolicy().hasHeightForWidth())
        self.cur_pin_lineedit.setSizePolicy(sizePolicy6)
        self.cur_pin_lineedit.setMinimumSize(QSize(252, 50))
        self.cur_pin_lineedit.setMaximumSize(QSize(300, 50))
        self.cur_pin_lineedit.setFont(font4)
        self.cur_pin_lineedit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.cur_pin_lineedit.setMaxLength(6)
        self.cur_pin_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.cur_pin_lineedit.setClearButtonEnabled(True)

        self.cur_pin_edit_layout.addWidget(self.cur_pin_lineedit)

        self.cur_pin_showhide = QPushButton(self.cur_pin_edit)
        self.cur_pin_showhide.setObjectName(u"cur_pin_showhide")
        sizePolicy4.setHeightForWidth(self.cur_pin_showhide.sizePolicy().hasHeightForWidth())
        self.cur_pin_showhide.setSizePolicy(sizePolicy4)
        self.cur_pin_showhide.setMinimumSize(QSize(40, 50))
        self.cur_pin_showhide.setMaximumSize(QSize(40, 50))
        icon5 = QIcon()
        icon5.addFile(u":/icons/util/eye_slash_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/util/eye_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.cur_pin_showhide.setIcon(icon5)
        self.cur_pin_showhide.setIconSize(QSize(30, 30))
        self.cur_pin_showhide.setCheckable(True)
        self.cur_pin_showhide.setChecked(False)

        self.cur_pin_edit_layout.addWidget(self.cur_pin_showhide)

        self.cur_pin_keyboard = QPushButton(self.cur_pin_edit)
        self.cur_pin_keyboard.setObjectName(u"cur_pin_keyboard")
        sizePolicy2.setHeightForWidth(self.cur_pin_keyboard.sizePolicy().hasHeightForWidth())
        self.cur_pin_keyboard.setSizePolicy(sizePolicy2)
        self.cur_pin_keyboard.setMinimumSize(QSize(40, 50))
        self.cur_pin_keyboard.setMaximumSize(QSize(40, 50))
        self.cur_pin_keyboard.setIcon(icon4)
        self.cur_pin_keyboard.setIconSize(QSize(30, 30))
        self.cur_pin_keyboard.setCheckable(True)

        self.cur_pin_edit_layout.addWidget(self.cur_pin_keyboard)


        self.cur_pin_layout.addWidget(self.cur_pin_edit)


        self.verticalLayout.addWidget(self.cur_pin)


        self.current_user_internal_layout.addWidget(self.left_pane)


        self.current_user_layout.addWidget(self.current_internal)

        self.current_spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.current_user_layout.addItem(self.current_spacer_right)

        icon6 = QIcon()
        icon6.addFile(u":/icons/user/nav/user_current_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/user/nav/user_current_selected.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon6.addFile(u":/icons/user/nav/user_current_selected.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon6.addFile(u":/icons/user/nav/user_current_selected.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.user_view_option.addTab(self.current_user, icon6, "")
        self.select_user = QWidget()
        self.select_user.setObjectName(u"select_user")
        self.select_user_container = QVBoxLayout(self.select_user)
        self.select_user_container.setSpacing(0)
        self.select_user_container.setObjectName(u"select_user_container")
        self.select_user_container.setContentsMargins(0, 0, 0, 0)
        self.user_select_wrapper = QScrollArea(self.select_user)
        self.user_select_wrapper.setObjectName(u"user_select_wrapper")
        self.user_select_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.user_select_wrapper.setLineWidth(0)
        self.user_select_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.user_select_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.user_select_wrapper.setWidgetResizable(True)
        self.user_list = UserList()
        self.user_list.setObjectName(u"user_list")
        self.user_list.setGeometry(QRect(0, 0, 635, 420))
        sizePolicy3.setHeightForWidth(self.user_list.sizePolicy().hasHeightForWidth())
        self.user_list.setSizePolicy(sizePolicy3)
        self.user_list.setMinimumSize(QSize(0, 420))
        self.user_list.setMaximumSize(QSize(16777215, 420))
        self.user_select_wrapper.setWidget(self.user_list)

        self.select_user_container.addWidget(self.user_select_wrapper)

        icon7 = QIcon()
        icon7.addFile(u":/icons/user/nav/user_select_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/user/nav/user_select_selected.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.user_view_option.addTab(self.select_user, icon7, "")
        self.add_user = QWidget()
        self.add_user.setObjectName(u"add_user")
        self.add_user_layout = QVBoxLayout(self.add_user)
        self.add_user_layout.setSpacing(10)
        self.add_user_layout.setObjectName(u"add_user_layout")
        self.add_user_layout.setContentsMargins(0, 0, 0, 0)
        self.add_user_header = QWidget(self.add_user)
        self.add_user_header.setObjectName(u"add_user_header")
        sizePolicy1.setHeightForWidth(self.add_user_header.sizePolicy().hasHeightForWidth())
        self.add_user_header.setSizePolicy(sizePolicy1)
        self.add_user_header.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(120,120,120,1);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(30,30,30,1);\n"
"	border: 0px solid transparent;\n"
"	border-bottom: 2px solid rgba(255, 80, 80, 1);\n"
"	padding-left: 5px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QLineEdit::clear-button {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QLabel{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}")
        self.gridLayout = QGridLayout(self.add_user_header)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.user_password = QWidget(self.add_user_header)
        self.user_password.setObjectName(u"user_password")
        sizePolicy.setHeightForWidth(self.user_password.sizePolicy().hasHeightForWidth())
        self.user_password.setSizePolicy(sizePolicy)
        self.user_password.setMinimumSize(QSize(0, 40))
        self.user_password.setMaximumSize(QSize(16777215, 40))
        self.user_password_layout = QHBoxLayout(self.user_password)
        self.user_password_layout.setSpacing(0)
        self.user_password_layout.setObjectName(u"user_password_layout")
        self.user_password_layout.setContentsMargins(0, 0, 0, 0)
        self.user_password_icon = QPushButton(self.user_password)
        self.user_password_icon.setObjectName(u"user_password_icon")
        self.user_password_icon.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.user_password_icon.sizePolicy().hasHeightForWidth())
        self.user_password_icon.setSizePolicy(sizePolicy4)
        self.user_password_icon.setMinimumSize(QSize(40, 40))
        self.user_password_icon.setMaximumSize(QSize(40, 40))
        icon8 = QIcon()
        icon8.addFile(u":/icons/user/security_password_light.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon8.addFile(u":/icons/user/security_tick_blue.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.user_password_icon.setIcon(icon8)
        self.user_password_icon.setIconSize(QSize(30, 30))
        self.user_password_icon.setCheckable(True)
        self.user_password_icon.setChecked(False)

        self.user_password_layout.addWidget(self.user_password_icon)

        self.user_password_lineedit = QLineEdit(self.user_password)
        self.user_password_lineedit.setObjectName(u"user_password_lineedit")
        self.user_password_lineedit.setMinimumSize(QSize(0, 40))
        self.user_password_lineedit.setMaximumSize(QSize(16777215, 40))
        self.user_password_lineedit.setFont(font)
        self.user_password_lineedit.setMaxLength(32767)
        self.user_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_password_lineedit.setDragEnabled(True)

        self.user_password_layout.addWidget(self.user_password_lineedit)

        self.user_password_showhide = QPushButton(self.user_password)
        self.user_password_showhide.setObjectName(u"user_password_showhide")
        sizePolicy4.setHeightForWidth(self.user_password_showhide.sizePolicy().hasHeightForWidth())
        self.user_password_showhide.setSizePolicy(sizePolicy4)
        self.user_password_showhide.setMinimumSize(QSize(40, 40))
        self.user_password_showhide.setMaximumSize(QSize(40, 40))
        self.user_password_showhide.setIcon(icon5)
        self.user_password_showhide.setIconSize(QSize(30, 30))
        self.user_password_showhide.setCheckable(True)
        self.user_password_showhide.setChecked(False)

        self.user_password_layout.addWidget(self.user_password_showhide)


        self.gridLayout.addWidget(self.user_password, 2, 0, 1, 1)

        self.user_username = QWidget(self.add_user_header)
        self.user_username.setObjectName(u"user_username")
        sizePolicy1.setHeightForWidth(self.user_username.sizePolicy().hasHeightForWidth())
        self.user_username.setSizePolicy(sizePolicy1)
        self.user_username.setMinimumSize(QSize(0, 40))
        self.user_username.setMaximumSize(QSize(16777215, 40))
        self.user_username.setStyleSheet(u"")
        self.user_username_layout = QHBoxLayout(self.user_username)
        self.user_username_layout.setSpacing(0)
        self.user_username_layout.setObjectName(u"user_username_layout")
        self.user_username_layout.setContentsMargins(0, 0, 0, 0)
        self.user_username_icon = QPushButton(self.user_username)
        self.user_username_icon.setObjectName(u"user_username_icon")
        self.user_username_icon.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.user_username_icon.sizePolicy().hasHeightForWidth())
        self.user_username_icon.setSizePolicy(sizePolicy4)
        self.user_username_icon.setMinimumSize(QSize(40, 40))
        self.user_username_icon.setMaximumSize(QSize(40, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/user/security_user_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon9.addFile(u":/icons/user/security_tick_blue.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.user_username_icon.setIcon(icon9)
        self.user_username_icon.setIconSize(QSize(30, 30))
        self.user_username_icon.setCheckable(True)
        self.user_username_icon.setChecked(False)

        self.user_username_layout.addWidget(self.user_username_icon)

        self.user_select_username = QLineEdit(self.user_username)
        self.user_select_username.setObjectName(u"user_select_username")
        self.user_select_username.setMinimumSize(QSize(0, 40))
        self.user_select_username.setMaximumSize(QSize(16777215, 40))
        self.user_select_username.setFont(font)
        self.user_select_username.setStyleSheet(u"")
        self.user_select_username.setMaxLength(32767)
        self.user_select_username.setDragEnabled(True)

        self.user_username_layout.addWidget(self.user_select_username)


        self.gridLayout.addWidget(self.user_username, 0, 0, 1, 1)

        self.user_surname = QLineEdit(self.add_user_header)
        self.user_surname.setObjectName(u"user_surname")
        self.user_surname.setMinimumSize(QSize(0, 40))
        self.user_surname.setMaximumSize(QSize(16777215, 40))
        self.user_surname.setFont(font)
        self.user_surname.setDragEnabled(True)

        self.gridLayout.addWidget(self.user_surname, 2, 1, 1, 1)

        self.user_pin = QWidget(self.add_user_header)
        self.user_pin.setObjectName(u"user_pin")
        sizePolicy1.setHeightForWidth(self.user_pin.sizePolicy().hasHeightForWidth())
        self.user_pin.setSizePolicy(sizePolicy1)
        self.user_pin.setMinimumSize(QSize(0, 40))
        self.user_pin.setMaximumSize(QSize(16777215, 40))
        self.user_username_layout_2 = QHBoxLayout(self.user_pin)
        self.user_username_layout_2.setSpacing(0)
        self.user_username_layout_2.setObjectName(u"user_username_layout_2")
        self.user_username_layout_2.setContentsMargins(0, 0, 0, 0)
        self.user_pin_icon = QPushButton(self.user_pin)
        self.user_pin_icon.setObjectName(u"user_pin_icon")
        self.user_pin_icon.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.user_pin_icon.sizePolicy().hasHeightForWidth())
        self.user_pin_icon.setSizePolicy(sizePolicy4)
        self.user_pin_icon.setMinimumSize(QSize(40, 40))
        self.user_pin_icon.setMaximumSize(QSize(40, 40))
        icon10 = QIcon()
        icon10.addFile(u":/icons/user/security_pin_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon10.addFile(u":/icons/user/security_tick_blue.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.user_pin_icon.setIcon(icon10)
        self.user_pin_icon.setIconSize(QSize(30, 30))
        self.user_pin_icon.setCheckable(True)
        self.user_pin_icon.setChecked(False)

        self.user_username_layout_2.addWidget(self.user_pin_icon)

        self.user_pin_lineedit = QLineEdit(self.user_pin)
        self.user_pin_lineedit.setObjectName(u"user_pin_lineedit")
        self.user_pin_lineedit.setMinimumSize(QSize(0, 40))
        self.user_pin_lineedit.setMaximumSize(QSize(16777215, 40))
        self.user_pin_lineedit.setFont(font)
        self.user_pin_lineedit.setMaxLength(6)
        self.user_pin_lineedit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.user_pin_lineedit.setDragEnabled(True)

        self.user_username_layout_2.addWidget(self.user_pin_lineedit)


        self.gridLayout.addWidget(self.user_pin, 3, 0, 1, 1)

        self.user_forename = QLineEdit(self.add_user_header)
        self.user_forename.setObjectName(u"user_forename")
        self.user_forename.setMinimumSize(QSize(0, 40))
        self.user_forename.setMaximumSize(QSize(16777215, 40))
        self.user_forename.setFont(font)
        self.user_forename.setDragEnabled(True)

        self.gridLayout.addWidget(self.user_forename, 0, 1, 1, 1)


        self.add_user_layout.addWidget(self.add_user_header)

        self.add_user_footer = QWidget(self.add_user)
        self.add_user_footer.setObjectName(u"add_user_footer")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.add_user_footer.sizePolicy().hasHeightForWidth())
        self.add_user_footer.setSizePolicy(sizePolicy7)
        self.footer_layout = QHBoxLayout(self.add_user_footer)
        self.footer_layout.setSpacing(10)
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.user_DoB = QWidget(self.add_user_footer)
        self.user_DoB.setObjectName(u"user_DoB")
        sizePolicy5.setHeightForWidth(self.user_DoB.sizePolicy().hasHeightForWidth())
        self.user_DoB.setSizePolicy(sizePolicy5)
        self.user_dob_layout = QVBoxLayout(self.user_DoB)
        self.user_dob_layout.setSpacing(0)
        self.user_dob_layout.setObjectName(u"user_dob_layout")
        self.user_dob_layout.setContentsMargins(0, 0, 0, 0)
        self.user_DoB_label = QLabel(self.user_DoB)
        self.user_DoB_label.setObjectName(u"user_DoB_label")
        self.user_DoB_label.setMinimumSize(QSize(0, 30))
        self.user_DoB_label.setMaximumSize(QSize(16777215, 30))
        self.user_DoB_label.setSizeIncrement(QSize(0, 0))
        self.user_DoB_label.setBaseSize(QSize(0, 0))
        self.user_DoB_label.setFont(font)
        self.user_DoB_label.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QLabel{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}")
        self.user_DoB_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.user_dob_layout.addWidget(self.user_DoB_label)

        self.user_DoB_DateSelect = DateSelect(self.user_DoB)
        self.user_DoB_DateSelect.setObjectName(u"user_DoB_DateSelect")
        self.user_DoB_DateSelect.setSelectedDate(QDate(2002, 1, 1))

        self.user_dob_layout.addWidget(self.user_DoB_DateSelect)


        self.footer_layout.addWidget(self.user_DoB)

        self.add_and_icon = QWidget(self.add_user_footer)
        self.add_and_icon.setObjectName(u"add_and_icon")
        sizePolicy4.setHeightForWidth(self.add_and_icon.sizePolicy().hasHeightForWidth())
        self.add_and_icon.setSizePolicy(sizePolicy4)
        self.add_and_icon.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(120,120,120,1);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(30,30,30,1);\n"
"	border: 0px solid transparent;\n"
"	border-bottom: 2px solid rgba(255, 80, 80, 1);\n"
"	padding-left: 5px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QLineEdit::clear-button {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QLabel{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#current_user{\n"
"	border-radius: 0px;\n"
"}\n"
"#current_user QPushButton {\n"
"	border-bottom-right-radius: 4px; border-top-right-radius: 4px;\n"
"}\n"
"#current_user QLineEdit, #current_user QLabel {\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#current_user QPushButton {\n"
"	border-left: 1px solid white;\n"
"}\n"
"#curre"
                        "nt_user QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"}\n"
"#current_user QScrollBar::handle:horizontal {\n"
"    	background: rgba(75,150,255,1);\n"
"}")
        self.add_and_icon_layout = QVBoxLayout(self.add_and_icon)
        self.add_and_icon_layout.setSpacing(0)
        self.add_and_icon_layout.setObjectName(u"add_and_icon_layout")
        self.add_and_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_select = QWidget(self.add_and_icon)
        self.icon_select.setObjectName(u"icon_select")
        sizePolicy.setHeightForWidth(self.icon_select.sizePolicy().hasHeightForWidth())
        self.icon_select.setSizePolicy(sizePolicy)
        self.icon_select.setMinimumSize(QSize(110, 150))
        self.icon_select.setMaximumSize(QSize(16777215, 150))
        self.icon_select.setFont(font)
        self.icon_select_layout = QVBoxLayout(self.icon_select)
        self.icon_select_layout.setSpacing(0)
        self.icon_select_layout.setObjectName(u"icon_select_layout")
        self.icon_select_layout.setContentsMargins(0, 0, 0, 0)
        self.new_icon_view = QGraphicsView(self.icon_select)
        self.new_icon_view.setObjectName(u"new_icon_view")
        sizePolicy4.setHeightForWidth(self.new_icon_view.sizePolicy().hasHeightForWidth())
        self.new_icon_view.setSizePolicy(sizePolicy4)
        self.new_icon_view.setMinimumSize(QSize(110, 110))
        self.new_icon_view.setMaximumSize(QSize(110, 110))
        self.new_icon_view.setStyleSheet(u"border: 2px solid grey;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.new_icon_view.setFrameShadow(QFrame.Shadow.Plain)

        self.icon_select_layout.addWidget(self.new_icon_view)

        self.new_icon_change_pushbutton = QPushButton(self.icon_select)
        self.new_icon_change_pushbutton.setObjectName(u"new_icon_change_pushbutton")
        self.new_icon_change_pushbutton.setMinimumSize(QSize(110, 40))
        self.new_icon_change_pushbutton.setMaximumSize(QSize(110, 40))
        font5 = QFont()
        font5.setPointSize(18)
        self.new_icon_change_pushbutton.setFont(font5)
        icon11 = QIcon()
        icon11.addFile(u":/icons/arrows/arrow_down_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/arrows/arrow_down_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.new_icon_change_pushbutton.setIcon(icon11)
        self.new_icon_change_pushbutton.setIconSize(QSize(20, 20))
        self.new_icon_change_pushbutton.setCheckable(True)

        self.icon_select_layout.addWidget(self.new_icon_change_pushbutton)


        self.add_and_icon_layout.addWidget(self.icon_select)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.add_and_icon_layout.addItem(self.verticalSpacer)

        self.user_add_button = QPushButton(self.add_and_icon)
        self.user_add_button.setObjectName(u"user_add_button")
        sizePolicy4.setHeightForWidth(self.user_add_button.sizePolicy().hasHeightForWidth())
        self.user_add_button.setSizePolicy(sizePolicy4)
        self.user_add_button.setMinimumSize(QSize(110, 110))
        self.user_add_button.setMaximumSize(QSize(110, 110))
        icon12 = QIcon()
        icon12.addFile(u":/icons/util/add_2_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_add_button.setIcon(icon12)
        self.user_add_button.setIconSize(QSize(40, 40))

        self.add_and_icon_layout.addWidget(self.user_add_button)


        self.footer_layout.addWidget(self.add_and_icon)


        self.add_user_layout.addWidget(self.add_user_footer)

        icon13 = QIcon()
        icon13.addFile(u":/icons/user/nav/user_add_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/user/nav/user_add_selected.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.user_view_option.addTab(self.add_user, icon13, "")

        self.retranslateUi(user_view)
        self.cur_username_edit_button.toggled.connect(self.cur_username_edit.setVisible)
        self.cur_username_edit_button.toggled.connect(self.cur_username_view.setHidden)
        self.cur_username_lineedit.editingFinished.connect(self.cur_username_edit_button.toggle)
        self.cur_user_loggedin_status.toggled.connect(self.cur_username_edit_button.setEnabled)
        self.cur_user_loggedin_status.toggled.connect(self.cur_icon_change_pushbutton.setEnabled)
        self.cur_user_loggedin_status.toggled.connect(self.cur_pin_edit_button.setEnabled)
        self.cur_pin_lineedit.editingFinished.connect(self.cur_pin_edit_button.toggle)
        self.cur_pin_edit_button.toggled.connect(self.cur_pin_edit.setVisible)
        self.cur_pin_edit_button.toggled.connect(self.cur_pin_view.setHidden)
        self.cur_user_loggedin_status.toggled.connect(self.cur_username_edit_button.setVisible)
        self.cur_user_loggedin_status.toggled.connect(self.cur_pin_edit_button.setVisible)
        self.cur_user_loggedin_status.toggled.connect(self.cur_change_password.setVisible)
        self.cur_user_loggedin_status.toggled.connect(self.cur_change_password.setEnabled)

        self.user_view_option.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(user_view)
    # setupUi

    def retranslateUi(self, user_view):
        user_view.setWindowTitle(QCoreApplication.translate("user_view", u"Form", None))
        self.cur_user_loggedin_status.setText("")
        self.cur_save_user.setText(QCoreApplication.translate("user_view", u"Save", None))
        self.cur_change_password.setText(QCoreApplication.translate("user_view", u"Change Password", None))
        self.cur_log_out.setText(QCoreApplication.translate("user_view", u"Log out", None))
        self.cur_icon_change_pushbutton.setText("")
        self.cur_username_label.setText(QCoreApplication.translate("user_view", u"Username", None))
        self.cur_username_edit_button.setText("")
        self.cur_username_lineedit.setText("")
        self.cur_username_lineedit.setPlaceholderText(QCoreApplication.translate("user_view", u"Username", None))
        self.cur_keyboard_button.setText("")
        self.cur_pin_label.setText(QCoreApplication.translate("user_view", u"Pin", None))
        self.cur_pin_edit_button.setText("")
        self.cur_pin_lineedit.setInputMask(QCoreApplication.translate("user_view", u"999999", None))
        self.cur_pin_lineedit.setText("")
        self.cur_pin_lineedit.setPlaceholderText("")
        self.cur_pin_showhide.setText("")
        self.cur_pin_keyboard.setText("")
        self.user_view_option.setTabText(self.user_view_option.indexOf(self.current_user), QCoreApplication.translate("user_view", u"Current", None))
        self.user_view_option.setTabText(self.user_view_option.indexOf(self.select_user), QCoreApplication.translate("user_view", u"Select", None))
        self.user_password_icon.setText("")
        self.user_password_lineedit.setPlaceholderText(QCoreApplication.translate("user_view", u"Password", None))
        self.user_password_showhide.setText("")
        self.user_username_icon.setText("")
        self.user_select_username.setPlaceholderText(QCoreApplication.translate("user_view", u"Username", None))
        self.user_surname.setInputMask(QCoreApplication.translate("user_view", u"Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", None))
        self.user_surname.setText("")
        self.user_surname.setPlaceholderText(QCoreApplication.translate("user_view", u"Surname", None))
        self.user_pin_icon.setText("")
        self.user_pin_lineedit.setInputMask(QCoreApplication.translate("user_view", u"999999", None))
        self.user_pin_lineedit.setPlaceholderText("")
        self.user_forename.setInputMask(QCoreApplication.translate("user_view", u"Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", None))
        self.user_forename.setPlaceholderText(QCoreApplication.translate("user_view", u"Forename", None))
        self.user_DoB_label.setText(QCoreApplication.translate("user_view", u"Date of Birth", None))
        self.new_icon_change_pushbutton.setText(QCoreApplication.translate("user_view", u"Change", None))
        self.user_add_button.setText("")
        self.user_view_option.setTabText(self.user_view_option.indexOf(self.add_user), QCoreApplication.translate("user_view", u"New", None))
    # retranslateUi

