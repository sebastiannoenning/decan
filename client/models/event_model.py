import sys, re, datetime
from typing import List, Optional
from PySide6 import QtCore
from PySide6.QtCore import Qt, QObject, QSortFilterProxyModel, QConcatenateTablesProxyModel, QDate, QDateTime
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery

import modules.sql_qt as sqlFuncs
import modules.datetime_qt as dtFuncs

class DateRange():
    def __init__ (self, startDate: QDateTime, endDate: QDateTime):
        super().__init__()
        self._startDate = startDate
        self._endDate = endDate
    
    # Getters (no setters; changes to the date must be first determined via the EventFilter, as overlap is acknowledged there)
    def startDate(self): return self._startDate
    def endDate(self): return self._endDate

    # Function for determining overlap without pulling either out
    def overlap(self, n_sDate: QDateTime, n_eDate: QDateTime):
        if (self._endDate <= n_sDate) or (self._startDate >= n_eDate): return False
        return True

class EventFilter():
    def __init__(self):
        super().__init__()
        self._userID: Optional[int] = None
        self._scheduleID: Optional[int] = None
        self._locationID: Optional[int] = None
        self._date_ranges: List[DateRange] = []
    
    # Setters for userFilter; Could connect to userModel later
    def addUserFilter(self, userID: int): self._userID = userID
    def clearUserFilter(self): self._userID = None

    # Setters for schedules; One 1 schedule permitted to search at one time
    def addScheduleFilter(self, scheduleID): self._scheduleID = scheduleID
    def clearScheduleFilter(self): self._scheduleID = None

    # Setters for location; Could expand to allow tagging of multiple locations, similar to DateRange
    def addLocationFilter(self, locationID): self._locationID = locationID
    def clearLocationFilter(self): self._locationID = None

    # Setters for DateRange(s)
    """ All indexes are subtracted with 1 """
    def addManyDateRangeFilters(self, date_ranges: List[DateRange] = [], test_en=False):
        """ Convenience function for adding multiple DateRanges at once """
        if len(date_ranges) == 0: return
        for dr in date_ranges:
            try: 
                self.addDateRangeFilter(dr.startDate(),dr.endDate(), test_en=test_en)
            except Exception as e:
                if (test_en): print(f'addManyDateRangeFilters()->{e}')
    def addDateRangeFilter(self, n_sDate: QDateTime, n_eDate: QDateTime, test_en=False):
        """ Function for adding a DateRange to the DateRanges list """
        format = dtFuncs.EDateTime.Date  #Format for error printing
        i = 0                   #Insertion index

        if len(self._date_ranges) == 0: # Exits program early if list is empty & adds the new DateRange to the list
            self._date_ranges.append(DateRange(n_sDate, n_eDate))
            return
        
        for index, dr in enumerate(self._date_ranges, start=1):
            i_sDate, i_eDate = dr.startDate(), dr.endDate()     #Index start & end dates
            if (dr.overlap(n_sDate, n_eDate)): raise Exception(f"""addDateRange() error: New date range overlaps with existing filter
                                                               [{dtFuncs.dateTimeToFS(i_sDate, format)}< (...) <{dtFuncs.dateTimeToFS(i_eDate, format)}]:[Filter @ {index}]
                                                               [{dtFuncs.dateTimeToFS(n_sDate, format)}< (...) <{dtFuncs.dateTimeToFS(n_eDate, format)}]:[Proposed Filter]""")
            else: 
                if (test_en): print(f"Cleared [{index}/{len(self._date_ranges)}] of date_ranges")

                # Updates the insertion index if either value is true
                if (n_eDate < i_sDate) or (i_eDate < n_sDate): i = index-1
        # Will insert DateRange at appropriate place in filter list
        self._date_ranges.insert(i, DateRange(n_sDate,n_eDate))          
    def editDateRangeFilter(self, index: int, n_sDate: QDateTime, n_eDate: QDateTime, test_en=False):
        """ Changes the date range via removing the old one"""
        index -= 1
        o_dr = self._date_ranges[index] # Original DateRange
        self._date_ranges.remove(index)
        try:
            self.addDateRangeFilter(n_sDate, n_eDate, test_en=test_en)
        except Exception as e:
            if (test_en): print(f"editDateRangeFilter()->{e}")
            self._date_ranges.insert(index, o_dr)
            return
        del o_dr # Deletes local reference
    def deleteDateRangeFilter(self, index: int, test_en=False):
        """ Deletes a date range with a given index """
        index -= 1
        try: 
            o_dr = self._date_ranges[index]
            self._date_ranges.remove(index)
            del o_dr # Deletes local reference
        except Exception as e:
            if (test_en): print(f"deleteDateRangeFilter() error: {e}")
    def clearDateRangeFilters(self):
        while self._date_ranges:
            p_dr = self._date_ranges.pop()
            del p_dr   
    # Getters for DateRange(s)
    def getDateRanges(self): return enumerate(self._date_ranges, start=1)
    def getDateRange(self, index: int):
        index -= 1
        if (index >= len(self._date_ranges)): raise Exception(f"getDateRange() error: Please select an index between [1-{len(self._date_ranges)}]")
        return self._date_ranges[index]

    def constructFilter(self):
        """ Function that builds a SQL WHERE filter from the stored information """
        format: dtFuncs.EDateTime = dtFuncs.EDateTime.Date
        filter: str = ''
        generic_filters: List[str] = []
        date_filters: List[str] = []

        if not (len(self._date_ranges) == 0):
            for dr in self._date_ranges:
                t_sDate, t_eDate = dtFuncs.dateTimeToPy(dr.startDate(), format), dtFuncs.dateTimeToPy(dr.endDate(), format)
                date_filters.append(('(EStart_Date <= {} AND COALESCE(EEnd_Date, EStart_Date) >= {})').format(t_eDate, t_sDate))
            d_f = ' OR '.join(date_filters)
            generic_filters.append(f'({d_f})')

        if type(self._userID)==int: generic_filters.append(f'E_CreatorUserID = {self._userID}')
        #if type(self._userID)==int: generic_filters.append(f'ScheduleID = {self._scheduleID}')
        #if type(self._userID)==int: generic_filters.append(f'E_LocationID = {self._locationID}')

        filter = ' AND '.join(generic_filters)
        return filter

class EventModel(QSortFilterProxyModel):
    def __init__(self, /, parent=None, *, 
                 db: QSqlDatabase=None,
                 filterRegularExpression=None, 
                 filterKeyColumn=-1, 
                 dynamicSortFilter=False, 
                 filterCaseSensitivity=Qt.CaseSensitivity.CaseSensitive, 
                 sortCaseSensitivity=Qt.CaseSensitivity.CaseSensitive, 
                 isSortLocaleAware=False, 
                 sortRole=Qt.ItemDataRole.UserRole, 
                 filterRole=Qt.ItemDataRole.DisplayRole, 
                 recursiveFilteringEnabled=False, 
                 autoAcceptChildRows=False):
        super().__init__(parent)
        self._userID: Optional[int] = None

        self._Queries = self.queries()
        self._Filters = self.filters()

        self._database: Optional[QSqlDatabase] = db

        #Bottom-most models; direct connections to the database
        self._eventModel = QSqlTableModel(self, db=self._database)                      #Bottom-most layer      (1.1)
        self._eventsUsersModel = QSqlTableModel(self, db=self._database)                #Bottom-most layer      (1.2) 

        self._eventConcatanationProxyModel = QConcatenateTablesProxyModel(self)         #Concatanation layer    (2)

        self.setupLayers


    def setupLayers(self):
        #Setup bottom-most layers
        self._eventModel.setTable('Events')
        self._eventsUsersModel.setTable('EU_Events_access')

        self._eventConcatanationProxyModel.addSourceModel(self._eventModel)
        self._eventConcatanationProxyModel.addSourceModel(self._eventsUsersModel)

        self.setSourceModel(self._eventConcatanationProxyModel)

    def changeUser(self, uid: int):
        # Will validate userID and act as padding before running on the view program
        self._setUserIDFilter(uid, test_en=True)
        pass

    def clearUser(self):
        self._setUserIDFilter(None)

    def _setUserIDFilter(self, uid, test_en=False):
        if (self._userID == uid): 
            if (test_en): print(f'{uid} is already current; exiting early')
            return
        else:            
            self._Filters.EventUserModel.clearUserFilter()      # As EventUserModel pulls in tagged* events; it should always remain clear

            if uid is None:     
                self._Filters.EventModel.clearUserFilter()     
                real_id = -1                                    # -1 Creates an empty set on the alterView
            else:               
                self._Filters.EventModel.addUserFilter(uid)
                real_id = uid                                   # Sets real_id to the actual ID 
        
        try:
            self._Queries.EventsUsersView.alterView(real_id, id_check=True)
        except Exception as e:
            if (test_en): print(f"###EventModel->setUserIDFilter()->{e}\n#### CANCELLING USER CHANGE, CALL AGAIN ####")
            return  # Early exit if the view could not be altered

        self._eventModel.setFilter(self._Filters.EventModel.constructFilter())
        self._eventsUsersModel.setFilter(self._Filters.EventUserModel.constructFilter())

        self._userID = uid

        self._selectall()

    def _selectall(self):
        self._eventModel.select()
        self._eventsUsersModel.select()

    def _alterView(self, uid):
        if (uid == None):
            pass

    class filters():
        """ Inner class for bundling EventFilters together under a common namespace
        """
        def __init__(self):
            self.EventModel = EventFilter()
            self.EventUserModel = EventFilter()
            pass

    class queries():
        """ Inner class for bundling database functions & QSqlQuery objects under common/legible namespaces.
        """
        def __init__(self):
            self.Users = self._UserQueries()
            self.EventsUsersView = self._EventViewQueries()
            pass

        class _UserQueries():  # Inner class for validating userIDs. Later implementations might see this conclusively stored & used in a user model;
            def __init__(self):
                self.defaultID = QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")

                self.validateID = QSqlQuery() 
                self.validateID.prepare("SELECT * FROM `Users` WHERE `UserID` = :user ;")
                pass

        class _EventViewQueries(): # Inner class for running operatings on the EU_Events views
            """     DB Structure: 
                        Tables:
                            Events
                            Events_Users (alias EU)
                        Views: 
                            EU_Events_edit      Edit table; contains only EventIDs based on the userID defined in the schema.
                                                    Queries will only edit this view; the Access view will reflect the changes.
                            EU_Events_access    Access table; contains only Events records. 
                                                    Program models connect to this view; the Edit view will dictate the Events in here.
            """ 
            def __init__(self):
                # DDL QSqlQuery; Internal use only, returns a result set on the schema table & should only be bundled with returnCurrentUID()
                self._exposeViewSchema = QSqlQuery("SHOW CREATE VIEW `EU_Events_edit`")
                
                # DDL Query for changing the view's current user
                self.changeEditViewCondition = QSqlQuery()
                self.changeEditViewCondition.prepare("ALTER VIEW `EU_Events_edit` AS SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user ;")
                
                # DML Query for checking common rows between the predicted & current dataset
                self.intersectingRowCheck = QSqlQuery()
                self.intersectingRowCheck.prepare("""
                                          SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                          INTERSECT
                                          SELECT * FROM `EU_Events_edit`
                                          """)
                # DML Query for counting number of common rows
                self.intersectingRowCount = QSqlQuery()
                self.intersectingRowCount.prepare("""
                                          SELECT COUNT(*) AS intersection_count
                                          FROM (
                                            SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                            INTERSECT
                                            SELECT * FROM `EU_Events_edit`
                                          ) AS intersecting_rows
                                          """)
                pass

            def returnCurrentUID(self):
                """ Convenience function for pulling the currently active view userID. Could be used as a form of persistant storage
                    on the event model; using the formerly saved view id as a way of storing the previously accessed user.
                    Provides some small degree of error handling & due to its intention of directly 
                """
                self._exposeViewSchema = sqlFuncs.execnext(self._exposeViewSchema)                                                           
                uid_check = re.search('`EU_UserID`\s*=\s*(\d+)',self._exposeViewSchema.value(1))                              
                if (uid_check): 
                    if ((uid_check.group(1)) != -1):    return uid_check.group(1)   # uid_check.group(1) should return the current users digit
                    else:                               return None                 # '-1' is a None value for EU_Events_edit; will return an empty set
                else: raise Exception("Could not pull a UserID from the schema")    # Error, if uid_check was not valid & thus a user digit was not associated with the set

            def alterView(self, uid: int, test_en=True, id_check=False):
                """ Convenience function for changing the userID via the changeEditViewCondition QSqlQuery.
                    sqlFuncs.execnext would not function here as its a DDL statement & thus will not return a result set.
                """
                # Optional clause that performs a id_check first
                if (id_check):
                    try: 
                        uid_check = self.returnCurrentUID()
                        if (uid == uid_check) and (test_en): raise Exception(f"alterView() error: UserID already set to {uid}, ALTER cancelled")
                    except Exception as e: print('alterView()->returnCurrentUID() error: UID Check failed, ',e)
                
                self.changeEditViewCondition.bindValue(':user', uid)
                exec_check = self.changeEditViewCondition.exec()
                if not (exec_check): raise Exception("alterView() error: ALTER VIEW Statement did not exec, SQL Error Msg: ",self.changeEditViewCondition.lastError())




# Function just to cascade some SQL queries passed        
def empty_proc():
        pass
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
SELECT * FROM `EU_layer1_FilteredEvents`

--
-- Triggers `Events`
--
DELIMITER $$
CREATE TRIGGER `AUTO_Event_Initial_JSON_Format` BEFORE INSERT ON `Events` FOR EACH ROW BEGIN
	DECLARE object_index INT DEFAULT 0;
	DECLARE event_type INT DEFAULT 0;
	DECLARE info JSON DEFAULT JSON_OBJECT('object_index', 0, 'event_type', 0);
    	DECLARE objects JSON DEFAULT JSON_OBJECT();
		-- If none specified, generate a default value --
		IF (NEW.EAttributes IS Null OR NEW.Eattributes ='') THEN
        		SET NEW.EAttributes = JSON_OBJECT("info", info);
		ELSE
            -- Extract any $.info attributes & set to local variables -- 
          	IF JSON_EXTRACT(NEW.EAttributes, "$.info") IS Null THEN
              	IF (JSON_EXISTS(NEW.EAttributes, "$.object_index") IS NOT Null) THEN
					SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$.object_index") AS UNSIGNED);
                    SET info = JSON_SET(info, "object_index", object_index);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.object_index");
				END IF;
				IF (JSON_EXISTS(NEW.EAttributes, "$.event_type") IS NOT Null) THEN
					SET event_type = JSON_VALUE(NEW.EAttributes, "$.event_type");
                    SET info = JSON_SET(info, "event_type", event_type);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.event_type");
				END IF;
            -- Otherwise, if info provided --
          	ELSE
            	-- Local store --
            	SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$info.object_index") AS UNSIGNED);
            	SET event_type = JSON_VALUE(NEW.EAttributes, "$info.event_type");
                
                SET info = JSON_EXTRACT(NEW.EAttributes, "$.info");
                SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.info");
            END IF;
            -- After that if-else execution, any info values should be safely contained in $.info with their individual values in object_index & event_type -- 
        	-- Check then for existence of keys in absence of objects -- 
        	IF JSON_EXTRACT(NEW.EAttributes, "$.objects") IS Null THEN
                -- Post processing existing keys, check if the attributes leftover are still equal to 0
                IF JSON_LENGTH(JSON_KEYS(NEW.EAttributes)) > 0 THEN
                	SET objects = NEW.EAttributes;
                END IF;
            -- However, if $.objects is there -- 
		ELSE
                -- Extract objects as standalone JSON_OBJECT --
                SET objects = JSON_EXTRACT(NEW.EAttributes, "$.objects");
            END IF;
                
            -- Quickly update the object_index if there's a mismatch between the predicted lengths --     
            IF (JSON_LENGTH(JSON_KEYS(objects)) != object_index) THEN
                -- Take the count of objects & update the index --
                SET object_index = CAST(JSON_LENGTH(JSON_KEYS(objects)) AS UNSIGNED)
                SET info = JSON_SET(info, "object_index", object_index);
            END IF;
            
            -- If object_index is still 0, only add info tab --
            IF (object_index == 0) THEN
                SET NEW.EAttributes = JSON_OBJECT(
                 	'info', info
                );
            ELSE
                SET NEW.EAttributes = JSON_OBJECT(
                  	'info', info,
                    'objects', objects
                ); 
            END IF;
        END IF;
	END
$$
DELIMITER ;"""
        
def new_dump():
    """SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `decan`
--

DROP TABLE IF EXISTS `Events_Tags`;
DROP TABLE IF EXISTS `Events_Users`;
DROP TABLE IF EXISTS `Events`;
DROP VIEW IF EXISTS `EU_FilteredEvents`;
DROP VIEW IF EXISTS `EU_Events_edit`;
DROP VIEW IF EXISTS `EU_Events_access`;

-- --------------------------------------------------------

--
-- Table structure for table `Events`
--

CREATE TABLE `decan`.`Events` 
(`EventID` INT(6) NOT NULL AUTO_INCREMENT ,
 `ETitle` VARCHAR(64) NOT NULL ,
 `EStart` DATETIME NOT NULL ,
 `EEnd` DATETIME NOT NULL CHECK (`EEnd` >= `EStart`) , 
 `EAttributes` JSON NULL ,
 `E_CreatorUserID` INT(3) NOT NULL ,
 `E_LocationID` INT(10) NULL ,
CONSTRAINT `PK_Event` PRIMARY KEY (`EventID`) ,
CONSTRAINT `FK_User_Event` 
FOREIGN KEY (`E_CreatorUserID`) REFERENCES `Users`(`UserID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
FOREIGN KEY (`E_LocationID`) REFERENCES `Address`(`AddressID`) 
ON DELETE SET NULL ON UPDATE NO ACTION )
ENGINE = InnoDB;

CREATE TABLE `decan`.`Events_Users` 
(`EU_EventID` INT(6) NOT NULL ,
 `EU_UserID` INT(3) NOT NULL ,
CONSTRAINT `PK_EU` PRIMARY KEY (`EU_EventID`,`EU_UserID`) ,
CONSTRAINT `FK_EU_Event` 
FOREIGN KEY (`EU_EventID`) REFERENCES `Events`(`EventID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
CONSTRAINT `FK_EU_User` 
FOREIGN KEY (`EU_UserID`) REFERENCES `Users`(`UserID`) 
ON DELETE CASCADE ON UPDATE NO ACTION )
ENGINE = InnoDB;

CREATE TABLE `decan`.`Events_Tags` 
(`ET_EventID` INT(6) NOT NULL ,
 `ET_TagID` INT(3) NOT NULL ,
CONSTRAINT `PK_ET` PRIMARY KEY (`ET_EventID`,`ET_TagID`) ,
CONSTRAINT `FK_ET_Event` 
FOREIGN KEY (`ET_EventID`) REFERENCES `Events`(`EventID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
CONSTRAINT `FK_ET_Tags` 
FOREIGN KEY (`ET_TagID`) REFERENCES `Tags`(`TagID`) 
ON DELETE CASCADE ON UPDATE NO ACTION )
ENGINE = InnoDB;

--
-- Triggers `Events`
--
DELIMITER $$
CREATE TRIGGER `AUTO_Event_Initial_JSON_Format` BEFORE INSERT ON `Events` FOR EACH ROW BEGIN
	DECLARE object_index INT DEFAULT 0;
	DECLARE event_type INT DEFAULT 0;
	DECLARE info JSON DEFAULT JSON_OBJECT('object_index', 0, 'event_type', 0);
	DECLARE objects JSON DEFAULT JSON_OBJECT();
	-- If none specified, generate a default value --
		IF (NEW.EAttributes IS Null OR NEW.Eattributes ='') THEN
        		SET NEW.EAttributes = JSON_OBJECT("info", info);
		ELSE
            -- Extract any $.info attributes & set to local variables -- 
          		IF JSON_EXTRACT(NEW.EAttributes, "$.info") IS Null THEN
          			IF (JSON_EXISTS(NEW.EAttributes, "$.object_index") IS NOT Null) THEN
					SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$.object_index") AS UNSIGNED);
					SET info = JSON_SET(info, "object_index", object_index);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.object_index");
				END IF;
				IF (JSON_EXISTS(NEW.EAttributes, "$.event_type") IS NOT Null) THEN
					SET event_type = JSON_VALUE(NEW.EAttributes, "$.event_type");
					SET info = JSON_SET(info, "event_type", event_type);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.event_type");
				END IF;
            			-- Otherwise, if info provided --
            		ELSE
            			-- Local store --
            			SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$info.object_index") AS UNSIGNED);
            			SET event_type = JSON_VALUE(NEW.EAttributes, "$info.event_type");
            			
            			SET info = JSON_EXTRACT(NEW.EAttributes, "$.info");
            			SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.info");
            		END IF;
            		
            		-- After that if-else execution, any info values should be safely contained in $.info with their individual values in object_index & event_type -- 
            		-- Check then for existence of keys in absence of objects -- 
            		IF JSON_EXTRACT(NEW.EAttributes, "$.objects") IS Null THEN
            			-- Post processing existing keys, check if the attributes leftover are still equal to 0
            			IF JSON_LENGTH(JSON_KEYS(NEW.EAttributes)) > 0 THEN
            				SET objects = NEW.EAttributes;
            			END IF;
            		-- However, if $.objects is there --
            		ELSE
            			-- Extract objects as standalone JSON_OBJECT --
            			SET objects = JSON_EXTRACT(NEW.EAttributes, "$.objects");
            		END IF;
            		
            		-- Quickly update the object_index if there's a mismatch between the predicted lengths --
            		IF (JSON_LENGTH(JSON_KEYS(objects)) != object_index) THEN
            			-- Take the count of objects & update the index --
            			SET object_index = CAST(JSON_LENGTH(JSON_KEYS(objects)) AS UNSIGNED);
            			SET info = JSON_SET(info, "object_index", object_index);
            		END IF;
            		
            		-- If object_index is still 0, only add info tab --
            		IF object_index = 0 THEN
            			SET NEW.EAttributes = JSON_OBJECT(
            				'info', info
            			);
            		ELSE
            			SET NEW.EAttributes = JSON_OBJECT(
            				'info', info,
            				'objects', objects
            			); 
            		END IF;
            	END IF;
	END
$$
DELIMITER ;

--
-- Dumping data for table `Events`
--

INSERT INTO `Events` (`EventID`, `ETitle`, `EStart`, `EEnd`, `EAttributes`, `E_CreatorUserID`, `E_LocationID`) VALUES
(3, 'Date with Danielle', '2024-04-05 20:00:00', '2024-04-05 20:25:00', '{\"object_index\": 0}', 2, NULL),
(4, 'Halloween Party', '2024-10-23 23:00:00', '2024-10-24 02:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Bring a costume that shares your initial!\"}', 1, NULL),
(5, 'Shopping', '2024-10-15 20:00:00', '2024-10-15 20:25:00', '{\"object_index\": 0}', 2, NULL),
(6, 'James Trip', '2024-10-26 23:00:00', '2024-10-27 00:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Going fishing with James!\"}', 3, NULL),
(7, 'Christmas', '2024-12-25 00:00:00', '2024-12-25 23:59:00', '{\"object_index\": 1, \"EDescription_1\": \"Santa Clause is coming to town!\"}', 1, NULL),
(8, 'Christmas Shopping', '2024-12-25 20:00:00', '2024-12-25 20:25:00', '{\"EToDo_1\":{\"EBool\":false,\"ETaskDescription\":\"Buy Gerald Shoes\"},\"object_index\":1}', 1, NULL),
(9, 'Gaming session', '2024-11-04 23:00:00', '2024-11-05 02:00:00', '{\"object_index\": 0}', 2, NULL),
(10, 'Fun times at beach', '2024-10-12 23:00:00', '2024-10-13 02:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Bring a costume that shares your initial!\"}', 2, NULL),
(11, 'Shopping at Walmart', '2024-10-24 19:00:00', '2024-10-24 20:00:00', '{\"EDescription_3\":\"Check if there is any baby carriers as well\",\"EToDo_1\":{\"EBool\":false,\"ETaskDescription\":\"Buy eggs\"},\"EToDo_2\":{\"EBool\":false,\"ETaskDescription\":\"Buy milk\"},\"object_index\":3}', 3, NULL),
(17, 'Dentist', '2025-02-09 00:00:00', '2025-02-10 00:00:00', '{\"object_index\": 0}', 3, NULL);
    
CREATE ALGORITHM = MERGE VIEW `EU_Events_edit` AS SELECT
    `Events_Users`.`EU_EventID` AS `EU_EventID`
FROM
    `Events_Users`
WHERE
    `Events_Users`.`EU_UserID` = 3;

CREATE ALGORITHM = MERGE VIEW `EU_Events_access` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `EU_Events_edit` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    );

ALTER VIEW `EU_Events_edit` AS 
SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = 2;

SELECT * FROM `Events` WHERE 
(
    (
        (`EStart_Date` <= '2024-04-30' AND COALESCE(`EEnd_Date`,`EStart_Date`) >= '2023-03-00')
    ) OR (
        (`EStart_Date` <= '2025-05-30' AND COALESCE(`EEnd_Date`,`EStart_Date`) >= '2024-11-00')
    )
)
AND `E_CreatorUserID` = 2

--
-- AUTO_INCREMENT for table `Events`
--
ALTER TABLE `Events`
  MODIFY `EventID` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Dumping data for table `Events_Users`
--

INSERT INTO `Events_Users` (`EU_EventID`, `EU_UserID`) VALUES
(3, 1),
(3, 3),
(4, 3),
(5, 1),
(6, 1),
(6, 2),
(8, 2),
(10, 3);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

#1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'ALTER TABLE `Events`
  MODIFY `EventID` int(6) NOT NULL AUTO_INCREMENT, AUTO...' at line 14"""
        
class CEventUserModel(QSqlTableModel): #Access model for view in database
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
        self.pullUser = sqlFuncs.execnext(self.pullUser)                                                           # Error messages to be passed to terminal
        uid_check, msg = re.search('`EU_UserID`\s*=\s*(\d+)',self.pullUser.value(1)),                                       'N/A'
        if (uid_check): self._user_id, msg = uid_check.group(1),                                                            'Successfully managed to'
        else:           self._user_id, msg = int(sqlFuncs.execnext(QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")).value(0)),     'Failed to'
        # Above code checks if a match was found in the view's initial query; if not, it defaults to another user. 
        if (test_en): print(f"###EUModel {msg} extract ID from view\nCurrent UserID: ",self._user_id)
        if ((msg) == 'Failed to'): self.changeUser(uid=self._user_id)
    
    def changeUser(self, uid: int, test_en=True):
        if (uid == self._user_id): return #Exit early if _user_id already matches the current
        else:
            # Validate userID
            cur_id = self._user_id
            self.userValidate.bindValue(":user", uid)
            self.userValidate = sqlFuncs.execnext(self.userValidate)
            if not (self.userValidate.isValid()):
                if (test_en): print(f"###EUModel Validate Error: {self.userValidate.lastError()}")
                return #Exit early if _user_id does not exist
            else: self._user_id = uid 
            # Change view Query
            self.userChange.bindValue(":user", uid)
            self.userChange.exec()
            self.select()
            self.intersectingRowCount.bindValue(':user', cur_id)
            same_rows = sqlFuncs.execnext(self.intersectingRowCount).value(0)
            if (test_en): print('###EUModel: User changed\n#### (Overall) Matching:New Rows: (',self.rowCount(),') ',same_rows,':',self.rowCount()-same_rows)
    


"""class UserFilterModel(QSortFilterProxyModel):

class EventUserModel(QSqlQueryModel):

class EventModelMapper(QConcatenateTablesProxyModel):

class EventFilterModel(QSortFilterProxyModel):"""