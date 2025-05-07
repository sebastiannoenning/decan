# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_tab.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_user_tab(object):
    def setupUi(self, user_tab):
        if not user_tab.objectName():
            user_tab.setObjectName(u"user_tab")
        user_tab.resize(110, 195)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user_tab.sizePolicy().hasHeightForWidth())
        user_tab.setSizePolicy(sizePolicy)
        user_tab.setMinimumSize(QSize(110, 195))
        self.verticalLayout = QVBoxLayout(user_tab)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(user_tab)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 195))
        self.header.setMaximumSize(QSize(150, 285))
        self.header_layout = QVBoxLayout(self.header)
        self.header_layout.setSpacing(10)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.icon = QGraphicsView(self.header)
        self.icon.setObjectName(u"icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy1)
        self.icon.setMinimumSize(QSize(110, 110))
        self.icon.setMaximumSize(QSize(110, 110))
        self.icon.setFrameShadow(QFrame.Shadow.Plain)
        self.icon.setLineWidth(0)
        self.icon.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.BoundingRectViewportUpdate)

        self.header_layout.addWidget(self.icon)

        self.name = QLabel(self.header)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 35))
        self.name.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.name.setFont(font)
        self.name.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}")
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_layout.addWidget(self.name)

        self.status = QLabel(self.header)
        self.status.setObjectName(u"status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy2)
        self.status.setMinimumSize(QSize(0, 35))
        self.status.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setItalic(False)
        self.status.setFont(font1)
        self.status.setStyleSheet(u"QLabel{\n"
"	background-color:  transparent;\n"
"	border: 2px solid rgba(140,150,180,1);\n"
"	border-radius: 17px;\n"
"	color: white;\n"
"}")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_layout.addWidget(self.status)

        self.active = QLabel(self.header)
        self.active.setObjectName(u"active")
        self.active.setMinimumSize(QSize(0, 35))
        self.active.setMaximumSize(QSize(16777215, 35))
        self.active.setFont(font)
        self.active.setStyleSheet(u"QLabel{\n"
"	background-color:  transparent;\n"
"	border: 2px solid rgba(255,200,100,1);\n"
"	border-radius: 17px;\n"
"	color: white;\n"
"}")
        self.active.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_layout.addWidget(self.active)


        self.verticalLayout.addWidget(self.header)

        self.options = QWidget(user_tab)
        self.options.setObjectName(u"options")
        self.options.setMinimumSize(QSize(0, 35))
        self.options.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        self.options.setFont(font2)
        self.options.setStyleSheet(u"QLabel, QPushButton{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}")
        self.options_layout = QVBoxLayout(self.options)
        self.options_layout.setSpacing(0)
        self.options_layout.setObjectName(u"options_layout")
        self.options_layout.setContentsMargins(0, 0, 0, 0)
        self.sign_in_button = QPushButton(self.options)
        self.sign_in_button.setObjectName(u"sign_in_button")
        self.sign_in_button.setMinimumSize(QSize(0, 35))
        self.sign_in_button.setMaximumSize(QSize(16777215, 35))
        self.sign_in_button.setFont(font)
        self.sign_in_button.setIconSize(QSize(30, 30))

        self.options_layout.addWidget(self.sign_in_button)

        self.sign_out_button = QPushButton(self.options)
        self.sign_out_button.setObjectName(u"sign_out_button")
        self.sign_out_button.setMinimumSize(QSize(0, 35))
        self.sign_out_button.setMaximumSize(QSize(16777215, 35))
        self.sign_out_button.setFont(font)

        self.options_layout.addWidget(self.sign_out_button)


        self.verticalLayout.addWidget(self.options)

        self.bottompad = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.bottompad)


        self.retranslateUi(user_tab)

        QMetaObject.connectSlotsByName(user_tab)
    # setupUi

    def retranslateUi(self, user_tab):
        user_tab.setWindowTitle(QCoreApplication.translate("user_tab", u"Form", None))
        self.name.setText(QCoreApplication.translate("user_tab", u"Name", None))
        self.status.setText(QCoreApplication.translate("user_tab", u"Signed-in", None))
        self.active.setText(QCoreApplication.translate("user_tab", u"Active", None))
        self.sign_in_button.setText(QCoreApplication.translate("user_tab", u"Sign-in", None))
        self.sign_out_button.setText(QCoreApplication.translate("user_tab", u"Log-out", None))
    # retranslateUi

