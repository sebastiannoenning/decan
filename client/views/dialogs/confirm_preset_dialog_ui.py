# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_preset_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from modules.eventlist.eventattributes import EBody
from views import rss_rc

class Ui_confirm_preset_dialog(object):
    def setupUi(self, confirm_preset_dialog):
        if not confirm_preset_dialog.objectName():
            confirm_preset_dialog.setObjectName(u"confirm_preset_dialog")
        confirm_preset_dialog.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirm_preset_dialog.sizePolicy().hasHeightForWidth())
        confirm_preset_dialog.setSizePolicy(sizePolicy)
        confirm_preset_dialog.setMinimumSize(QSize(200, 130))
        confirm_preset_dialog.setMaximumSize(QSize(500, 300))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        confirm_preset_dialog.setFont(font)
        confirm_preset_dialog.setStyleSheet(u"QDialog {\n"
"background-color: rgba(20,20,20,1);\n"
"}\n"
"\n"
"#footer *[text=\"Cancel\"] {\n"
"    background: red;\n"
"}\n"
"#footer *[text=\"OK\"] {\n"
"    background: green;\n"
"}")
        confirm_preset_dialog.setModal(False)
        self.dialog_layout = QVBoxLayout(confirm_preset_dialog)
        self.dialog_layout.setSpacing(0)
        self.dialog_layout.setObjectName(u"dialog_layout")
        self.dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(confirm_preset_dialog)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"background-color: rgb(30, 30, 30)")
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setSpacing(5)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.header)
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

        self.header_layout.addWidget(self.label)

        self.alert_label = QLabel(self.header)
        self.alert_label.setObjectName(u"alert_label")
        sizePolicy2.setHeightForWidth(self.alert_label.sizePolicy().hasHeightForWidth())
        self.alert_label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.alert_label.setFont(font1)

        self.header_layout.addWidget(self.alert_label)

        self.message_wrapper = QScrollArea(self.header)
        self.message_wrapper.setObjectName(u"message_wrapper")
        self.message_wrapper.setStyleSheet(u"#message_wrapper {border-radius: 4px;\n"
"border: 2px solid rgb(255, 180, 130);}")
        self.message_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.message_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.message_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.message_wrapper.setWidgetResizable(True)
        self.message_container = QWidget()
        self.message_container.setObjectName(u"message_container")
        self.message_container.setGeometry(QRect(0, 0, 768, 56))
        self.message_container_layout = QHBoxLayout(self.message_container)
        self.message_container_layout.setSpacing(0)
        self.message_container_layout.setObjectName(u"message_container_layout")
        self.message_container_layout.setContentsMargins(10, 0, 0, 0)
        self.message = QLabel(self.message_container)
        self.message.setObjectName(u"message")
        self.message.setFont(font)
        self.message.setLineWidth(0)

        self.message_container_layout.addWidget(self.message)

        self.message_wrapper.setWidget(self.message_container)

        self.header_layout.addWidget(self.message_wrapper)


        self.dialog_layout.addWidget(self.header)

        self.middle = QWidget(confirm_preset_dialog)
        self.middle.setObjectName(u"middle")
        self.before_after_layout = QVBoxLayout(self.middle)
        self.before_after_layout.setSpacing(0)
        self.before_after_layout.setObjectName(u"before_after_layout")
        self.before_after_layout.setContentsMargins(0, 0, 0, 0)
        self.expand_push_button = QPushButton(self.middle)
        self.expand_push_button.setObjectName(u"expand_push_button")
        sizePolicy.setHeightForWidth(self.expand_push_button.sizePolicy().hasHeightForWidth())
        self.expand_push_button.setSizePolicy(sizePolicy)
        self.expand_push_button.setMinimumSize(QSize(30, 0))
        self.expand_push_button.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(15)
        self.expand_push_button.setFont(font2)
        self.expand_push_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.expand_push_button.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	background-color: rgba(40,40,40,1);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/arrows/arrow_right_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/arrows/arrow_down_red.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.expand_push_button.setIcon(icon)
        self.expand_push_button.setIconSize(QSize(20, 20))
        self.expand_push_button.setCheckable(True)
        self.expand_push_button.setChecked(False)

        self.before_after_layout.addWidget(self.expand_push_button)

        self.before_after_expanded = QWidget(self.middle)
        self.before_after_expanded.setObjectName(u"before_after_expanded")
        self.before_after_expanded.setStyleSheet(u"QWidget#before_after_expanded {\n"
"	background-color: rgba(30,30,30,1);\n"
"}\n"
"QScrollArea {\n"
"	border: 2px solid rgba(120,120,120,1);\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"QLabel#before_label, QLabel#after_label {\n"
"	background: rgba(30,30,30,1);\n"
"	border: 2px solid rgba(100,100,100,1);\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 4px;\n"
"}")
        self.expanded_layout = QHBoxLayout(self.before_after_expanded)
        self.expanded_layout.setSpacing(0)
        self.expanded_layout.setObjectName(u"expanded_layout")
        self.expanded_layout.setContentsMargins(0, 0, 0, 0)
        self.before = QWidget(self.before_after_expanded)
        self.before.setObjectName(u"before")
        self.before.setMaximumSize(QSize(285, 16777215))
        self.before_layout = QVBoxLayout(self.before)
        self.before_layout.setSpacing(0)
        self.before_layout.setObjectName(u"before_layout")
        self.before_layout.setContentsMargins(0, 0, 0, 0)
        self.before_label = QLabel(self.before)
        self.before_label.setObjectName(u"before_label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        self.before_label.setFont(font3)
        self.before_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.before_layout.addWidget(self.before_label)

        self.before_layers = QScrollArea(self.before)
        self.before_layers.setObjectName(u"before_layers")
        self.before_layers.setMaximumSize(QSize(285, 285))
        self.before_layers.setWidgetResizable(True)
        self.proposed_layers_container = QWidget()
        self.proposed_layers_container.setObjectName(u"proposed_layers_container")
        self.proposed_layers_container.setGeometry(QRect(0, 0, 231, 145))
        self.before_layers_layout = QVBoxLayout(self.proposed_layers_container)
        self.before_layers_layout.setSpacing(0)
        self.before_layers_layout.setObjectName(u"before_layers_layout")
        self.before_layers_layout.setContentsMargins(0, 0, 0, 0)
        self.before_ebody = EBody(self.proposed_layers_container)
        self.before_ebody.setObjectName(u"before_ebody")

        self.before_layers_layout.addWidget(self.before_ebody)

        self.before_layers.setWidget(self.proposed_layers_container)

        self.before_layout.addWidget(self.before_layers)


        self.expanded_layout.addWidget(self.before)

        self.arrow_wrapper = QWidget(self.before_after_expanded)
        self.arrow_wrapper.setObjectName(u"arrow_wrapper")
        self.arrow_wrapper.setMaximumSize(QSize(30, 16777215))
        self.arrow_container = QVBoxLayout(self.arrow_wrapper)
        self.arrow_container.setSpacing(0)
        self.arrow_container.setObjectName(u"arrow_container")
        self.arrow_container.setContentsMargins(0, 0, 0, 0)
        self.arrow_icon = QLabel(self.arrow_wrapper)
        self.arrow_icon.setObjectName(u"arrow_icon")
        self.arrow_icon.setMinimumSize(QSize(30, 30))
        self.arrow_icon.setMaximumSize(QSize(30, 30))
        self.arrow_icon.setPixmap(QPixmap(u":/icons/arrows/arrow_right_dark.svg"))
        self.arrow_icon.setScaledContents(True)

        self.arrow_container.addWidget(self.arrow_icon)


        self.expanded_layout.addWidget(self.arrow_wrapper)

        self.after = QWidget(self.before_after_expanded)
        self.after.setObjectName(u"after")
        self.after.setMaximumSize(QSize(285, 16777215))
        self.after_layout = QVBoxLayout(self.after)
        self.after_layout.setSpacing(0)
        self.after_layout.setObjectName(u"after_layout")
        self.after_layout.setContentsMargins(0, 0, 0, 0)
        self.after_label = QLabel(self.after)
        self.after_label.setObjectName(u"after_label")
        self.after_label.setFont(font3)
        self.after_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.after_layout.addWidget(self.after_label)

        self.after_layers = QScrollArea(self.after)
        self.after_layers.setObjectName(u"after_layers")
        self.after_layers.setMaximumSize(QSize(285, 285))
        self.after_layers.setWidgetResizable(True)
        self.after_layers_container = QWidget()
        self.after_layers_container.setObjectName(u"after_layers_container")
        self.after_layers_container.setGeometry(QRect(0, 0, 231, 145))
        self.after_layers_layout = QVBoxLayout(self.after_layers_container)
        self.after_layers_layout.setSpacing(0)
        self.after_layers_layout.setObjectName(u"after_layers_layout")
        self.after_layers_layout.setContentsMargins(0, 0, 0, 0)
        self.after_ebody = EBody(self.after_layers_container)
        self.after_ebody.setObjectName(u"after_ebody")

        self.after_layers_layout.addWidget(self.after_ebody)

        self.after_layers.setWidget(self.after_layers_container)

        self.after_layout.addWidget(self.after_layers)


        self.expanded_layout.addWidget(self.after)


        self.before_after_layout.addWidget(self.before_after_expanded)


        self.dialog_layout.addWidget(self.middle)

        self.footer = QDialogButtonBox(confirm_preset_dialog)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 30))
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        self.footer.setFont(font4)
        self.footer.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.footer.setAutoFillBackground(False)
        self.footer.setStyleSheet(u"#footer {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#footer * {\n"
"	min-width: 80px;\n"
"	background-color: rgba(120,120,120,1);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#footer *[text=\"Cancel\"] {\n"
"    background: rgba(255,80,80,1);\n"
"}\n"
"#footer *[text=\"OK\"] {\n"
"    background: rgba(180,200,150,1);\n"
"}")
        self.footer.setOrientation(Qt.Orientation.Horizontal)
        self.footer.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.footer.setCenterButtons(True)

        self.dialog_layout.addWidget(self.footer)


        self.retranslateUi(confirm_preset_dialog)
        self.footer.accepted.connect(confirm_preset_dialog.accept)
        self.footer.rejected.connect(confirm_preset_dialog.reject)
        self.expand_push_button.toggled.connect(self.before_after_expanded.setVisible)

        QMetaObject.connectSlotsByName(confirm_preset_dialog)
    # setupUi

    def retranslateUi(self, confirm_preset_dialog):
        confirm_preset_dialog.setWindowTitle(QCoreApplication.translate("confirm_preset_dialog", u"Dialog", None))
        self.label.setText("")
        self.alert_label.setText(QCoreApplication.translate("confirm_preset_dialog", u"Alert ", None))
        self.message.setText(QCoreApplication.translate("confirm_preset_dialog", u"Selecting this option will cause any pre-existing settings to be overriden", None))
        self.expand_push_button.setText(QCoreApplication.translate("confirm_preset_dialog", u"Expand", None))
        self.before_label.setText(QCoreApplication.translate("confirm_preset_dialog", u"Before", None))
        self.arrow_icon.setText("")
        self.after_label.setText(QCoreApplication.translate("confirm_preset_dialog", u"After", None))
    # retranslateUi

