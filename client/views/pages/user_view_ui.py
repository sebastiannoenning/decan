# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_view.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from modules.touchdatetime.tdateedit import DateSelect

class Ui_user_view(object):
    def setupUi(self, user_view):
        if not user_view.objectName():
            user_view.setObjectName(u"user_view")
        user_view.resize(710, 460)
        self.calendarWidget = DateSelect(user_view)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(90, 20, 591, 391))

        self.retranslateUi(user_view)

        QMetaObject.connectSlotsByName(user_view)
    # setupUi

    def retranslateUi(self, user_view):
        user_view.setWindowTitle(QCoreApplication.translate("user_view", u"Form", None))
    # retranslateUi

