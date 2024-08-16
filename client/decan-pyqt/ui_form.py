# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QWidget)

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
        self.label = QLabel(self.navigation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 16))
        self.container = QWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(130, 10, 660, 460))
        self.pages = QStackedWidget(self.container)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 660, 460))
        self.page_usr = QWidget()
        self.page_usr.setObjectName(u"page_usr")
        self.pages.addWidget(self.page_usr)
        self.p_cal = QWidget()
        self.p_cal.setObjectName(u"p_cal")
        self.upcomingevents = QScrollArea(self.p_cal)
        self.upcomingevents.setObjectName(u"upcomingevents")
        self.upcomingevents.setGeometry(QRect(10, 10, 260, 440))
        self.upcomingevents.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 258, 438))
        self.upcomingevents.setWidget(self.scrollAreaWidgetContents)
        self.pages.addWidget(self.p_cal)
        self.page_set = QWidget()
        self.page_set.setObjectName(u"page_set")
        self.pages.addWidget(self.page_set)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_user.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.b_calendar.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.b_events.setText(QCoreApplication.translate("MainWindow", u"Events", None))
        self.b_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
    # retranslateUi

