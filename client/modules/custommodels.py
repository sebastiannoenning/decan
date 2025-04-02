import sys
from PySide6.QtCore import QObject, QSortFilterProxyModel, QConcatenateTablesProxyModel, QModelIndex
from PySide6 import QtSql
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel

# Custom QSortFilterProxyModel
class CSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, /, parent):
        super().__init__(parent)

    def data(self, index, /, role = ...):
        return super().data(index, role)

# Custom QConcatanateTabblesProxyModel
class CConcatanateTablesProxyModel(QConcatenateTablesProxyModel):
    def __init__(self, /, parent = ...):
        super().__init__(parent)

    def setData(self, index, value, /, role = ...):
        return super().setData(index, value, role)