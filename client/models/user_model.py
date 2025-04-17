import sys, re, datetime
from typing import List, Optional
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, 
                            QSortFilterProxyModel, QConcatenateTablesProxyModel, 
                            QDate, QDateTime, QTime,
                            QRegularExpression)
from PySide6.QtSql import (QSqlDatabase, 
                           QSqlTableModel, QSqlQueryModel, 
                           QSqlQuery)

import modules.sql_qt as sqlFuncs
import modules.datetime_qt as dtFuncs

class UserModel(QSortFilterProxyModel):
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

        self._userModel = QSqlTableModel(self, db=self._database)
        self._userProfileModel = QSqlTableModel(self, db=self._database)

    def setupLayers(self):
        self._userModel.setTable('Users')
        self._userProfileModel.setTable('UserProfile')

class UModel(QSortFilterProxyModel):
    def __init__(self, /, parent = ..., *, filterRegularExpression = ..., filterKeyColumn = ..., dynamicSortFilter = ..., filterCaseSensitivity = ..., sortCaseSensitivity = ..., isSortLocaleAware = ..., sortRole = ..., filterRole = ..., recursiveFilteringEnabled = ..., autoAcceptChildRows = ...):
        super().__init__(parent, 
                         filterRegularExpression=filterRegularExpression, 
                         filterKeyColumn=filterKeyColumn, 
                         dynamicSortFilter=dynamicSortFilter, 
                         filterCaseSensitivity=filterCaseSensitivity, 
                         sortCaseSensitivity=sortCaseSensitivity, 
                         isSortLocaleAware=isSortLocaleAware, 
                         sortRole=sortRole, 
                         filterRole=filterRole, 
                         recursiveFilteringEnabled=recursiveFilteringEnabled, 
                         autoAcceptChildRows=autoAcceptChildRows)