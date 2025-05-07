from typing import List
import json

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QModelIndex, QByteArray, Signal
from PySide6.QtWidgets import QWidget, QScroller, QDataWidgetMapper, QPushButton, QDialog, QDialogButtonBox, QLayoutItem
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/dialogs/icon_picker_dialog.ui -o client/views/dialogs/icon_picker_dialog_ui.py, or
#       pyside6-uic --from-imports dialogs/icon_picker_dialog.ui -o ../client/views/dialogs/icon_picker_dialog_ui.py
#
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o resources/assets/rss.py
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py

from .icon_picker_dialog_ui import Ui_icon_picker_dialog

class IconPicker(QDialog):

    iconSelected = Signal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("")
        self._Ui = Ui_icon_picker_dialog()
        self._Ui.setupUi(self)

        self.hide()

        self._recent : Str = ''

        self.connectIcons()

    def connectIcons(self, test_en: bool=False):
        for row in range(self._Ui.icon_grid.rowCount()):
            for column in range(self._Ui.icon_grid.columnCount()):
                item : QLayoutItem = self._Ui.icon_grid.itemAtPosition(row, column)
                if item is None:
                    if test_en: print(f'Item skipped    at[{row},{column}]')
                    continue
                button : QPushButton = item.widget()
                button.clicked.connect(lambda _checked, name=button.objectName(): self.iconPressed(f'user_{name}'))
                if test_en: print(f'Item connected  at[{row},{column}]')

    def Icon(self) -> str: return self._recent

    def iconPressed(self, iconPath: str, test_en: bool=False):
        self._recent = iconPath
        if test_en: print(f'Icon[{self._recent}] Selected')
        self.iconSelected.emit(self._recent)
        self.accept()

