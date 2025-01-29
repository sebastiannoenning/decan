from typing import Union
from PySide6.QtWidgets import QComboBox
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel, QSqlRecord
from PySide6.QtCore import Qt

class QModelComboBox(QComboBox):
    def __init__(self, parent) -> None:
        super().__init__()
        self._model = None
        self._column = 0
        self.show()

    def setModel(self, model: Union[QSqlRelationalTableModel, QSqlTableModel, QSqlQueryModel], column: 0):
        self._model, self._column = model, column
        model_elements = model.rowCount()
        for i in range (0, model_elements):
            record = self._model.record(i)
            print("Value added to combo box:",record.value(column))
            self.addItem(record.value(column))
        