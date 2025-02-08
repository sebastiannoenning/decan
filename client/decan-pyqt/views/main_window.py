# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime

from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QDate

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic resources/ui_files/main_view.ui -o resources/ui_designs/ui_main_view.py, or
#     pyside2-uic main_view.ui -o ui_main_view.py
from views.resources.ui_designs.ui_main_view import Ui_MainWindow
from views.resources.custom_classes.eventitem import EventItem#, Event
from models.user_model import UserModel

class MainWindow(QMainWindow):
    def __init__(self, parent=None):#, model, controller):
        super().__init__(parent)

        #self._model = model
        #self._controller = controller

        #self load ui components
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        #print(QSqlDatabase.drivers())

        #remove title bar
        #self.setWindowFlag(Qt.FramelessWindowHint)

        self._ui.pages.setCurrentIndex(0)
        self.setup_links_nav()
        self.setup_connection()
        self.setup_tables()
        self.setup_links_combo()
        self.setup_add_event()

        #self._ui.Event.set_data('Daniels Birthday'*10, 'I love the rain'*100, '16:30')

    def setup_links_nav(self):
        #defines all links for components in ui
        self._ui.b_user.clicked.connect(lambda: self._ui.pages.setCurrentIndex(0))
        self._ui.b_calendar.clicked.connect(lambda: self._ui.pages.setCurrentIndex(1))
        self._ui.b_events.clicked.connect(lambda: self._ui.pages.setCurrentIndex(2))
        self._ui.b_settings.clicked.connect(lambda: self._ui.pages.setCurrentIndex(3))

    def setup_links_combo(self): #Temporary function for connecting userSelect to the 
        self._ui.userSelect.currentTextChanged.connect(lambda name: self.changeEventFilter(name))
        self._ui.b_delete.clicked.connect(self._ui.scrollAreaWidgetContents.deleteSelected)

    def setup_add_event(self):
        self._ui.AE_CB_userSelect.setModel(self._user_profile_model)
        self._ui.AE_CB_userSelect.setModelColumn(2)

        #self._ui.AE_LE_inputTitle.editingFinished
        self._ui.AE_DTE_startDTSelect.dateChanged.connect(lambda: 
                                                          self._ui.AE_DTE_endDTSelect.setMinimumDateTime(
                                                              self._ui.AE_DTE_startDTSelect.dateTime()
                                                          ))

        self._ui.AE_DTE_startDTSelect.setDate(QDate.currentDate())
        self._ui.AE_DTE_endDTSelect.setDate(QDate.currentDate())

        self._ui.AE_PB_addEvent.clicked.connect(lambda: self.addEvent())

    def setup_tables(self):
        print(self._database.tables())
        #query = QSqlQuery()
        #query.exec('SELECT * FROM Events')
        #print(query.size(), query.record().count())
        self._user_model = QSqlTableModel()
        self._user_profile_model = QSqlTableModel()
        self._event_model = QSqlRelationalTableModel()
        
        self._user_model.setTable("Users")
        self._user_profile_model.setTable("UserProfile")
        self._event_model.setTable("Events")
        
        #self._user_profile_model.setRelation(5, QSqlRelation("Address","AddressID","AddressID"))
        self._event_model.setRelation(7, QSqlRelation("Users","UserID","Username"))
        self._event_model.setFilter("UserID = '2'")
        
        self._user_model.select()
        self._user_profile_model.select()
        self._event_model.select()
        
        self._ui.table_user.setModel(self._user_model)
        self._ui.table_user_profile.setModel(self._user_profile_model)
        self._ui.table_events.setModel(self._event_model)

        self._ui.userSelect.setModel(self._user_profile_model)
        self._ui.userSelect.setModelColumn(2)

        self._ui.scrollAreaWidgetContents.resize(self._ui.upcomingevents.width(), self._ui.upcomingevents.height())
        self._ui.scrollAreaWidgetContents.setModel(self._event_model)
        #print(self._user_model.rowCount())
        # 
        """self._event_model2 =  QSqlRelationalTableModel()
        self._event_model2.setTable("Events") 
        self._event_model2.setRelation(7, QSqlRelation("Users","UserID","Username"))
        self._event_model2.setFilter("UserID = '3'")
        self._event_model2.select()
        self._ui.scrollAreaWidgetContents.setModel(self._event_model2)"""
        
    def setup_connection(self):
        self._database = QSqlDatabase.addDatabase('QMYSQL')
        self._database.setHostName('localhost')
        self._database.setUserName('sebastianji')
        self._database.setPassword('admin')#genTen212!')
        self._database.setDatabaseName('decan')

        if not self._database.open():
            print('connection failed')
            print(self._database.lastError().text())

    def changeEventFilter(self, currentText):
        try:
            userID = self.returnQuery(QSqlQuery(f"SELECT `UP_UserID` FROM `UserProfile` WHERE `Forename` = '{currentText}'"))
            self._event_model.setFilter(f"UserID = '{userID}'")
            self._event_model.select()
            self._ui.table_events.setModel(self._event_model)
        except Exception as e:
            print("eventFilter change not possible:",e)
    
    def addEvent(self):
        userID = self.returnQuery(QSqlQuery(f"SELECT `UP_UserID` FROM `UserProfile` WHERE `Forename` = '{(self._ui.AE_CB_userSelect.currentText())}'"))
        print(self._ui.AE_LE_inputTitle.displayText())
        newEvent = {
            'ETitle'            :   self._ui.AE_LE_inputTitle.displayText(),
            'EStart_Date'       :   (self._ui.AE_DTE_startDTSelect.date()).toPython().strftime('%Y-%m-%d'),
            'EStart_Time'       :   (self._ui.AE_DTE_startDTSelect.time()).toPython().strftime('%H:%M:%S'),
            'EEnd_Date'         :   (self._ui.AE_DTE_endDTSelect.date()).toPython().strftime('%Y-%m-%d'),
            'EEnd_Time'         :   (self._ui.AE_DTE_endDTSelect.time()).toPython().strftime('%H:%M:%S'),
            'E_CreatorUserID'   :   userID,
        }

    def returnQuery(self, query: QSqlQuery):
        query.exec()
        query.next()
        return query.value(0)

    #def clearEvent(self):