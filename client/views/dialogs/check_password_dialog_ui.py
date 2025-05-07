# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_password_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
from . import rss_rc

class Ui_check_password_dialog(object):
    def setupUi(self, check_password_dialog):
        if not check_password_dialog.objectName():
            check_password_dialog.setObjectName(u"check_password_dialog")
        check_password_dialog.resize(420, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(check_password_dialog.sizePolicy().hasHeightForWidth())
        check_password_dialog.setSizePolicy(sizePolicy)
        check_password_dialog.setMinimumSize(QSize(420, 170))
        check_password_dialog.setMaximumSize(QSize(16777215, 200))
        check_password_dialog.setStyleSheet(u"* {\n"
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
"	background-color: rgba(40,40,40,1);\n"
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
        check_password_dialog.setModal(True)
        self.confirm_password_dialog_layout = QVBoxLayout(check_password_dialog)
        self.confirm_password_dialog_layout.setSpacing(10)
        self.confirm_password_dialog_layout.setObjectName(u"confirm_password_dialog_layout")
        self.confirm_password_dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(check_password_dialog)
        self.header.setObjectName(u"header")
        self.header_layout = QVBoxLayout(self.header)
        self.header_layout.setSpacing(0)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.alert = QWidget(self.header)
        self.alert.setObjectName(u"alert")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.alert.sizePolicy().hasHeightForWidth())
        self.alert.setSizePolicy(sizePolicy1)
        self.alert.setMinimumSize(QSize(0, 60))
        self.alert.setMaximumSize(QSize(16777215, 60))
        self.alert.setStyleSheet(u"background-color: rgb(30, 30, 30)")
        self.alert_layout = QHBoxLayout(self.alert)
        self.alert_layout.setSpacing(5)
        self.alert_layout.setObjectName(u"alert_layout")
        self.alert_layout.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.alert)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(35, 35))
        self.label.setMaximumSize(QSize(35, 35))
        self.label.setPixmap(QPixmap(u":/icons/util/alert_yellow.svg"))
        self.label.setScaledContents(True)

        self.alert_layout.addWidget(self.label)

        self.alert_label = QLabel(self.alert)
        self.alert_label.setObjectName(u"alert_label")
        sizePolicy2.setHeightForWidth(self.alert_label.sizePolicy().hasHeightForWidth())
        self.alert_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        font.setBold(True)
        self.alert_label.setFont(font)

        self.alert_layout.addWidget(self.alert_label)

        self.message_wrapper = QScrollArea(self.alert)
        self.message_wrapper.setObjectName(u"message_wrapper")
        self.message_wrapper.setStyleSheet(u"#message_wrapper {border-radius: 4px;\n"
"border: 2px solid rgb(255, 180, 130);}")
        self.message_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.message_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.message_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.message_wrapper.setWidgetResizable(True)
        self.message_container = QWidget()
        self.message_container.setObjectName(u"message_container")
        self.message_container.setGeometry(QRect(0, 0, 441, 56))
        self.message_container_layout = QHBoxLayout(self.message_container)
        self.message_container_layout.setSpacing(0)
        self.message_container_layout.setObjectName(u"message_container_layout")
        self.message_container_layout.setContentsMargins(10, 0, 0, 0)
        self.message = QLabel(self.message_container)
        self.message.setObjectName(u"message")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        self.message.setFont(font1)
        self.message.setLineWidth(0)

        self.message_container_layout.addWidget(self.message)

        self.message_wrapper.setWidget(self.message_container)

        self.alert_layout.addWidget(self.message_wrapper)


        self.header_layout.addWidget(self.alert)

        self.diagnostic_label = QLabel(self.header)
        self.diagnostic_label.setObjectName(u"diagnostic_label")
        self.diagnostic_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.diagnostic_label.sizePolicy().hasHeightForWidth())
        self.diagnostic_label.setSizePolicy(sizePolicy1)
        self.diagnostic_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        self.diagnostic_label.setFont(font2)
        self.diagnostic_label.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(240,120,120,1);\n"
"	color: white;\n"
"}\n"
"QLabel:disabled{\n"
"	background-color: rgba(120,120,120,1);\n"
"	color: black;\n"
"}")

        self.header_layout.addWidget(self.diagnostic_label)


        self.confirm_password_dialog_layout.addWidget(self.header)

        self.password_edit = QWidget(check_password_dialog)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setMinimumSize(QSize(312, 50))
        self.password_edit_layout = QHBoxLayout(self.password_edit)
        self.password_edit_layout.setSpacing(0)
        self.password_edit_layout.setObjectName(u"password_edit_layout")
        self.password_edit_layout.setContentsMargins(0, 0, 0, 0)
        self.password_lineedit = QLineEdit(self.password_edit)
        self.password_lineedit.setObjectName(u"password_lineedit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.password_lineedit.sizePolicy().hasHeightForWidth())
        self.password_lineedit.setSizePolicy(sizePolicy3)
        self.password_lineedit.setMinimumSize(QSize(252, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(27)
        self.password_lineedit.setFont(font3)
        self.password_lineedit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.password_lineedit.setMaxLength(32767)
        self.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_lineedit.setClearButtonEnabled(True)

        self.password_edit_layout.addWidget(self.password_lineedit)

        self.password_showhide = QPushButton(self.password_edit)
        self.password_showhide.setObjectName(u"password_showhide")
        sizePolicy2.setHeightForWidth(self.password_showhide.sizePolicy().hasHeightForWidth())
        self.password_showhide.setSizePolicy(sizePolicy2)
        self.password_showhide.setMinimumSize(QSize(40, 50))
        self.password_showhide.setMaximumSize(QSize(40, 50))
        icon = QIcon()
        icon.addFile(u":/icons/util/eye_slash_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/util/eye_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.password_showhide.setIcon(icon)
        self.password_showhide.setIconSize(QSize(30, 30))
        self.password_showhide.setCheckable(True)
        self.password_showhide.setChecked(False)

        self.password_edit_layout.addWidget(self.password_showhide)

        self.password_keyboard = QPushButton(self.password_edit)
        self.password_keyboard.setObjectName(u"password_keyboard")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.password_keyboard.sizePolicy().hasHeightForWidth())
        self.password_keyboard.setSizePolicy(sizePolicy4)
        self.password_keyboard.setMinimumSize(QSize(40, 50))
        self.password_keyboard.setMaximumSize(QSize(40, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/util/keyboard_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.password_keyboard.setIcon(icon1)
        self.password_keyboard.setIconSize(QSize(30, 30))
        self.password_keyboard.setCheckable(True)

        self.password_edit_layout.addWidget(self.password_keyboard)


        self.confirm_password_dialog_layout.addWidget(self.password_edit)

        self.footer = QWidget(check_password_dialog)
        self.footer.setObjectName(u"footer")
        self.footer_layout = QHBoxLayout(self.footer)
        self.footer_layout.setSpacing(0)
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.confirm = QPushButton(self.footer)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.confirm.sizePolicy().hasHeightForWidth())
        self.confirm.setSizePolicy(sizePolicy5)
        self.confirm.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(20)
        self.confirm.setFont(font4)
        self.confirm.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(20,20,20,1);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(80,160,100);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgba(120,120,120,1);\n"
"	color: rgba(200,200,200,1);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/util/tick_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/util/tick_square1_green.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon2.addFile(u":/icons/util/close_square2_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon2.addFile(u":/icons/util/close_square2_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.confirm.setIcon(icon2)
        self.confirm.setIconSize(QSize(30, 30))
        self.confirm.setCheckable(False)
        self.confirm.setChecked(False)
        self.confirm.setAutoExclusive(False)

        self.footer_layout.addWidget(self.confirm)

        self.cancel = QPushButton(self.footer)
        self.cancel.setObjectName(u"cancel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy6)
        self.cancel.setMaximumSize(QSize(16777215, 60))
        self.cancel.setFont(font4)
        self.cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(20,20,20,1);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(240,120,120);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/util/back_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel.setIcon(icon3)
        self.cancel.setIconSize(QSize(30, 30))
        self.cancel.setCheckable(True)
        self.cancel.setChecked(True)
        self.cancel.setAutoExclusive(True)

        self.footer_layout.addWidget(self.cancel)


        self.confirm_password_dialog_layout.addWidget(self.footer)


        self.retranslateUi(check_password_dialog)
        self.cancel.clicked.connect(check_password_dialog.reject)

        QMetaObject.connectSlotsByName(check_password_dialog)
    # setupUi

    def retranslateUi(self, check_password_dialog):
        check_password_dialog.setWindowTitle(QCoreApplication.translate("check_password_dialog", u"Dialog", None))
        self.label.setText("")
        self.alert_label.setText(QCoreApplication.translate("check_password_dialog", u"Alert", None))
        self.message.setText(QCoreApplication.translate("check_password_dialog", u"Please enter your password to proceed", None))
        self.diagnostic_label.setText(QCoreApplication.translate("check_password_dialog", u"Wrong password, try again", None))
        self.password_lineedit.setText("")
        self.password_lineedit.setPlaceholderText(QCoreApplication.translate("check_password_dialog", u"Password", None))
        self.password_showhide.setText("")
        self.password_keyboard.setText("")
        self.confirm.setText(QCoreApplication.translate("check_password_dialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("check_password_dialog", u"Cancel", None))
    # retranslateUi

