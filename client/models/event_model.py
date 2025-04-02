import sys
from PySide6.QtCore import QObject, QSortFilterProxyModel, QConcatenateTablesProxyModel
from PySide6 import QtSql
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel

from client.modules.custommodels import CConcatanateTablesProxyModel, CSortFilterProxyModel

class EventModel(QSqlTableModel):
    def __init__(self, /, parent = ..., db = ...):
        super().__init__(parent, db)
        cur_user = 1

class EventUserModel(QSqlTableModel):
    def __init__(self, /, parent = ..., db = ...):
        super().__init__(parent, db)
        cur_user = 1

    def changeUser(userID: int):
        # Validate userID


        # Change view Query
        


class UserFilterModel(QSortFilterProxyModel):

class EventUserModel(QSqlQueryModel):

class EventModelMapper(QConcatenateTablesProxyModel):

class EventFilterModel(QSortFilterProxyModel):