# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow
from PySide6.QtSql import QSqlDatabase

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic --from-imports resources/ui/main_view.ui -o client/views/main_view_ui.py

from .main_view_ui import Ui_main_view
from .pages.user_view import UserView
from .pages.event_view import EventView


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        print(QSqlDatabase.drivers())

        self._database = QSqlDatabase.addDatabase('QMYSQL')
        self._database.setHostName('192.168.1.147')
        self._database.setUserName('sebastianji')
        self._database.setPassword('admin')  #genTen212!')
        self._database.setDatabaseName('decan')

        self._database.setConnectOptions("SSL_CA=/Users/sebastianji/Documents/DB Certs/ca.pem")

        if not self._database.open():
            print('connection failed')
            print('open() error->',self._database.lastError().text())


        self._Ui = Ui_main_view()
        self._Ui.setupUi(self)
        self._Ui.collapsed.hide()

        self._Ui.UserPage = UserView(self, self._database)
        self._Ui.pages.addWidget(self._Ui.UserPage)
        self._Ui.EventPage = EventView(self, self._database)
        self._Ui.pages.addWidget(self._Ui.EventPage)

        self.setup_connections()

    def setup_connections(self):
        self._Ui.col_toggle.clicked.connect(lambda: self.toggle_nav())
        self._Ui.exp_toggle.clicked.connect(lambda: self.toggle_nav())

        self._Ui.exp_p1_user.clicked.connect(lambda: self._Ui.pages.setCurrentIndex(0))
        self._Ui.exp_p2_events.clicked.connect(lambda: self._Ui.pages.setCurrentIndex(1))

        self._Ui.col_p1_user.clicked.connect(lambda: self._Ui.pages.setCurrentIndex(0))
        self._Ui.col_p2_events.clicked.connect(lambda: self._Ui.pages.setCurrentIndex(1))

        self._Ui.UserPage.userChanged.connect(lambda package: self._Ui.EventPage.setUserFilter(package))


    def toggle_nav(self):
        if self._Ui.collapsed.isVisible():
            self._Ui.expanded.show()
            self._Ui.collapsed.hide()
        else:
            self._Ui.collapsed.show()
            self._Ui.expanded.hide()
