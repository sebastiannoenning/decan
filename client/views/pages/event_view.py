from typing import List

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QModelIndex, QByteArray
from PySide6.QtWidgets import QWidget, QScroller, QDataWidgetMapper
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
import modules.scrollers_qt as scrQt

class EventView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._Ui = Ui_event_view()
        self._Ui.setupUi(self)
        self.additionalUiSettings()

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

        self.eventmodel = EventModel(self, db=self._database)
        self._Ui.event_view_table.setModel(self.eventmodel)

    def connections(self):
        self._Ui.time_schedule_label_button.clicked.connect(lambda: print(f"""
            Family: {self._Ui.time_schedule_label_button.fontInfo().family()}
            PixelSize: {self._Ui.time_schedule_label_button.fontInfo().pixelSize()}
            PointSize: {self._Ui.time_schedule_label_button.fontInfo().pointSize()}
            WidgetSize: {self._Ui.time_schedule_label_button.size()}
            """)
            )

        self._Ui.user1.clicked.connect(lambda: self.eventmodel.changeUser(1))
        self._Ui.user2.clicked.connect(lambda: self.eventmodel.changeUser(2))
        self._Ui.user3.clicked.connect(lambda: self.eventmodel.changeUser(3))
    
    def additionalUiSettings(self):
        # Remove perpendicular scroll ability from all scroll-areas & place a touch scroller on all of them
        #   Vertical only scrolls:
        self._Ui.form_wrapper.horizontalScrollBar().setEnabled(False)                  
        self.form_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.form_wrapper)
        self._Ui.preset_wrapper.horizontalScrollBar().setEnabled(False)               
        self.preset_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.preset_wrapper)
        self._Ui.event_list_wrapper.horizontalScrollBar().setEnabled(False),           
        self.event_list_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.event_list_wrapper)
        #   Horizontal only scrolls:
        self._Ui.title_view_wrapper.verticalScrollBar().setEnabled(False)           
        self.title_view_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.title_view_wrapper)
        self._Ui.layer_header_wrapper.verticalScrollBar().setEnabled(False)            
        self.layer_header_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.layer_header_wrapper)
        self._Ui.layer_header_exp_add_wrapper.verticalScrollBar().setEnabled(False)
        self.layer_header_exp_add_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.layer_header_exp_add_wrapper)
        self._Ui.layer_note_edit_header_wrapper.verticalScrollBar().setEnabled(False)
        self.layer_note_edit_header_wrapper_scroller : QScroller = scrQt.returnUniScroller(self._Ui.layer_note_edit_header_wrapper)

        self.eventMapper = QDataWidgetMapper()
        self.locationMapper = QDataWidgetMapper()


    def openFormEditing(self):
        pass

    def mapToWidgets(self, index: QModelIndex):
        # Title Mappings
        self.eventMapper.addMapping(self._Ui.title_label,                   1, QByteArray('text'))
        self.eventMapper.addMapping(self._Ui.title_line_edit,               1, QByteArray('text'))

        # Time Mappings
        self._Ui.time_view.addMappings(mapper=self.eventMapper, 
                                       col_start=2, 
                                       col_end=3)
        self.eventMapper.addMapping(self._Ui.time_start_select,             2, QByteArray('DateTime'))
        self.eventMapper.addMapping(self._Ui.time_end_select,               2, QByteArray('DateTime'))

        # Attribute Mappings

        # Location Mappings
        self.eventMapper.addMapping(self._Ui.loc_view_col_label,            6, QByteArray('text'))

        self.locationMapper.addMapping(self._Ui.loc_address_line_1_label,   1, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_address_line_2_label,   2, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_address_line_3_label,   3, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_county_label,           4, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_city_label,             5, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_postcode_label,         6, QByteArray('text'))
        pass

    def clearMap(self):
        self.eventMapper.clearMapping()
        self.locationMapper.clearMapping()
    
    def emptyForm(self):
        pass

