# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_view.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_event_view(object):
    def setupUi(self, event_view):
        if not event_view.objectName():
            event_view.setObjectName(u"event_view")
        event_view.resize(800, 480)
        self.event_table = QTableView(event_view)
        self.event_table.setObjectName(u"event_table")
        self.event_table.setGeometry(QRect(70, 40, 591, 371))
        self.user1 = QPushButton(event_view)
        self.user1.setObjectName(u"user1")
        self.user1.setGeometry(QRect(130, 430, 100, 32))
        self.user2 = QPushButton(event_view)
        self.user2.setObjectName(u"user2")
        self.user2.setGeometry(QRect(280, 430, 100, 32))
        self.user3 = QPushButton(event_view)
        self.user3.setObjectName(u"user3")
        self.user3.setGeometry(QRect(430, 430, 100, 32))

        self.retranslateUi(event_view)

        QMetaObject.connectSlotsByName(event_view)
    # setupUi

    def retranslateUi(self, event_view):
        event_view.setWindowTitle(QCoreApplication.translate("event_view", u"Form", None))
        self.user1.setText(QCoreApplication.translate("event_view", u"user1", None))
        self.user2.setText(QCoreApplication.translate("event_view", u"user2", None))
        self.user3.setText(QCoreApplication.translate("event_view", u"user3", None))
    # retranslateUi

