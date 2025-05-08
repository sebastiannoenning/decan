from typing import List

from PySide6 import QtCore
from PySide6.QtCore import Qt, QDateTime, QDate, QTime, QModelIndex, QByteArray
from PySide6.QtWidgets import QWidget, QScroller, QDataWidgetMapper, QPushButton
from PySide6.QtSql import QSqlDatabase

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
from modules.eventlist.eventtype import EventType
from modules.eventlist.eventjsonparser import EventJsonParser
from client.modules.eventlist.eventattributes import EBodySingleDisplay
from models.event_model import EventModel, EventFilter, DateRange
import modules.scrollers_qt as scr_qt


# noinspection PyTypeChecker
class EventView(QWidget):
    def __init__(self, parent, db: QSqlDatabase):
        super().__init__(parent)

        self._database = db

        self._Ui = Ui_event_view()
        self._Ui.setupUi(self)
        self.additionalUiSettings()

        self.eventmodel = EventModel(self, db=self._database)
        self._Ui.event_view_table.setModel(self.eventmodel)
        self._Ui.event_list.setModel(self.eventmodel)

        self.eventmodel.select()

        self.connections()

        self.setFormDefault()

    def setUserFilter(self, index: QModelIndex):
        print(index)
        self.eventmodel.changeUser(index)

    # noinspection PyAttributeOutsideInit
    def additionalUiSettings(self):
        # Remove perpendicular scroll ability from all scroll-areas & place a touch scroller on all of them
        #   Vertical only scrolls:
        self._Ui.form_wrapper.horizontalScrollBar().setEnabled(False)
        self.form_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.form_wrapper)
        self._Ui.event_list_wrapper.horizontalScrollBar().setEnabled(False),
        self.event_list_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.event_list_wrapper)
        #   Horizontal only scrolls:
        self._Ui.preset_wrapper.verticalScrollBar().setEnabled(False)
        self.preset_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.preset_wrapper)
        self._Ui.title_view_wrapper.verticalScrollBar().setEnabled(False)
        self.title_view_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.title_view_wrapper)
        self._Ui.layer_header_wrapper.verticalScrollBar().setEnabled(False)
        self.layer_header_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.layer_header_wrapper)
        self._Ui.layer_header_exp_add_wrapper.verticalScrollBar().setEnabled(False)
        self.layer_header_exp_add_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.layer_header_exp_add_wrapper)
        self._Ui.layer_note_edit_header_wrapper.verticalScrollBar().setEnabled(False)
        self.layer_note_edit_header_wrapper_scroller: QScroller = scr_qt.returnUniScroller(self._Ui.layer_note_edit_header_wrapper)

        # Create additional helper classes
        self.eventMapper = QDataWidgetMapper(self)
        self.formParser = EventJsonParser(self)
        self.locationMapper = QDataWidgetMapper(self)

    def connections(self):
        self._Ui.user1.clicked.connect(lambda: self.eventmodel.changeUser(1))
        self._Ui.user2.clicked.connect(lambda: self.eventmodel.changeUser(2))
        self._Ui.user3.clicked.connect(lambda: self.eventmodel.changeUser(3))

        self._Ui.prev_day.clicked.connect(lambda: self.prev_page())
        self._Ui.next_day.clicked.connect(lambda: self.next_page())

        # Custom Auto Default Behaviour
        self._Ui.layer_finish_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_finish_button))
        self._Ui.layer_add_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_add_button))
        self._Ui.layer_add_button.toggled.connect(lambda toggled: self.clearDependentToggles(toggled, self._Ui.layer_header_exp_add))
        self._Ui.layer_remove_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_remove_button))
        self._Ui.layer_edit_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_edit_button))

        self._Ui.layer_add_note_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_add_note_button))
        self._Ui.layer_add_task_button.toggled.connect(lambda: self.clearOtherToggles(self._Ui.layer_add_task_button))

        self.formParser.typeChanged.connect(lambda: self.updateInfo())

        self._Ui.event_list.itemSelected.connect(lambda load: self.loadItem(load))

        self._Ui.layer_view_display_ebody.setJsonParser(self.formParser)
        self._Ui.layer_view_list_ebody.setJsonParser(self.formParser)

        self.eventMapper.setModel(self.eventmodel)
        self.mapToWidgets()
        self._Ui.add_event_button.clicked.connect(lambda: self._Ui.details_container.setCurrentIndex(3))
        self._Ui.add_event_button.clicked.connect(self.onAddEvent)
        self._Ui.save_button.clicked.connect(self.onSaveEvent)

    def onAddEvent(self, test_en: bool = True):
        self.setFormDefault()
        if not self.eventmodel.insertRow(-1):
            if test_en: print("[EventView] Failed to insert empty row")
            return

        self.mapper.setCurrentIndex(-1)

        self._Ui.title_line_edit.clear()
        now = QDateTime.currentDateTime()
        self._Ui.time_start_select.setDateTime(now)
        self._Ui.time_end_select.setDateTime(now.addSecs(3600))

        self._Ui.details_container.setCurrentIndex(2)

    def onSaveEvent(self, test_en: bool = False):
        if not self.mapper.submit():
            if test_en: ("EventView mapper.submit() failed")
            return

        if not self.eventmodel.submitAll():
            err = self.eventmodel.lastError().text()
            print(f"[EventView] submitAll() failed → {err}")
            self.eventmodel.revertAll()
            return

        self._Ui.details_container.setCurrentIndex(3)
        self._Ui.setFormDefault()
        t = None
        if t == None: return None

    # noinspection PyTypeChecker
    @staticmethod
    def clearOtherToggles(exception: QPushButton):
        parent_container = exception.parentWidget().layout()
        if exception.isChecked():
            for i in range(parent_container.count()):
                lay_item = parent_container.itemAt(i)
                if isinstance(lay_item.widget(), QPushButton):
                    button: QPushButton = lay_item.widget()
                    if button == exception:
                        pass
                    else:
                        button.setChecked(False)
                        button.setEnabled(False)
        else:
            ignore = False
            for i in range(parent_container.count()):
                lay_item = parent_container.itemAt(i)
                if isinstance(lay_item.widget(), QPushButton):
                    button: QPushButton = lay_item.widget()
                    if button.isChecked() and (button != exception):
                        ignore = True
            if not ignore:
                for i in range(parent_container.count()):
                    lay_item = parent_container.itemAt(i)
                    if isinstance(lay_item.widget(), QPushButton):
                        button: QPushButton = lay_item.widget()
                        button.setEnabled(True)

    # noinspection PyTypeChecker
    @staticmethod
    def clearDependentToggles(ignore: bool, container: QWidget):
        if not ignore:
            dependent_container = container.layout()
            for i in range(dependent_container.count()):
                lay_item = dependent_container.itemAt(i)
                if isinstance(lay_item.widget(), QPushButton):
                    button: QPushButton = lay_item.widget()
                    button.setChecked(False)
                    button.setEnabled(True)

    def prev_page(self):
        index = self._Ui.details_container.currentIndex()
        index = (index - 1) % self._Ui.details_container.count()
        self._Ui.details_container.setCurrentIndex(index)

    def next_page(self):
        index = self._Ui.details_container.currentIndex()
        index = (index + 1) % self._Ui.details_container.count()
        self._Ui.details_container.setCurrentIndex(index)

    def mapToWidgets(self):
        # Title Mappings
        self.eventMapper.addMapping(self._Ui.title_line_edit, 1, QByteArray('text'))

        # Time Mappings
        self._Ui.time_view.addMappings(mapper=self.eventMapper,
                                       col_start=2,
                                       col_end=3)
        self.eventMapper.addMapping(self._Ui.time_start_select, 2, QByteArray('DateTime'))
        self.eventMapper.addMapping(self._Ui.time_end_select, 3, QByteArray('DateTime'))

        # Attribute Mappings
        self.eventMapper.addMapping(self.formParser, 4, QByteArray('Attributes'))

        # Location Mappings
        self.eventMapper.addMapping(self._Ui.loc_view_col_label, 6, QByteArray('text'))
        #self.eventMapper.addMapping(self                                    6, )   Add Mapper to a helper object that will update locationMapper with the correct attributes

        self.locationMapper.addMapping(self._Ui.loc_address_line_1_label, 1, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_address_line_2_label, 2, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_address_line_3_label, 3, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_county_label, 4, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_city_label, 5, QByteArray('text'))
        self.locationMapper.addMapping(self._Ui.loc_postcode_label, 6, QByteArray('text'))
        pass

    def clearMap(self):
        self.eventMapper.clearMapping()
        self.locationMapper.clearMapping()

    @staticmethod
    def defaultParserValues(f: EventType = EventType.Simple):
        default_text: str = ''
        if f == EventType.Simple:
            default_text = """
            {
                "info": {
                    "index": 0,
                    "increment" : 0,
                    "type": 0
                    "types": ["Simple", "Complex", "Note", "Task"]
                },
            }"""
        if f == EventType.Complex:
            default_text = """
            {
                "info": {
                    "index": 0,
                    "increment" : 0,
                    "type": 2,
                    "types": ["Simple", "Complex", "Note", "Task"]
                },
                "positions":[],
                "objects": {
                },
            }"""
        if f == EventType.Note:
            default_text = """
            {
                "info": {
                    "index": 1,
                    "increment" : 1,
                    "type": 3,
                    "types": ["Simple", "Complex", "Note", "Task"]
                },
                "positions":["EDescription_1"],
                "objects": {
                    "EDescription_1": "Your description here"
                },
            }"""
        if f == EventType.Task:
            default_text = """
            {
                "info": {
                    "index": 1,
                    "increment" : 1,
                    "type": 4,
                    "types": ["Simple", "Complex", "Note", "Task"]
                },
                "positions":["EToDo_1"],
                "objects": {
                    "EToDo_1": {
                        "EBool": false,
                        "ETaskDescription": "Your task name"
                    }
                },
            }"""

        return default_text

    def eventModel(self) -> EventModel: return self.eventmodel

    def setFormDefault(self):
        self._Ui.title_edit_button.toggle()
        self._Ui.title_edit_button.setChecked(False)

        self._Ui.time_button.toggle()
        self._Ui.time_button.setChecked(False)

        self._Ui.layer_button.toggle()
        self._Ui.layer_button.setChecked(False)

        self._Ui.location_button.toggle()
        self._Ui.location_button.setChecked(False)
        self._Ui.location_button.setEnabled(False)
        self._Ui.location_view.hide()
        self._Ui.location_button.hide()
        self._Ui.location_edit_combobox.hide()

        self._Ui.invitees_button.hide()
        self._Ui.tags_button.hide()

        self._Ui.layer_finish_button.toggle()
        self._Ui.layer_finish_button.setChecked(False)

    def loadItem(self, load: bool):
        self.setFormDefault()
        if not load:
            self.eventMapper.setCurrentIndex(-1)
            self._Ui.details_container.setCurrentIndex(2)
        else:
            l_row = self._Ui.event_list.current()
            self.eventMapper.setCurrentIndex(l_row)
            self._Ui.details_container.setCurrentIndex(3)

