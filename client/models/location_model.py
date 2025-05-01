import sys, re, datetime
from typing import List, Optional
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, 
                            QSortFilterProxyModel, QConcatenateTablesProxyModel, 
                            QDate, QDateTime, QTime,
                            QRegularExpression, Signal)
from PySide6.QtSql import (QSqlDatabase, 
                           QSqlTableModel, QSqlQueryModel, 
                           QSqlQuery)

from .user_model import UserModel
import modules.sql_qt as sqlFuncs
import modules.datetime_qt as dt_funcs

class LocationModel(QSortFilterProxyModel):
    def __init__(self, /, parent=None, *, 
                 db                         :QSqlDatabase       =None,
                 filterRegularExpression    :QRegularExpression =None, 
                 filterKeyColumn            :int                =-1, 
                 dynamicSortFilter          :bool               =False, 
                 filterCaseSensitivity      :Qt.CaseSensitivity =Qt.CaseSensitivity.CaseSensitive, 
                 sortCaseSensitivity        :Qt.CaseSensitivity =Qt.CaseSensitivity.CaseSensitive, 
                 isSortLocaleAware          :bool               =False, 
                 sortRole                   :Qt.ItemDataRole    =Qt.ItemDataRole.UserRole, 
                 filterRole                 :Qt.ItemDataRole    =Qt.ItemDataRole.DisplayRole, 
                 recursiveFilteringEnabled  :bool               =False, 
                 autoAcceptChildRows        :bool               =False):
        super().__init__(parent, 
                         filterRegularExpression    =filterRegularExpression, 
                         filterKeyColumn            =filterKeyColumn, 
                         dynamicSortFilter          =dynamicSortFilter, 
                         filterCaseSensitivity      =filterCaseSensitivity, 
                         sortCaseSensitivity        =sortCaseSensitivity, 
                         isSortLocaleAware          =isSortLocaleAware, 
                         sortRole                   =sortRole, 
                         filterRole                 =filterRole, 
                         recursiveFilteringEnabled  =recursiveFilteringEnabled, 
                         autoAcceptChildRows        =autoAcceptChildRows)
        
        self._database: Optional[QSqlDatabase] = db

        #Bottom-most models; direct connections to the database
        self._locationModel = QSqlTableModel(self, db=self._database)                   #Bottom-most layer      (1)

        self._locationLookupModel = QSortFilterProxyModel(self)                            #Look-up access, sits 'parallel' to this one

        self.setupLayers()

    def setupLayers(self):
        self._locationModel.setTable('Address')

        self.setSourceModel(self._locationModel)

        self._locationLookupModel.setSourceModel(self._locationModel)
