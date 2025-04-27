# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
from . import rss_rc

class Ui_main_view(object):
    def setupUi(self, main_view):
        if not main_view.objectName():
            main_view.setObjectName(u"main_view")
        main_view.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_view.sizePolicy().hasHeightForWidth())
        main_view.setSizePolicy(sizePolicy)
        main_view.setMinimumSize(QSize(800, 480))
        main_view.setMaximumSize(QSize(800, 480))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 63))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        main_view.setPalette(palette)
        main_view.setStyleSheet(u"#nav * QPushButton{\n"
"background-color: rgba(20, 20, 20, 1);\n"
"border-radius: 8px;\n"
"}\n"
"#nav * QPushButton:pressed{\n"
"background-color: rgba(120,120,120,1);\n"
"}")
        self.main_container = QWidget(main_view)
        self.main_container.setObjectName(u"main_container")
        self.central_layout = QHBoxLayout(self.main_container)
        self.central_layout.setSpacing(10)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(10, 10, 10, 10)
        self.nav = QWidget(self.main_container)
        self.nav.setObjectName(u"nav")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy1)
        self.nav.setMinimumSize(QSize(60, 0))
        self.nav.setMaximumSize(QSize(135, 16777215))
        self.nav.setStyleSheet(u"QPushButton {\n"
"	padding: 10px; \n"
"	font-size: 20px;\n"
"}")
        self.nav_layout = QHBoxLayout(self.nav)
        self.nav_layout.setSpacing(0)
        self.nav_layout.setObjectName(u"nav_layout")
        self.nav_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.nav_layout.setContentsMargins(0, 0, 0, 0)
        self.collapsed = QWidget(self.nav)
        self.collapsed.setObjectName(u"collapsed")
        sizePolicy1.setHeightForWidth(self.collapsed.sizePolicy().hasHeightForWidth())
        self.collapsed.setSizePolicy(sizePolicy1)
        self.collapsed.setMinimumSize(QSize(60, 0))
        self.collapsed.setMaximumSize(QSize(60, 16777215))
        self.collapsed_layout = QVBoxLayout(self.collapsed)
        self.collapsed_layout.setSpacing(10)
        self.collapsed_layout.setObjectName(u"collapsed_layout")
        self.collapsed_layout.setContentsMargins(0, 0, 0, 0)
        self.col_toggle = QPushButton(self.collapsed)
        self.col_toggle.setObjectName(u"col_toggle")
        self.col_toggle.setMinimumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/icons/nav/burger_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/nav/burger_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_toggle.setIcon(icon)
        self.col_toggle.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_toggle)

        self.col_p1_user = QPushButton(self.collapsed)
        self.col_p1_user.setObjectName(u"col_p1_user")
        self.col_p1_user.setMinimumSize(QSize(60, 90))
        icon1 = QIcon()
        icon1.addFile(u":/icons/user/profile_2_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/user/profile_2_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_p1_user.setIcon(icon1)
        self.col_p1_user.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_p1_user)

        self.col_p2_cal = QPushButton(self.collapsed)
        self.col_p2_cal.setObjectName(u"col_p2_cal")
        self.col_p2_cal.setMinimumSize(QSize(60, 90))
        self.col_p2_cal.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/nav/calendar_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/nav/calendar_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_p2_cal.setIcon(icon2)
        self.col_p2_cal.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_p2_cal)

        self.col_p3_events = QPushButton(self.collapsed)
        self.col_p3_events.setObjectName(u"col_p3_events")
        self.col_p3_events.setMinimumSize(QSize(60, 90))
        icon3 = QIcon()
        icon3.addFile(u":/icons/calendar/calendar_edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/calendar/calendar_edit_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_p3_events.setIcon(icon3)
        self.col_p3_events.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_p3_events)

        self.col_p4_pref = QPushButton(self.collapsed)
        self.col_p4_pref.setObjectName(u"col_p4_pref")
        self.col_p4_pref.setMinimumSize(QSize(60, 90))
        icon4 = QIcon()
        icon4.addFile(u":/icons/nav/setting_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/nav/setting_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_p4_pref.setIcon(icon4)
        self.col_p4_pref.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_p4_pref)


        self.nav_layout.addWidget(self.collapsed)

        self.expanded = QWidget(self.nav)
        self.expanded.setObjectName(u"expanded")
        sizePolicy1.setHeightForWidth(self.expanded.sizePolicy().hasHeightForWidth())
        self.expanded.setSizePolicy(sizePolicy1)
        self.expanded.setMinimumSize(QSize(135, 0))
        self.expanded.setMaximumSize(QSize(135, 16777215))
        self.expanded.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"}")
        self.expanded_layout = QVBoxLayout(self.expanded)
        self.expanded_layout.setSpacing(10)
        self.expanded_layout.setObjectName(u"expanded_layout")
        self.expanded_layout.setContentsMargins(0, 0, 0, 0)
        self.exp_toggle = QPushButton(self.expanded)
        self.exp_toggle.setObjectName(u"exp_toggle")
        self.exp_toggle.setMinimumSize(QSize(135, 60))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.exp_toggle.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/nav/burger_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.exp_toggle.setIcon(icon5)
        self.exp_toggle.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_toggle)

        self.exp_p1_user = QPushButton(self.expanded)
        self.exp_p1_user.setObjectName(u"exp_p1_user")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.exp_p1_user.sizePolicy().hasHeightForWidth())
        self.exp_p1_user.setSizePolicy(sizePolicy2)
        self.exp_p1_user.setMinimumSize(QSize(135, 90))
        self.exp_p1_user.setFont(font)
        self.exp_p1_user.setIcon(icon1)
        self.exp_p1_user.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_p1_user)

        self.exp_p2_cal = QPushButton(self.expanded)
        self.exp_p2_cal.setObjectName(u"exp_p2_cal")
        self.exp_p2_cal.setMinimumSize(QSize(135, 90))
        self.exp_p2_cal.setFont(font)
        self.exp_p2_cal.setIcon(icon2)
        self.exp_p2_cal.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_p2_cal)

        self.exp_p3_events = QPushButton(self.expanded)
        self.exp_p3_events.setObjectName(u"exp_p3_events")
        self.exp_p3_events.setMinimumSize(QSize(135, 90))
        self.exp_p3_events.setFont(font)
        self.exp_p3_events.setIcon(icon3)
        self.exp_p3_events.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_p3_events)

        self.exp_p4_pref = QPushButton(self.expanded)
        self.exp_p4_pref.setObjectName(u"exp_p4_pref")
        self.exp_p4_pref.setMinimumSize(QSize(135, 90))
        self.exp_p4_pref.setFont(font)
        self.exp_p4_pref.setIcon(icon4)
        self.exp_p4_pref.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_p4_pref)


        self.nav_layout.addWidget(self.expanded)


        self.central_layout.addWidget(self.nav)

        self.pages = QStackedWidget(self.main_container)
        self.pages.setObjectName(u"pages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy3)
        self.pages.setMinimumSize(QSize(635, 460))
        self.pages.setMaximumSize(QSize(710, 460))
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"")

        self.central_layout.addWidget(self.pages)

        main_view.setCentralWidget(self.main_container)

        self.retranslateUi(main_view)

        QMetaObject.connectSlotsByName(main_view)
    # setupUi

    def retranslateUi(self, main_view):
        main_view.setWindowTitle(QCoreApplication.translate("main_view", u"main", None))
        self.col_toggle.setText("")
        self.col_p1_user.setText("")
        self.col_p2_cal.setText("")
        self.col_p3_events.setText("")
        self.col_p4_pref.setText("")
        self.exp_toggle.setText(QCoreApplication.translate("main_view", u"Menu", None))
        self.exp_p1_user.setText(QCoreApplication.translate("main_view", u"Users", None))
        self.exp_p2_cal.setText(QCoreApplication.translate("main_view", u"Calendar", None))
        self.exp_p3_events.setText(QCoreApplication.translate("main_view", u"Events", None))
        self.exp_p4_pref.setText(QCoreApplication.translate("main_view", u"Settings", None))
    # retranslateUi

