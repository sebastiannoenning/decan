from typing import List
import json

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QModelIndex, QByteArray
from PySide6.QtWidgets import QWidget, QScroller, QDataWidgetMapper, QPushButton, QDialog, QDialogButtonBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/dialogs/check_pin_dialog.ui -o client/views/dialogs/check_pin_dialog_ui.py, or
#       pyside6-uic --from-imports dialogs/check_pin_dialog.ui -o ../client/views/dialogs/check_pin_dialog_ui.py.py
#
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py

from client.models.user_model import UserModel
from client.views.dialogs.

class CheckPin(QDialog):
    def __init__(self, /, parent, username: str, model: UserModel):
        super().__init__(parent)
        self._Ui = Ui_icon_picker_dialog()
        self._Ui.setupUi(self)

        self._username = username

        self._Ui.diagnostic_label.hide()

        self.connections()

    def connections(self):
        self._Ui.confirm.clicked.connect(self._validatePassword)
        self._Ui.password_showhide.toggled.connect(lambda toggled: self.toggleEchos(toggled))
        self._Ui.password_lineedit.textedited.connect(lambda: self._Ui.diagnostic_label.setDiagnosticLabelDisabled())

    def toggleEchos(self, enable: bool):
        if enable: self._Ui.password_lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        else: self._Ui.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)

    def setDiagnosticLabelDisabled(self):
        self._Ui.diagnostic_label.setDisabled(True)
        self._Ui.diagnostic_label.setText(' Awaiting user completion...')

    def setDiagnotisticLabelEnabled(self):
        self._Ui.diagnostic_label.setEnabled(True)
        self._Ui.diagnostic_label.setText(' Wrong password, try again')

    def _validatePassword(self):
        password = self._Ui.password_lineedit.text()