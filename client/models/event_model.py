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


class UserFilterModel(QSortFilterProxyModel):

class EventUserModel(QSqlQueryModel):

class EventModelMapper(QConcatenateTablesProxyModel):

class EventFilterModel(QSortFilterProxyModel):