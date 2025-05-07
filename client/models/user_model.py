import sys, re, datetime
import hashlib, io
from typing import List, Optional

from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, 
                            QSortFilterProxyModel, QConcatenateTablesProxyModel, QModelIndex,
                            QDate, QDateTime, QTime,
                            QRegularExpression)
from PySide6.QtSql import (QSqlDatabase, 
                           QSqlTableModel, QSqlQueryModel, 
                           QSqlQuery)

import modules.sql_qt as sql_funcs
import modules.datetime_qt as dt_funcs

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

        self._queries = self.Queries()

        self.setupLayers()

    def setupLayers(self):
        self._userModel.setTable('Users')
        self._userProfileModel.setTable('UserProfile')

        self.setSourceModel(self._userProfileModel)

        self.select()

    def underlyingUserModel(self) -> QSqlTableModel: return self._userModel

    def select(self):
        self._userModel.select()
        self._userProfileModel.select()

    def loginViaPin(self, profile_id: QModelIndex, pin: str):
        if isinstance(pin, str):
            if pin.len() != 6: raise Exception("Invalid pin length")
            try: chck = int(pin)
            except Exception as e: raise Exception(f"Pin-format error: {e}")
        else: raise Exception("Invalid pin type")

        self._userProfileModel.index(profile_id)

        self._Queries.Users.validateIDviaPin.bindValue(":username", username)
        self._Queries.Users.validateIDviaPin.bindValue(":pin", pin)
        uid = sql_funcs.execnext(self._Queries.Users.validateIDviaPin)

    def validatePassword(self, username: str, password: str):
        if password.len() < 250:
            h = hashlib.sha256()
            h.update(password.encode("utf-8"))
            password = h.hexdigest()

        self._Queries.Users.validateIDviaPass.bindValue(":username", username)
        self._Queries.Users.validateIDviaPass.bindValue(":password", password)
        uid = sql_funcs.execnext(self._Queries.Users.validateIDviaPass)

        if isinstance(uid, int) and uid != -1: return True
        else: return False


    class Queries:
        """ Inner class for bundling database functions & QSqlQuery objects under common/legible namespaces.
        """
        def __init__(self):
            self.Users = self._UserQueries()
            self.UserProfile = self._UserProfileQueries()
            pass

        class _UserProfileQueries:
            def __init__(self):
                pass

        class _UserQueries:  # Inner class for validating userIDs. Later implementations might see this conclusively stored and used in a user model;
            def __init__(self):
                self.defaultID = QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")

                self.validateIDviaPass = QSqlQuery()
                self.validateIDviaPass.prepare("SELECT `UserID` FROM `Users` WHERE `Username` = :username AND `Password` = :password;")

                self.validateIDviaPin = QSqlQuery()
                self.validateIDviaPin.prepare("SELECT `UserID` FROM `Users` WHERE `Username` = :username AND `Pin` = :pin;")

                self.getUsername = QSqlQuery()
                self.getUsername.prepare("SELECT `Username` FROM `Users` WHERE `UserID` = :uid")
                pass
