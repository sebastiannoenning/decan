import sys
from PySide6.QtCore import QObject, QSortFilterProxyModel, QConcatenateTablesProxyModel
from PySide6 import QtSql
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel

from client.modules.custommodels import CConcatanateTablesProxyModel, CSortFilterProxyModel

class UserModel(QSqlTableModel):
    def __init__(self):
        self._database = QSqlDatabase.addDatabase('QMYSQL')
        self._database.setDatabaseName('decan')


        if not self._database.open():
            print('connection failed')
            sys.exit(1)
        
        self.setTable('Users')
        print(self.rowCount)