from typing import List
import json

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QModelIndex, QByteArray
from PySide6.QtWidgets import QWidget, QScroller, QDataWidgetMapper, QPushButton, QDialog, QDialogButtonBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/dialogs/confirm_preset_dialog.ui -o client/views/dialogs/confirm_preset_dialog_ui.py, or
#       pyside6-uic --from-imports dialogs/confirm_preset_dialog.ui -o ../client/views/dialogs/confirm_preset_dialog_ui.py
#       
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o resources/assets/rss.py
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py 

from .confirm_preset_dialog_ui import Ui_confirm_preset_dialog
from modules.eventlist.eventattributes import EBody
from modules.eventlist.eventtype import EventType
from modules.eventlist.eventjsonparser import EventJsonParser
import modules.scrollers_qt as scrQt

class ConfirmPreset(QDialog):
    def __init__(self, /, parent = None, f = ..., *, sizeGripEnabled = ..., modal = ...):
        super().__init__(parent, f, sizeGripEnabled=sizeGripEnabled, modal=modal)
        self.setWindowTitle("")
        self._Ui = Ui_confirm_preset_dialog()
        self._Ui.setupUi(self)

        self._Io

    def defaultSimple(self):


