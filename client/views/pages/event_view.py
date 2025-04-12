from typing import List

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime
from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/pages/event_view.ui -o client/views/pages/event_view_ui.py, or
#       pyside6-uic --from-imports pages/event_view.ui -o ../client/views/pages/event_view_ui.py
#       
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o resources/assets/rss.py
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py 

from .event_view_ui import Ui_event_view
from modules.touchdatetime.tdateedit import DateSelect
from models.event_model import EventModel, EventFilter, DateRange

class EventView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_event_view()
        self._ui.setupUi(self)

        self._database = QSqlDatabase.addDatabase('QMYSQL')
        self._database.setHostName('localhost')
        self._database.setUserName('sebastianji')
        self._database.setPassword('admin')#genTen212!')
        self._database.setDatabaseName('decan')

        if not self._database.open():
            print('connection failed')
            print(self._database.lastError().text())

        self._event_filter = EventFilter()
        self._date_range_list: List[DateRange] = []
        self._date_range_list.append(
            DateRange(
                QDateTime(
                    QDate(2022, 3, 2),
                    QTime(19, 32, 21))
                    ,
                QDateTime(
                    QDate(2022, 4, 14),
                    QTime(23, 59, 59))
                      )
                      )
        
        self._date_range_list.append(
            DateRange(
                QDateTime(
                    QDate(2023, 8, 5),
                    QTime(10, 0, 0))
                    ,
                QDateTime(
                    QDate(2023, 11, 10),
                    QTime(14, 0, 0))
                      )
                      )
        
        self._date_range_list.append(
            DateRange(
                QDateTime(
                    QDate(2022, 3, 2),
                    QTime(19, 32, 21))
                    ,
                QDateTime(
                    QDate(2023, 11, 10),
                    QTime(14, 0, 0))
                      )
                      )
        
        self._event_filter.addManyDateRangeFilters(self._date_range_list)
        self._event_filter.addUserFilter(2)
        print(self._event_filter.constructFilter())
                    

        self.eventmodel = EventModel(parent=self, database=self._database)

        self._ui.event_table.setModel(self.eventmodel)

        self._ui.user1.clicked.connect(lambda: self.eventmodel.changeUser(1))
        self._ui.user2.clicked.connect(lambda: self.eventmodel.changeUser(2))
        self._ui.user3.clicked.connect(lambda: self.eventmodel.changeUser(3))