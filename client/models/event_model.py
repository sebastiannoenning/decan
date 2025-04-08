import sys, re
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
        test_en = True
        self._user_id = 1

        self.setTable('EU_layer2_FilteredEvents')
        self.select()

        # Query ran once to check current user in table
        self.pullUser = QSqlQuery("SHOW CREATE VIEW `EU_layer1_FilteredEvents`")
        self.currentUser()

        self.userValidate = QSqlQuery() #Query for validating the _user_id passed to the 
        self.userValidate.prepare("SELECT * FROM `Users` WHERE `UserID` = :user ;")
        self.userChange = QSqlQuery() #Query for changing the view's current user
        self.userChange.prepare("ALTER VIEW `EU_layer1_FilteredEvents` AS SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user ;")
        
        self.intersectingRowCheck = QSqlQuery() #Query for checking common rows between the predicted & current dataset
        self.intersectingRowCheck.prepare("""
                                  SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                  INTERSECT
                                  SELECT * FROM `EU_layer1_FilteredEvents`""")
        
        self.intersectingRowCount = QSqlQuery() #Query for number of checking common rows
        self.intersectingRowCount.prepare("""
                                    SELECT COUNT(*) AS intersection_count
                                    FROM (
                                        SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                        INTERSECT
                                        SELECT * FROM `EU_layer1_FilteredEvents`
                                    ) AS intersecting_rows""")
        
    def currentUser(self, test_en=True):
        self.pullUser = execnext(self.pullUser)                                                           # Error messages to be passed to terminal
        uid_check, msg = re.search('`EU_UserID`\s*=\s*(\d+)',self.pullUser.value(1)),                                       'N/A'
        if (uid_check): self._user_id, msg = uid_check.group(1),                                                            'Successfully managed to'
        else:           self._user_id, msg = int(execnext(QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")).value(0)),     'Failed to'
        # Above code checks if a match was found in the view's initial query; if not, it defaults to another user. 
        if (test_en): print(f"###EUModel {msg} extract ID from view\nCurrent UserID: ",self._user_id)
        if ((msg) == 'Failed to'): self.changeUser(uid=self._user_id)
    
    def changeUser(self, uid: int, test_en=True):
        if (uid == self._user_id): return #Exit early if _user_id already matches the current
        else:
            # Validate userID
            cur_id = self._user_id
            self.userValidate.bindValue(":user", uid)
            self.userValidate = execnext(self.userValidate)
            if not (self.userValidate.isValid()):
                if (test_en): print("###EUModel Validate Error: ",self.userValidate.lastError())
                return #Exit early if _user_id does not exist
            else: self._user_id = uid 
            # Change view Query
            self.userChange.bindValue(":user", uid)
            self.userChange.exec()
            self.select()
            self.intersectingRowCount.bindValue(':user', cur_id)
            same_rows = execnext(self.intersectingRowCount).value(0)
            if (test_en): print('###EUModel: User changed\n#### Total number of matching rows: ',same_rows,'\n#### New rows: ',self.rowCount()-same_rows)
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

SELECT * FROM `Users` WHERE `UserID` = 1


SELECT `EU_UserID` FROM `Events_Users` WHERE `EU_UserID` = 3 
INTERSECT
SELECT * FROM `EU_layer1_FilteredEvents`"""


"""class UserFilterModel(QSortFilterProxyModel):

class EventUserModel(QSqlQueryModel):

class EventModelMapper(QConcatenateTablesProxyModel):

class EventFilterModel(QSortFilterProxyModel):"""