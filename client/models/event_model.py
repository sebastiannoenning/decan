import sys
from PySide6.QtCore import QObject, QSortFilterProxyModel, QConcatenateTablesProxyModel
from PySide6 import QtSql
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery

from modules.custommodels import CConcatanateTablesProxyModel, CSortFilterProxyModel
from modules.comqt import execnext

class EventModel(QSqlTableModel):
    def __init__(self, /, parent = ..., db = ...):
        super().__init__(parent, db)
        cur_user = 1

class EventUserModel(QSqlTableModel):
    def __init__(self, /, parent = ..., db = ...):
        super().__init__(parent, db)
        self.user_id = 1

        self.setTable('EU_layer2_FilteredEvents')
        self.select()

        self.userValidate = QSqlQuery()
        self.userValidate.prepare("SELECT * FROM `Users` WHERE `UserID` = :user ;")
        self.userChange = QSqlQuery()
        self.userChange.prepare("ALTER VIEW `EU_layer1_FilteredEvents` AS SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user ;")

    def changeUser(self, uid: int, test_en = True):
        if (uid == self.user_id): return
        else:
            # Validate userID
            self.userValidate.bindValue(":user", uid)
            self.userValidate = execnext(self.userValidate)
            if not (self.userValidate.isValid()):
                if (test_en): print("###EUModel Validate Error: ",self.userValidate.lastError())
                return
            else: self.user_id = uid
            # Change view Query
            self.userChange.bindValue(":user", uid)
            self.userChange.exec()
            self.select()
            if (test_en): print("###EUModel New rows:", self.rowCount)
        """CREATE ALGORITHM = MERGE VIEW `EU_FilteredEvents` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `Events_Users` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    )
WHERE
    `EU`.`EU_UserID` = 1;

DROP TABLE IF EXISTS `EU_layer1_FilteredEvents`;
DROP TABLE IF EXISTS `EU_layer2_FilteredEvents`;
    
CREATE ALGORITHM = MERGE VIEW `EU_layer1_FilteredEvents` AS SELECT
    `Events_Users`.`EU_EventID` AS `EU_EventID`
FROM
    `Events_Users`
WHERE
    `Events_Users`.`EU_UserID` = 3;

CREATE ALGORITHM = MERGE VIEW `EU_layer2_FilteredEvents` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `EU_layer1_FilteredEvents` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    );

ALTER VIEW `EU_layer1_FilteredEvents` AS 
SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = 2;

SELECT * FROM `Users` WHERE `UserID` = 1"""


"""class UserFilterModel(QSortFilterProxyModel):

class EventUserModel(QSqlQueryModel):

class EventModelMapper(QConcatenateTablesProxyModel):

class EventFilterModel(QSortFilterProxyModel):"""