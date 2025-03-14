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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
from . import rss_rc

class Ui_main_view(object):
    def setupUi(self, main_view):
        if not main_view.objectName():
            main_view.setObjectName(u"main_view")
        main_view.resize(800, 480)
        main_view.setStyleSheet(u"")
        self.centralwidget = QWidget(main_view)
        self.centralwidget.setObjectName(u"centralwidget")
        self.central_layout = QHBoxLayout(self.centralwidget)
        self.central_layout.setSpacing(10)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(10, 10, 10, 10)
        self.nav = QWidget(self.centralwidget)
        self.nav.setObjectName(u"nav")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy)
        self.nav.setMinimumSize(QSize(0, 0))
        self.nav.setStyleSheet(u"QPushButton {\n"
"	padding: 10px; \n"
"	font-size: 20px;\n"
"}")
        self.nav_layout = QHBoxLayout(self.nav)
        self.nav_layout.setSpacing(0)
        self.nav_layout.setObjectName(u"nav_layout")
        self.nav_layout.setContentsMargins(0, 0, 0, 0)
        self.collapsed = QWidget(self.nav)
        self.collapsed.setObjectName(u"collapsed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.collapsed.sizePolicy().hasHeightForWidth())
        self.collapsed.setSizePolicy(sizePolicy1)
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

        self.col_page_1 = QPushButton(self.collapsed)
        self.col_page_1.setObjectName(u"col_page_1")
        self.col_page_1.setMinimumSize(QSize(60, 95))
        icon1 = QIcon()
        icon1.addFile(u":/icons/user/profile_2_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/user/profile_2_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_page_1.setIcon(icon1)
        self.col_page_1.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_page_1)

        self.col_page_2 = QPushButton(self.collapsed)
        self.col_page_2.setObjectName(u"col_page_2")
        self.col_page_2.setMinimumSize(QSize(60, 95))
        icon2 = QIcon()
        icon2.addFile(u":/icons/nav/calendar_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/nav/calendar_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_page_2.setIcon(icon2)
        self.col_page_2.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_page_2)

        self.col_page_3 = QPushButton(self.collapsed)
        self.col_page_3.setObjectName(u"col_page_3")
        self.col_page_3.setMinimumSize(QSize(60, 95))
        icon3 = QIcon()
        icon3.addFile(u":/icons/calendar/calendar_edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/calendar/calendar_edit_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_page_3.setIcon(icon3)
        self.col_page_3.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_page_3)

        self.col_page_4 = QPushButton(self.collapsed)
        self.col_page_4.setObjectName(u"col_page_4")
        self.col_page_4.setMinimumSize(QSize(60, 95))
        icon4 = QIcon()
        icon4.addFile(u":/icons/nav/setting_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/nav/setting_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.col_page_4.setIcon(icon4)
        self.col_page_4.setIconSize(QSize(30, 30))

        self.collapsed_layout.addWidget(self.col_page_4)


        self.nav_layout.addWidget(self.collapsed)

        self.expanded = QWidget(self.nav)
        self.expanded.setObjectName(u"expanded")
        sizePolicy.setHeightForWidth(self.expanded.sizePolicy().hasHeightForWidth())
        self.expanded.setSizePolicy(sizePolicy)
        self.expanded.setMaximumSize(QSize(130, 16777215))
        self.expanded.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"}")
        self.expanded_layout = QVBoxLayout(self.expanded)
        self.expanded_layout.setSpacing(10)
        self.expanded_layout.setObjectName(u"expanded_layout")
        self.expanded_layout.setContentsMargins(0, 0, 0, 0)
        self.exp_toggle = QPushButton(self.expanded)
        self.exp_toggle.setObjectName(u"exp_toggle")
        self.exp_toggle.setMinimumSize(QSize(0, 60))
        self.exp_toggle.setIcon(icon)
        self.exp_toggle.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_toggle)

        self.exp_page_1 = QPushButton(self.expanded)
        self.exp_page_1.setObjectName(u"exp_page_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.exp_page_1.sizePolicy().hasHeightForWidth())
        self.exp_page_1.setSizePolicy(sizePolicy2)
        self.exp_page_1.setMinimumSize(QSize(95, 95))
        self.exp_page_1.setIcon(icon1)
        self.exp_page_1.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_page_1)

        self.exp_page_2 = QPushButton(self.expanded)
        self.exp_page_2.setObjectName(u"exp_page_2")
        self.exp_page_2.setMinimumSize(QSize(95, 95))
        self.exp_page_2.setIcon(icon2)
        self.exp_page_2.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_page_2)

        self.exp_page_3 = QPushButton(self.expanded)
        self.exp_page_3.setObjectName(u"exp_page_3")
        self.exp_page_3.setMinimumSize(QSize(95, 95))
        self.exp_page_3.setIcon(icon3)
        self.exp_page_3.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_page_3)

        self.exp_page_4 = QPushButton(self.expanded)
        self.exp_page_4.setObjectName(u"exp_page_4")
        self.exp_page_4.setMinimumSize(QSize(95, 95))
        self.exp_page_4.setIcon(icon4)
        self.exp_page_4.setIconSize(QSize(30, 30))

        self.expanded_layout.addWidget(self.exp_page_4)


        self.nav_layout.addWidget(self.expanded)


        self.central_layout.addWidget(self.nav)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy3)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.central_layout.addWidget(self.pages)

        main_view.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_view)

        QMetaObject.connectSlotsByName(main_view)
    # setupUi

    def retranslateUi(self, main_view):
        main_view.setWindowTitle(QCoreApplication.translate("main_view", u"main", None))
        self.col_toggle.setText("")
        self.col_page_1.setText("")
        self.col_page_2.setText("")
        self.col_page_3.setText("")
        self.col_page_4.setText("")
        self.exp_toggle.setText(QCoreApplication.translate("main_view", u"Menu", None))
        self.exp_page_1.setText(QCoreApplication.translate("main_view", u"Users", None))
        self.exp_page_2.setText(QCoreApplication.translate("main_view", u"Calendar", None))
        self.exp_page_3.setText(QCoreApplication.translate("main_view", u"Events", None))
        self.exp_page_4.setText(QCoreApplication.translate("main_view", u"Settings", None))
    # retranslateUi

