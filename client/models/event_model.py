import sys, re, datetime
from typing import List, Optional, Union
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, 
                            QSortFilterProxyModel, QConcatenateTablesProxyModel, 
                            QDate, QDateTime, QTime,
                            QRegularExpression, Signal,
                            QModelIndex)
from PySide6.QtSql import (QSqlDatabase, 
                           QSqlTableModel, QSqlQueryModel, 
                           QSqlQuery,
                           QSqlRecord)

from .user_model import UserModel
from .location_model import LocationModel
import modules.sql_qt as sql_funcs
import modules.datetime_qt as dt_funcs

class DateRange:
    def __init__ (self, start_date: QDateTime, end_date: QDateTime):
        super().__init__()
        self._startDate = start_date
        self._endDate = end_date
    
    # Getters (no setters; changes to the date must be first determined via the EventFilter, as overlap is acknowledged there)
    def startDate(self): return self._startDate
    def endDate(self): return self._endDate

    # Function for determining overlap without pulling either out
    def overlap(self, n_s_date: QDateTime, n_e_date: QDateTime):
        if (self._endDate <= n_s_date) or (self._startDate >= n_e_date): return False
        return True

class EventFilter:
    def __init__(self):
        super().__init__()
        self._userID: Optional[int] = None
        self._scheduleID: Optional[int] = None
        self._locationID: Optional[int] = None
        self._date_ranges: List[DateRange] = []
    
    # Setters for userFilter; Could connect to user_model later
    def addUserFilter(self, user_id: int): self._userID = user_id
    def clearUserFilter(self): self._userID = None

    # Setters for schedules; One 1 schedule permitted to search at one time
    def addScheduleFilter(self, schedule_id): self._scheduleID = schedule_id
    def clearScheduleFilter(self): self._scheduleID = None

    # Setters for location; Could expand to allow tagging of multiple locations, similar to DateRange
    def addLocationFilter(self, location_id): self._locationID = location_id
    def clearLocationFilter(self): self._locationID = None

    # Setters for DateRange(s)
    """ All indexes are subtracted with 1 """
    def addManyDateRangeFilters(self, date_ranges: List[DateRange], test_en=False):
        """ Convenience function for adding multiple DateRanges at once """
        if len(date_ranges) <= 0: return
        for dr in date_ranges:
            try: 
                self.addDateRangeFilter(dr.startDate(),dr.endDate(), test_en=test_en)
            except Exception as e:
                if test_en: print(f'addManyDateRangeFilters()->{e}')
    def addDateRangeFilter(self, n_s_date: QDateTime, n_e_date: QDateTime, test_en=False):
        """ Function for adding a DateRange to the DateRanges list """
        f = dt_funcs.EDateTime.Date  #Format for error printing
        i = 0                   #Insertion index

        if len(self._date_ranges) <= 0: # Exits program early if the list is empty and adds the new DateRange to the list
            self._date_ranges.append(DateRange(n_s_date, n_e_date))
            return
        
        for index, dr in enumerate(self._date_ranges, start=1):
            i_s_date, i_e_date = dr.startDate(), dr.endDate()     #Index start and end dates
            if dr.overlap(n_s_date, n_e_date): raise Exception(f"""addDateRange() error: New date range overlaps with existing filter
                                                               [{dt_funcs.date_time_to_fs(i_s_date, f)}< (...) <{dt_funcs.date_time_to_fs(i_e_date, f)}]:[Filter @ {index}]
                                                               [{dt_funcs.date_time_to_fs(n_s_date, f)}< (...) <{dt_funcs.date_time_to_fs(n_e_date, f)}]:[Proposed Filter]""")
            else: 
                if test_en: print(f"Cleared [{index}/{len(self._date_ranges)}] of date_ranges")

                # Updates the insertion index if either value is true
                if (n_e_date < i_s_date) or (i_e_date < n_s_date): i = index - 1
        # Will insert DateRange at the appropriate place in the filter list
        self._date_ranges.insert(i, DateRange(n_s_date, n_e_date))
    def editDateRangeFilter(self, index: int, n_s_date: QDateTime, n_e_date: QDateTime, test_en=False):
        """ Changes the date range via removing the old one"""
        index -= 1
        o_dr = self._date_ranges[index] # Original DateRange
        self._date_ranges.remove(o_dr)
        try:
            self.addDateRangeFilter(n_s_date, n_e_date, test_en=test_en)
        except Exception as e:
            if test_en: print(f"editDateRangeFilter()->{e}")
            self._date_ranges.insert(index, o_dr)
            return
        del o_dr # Deletes local reference
    def deleteDateRangeFilter(self, index: int, test_en=False):
        """ Deletes a date range with a given index """
        index -= 1
        try: 
            o_dr = self._date_ranges[index]
            self._date_ranges.remove(o_dr)
            del o_dr # Deletes local reference
        except Exception as e:
            if test_en: print(f"deleteDateRangeFilter() error: {e}")
    def clearDateRangeFilters(self):
        while self._date_ranges:
            p_dr: DateRange = self._date_ranges.pop()
            del p_dr   
    # Getters for DateRange(s)
    def getDateRanges(self): return enumerate(self._date_ranges, start=1)
    def getDateRange(self, index: int):
        index -= 1
        if index >= len(self._date_ranges): raise Exception(f"getDateRange() error: Please select an index between [1-{len(self._date_ranges)}]")
        return self._date_ranges[index]


    def constructFilter(self):
        """ Function that builds a SQL WHERE complete_filter from the stored information """
        f: dt_funcs.EDateTime = dt_funcs.EDateTime.Date
        generic_filters: List[str] = []
        date_filters: List[str] = []

        if not (len(self._date_ranges) <= 0):
            for dr in self._date_ranges:
                t_s_date, t_e_date = dt_funcs.date_time_to_py(dr.startDate(), f), dt_funcs.date_time_to_py(dr.endDate(), f)
                date_filters.append(
                    '(EStart_Date <= {} AND COALESCE(EEnd_Date, EStart_Date) >= {})'.format(t_e_date, t_s_date))
            d_f = ' OR '.join(date_filters)
            generic_filters.append(f'({d_f})')

        if isinstance(self._userID, int): generic_filters.append(f'E_CreatorUserID = {self._userID}')
        #if type(self._userID)==int: generic_filters.append(f'ScheduleID = {self._scheduleID}')
        #if type(self._userID)==int: generic_filters.append(f'E_LocationID = {self._locationID}')

        complete_filter = ' AND '.join(generic_filters)
        return complete_filter

class EventModel(QSortFilterProxyModel):

    def __init__(self, /, parent=None, *,
                 db                         :QSqlDatabase       =None,
                 userModel                  :UserModel          =None,
                 locationModel              :LocationModel      =None,
                 filterRegularExpression    :QRegularExpression =None,
                 filterKeyColumn            :int                =-1,
                 dynamicSortFilter          :bool               =True,
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
        self._Queries = self.Queries()
        self._Filters = self.Filters()

        self._userID: Optional[int] = None
        self._database: Optional[QSqlDatabase] = db
        self._userModel: Optional[UserModel] = userModel
        self._locationModel: Optional[LocationModel] = locationModel

        #Bottom-most models; direct connections to the database
        self._eventModel = QSqlTableModel(self, db=self._database)                      #Bottom-most layer      (1.1)
        self._eventsUsersModel = QSqlTableModel(self, db=self._database)                #Bottom-most layer      (1.2) 

        self._eventConcatenationProxyModel = QConcatenateTablesProxyModel(self)         #Concatanation layer    (2)

        self._eventLookupModel = QSortFilterProxyModel(self)                            #Look-up access - sits 'parallel' to this one

        self.setupLayers()

    def setupLayers(self):
        #Setup bottom-most layers
        self._eventModel.setTable('Events')
        self._eventsUsersModel.setTable('EU_Events_access')

        self._eventConcatenationProxyModel.addSourceModel(self._eventModel)
        self._eventConcatenationProxyModel.addSourceModel(self._eventsUsersModel)

        self._eventLookupModel.setSourceModel(self._eventConcatenationProxyModel)
        self._eventLookupModel.setDynamicSortFilter(True)
        self._eventLookupModel.setSortRole(Qt.ItemDataRole.DisplayRole)
        self._eventLookupModel.sort(0, Qt.SortOrder.AscendingOrder)

        self.setSourceModel(self._eventConcatenationProxyModel)
        self.setDynamicSortFilter(True)
        self.setSortRole(Qt.ItemDataRole.EditRole)
        self.sort(3, Qt.SortOrder.AscendingOrder)

    def data(self, index, /, role = ...):
        return super().data(index, role)

    def changeUser(self, uid: Union[int, QModelIndex]):
        # Will validate user_id and act as padding before running on the view program
        if isinstance(uid, QModelIndex):
            print(QModelIndex)
            uid = uid.row()
        self._setUserIDFilter(uid, test_en=True)
        pass

    def clearUser(self):
        self._setUserIDFilter(None)

    def _setUserIDFilter(self, uid, test_en=False):
        if self._userID == uid:
            if test_en: print(f'{uid} is already current; exiting early')
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
            if test_en: print(f"###EventModel->setUserIDFilter()->{e}\n#### CANCELLING USER CHANGE, CALL AGAIN ####")
            return  # Early exit if the view could not be altered

        self._eventModel.setFilter(self._Filters.EventModel.constructFilter())
        self._eventsUsersModel.setFilter(self._Filters.EventUserModel.constructFilter())

        self._userID = uid

        self.select()

    def select(self):
        self._eventModel.select()
        self._eventsUsersModel.select()

    def _alterView(self, uid):
        if uid is None:
            pass

    def refresh(self):
        self._eventModel.select()
        self._eventsUsersModel.select()

    class Filters:
        """ Inner class for bundling EventFilters together under a common namespace
        """
        def __init__(self):
            self.EventModel = EventFilter()
            self.EventUserModel = EventFilter()
            pass

    class Queries:
        """ Inner class for bundling database functions & QSqlQuery objects under common/legible namespaces.
        """
        def __init__(self):
            self.Users = self._UserQueries()
            self.EventsUsersView = self._EventViewQueries()
            pass

        class _UserQueries:  # Inner class for validating userIDs. Later implementations might see this conclusively stored and used in a user model;
            def __init__(self):
                self.defaultID = QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")

                self.validateID = QSqlQuery() 
                self.validateID.prepare("SELECT * FROM `Users` WHERE `UserID` = :user ;")
                pass
        
        class _EventQueries:
            def __init__(self):
                pass

        class _EventViewQueries: # Inner class for running operations on the EU_Events views
            """     DB Structure: 
                        Tables:
                            Events
                            Events_Users (alias EU)
                        Views: 
                            EU_Events_edit      Edit table; contains only EventIDs based on the user_id defined in the schema.
                                                    Queries will only edit this view; the Access view will reflect the changes.
                            EU_Events_access    Access table; contains only Events records. 
                                                    Program models connect to this view; the Edit view will dictate the Events in here.
            """ 
            def __init__(self):
                # DDL QSqlQuery; Internal use only, returns a result set on the schema table and should only be bundled with returnCurrentUID()
                self._exposeViewSchema = QSqlQuery("SHOW CREATE VIEW `EU_Events_edit`")
                
                # DDL Query for changing the view's current user
                self.changeEditViewCondition = QSqlQuery()
                self.changeEditViewCondition.prepare("ALTER VIEW `EU_Events_edit` AS SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user ;")
                
                # DML Query for checking common rows between the predicted and current dataset
                self.intersectingRowCheck = QSqlQuery()
                self.intersectingRowCheck.prepare("""
                                          SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                          INTERSECT
                                          SELECT * FROM `EU_Events_edit`
                                          """)
                # DML Query for counting the number of common rows
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
                """ Convenience function for pulling the currently active view user_id. Could be used as a form of persistent storage
                    on the event model; using the formerly saved view id as a way of storing the previously accessed user.
                    Provides some small degree of error handling and due to its intention of directly
                """
                self._exposeViewSchema = sql_funcs.execnext(self._exposeViewSchema)
                uid_check = re.search('`EU_UserID`\s*=\s*(\d+)',self._exposeViewSchema.value(1))                              
                if uid_check:
                    if (uid_check.group(1)) != -1:    return uid_check.group(1)   # uid_check.group(1) should return the current users digit
                    else:                               return None                 # '-1' is a None value for EU_Events_edit; will return an empty set
                else: raise Exception("Could not pull a UserID from the schema")    # Error, if uid_check was not valid and thus a user digit was not associated with the set

            def alterView(self, uid: int, test_en=True, id_check=False):
                """ Convenience function for changing the user_id via the changeEditViewCondition QSqlQuery.
                    sql_funcs.execnext would not function here as it's a DDL statement and thus will not return a result set.
                """
                # Optional clause that performs an id_check first
                if id_check:
                    try: 
                        uid_check = self.returnCurrentUID()
                        if (uid == uid_check) and test_en: raise Exception(f"alterView() error: UserID already set to {uid}, ALTER cancelled")
                    except Exception as e: print('alterView()->returnCurrentUID() error: UID Check failed, ',e)
                
                self.changeEditViewCondition.bindValue(':user', uid)
                exec_check = self.changeEditViewCondition.exec()
                if not exec_check: raise Exception("alterView() error: ALTER VIEW Statement did not exec, SQL Error Msg: ", self.changeEditViewCondition.lastError())