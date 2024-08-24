# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic resources/ui_files/main_view.ui -o resources/ui_designs/ui_main_view.py, or
#     pyside2-uic main_view.ui -o ui_main_view.py
from views.resources.ui_designs.ui_main_view import Ui_MainWindow
from views.resources.custom_classes.eventitem import EventItem, Event
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

        #self._ui.Event.set_data('Daniels Birthday'*10, 'I love the rain'*100, '16:30')


    def setup_links_nav(self):
        #defines all links for components in ui
        self._ui.b_user.clicked.connect(lambda: self._ui.pages.setCurrentIndex(0))
        self._ui.b_calendar.clicked.connect(lambda: self._ui.pages.setCurrentIndex(1))
        self._ui.b_settings.clicked.connect(lambda: self._ui.pages.setCurrentIndex(2))

    def setup_tables(self):
        self._user_model = QSqlTableModel()
        self._user_model.setTable("Users")
        self._ui.table_user.setModel(self._user_model)
        self._user_model.select()
        
    def setup_connection(self):
        self._database = QSqlDatabase.addDatabase('QMYSQL')
        self._database.setHostName('localhost')
        self._database.setUserName('sebastianji')
        self._database.setPassword('genTen212!')
        self._database.setDatabaseName('decan')

        if not self._database.open():
            print('connection failed')
            print(self._database.lastError().text())
            