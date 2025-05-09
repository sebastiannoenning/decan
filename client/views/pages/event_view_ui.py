# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

from modules.eventlist.eventattributes import (EBody, EBodySingleDisplay, ETime)
from modules.eventlist.eventlist import EventList
from modules.touchdatetime.tdatetimeedit import TDateTimeSelect
from . import rss_rc

class Ui_event_view(object):
    def setupUi(self, event_view):
        if not event_view.objectName():
            event_view.setObjectName(u"event_view")
        event_view.setEnabled(True)
        event_view.resize(634, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(event_view.sizePolicy().hasHeightForWidth())
        event_view.setSizePolicy(sizePolicy)
        event_view.setMinimumSize(QSize(634, 460))
        event_view.setMaximumSize(QSize(710, 460))
        event_view.setStyleSheet(u"* {\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(120,120,120,1);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(30,30,30,1);\n"
"	border: 0px solid transparent;\n"
"	border-bottom: 2px solid rgba(255, 80, 80, 1);\n"
"	padding-left: 5px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QLineEdit::clear-button {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgba(30,30,30,1);\n"
"	border-radius: 4px;\n"
"	border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;\n"
"	border: 0px solid transparent;\n"
"	border-bottom: 2px solid rgba(180,220,140, 1);\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(\":/icons/arrows/arrow_down_dark.svg\");\n"
"	width: 23px; \n"
"	height: 23px;\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	image: url(\":/icons/arrows/arrow_down_red"
                        ".svg\");\n"
"}\n"
"QComboBox::drop-down {\n"
"    	subcontrol-origin: padding;\n"
"    	subcontrol-position: top right;\n"
"	background-color: rgba(20,20,20,1);\n"
"	border-radius: 0px;\n"
"   	width: 40px;\n"
"    	border-left: 1px solid rgba(255,255,255,1);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	height: 30px; width: 30px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    	image: url(\":/icons/util/buttons/checkbox2_empty_dark.svg\");\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    	image: url(\":/icons/util/buttons/checkbox2_tick_dark.svg\");\n"
"}\n"
"\n"
"QLabel{\n"
"	padding-left: 1px;\n"
"	background-color: rgba(20, 20, 20, 1);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#title *, #location * {\n"
"	border-radius: 0px;\n"
"}\n"
"#title QPushButton, 							\n"
"#location QPushButton {\n"
"	border-bottom-right-radius: 4px; border-top-right-radius: 4px;\n"
"}\n"
"#title QLineEdit, #title QLabel, #location QLabel {\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"#title QScrollBar:horizontal, 				\n"
"#locatio"
                        "n QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height:  2px;\n"
"    padding: 0px 0px;\n"
"}\n"
"#title QScrollBar::groove:horizontal, 	\n"
"#location QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 2px;\n"
"}\n"
"#title QScrollBar::handle:horizontal, 	\n"
"#location QScrollBar::handle:horizontal {\n"
"    	background: rgba(75,150,255,1);\n"
"    	min-height: 2px; min-width: 30px;\n"
"    	border-radius: 0px;\n"
"}\n"
"#title QScrollBar::sub-page:vertical,			#title QScrollBar::add-page:vertical,\n"
"#title QScrollBar::sub-line:vertical,				#title QScrollBar::add-line:vertical,\n"
"#location QScrollBar::sub-page:vertical, 	#location QScrollBar::add-page:vertical, \n"
"#location QScrollBar::sub-line:vertical, 		#location QScrollBar::add-line:vertical {\n"
"    	background: None;\n"
"}\n"
"#title QScrollBar::left-arrow:horizontal, 		#title QScrollBar::right-arrow:horizontal,\n"
"#location QScrollBar::left-arrow:horizontal,#location QScrollBar::right-arr"
                        "ow:horizontal {\n"
"	image: None;\n"
"	width: 0px; height: 0px;\n"
"}\n"
"\n"
"#title QPushButton {\n"
"	border-left: 1px solid white;\n"
"}\n"
"#title QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"}\n"
"#title QScrollBar::handle:horizontal {\n"
"    	background: rgba(75,150,255,1);\n"
"}\n"
"\n"
"#location QScrollBar:horizontal {\n"
"    background: rgba(180, 220, 160, 1);\n"
"}\n"
"#location QScrollBar::handle:horizontal {\n"
"    	background: rgba(180,220,140, 1);\n"
"}\n"
"#location_view_collapsed QScrollArea{\n"
"	border-right: 1px solid white;\n"
"}\n"
"#location_view_expanded QLabel {\n"
"	padding-left: 1px;\n"
"	background-color: None;\n"
"	border-radius: 0px;\n"
"}\n"
"QWidget#location_view_exp_labels {\n"
"	border-top-left-radius: 4px;\n"
"	background: rgba(20,20,20,1);\n"
"	border-bottom: 2px solid rgba(180,220,140, 1);\n"
"	border-right: 1px solid white;\n"
"}\n"
"#event_navigation * {\n"
"	border-radius: 0px;\n"
"	border-left: 1px solid rgba(220,220,220,1);\n"
"}\n"
"QPushBu"
                        "tton#prev_day {\n"
"	border-left: 0px solid transparent;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QPushButton#filter_button {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"EToDo * QLabel{\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"}")
        self.event_view_container = QHBoxLayout(event_view)
        self.event_view_container.setSpacing(10)
        self.event_view_container.setObjectName(u"event_view_container")
        self.event_view_container.setContentsMargins(0, 0, 0, 0)
        self.events_view = QWidget(event_view)
        self.events_view.setObjectName(u"events_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.events_view.sizePolicy().hasHeightForWidth())
        self.events_view.setSizePolicy(sizePolicy1)
        self.events_view.setMinimumSize(QSize(312, 460))
        self.events_view.setMaximumSize(QSize(350, 460))
        self.events_view_container = QVBoxLayout(self.events_view)
        self.events_view_container.setSpacing(10)
        self.events_view_container.setObjectName(u"events_view_container")
        self.events_view_container.setContentsMargins(0, 0, 0, 0)
        self.event_navigation = QWidget(self.events_view)
        self.event_navigation.setObjectName(u"event_navigation")
        self.date_nav_container = QHBoxLayout(self.event_navigation)
        self.date_nav_container.setSpacing(0)
        self.date_nav_container.setObjectName(u"date_nav_container")
        self.date_nav_container.setContentsMargins(0, 0, 0, 0)
        self.prev_day = QPushButton(self.event_navigation)
        self.prev_day.setObjectName(u"prev_day")
        self.prev_day.setMinimumSize(QSize(30, 40))
        icon = QIcon()
        icon.addFile(u":/icons/arrows/arrow_left_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.prev_day.setIcon(icon)
        self.prev_day.setIconSize(QSize(23, 23))

        self.date_nav_container.addWidget(self.prev_day)

        self.next_day = QPushButton(self.event_navigation)
        self.next_day.setObjectName(u"next_day")
        self.next_day.setMinimumSize(QSize(30, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrows/arrow_right_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.next_day.setIcon(icon1)
        self.next_day.setIconSize(QSize(23, 23))

        self.date_nav_container.addWidget(self.next_day)

        self.date_label = QLabel(self.event_navigation)
        self.date_label.setObjectName(u"date_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy2)
        self.date_label.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.date_label.setFont(font)

        self.date_nav_container.addWidget(self.date_label)

        self.calendar_view = QPushButton(self.event_navigation)
        self.calendar_view.setObjectName(u"calendar_view")
        self.calendar_view.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/calendar/calendar_search_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/calendar/calendar_search_red.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.calendar_view.setIcon(icon2)
        self.calendar_view.setIconSize(QSize(23, 23))

        self.date_nav_container.addWidget(self.calendar_view)

        self.filter_button = QPushButton(self.event_navigation)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/calendar/events/filter/filter_add_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/calendar/events/filter/filter_add_red.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.filter_button.setIcon(icon3)
        self.filter_button.setIconSize(QSize(23, 23))

        self.date_nav_container.addWidget(self.filter_button)


        self.events_view_container.addWidget(self.event_navigation)

        self.event_list_wrapper = QScrollArea(self.events_view)
        self.event_list_wrapper.setObjectName(u"event_list_wrapper")
        self.event_list_wrapper.setMinimumSize(QSize(312, 0))
        self.event_list_wrapper.setMaximumSize(QSize(350, 16777215))
        self.event_list_wrapper.setLineWidth(0)
        self.event_list_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_list_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.event_list_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.event_list_wrapper.setWidgetResizable(True)
        self.event_list = EventList()
        self.event_list.setObjectName(u"event_list")
        self.event_list.setGeometry(QRect(0, 0, 340, 408))
        self.event_list.setMinimumSize(QSize(340, 0))
        self.event_list_wrapper.setWidget(self.event_list)

        self.events_view_container.addWidget(self.event_list_wrapper)


        self.event_view_container.addWidget(self.events_view)

        self.details_container = QStackedWidget(event_view)
        self.details_container.setObjectName(u"details_container")
        sizePolicy2.setHeightForWidth(self.details_container.sizePolicy().hasHeightForWidth())
        self.details_container.setSizePolicy(sizePolicy2)
        self.details_container.setMinimumSize(QSize(312, 460))
        self.details_container.setMaximumSize(QSize(350, 460))
        self.page_quick = QWidget()
        self.page_quick.setObjectName(u"page_quick")
        self.page_quick.setMinimumSize(QSize(312, 460))
        self.quick_layout = QVBoxLayout(self.page_quick)
        self.quick_layout.setSpacing(10)
        self.quick_layout.setObjectName(u"quick_layout")
        self.quick_layout.setContentsMargins(0, 0, 0, 0)
        self.user1 = QPushButton(self.page_quick)
        self.user1.setObjectName(u"user1")

        self.quick_layout.addWidget(self.user1)

        self.user2 = QPushButton(self.page_quick)
        self.user2.setObjectName(u"user2")

        self.quick_layout.addWidget(self.user2)

        self.user3 = QPushButton(self.page_quick)
        self.user3.setObjectName(u"user3")

        self.quick_layout.addWidget(self.user3)

        self.printsql = QPushButton(self.page_quick)
        self.printsql.setObjectName(u"printsql")

        self.quick_layout.addWidget(self.printsql)

        self.test_widgets = QWidget(self.page_quick)
        self.test_widgets.setObjectName(u"test_widgets")
        self.test_bar_3 = QScrollBar(self.test_widgets)
        self.test_bar_3.setObjectName(u"test_bar_3")
        self.test_bar_3.setGeometry(QRect(0, 0, 20, 120))
        self.test_bar_3.setStyleSheet(u"QScrollBar:vertical {\n"
"    background: rgba(40,40,40,0.9);\n"
"    width:  20px;\n"
"    padding: 25px 0;\n"
"}\n"
"\n"
"QScrollBar::groove:vertical {\n"
"    background: transparent;\n"
"    width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    	background: rgba(120,120,120,1);\n"
"    	min-height: 50px;\n"
"	min-width: 20px;\n"
"    	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {\n"
"    	background: rgba(40,40,40,1);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    	width: 20px;\n"
"    	height: 25px;             \n"
"    	background: rgba(20,20,20,1);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: top;\n"
"    	border-top-left-radius: 4px;\n"
"    	border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: bottom;\n"
"    border-bottom-left-radius: 4px;\n"
"    bor"
                        "der-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"    image: url(\":/icons/arrows/arrow_up_dark.svg\");\n"
"    width:  20px;   height: 20px;\n"
"}\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"    image: url(\":/icons/arrows/arrow_up_red.svg\");\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    image: url(\":/icons/arrows/arrow_down_dark.svg\");\n"
"    width:  20px;   height: 20px;\n"
"}\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"    image: url(\":/icons/arrows/arrow_down_red.svg\");\n"
"}")
        self.test_bar_3.setOrientation(Qt.Orientation.Vertical)
        self.test_bar_4 = QScrollBar(self.test_widgets)
        self.test_bar_4.setObjectName(u"test_bar_4")
        self.test_bar_4.setGeometry(QRect(20, 0, 292, 20))
        self.test_bar_4.setStyleSheet(u"QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height:  2px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 2px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    	background: rgba(75,150,255,1);\n"
"    	min-height: 2px;\n"
"	min-width: 30px;\n"
"    	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, \n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:vertical  {\n"
"    	background: None;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	image: None;\n"
"	width: 0px;\n"
"	height: 0px;\n"
"}")
        self.test_bar_4.setOrientation(Qt.Orientation.Horizontal)
        self.test_bar_2 = QScrollBar(self.test_widgets)
        self.test_bar_2.setObjectName(u"test_bar_2")
        self.test_bar_2.setGeometry(QRect(20, 20, 292, 20))
        self.test_bar_2.setStyleSheet(u"QScrollBar:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"    height: 30px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(255,255,255,0.9);\n"
"	min-width: 20px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: rgba(20,20,20,1);\n"
"    width: 30px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: rgba(20,20,20,1);\n"
"    width: 30px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.test_bar_2.setOrientation(Qt.Orientation.Horizontal)
        self.test_bar_1 = QScrollBar(self.test_widgets)
        self.test_bar_1.setObjectName(u"test_bar_1")
        self.test_bar_1.setGeometry(QRect(20, 40, 292, 20))
        self.test_bar_1.setStyleSheet(u"QScrollBar:horizontal {\n"
"   	background: rgba(40,40,40,0.9);\n"
"    	height: 25px;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"	padding: 0px 25px\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(120,120,120,1);\n"
"	min-width: 50px;\n"
"	min-height: 20px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 25px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    	background: rgba(20,20,20,1);\n"
"    	width: 25px;\n"
"	padding: 0px;\n"
"    	border: 0px solid rgba(0,0,0,0);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   	subcontrol-origin: margin;\n"
"    	subcontrol-position: left;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    	subcontrol-origin: m"
                        "argin;\n"
"    	subcontrol-position: right;\n"
"	border-bottom-right-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_left_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_left_red.svg\")\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_right_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_right_red.svg\")\n"
"}")
        self.test_bar_1.setOrientation(Qt.Orientation.Horizontal)
        self.tableView = QTableView(self.test_widgets)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 140, 311, 192))

        self.quick_layout.addWidget(self.test_widgets)

        self.details_container.addWidget(self.page_quick)
        self.page_json = QWidget()
        self.page_json.setObjectName(u"page_json")
        self.event_view_table = QTableView(self.page_json)
        self.event_view_table.setObjectName(u"event_view_table")
        self.event_view_table.setGeometry(QRect(0, 10, 311, 192))
        self.load = QPushButton(self.page_json)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(10, 220, 100, 32))
        self.next = QPushButton(self.page_json)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(10, 280, 100, 32))
        self.prev = QPushButton(self.page_json)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(10, 320, 100, 32))
        self.details_container.addWidget(self.page_json)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        sizePolicy2.setHeightForWidth(self.page_add.sizePolicy().hasHeightForWidth())
        self.page_add.setSizePolicy(sizePolicy2)
        self.page_add.setMinimumSize(QSize(312, 460))
        self.page_add.setMaximumSize(QSize(350, 460))
        self.page_add_container = QHBoxLayout(self.page_add)
        self.page_add_container.setSpacing(0)
        self.page_add_container.setObjectName(u"page_add_container")
        self.page_add_container.setContentsMargins(0, 0, 0, 0)
        self.add_event_button = QPushButton(self.page_add)
        self.add_event_button.setObjectName(u"add_event_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.add_event_button.sizePolicy().hasHeightForWidth())
        self.add_event_button.setSizePolicy(sizePolicy3)
        self.add_event_button.setMinimumSize(QSize(312, 460))
        self.add_event_button.setMaximumSize(QSize(350, 460))
        icon4 = QIcon()
        icon4.addFile(u":/icons/util/add_1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon4.addFile(u":/icons/util/add_2_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon4.addFile(u":/icons/util/add_2_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.add_event_button.setIcon(icon4)
        self.add_event_button.setIconSize(QSize(40, 40))

        self.page_add_container.addWidget(self.add_event_button)

        self.details_container.addWidget(self.page_add)
        self.page_details = QWidget()
        self.page_details.setObjectName(u"page_details")
        sizePolicy3.setHeightForWidth(self.page_details.sizePolicy().hasHeightForWidth())
        self.page_details.setSizePolicy(sizePolicy3)
        self.page_details.setMinimumSize(QSize(312, 460))
        self.page_details.setMaximumSize(QSize(350, 460))
        self.page_details_container = QHBoxLayout(self.page_details)
        self.page_details_container.setSpacing(0)
        self.page_details_container.setObjectName(u"page_details_container")
        self.page_details_container.setContentsMargins(0, 0, 0, 0)
        self.form_wrapper = QScrollArea(self.page_details)
        self.form_wrapper.setObjectName(u"form_wrapper")
        sizePolicy3.setHeightForWidth(self.form_wrapper.sizePolicy().hasHeightForWidth())
        self.form_wrapper.setSizePolicy(sizePolicy3)
        self.form_wrapper.setMinimumSize(QSize(312, 460))
        self.form_wrapper.setMaximumSize(QSize(350, 460))
        self.form_wrapper.setStyleSheet(u"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width:  5px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::groove:vertical {\n"
"    background: transparent;\n"
"    width: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    	background: rgba(120,120,120,1);\n"
"    	min-height: 50px;\n"
"	min-width: 5px;\n"
"    	border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, \n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:vertical  {\n"
"    	background: None\n"
"}")
        self.form_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.form_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.form_wrapper.setLineWidth(0)
        self.form_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.form_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.form_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.form_wrapper.setWidgetResizable(True)
        self.details_form = QWidget()
        self.details_form.setObjectName(u"details_form")
        self.details_form.setGeometry(QRect(0, -224, 312, 1777))
        sizePolicy1.setHeightForWidth(self.details_form.sizePolicy().hasHeightForWidth())
        self.details_form.setSizePolicy(sizePolicy1)
        self.details_form.setMinimumSize(QSize(312, 0))
        self.details_form.setMaximumSize(QSize(350, 16777215))
        self.details_form_container = QFormLayout(self.details_form)
        self.details_form_container.setObjectName(u"details_form_container")
        self.details_form_container.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.details_form_container.setHorizontalSpacing(10)
        self.details_form_container.setVerticalSpacing(10)
        self.details_form_container.setContentsMargins(0, 0, 0, 0)
        self.cancel_button = QPushButton(self.details_form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(50, 50))
        self.cancel_button.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/icons/util/close_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon5.addFile(u":/icons/util/close_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon5.addFile(u":/icons/util/close_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon5.addFile(u":/icons/util/close_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon5.addFile(u":/icons/util/close_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon5.addFile(u":/icons/util/close_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon5.addFile(u":/icons/util/close_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.cancel_button.setIcon(icon5)
        self.cancel_button.setIconSize(QSize(30, 30))
        self.cancel_button.setCheckable(False)

        self.details_form_container.setWidget(0, QFormLayout.ItemRole.LabelRole, self.cancel_button)

        self.title = QWidget(self.details_form)
        self.title.setObjectName(u"title")
        self.title.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy2)
        self.title.setMinimumSize(QSize(247, 0))
        self.title.setMaximumSize(QSize(290, 16777215))
        font1 = QFont()
        font1.setFamilies([u"American Typewriter"])
        font1.setPointSize(20)
        self.title.setFont(font1)
        self.title_container = QVBoxLayout(self.title)
        self.title_container.setSpacing(0)
        self.title_container.setObjectName(u"title_container")
        self.title_container.setContentsMargins(0, 0, 0, 0)
        self.title_view = QWidget(self.title)
        self.title_view.setObjectName(u"title_view")
        sizePolicy2.setHeightForWidth(self.title_view.sizePolicy().hasHeightForWidth())
        self.title_view.setSizePolicy(sizePolicy2)
        self.title_view.setMinimumSize(QSize(247, 50))
        self.title_view.setMaximumSize(QSize(290, 50))
        self.title_view.setStyleSheet(u"")
        self.title_view_container = QHBoxLayout(self.title_view)
        self.title_view_container.setSpacing(0)
        self.title_view_container.setObjectName(u"title_view_container")
        self.title_view_container.setContentsMargins(0, 0, 0, 0)
        self.title_view_wrapper = QScrollArea(self.title_view)
        self.title_view_wrapper.setObjectName(u"title_view_wrapper")
        self.title_view_wrapper.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.title_view_wrapper.sizePolicy().hasHeightForWidth())
        self.title_view_wrapper.setSizePolicy(sizePolicy4)
        self.title_view_wrapper.setMinimumSize(QSize(212, 50))
        self.title_view_wrapper.setMaximumSize(QSize(250, 50))
        self.title_view_wrapper.setAutoFillBackground(False)
        self.title_view_wrapper.setStyleSheet(u"#title_label_container { \n"
"	background: rgba(20,20,20,1);\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height:  2px;\n"
"    padding: 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::groove:horizontal {\n"
"    background: rgba(100,180,255,1);\n"
"    height: 2px;\n"
"    margin: 0px;\n"
"}")
        self.title_view_wrapper.setFrameShape(QFrame.Shape.Box)
        self.title_view_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.title_view_wrapper.setLineWidth(0)
        self.title_view_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.title_view_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.title_view_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.title_view_wrapper.setWidgetResizable(False)
        self.title_label_container = QWidget()
        self.title_label_container.setObjectName(u"title_label_container")
        self.title_label_container.setGeometry(QRect(0, 0, 250, 48))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.title_label_container.sizePolicy().hasHeightForWidth())
        self.title_label_container.setSizePolicy(sizePolicy5)
        self.title_label_container.setMinimumSize(QSize(212, 48))
        self.title_label_container.setMaximumSize(QSize(16777215, 48))
        self.title_label_container_layout = QHBoxLayout(self.title_label_container)
        self.title_label_container_layout.setSpacing(0)
        self.title_label_container_layout.setObjectName(u"title_label_container_layout")
        self.title_label_container_layout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.title_label_container)
        self.title_label.setObjectName(u"title_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy6)
        self.title_label.setMinimumSize(QSize(212, 48))
        self.title_label.setMaximumSize(QSize(800, 48))
        self.title_label.setBaseSize(QSize(212, 48))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(27)
        self.title_label.setFont(font2)
        self.title_label.setStyleSheet(u"background: None;")

        self.title_label_container_layout.addWidget(self.title_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.title_view_wrapper.setWidget(self.title_label_container)

        self.title_view_container.addWidget(self.title_view_wrapper)

        self.title_edit_button = QPushButton(self.title_view)
        self.title_edit_button.setObjectName(u"title_edit_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.title_edit_button.sizePolicy().hasHeightForWidth())
        self.title_edit_button.setSizePolicy(sizePolicy7)
        self.title_edit_button.setMinimumSize(QSize(40, 50))
        self.title_edit_button.setMaximumSize(QSize(40, 50))
        font3 = QFont()
        font3.setPointSize(15)
        self.title_edit_button.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/icons/util/edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon6.addFile(u":/icons/util/lock_circle_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon6.addFile(u":/icons/util/lock_circle_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon6.addFile(u":/icons/util/lock_circle_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon6.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon6.addFile(u":/icons/util/lock_circle_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon6.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.title_edit_button.setIcon(icon6)
        self.title_edit_button.setIconSize(QSize(30, 30))
        self.title_edit_button.setCheckable(True)
        self.title_edit_button.setChecked(False)

        self.title_view_container.addWidget(self.title_edit_button)


        self.title_container.addWidget(self.title_view)

        self.title_edit = QWidget(self.title)
        self.title_edit.setObjectName(u"title_edit")
        self.title_edit.setMinimumSize(QSize(247, 50))
        self.title_edit.setMaximumSize(QSize(290, 50))
        self.title_edit_container = QHBoxLayout(self.title_edit)
        self.title_edit_container.setSpacing(0)
        self.title_edit_container.setObjectName(u"title_edit_container")
        self.title_edit_container.setContentsMargins(0, 0, 0, 0)
        self.title_line_edit = QLineEdit(self.title_edit)
        self.title_line_edit.setObjectName(u"title_line_edit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.title_line_edit.sizePolicy().hasHeightForWidth())
        self.title_line_edit.setSizePolicy(sizePolicy8)
        self.title_line_edit.setMinimumSize(QSize(207, 50))
        self.title_line_edit.setMaximumSize(QSize(250, 50))
        self.title_line_edit.setFont(font2)
        self.title_line_edit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.title_line_edit.setClearButtonEnabled(True)

        self.title_edit_container.addWidget(self.title_line_edit)

        self.title_keyboard_button = QPushButton(self.title_edit)
        self.title_keyboard_button.setObjectName(u"title_keyboard_button")
        sizePolicy7.setHeightForWidth(self.title_keyboard_button.sizePolicy().hasHeightForWidth())
        self.title_keyboard_button.setSizePolicy(sizePolicy7)
        self.title_keyboard_button.setMinimumSize(QSize(40, 50))
        self.title_keyboard_button.setMaximumSize(QSize(40, 50))
        icon7 = QIcon()
        icon7.addFile(u":/icons/util/keyboard_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.title_keyboard_button.setIcon(icon7)
        self.title_keyboard_button.setIconSize(QSize(30, 30))
        self.title_keyboard_button.setCheckable(True)

        self.title_edit_container.addWidget(self.title_keyboard_button)


        self.title_container.addWidget(self.title_edit)


        self.details_form_container.setWidget(0, QFormLayout.ItemRole.FieldRole, self.title)

        self.preset_button = QPushButton(self.details_form)
        self.preset_button.setObjectName(u"preset_button")
        sizePolicy7.setHeightForWidth(self.preset_button.sizePolicy().hasHeightForWidth())
        self.preset_button.setSizePolicy(sizePolicy7)
        self.preset_button.setMinimumSize(QSize(50, 50))
        self.preset_button.setMaximumSize(QSize(50, 50))
        icon8 = QIcon()
        icon8.addFile(u":/icons/calendar/events/flash_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/calendar/events/flash_yellow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon8.addFile(u":/icons/calendar/events/flash_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon8.addFile(u":/icons/calendar/events/flash_slash_yellow.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.preset_button.setIcon(icon8)
        self.preset_button.setIconSize(QSize(30, 30))
        self.preset_button.setCheckable(True)
        self.preset_button.setChecked(False)
        self.preset_button.setAutoDefault(False)

        self.details_form_container.setWidget(1, QFormLayout.ItemRole.LabelRole, self.preset_button)

        self.preset_wrapper = QScrollArea(self.details_form)
        self.preset_wrapper.setObjectName(u"preset_wrapper")
        sizePolicy6.setHeightForWidth(self.preset_wrapper.sizePolicy().hasHeightForWidth())
        self.preset_wrapper.setSizePolicy(sizePolicy6)
        self.preset_wrapper.setMinimumSize(QSize(247, 70))
        self.preset_wrapper.setMaximumSize(QSize(290, 65))
        self.preset_wrapper.setStyleSheet(u"QScrollBar:horizontal {\n"
"   	background: rgba(40,40,40,0.9);\n"
"    	height: 20px;\n"
"	padding: 0px 25px\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(120,120,120,1);\n"
"	min-width: 50px;\n"
"	min-height: 20px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    	background: rgba(20,20,20,1);\n"
"    	width: 25px;\n"
"	padding: 0px;\n"
"    	border: 0px solid rgba(0,0,0,0);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   	subcontrol-origin: margin;\n"
"    	subcontrol-position: left;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: right;\n"
"	border-bottom-right-ra"
                        "dius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_left_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_left_red.svg\")\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_right_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_right_red.svg\")\n"
"}")
        self.preset_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.preset_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.preset_wrapper.setLineWidth(0)
        self.preset_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.preset_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.preset_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.preset_wrapper.setWidgetResizable(True)
        self.preset = QWidget()
        self.preset.setObjectName(u"preset")
        self.preset.setGeometry(QRect(0, 0, 390, 40))
        self.preset.setMaximumSize(QSize(16777215, 40))
        self.preset_container = QHBoxLayout(self.preset)
        self.preset_container.setSpacing(10)
        self.preset_container.setObjectName(u"preset_container")
        self.preset_container.setContentsMargins(0, 0, 0, 0)
        self.note_button = QPushButton(self.preset)
        self.note_button.setObjectName(u"note_button")
        self.note_button.setMinimumSize(QSize(80, 40))
        self.note_button.setMaximumSize(QSize(80, 40))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(15)
        self.note_button.setFont(font4)
        icon9 = QIcon()
        icon9.addFile(u":/icons/calendar/events/message_box_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/calendar/events/message_box_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon9.addFile(u":/icons/calendar/events/message_box_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.note_button.setIcon(icon9)
        self.note_button.setIconSize(QSize(20, 20))
        self.note_button.setCheckable(True)
        self.note_button.setAutoExclusive(True)

        self.preset_container.addWidget(self.note_button)

        self.task_button = QPushButton(self.preset)
        self.task_button.setObjectName(u"task_button")
        self.task_button.setEnabled(True)
        self.task_button.setMinimumSize(QSize(80, 40))
        self.task_button.setMaximumSize(QSize(80, 40))
        self.task_button.setFont(font4)
        icon10 = QIcon()
        icon10.addFile(u":/icons/calendar/events/todo_task_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/calendar/events/todo_task_green.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon10.addFile(u":/icons/calendar/events/message_box_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.task_button.setIcon(icon10)
        self.task_button.setIconSize(QSize(20, 20))
        self.task_button.setCheckable(True)
        self.task_button.setChecked(False)
        self.task_button.setAutoExclusive(True)

        self.preset_container.addWidget(self.task_button)

        self.simple_button = QPushButton(self.preset)
        self.simple_button.setObjectName(u"simple_button")
        self.simple_button.setMinimumSize(QSize(90, 40))
        self.simple_button.setMaximumSize(QSize(80, 40))
        self.simple_button.setFont(font4)
        icon11 = QIcon()
        icon11.addFile(u":/icons/calendar/events/other/simple_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/calendar/events/other/simple_orange.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon11.addFile(u":/icons/calendar/events/other/simple_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.simple_button.setIcon(icon11)
        self.simple_button.setIconSize(QSize(20, 20))
        self.simple_button.setCheckable(True)
        self.simple_button.setAutoExclusive(True)
        self.simple_button.setAutoDefault(True)

        self.preset_container.addWidget(self.simple_button)

        self.complex_button = QPushButton(self.preset)
        self.complex_button.setObjectName(u"complex_button")
        sizePolicy6.setHeightForWidth(self.complex_button.sizePolicy().hasHeightForWidth())
        self.complex_button.setSizePolicy(sizePolicy6)
        self.complex_button.setMinimumSize(QSize(110, 40))
        self.complex_button.setMaximumSize(QSize(80, 40))
        self.complex_button.setFont(font4)
        icon12 = QIcon()
        icon12.addFile(u":/icons/calendar/events/other/complex_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/calendar/events/other/complex_purple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon12.addFile(u":/icons/calendar/events/other/complex_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.complex_button.setIcon(icon12)
        self.complex_button.setIconSize(QSize(20, 20))
        self.complex_button.setCheckable(True)
        self.complex_button.setAutoExclusive(True)

        self.preset_container.addWidget(self.complex_button)

        self.preset_wrapper.setWidget(self.preset)

        self.details_form_container.setWidget(1, QFormLayout.ItemRole.FieldRole, self.preset_wrapper)

        self.time_button = QPushButton(self.details_form)
        self.time_button.setObjectName(u"time_button")
        self.time_button.setMinimumSize(QSize(50, 50))
        self.time_button.setMaximumSize(QSize(50, 50))
        icon13 = QIcon()
        icon13.addFile(u":/icons/calendar/clock_light.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/calendar/clock_orange.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon13.addFile(u":/icons/calendar/clock_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon13.addFile(u":/icons/calendar/clock_slash_orange.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.time_button.setIcon(icon13)
        self.time_button.setIconSize(QSize(30, 30))
        self.time_button.setCheckable(True)
        self.time_button.setChecked(False)

        self.details_form_container.setWidget(2, QFormLayout.ItemRole.LabelRole, self.time_button)

        self.time = QWidget(self.details_form)
        self.time.setObjectName(u"time")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy9)
        self.time.setMinimumSize(QSize(247, 68))
        self.time.setMaximumSize(QSize(290, 16777215))
        self.time.setAutoFillBackground(False)
        self.time.setStyleSheet(u"QWidget#time {\n"
"	border: 2px solid rgba(255, 177, 61, 1);\n"
"	border-radius: 10px;\n"
"}")
        self.time_viewedit_container = QVBoxLayout(self.time)
        self.time_viewedit_container.setSpacing(0)
        self.time_viewedit_container.setObjectName(u"time_viewedit_container")
        self.time_viewedit_container.setContentsMargins(3, 3, 3, 3)
        self.time_view = ETime(self.time)
        self.time_view.setObjectName(u"time_view")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.time_view.sizePolicy().hasHeightForWidth())
        self.time_view.setSizePolicy(sizePolicy10)
        self.time_view.setMinimumSize(QSize(247, 68))
        self.time_view.setMaximumSize(QSize(288, 68))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(18)
        self.time_view.setFont(font5)
        self.time_view.setStyleSheet(u"ETime{\n"
"                           background-color: rgba(20,20,20,1);\n"
"                           border-radius: 6px;                 \n"
"} ELabel {\n"
"                           background-color: None;\n"
"                           border-radius: 0px;\n"
"                           padding-left: 3px;\n"
"                           border: 0px solid transparent;\n"
"}")

        self.time_viewedit_container.addWidget(self.time_view)

        self.time_edit = QWidget(self.time)
        self.time_edit.setObjectName(u"time_edit")
        sizePolicy6.setHeightForWidth(self.time_edit.sizePolicy().hasHeightForWidth())
        self.time_edit.setSizePolicy(sizePolicy6)
        self.time_edit.setMinimumSize(QSize(247, 180))
        self.time_edit.setMaximumSize(QSize(16777215, 180))
        self.time_edit.setFont(font4)
        self.time_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_edit.setStyleSheet(u"QWidget#time_edit {\n"
"	background: rgba(30,30,30,1);\n"
"	border-radius: 6px;\n"
"}\n"
"QLabel {\n"
"	padding: 0px;\n"
"	background: none;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.time_edit_form = QFormLayout(self.time_edit)
        self.time_edit_form.setObjectName(u"time_edit_form")
        self.time_edit_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.time_edit_form.setFormAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.time_edit_form.setHorizontalSpacing(10)
        self.time_edit_form.setVerticalSpacing(10)
        self.time_edit_form.setContentsMargins(10, 10, 10, 10)
        self.time_allday_label = QLabel(self.time_edit)
        self.time_allday_label.setObjectName(u"time_allday_label")
        sizePolicy2.setHeightForWidth(self.time_allday_label.sizePolicy().hasHeightForWidth())
        self.time_allday_label.setSizePolicy(sizePolicy2)
        self.time_allday_label.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        font6.setBold(False)
        self.time_allday_label.setFont(font6)
        self.time_allday_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_allday_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.time_edit_form.setWidget(0, QFormLayout.ItemRole.LabelRole, self.time_allday_label)

        self.time_start_label = QLabel(self.time_edit)
        self.time_start_label.setObjectName(u"time_start_label")
        sizePolicy2.setHeightForWidth(self.time_start_label.sizePolicy().hasHeightForWidth())
        self.time_start_label.setSizePolicy(sizePolicy2)
        self.time_start_label.setMinimumSize(QSize(0, 30))
        self.time_start_label.setFont(font4)
        self.time_start_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.time_edit_form.setWidget(1, QFormLayout.ItemRole.LabelRole, self.time_start_label)

        self.time_start_select = TDateTimeSelect(self.time_edit)
        self.time_start_select.setObjectName(u"time_start_select")
        sizePolicy7.setHeightForWidth(self.time_start_select.sizePolicy().hasHeightForWidth())
        self.time_start_select.setSizePolicy(sizePolicy7)
        self.time_start_select.setMinimumSize(QSize(0, 30))
        self.time_start_select.setAutoFillBackground(False)

        self.time_edit_form.setWidget(1, QFormLayout.ItemRole.FieldRole, self.time_start_select)

        self.time_end_label = QLabel(self.time_edit)
        self.time_end_label.setObjectName(u"time_end_label")
        sizePolicy2.setHeightForWidth(self.time_end_label.sizePolicy().hasHeightForWidth())
        self.time_end_label.setSizePolicy(sizePolicy2)
        self.time_end_label.setMinimumSize(QSize(0, 30))
        self.time_end_label.setFont(font4)
        self.time_end_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.time_edit_form.setWidget(3, QFormLayout.ItemRole.LabelRole, self.time_end_label)

        self.time_end_select = TDateTimeSelect(self.time_edit)
        self.time_end_select.setObjectName(u"time_end_select")
        self.time_end_select.setMinimumSize(QSize(0, 30))
        self.time_end_select.setAutoFillBackground(False)

        self.time_edit_form.setWidget(3, QFormLayout.ItemRole.FieldRole, self.time_end_select)

        self.time_schedule_label = QLabel(self.time_edit)
        self.time_schedule_label.setObjectName(u"time_schedule_label")
        sizePolicy2.setHeightForWidth(self.time_schedule_label.sizePolicy().hasHeightForWidth())
        self.time_schedule_label.setSizePolicy(sizePolicy2)
        self.time_schedule_label.setMinimumSize(QSize(0, 30))
        self.time_schedule_label.setFont(font4)
        self.time_schedule_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.time_edit_form.setWidget(4, QFormLayout.ItemRole.LabelRole, self.time_schedule_label)

        self.time_allday_checkbox_to_right_wrapper = QWidget(self.time_edit)
        self.time_allday_checkbox_to_right_wrapper.setObjectName(u"time_allday_checkbox_to_right_wrapper")
        self.checkbox_toright_container = QHBoxLayout(self.time_allday_checkbox_to_right_wrapper)
        self.checkbox_toright_container.setSpacing(0)
        self.checkbox_toright_container.setObjectName(u"checkbox_toright_container")
        self.checkbox_toright_container.setContentsMargins(0, 0, 0, 0)
        self.time_allday_checkbox_to_right_spacer = QSpacerItem(155, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.checkbox_toright_container.addItem(self.time_allday_checkbox_to_right_spacer)

        self.time_allday_checkbox = QCheckBox(self.time_allday_checkbox_to_right_wrapper)
        self.time_allday_checkbox.setObjectName(u"time_allday_checkbox")
        self.time_allday_checkbox.setMinimumSize(QSize(30, 30))
        self.time_allday_checkbox.setMaximumSize(QSize(30, 30))
        self.time_allday_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_allday_checkbox.setIconSize(QSize(30, 30))
        self.time_allday_checkbox.setChecked(False)
        self.time_allday_checkbox.setTristate(False)

        self.checkbox_toright_container.addWidget(self.time_allday_checkbox)


        self.time_edit_form.setWidget(0, QFormLayout.ItemRole.FieldRole, self.time_allday_checkbox_to_right_wrapper)

        self.schedule_to_right_wrapper = QWidget(self.time_edit)
        self.schedule_to_right_wrapper.setObjectName(u"schedule_to_right_wrapper")
        self.schedule_to_right_container = QHBoxLayout(self.schedule_to_right_wrapper)
        self.schedule_to_right_container.setSpacing(0)
        self.schedule_to_right_container.setObjectName(u"schedule_to_right_container")
        self.schedule_to_right_container.setContentsMargins(0, 0, 0, 0)
        self.schedule_to_right_spacer = QSpacerItem(43, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.schedule_to_right_container.addItem(self.schedule_to_right_spacer)

        self.time_schedule_label_button = QPushButton(self.schedule_to_right_wrapper)
        self.time_schedule_label_button.setObjectName(u"time_schedule_label_button")
        self.time_schedule_label_button.setMinimumSize(QSize(140, 30))
        self.time_schedule_label_button.setMaximumSize(QSize(140, 16777215))
        self.time_schedule_label_button.setFont(font4)
        self.time_schedule_label_button.setStyleSheet(u"background-color: rgba(40, 40, 40, 1);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/nav/menu_board_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/nav/menu_board_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon14.addFile(u":/icons/nav/menu_board_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon14.addFile(u":/icons/nav/menu_board_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.time_schedule_label_button.setIcon(icon14)
        self.time_schedule_label_button.setIconSize(QSize(20, 20))
        self.time_schedule_label_button.setCheckable(False)

        self.schedule_to_right_container.addWidget(self.time_schedule_label_button)


        self.time_edit_form.setWidget(4, QFormLayout.ItemRole.FieldRole, self.schedule_to_right_wrapper)


        self.time_viewedit_container.addWidget(self.time_edit)


        self.details_form_container.setWidget(2, QFormLayout.ItemRole.FieldRole, self.time)

        self.layer_button = QPushButton(self.details_form)
        self.layer_button.setObjectName(u"layer_button")
        self.layer_button.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.layer_button.sizePolicy().hasHeightForWidth())
        self.layer_button.setSizePolicy(sizePolicy7)
        self.layer_button.setMinimumSize(QSize(50, 50))
        self.layer_button.setMaximumSize(QSize(50, 50))
        icon15 = QIcon()
        icon15.addFile(u":/icons/calendar/events/layer_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/icons/calendar/events/layer_blue2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon15.addFile(u":/icons/calendar/events/layer_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon15.addFile(u":/icons/calendar/events/layer_slash_blue2.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.layer_button.setIcon(icon15)
        self.layer_button.setIconSize(QSize(30, 30))
        self.layer_button.setCheckable(True)
        self.layer_button.setChecked(False)

        self.details_form_container.setWidget(3, QFormLayout.ItemRole.LabelRole, self.layer_button)

        self.location_button = QPushButton(self.details_form)
        self.location_button.setObjectName(u"location_button")
        sizePolicy7.setHeightForWidth(self.location_button.sizePolicy().hasHeightForWidth())
        self.location_button.setSizePolicy(sizePolicy7)
        self.location_button.setMinimumSize(QSize(50, 50))
        self.location_button.setMaximumSize(QSize(50, 50))
        icon16 = QIcon()
        icon16.addFile(u":/icons/calendar/events/location/location_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon16.addFile(u":/icons/calendar/events/location/location_green.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon16.addFile(u":/icons/calendar/events/location/location_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon16.addFile(u":/icons/calendar/events/location/location_slash_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.location_button.setIcon(icon16)
        self.location_button.setIconSize(QSize(30, 30))
        self.location_button.setCheckable(True)
        self.location_button.setChecked(False)

        self.details_form_container.setWidget(4, QFormLayout.ItemRole.LabelRole, self.location_button)

        self.invitees_button = QPushButton(self.details_form)
        self.invitees_button.setObjectName(u"invitees_button")
        sizePolicy7.setHeightForWidth(self.invitees_button.sizePolicy().hasHeightForWidth())
        self.invitees_button.setSizePolicy(sizePolicy7)
        self.invitees_button.setMinimumSize(QSize(50, 50))
        self.invitees_button.setMaximumSize(QSize(50, 50))
        icon17 = QIcon()
        icon17.addFile(u":/icons/user/profile2_user_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/icons/user/profile2_user_red.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon17.addFile(u":/icons/user/profile_2_slash_light.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon17.addFile(u":/icons/user/profile_2_slash_light.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.invitees_button.setIcon(icon17)
        self.invitees_button.setIconSize(QSize(30, 30))
        self.invitees_button.setCheckable(True)
        self.invitees_button.setChecked(False)

        self.details_form_container.setWidget(5, QFormLayout.ItemRole.LabelRole, self.invitees_button)

        self.tags_button = QPushButton(self.details_form)
        self.tags_button.setObjectName(u"tags_button")
        sizePolicy7.setHeightForWidth(self.tags_button.sizePolicy().hasHeightForWidth())
        self.tags_button.setSizePolicy(sizePolicy7)
        self.tags_button.setMinimumSize(QSize(50, 50))
        self.tags_button.setMaximumSize(QSize(50, 50))
        icon18 = QIcon()
        icon18.addFile(u":/icons/calendar/events/tags/tag_slash_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon18.addFile(u":/icons/calendar/events/tags/tag_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon18.addFile(u":/icons/calendar/events/tags/tag_slash_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon18.addFile(u":/icons/calendar/events/tags/tag_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon18.addFile(u":/icons/calendar/events/tags/tag_slash_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon18.addFile(u":/icons/calendar/events/tags/tag_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon18.addFile(u":/icons/calendar/events/tags/tag_slash_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon18.addFile(u":/icons/calendar/events/tags/tag_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.tags_button.setIcon(icon18)
        self.tags_button.setIconSize(QSize(30, 30))
        self.tags_button.setCheckable(True)
        self.tags_button.setChecked(True)

        self.details_form_container.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tags_button)

        self.save_button = QPushButton(self.details_form)
        self.save_button.setObjectName(u"save_button")
        sizePolicy6.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy6)
        self.save_button.setMinimumSize(QSize(100, 40))
        self.save_button.setFont(font)
        icon19 = QIcon()
        icon19.addFile(u":/icons/util/alert_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon19.addFile(u":/icons/util/add_2_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon19.addFile(u":/icons/util/alert_yellow.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon19.addFile(u":/icons/util/add_2_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon19.addFile(u":/icons/util/alert_yellow.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon19.addFile(u":/icons/util/add_2_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.save_button.setIcon(icon19)
        self.save_button.setIconSize(QSize(30, 30))
        self.save_button.setCheckable(True)
        self.save_button.setChecked(True)
        self.save_button.setAutoDefault(False)

        self.details_form_container.setWidget(7, QFormLayout.ItemRole.FieldRole, self.save_button)

        self.location = QWidget(self.details_form)
        self.location.setObjectName(u"location")
        self.location_container = QVBoxLayout(self.location)
        self.location_container.setSpacing(0)
        self.location_container.setObjectName(u"location_container")
        self.location_container.setContentsMargins(0, 0, 0, 0)
        self.location_view = QWidget(self.location)
        self.location_view.setObjectName(u"location_view")
        self.location_view_container = QVBoxLayout(self.location_view)
        self.location_view_container.setSpacing(0)
        self.location_view_container.setObjectName(u"location_view_container")
        self.location_view_container.setContentsMargins(0, 0, 0, 0)
        self.location_view_collapsed = QWidget(self.location_view)
        self.location_view_collapsed.setObjectName(u"location_view_collapsed")
        self.location_view_collapsed.setMinimumSize(QSize(0, 50))
        self.location_view_collapsed.setMaximumSize(QSize(16777215, 50))
        self.location_view_collapsed_container = QHBoxLayout(self.location_view_collapsed)
        self.location_view_collapsed_container.setSpacing(0)
        self.location_view_collapsed_container.setObjectName(u"location_view_collapsed_container")
        self.location_view_collapsed_container.setContentsMargins(0, 0, 0, 0)
        self.location_view_col_wrapper = QScrollArea(self.location_view_collapsed)
        self.location_view_col_wrapper.setObjectName(u"location_view_col_wrapper")
        sizePolicy4.setHeightForWidth(self.location_view_col_wrapper.sizePolicy().hasHeightForWidth())
        self.location_view_col_wrapper.setSizePolicy(sizePolicy4)
        self.location_view_col_wrapper.setMinimumSize(QSize(212, 50))
        self.location_view_col_wrapper.setMaximumSize(QSize(250, 50))
        self.location_view_col_wrapper.setFont(font)
        self.location_view_col_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.location_view_col_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.location_view_col_wrapper.setLineWidth(0)
        self.location_view_col_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.location_view_col_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.location_view_col_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.location_view_col_wrapper.setWidgetResizable(False)
        self.location_view_col_wrapper.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.location_view_col_label_container = QWidget()
        self.location_view_col_label_container.setObjectName(u"location_view_col_label_container")
        self.location_view_col_label_container.setGeometry(QRect(0, 0, 212, 48))
        sizePolicy5.setHeightForWidth(self.location_view_col_label_container.sizePolicy().hasHeightForWidth())
        self.location_view_col_label_container.setSizePolicy(sizePolicy5)
        self.location_view_col_label_container.setMinimumSize(QSize(212, 48))
        self.location_view_col_label_container.setMaximumSize(QSize(800, 48))
        self.location_view_col_container = QHBoxLayout(self.location_view_col_label_container)
        self.location_view_col_container.setSpacing(0)
        self.location_view_col_container.setObjectName(u"location_view_col_container")
        self.location_view_col_container.setContentsMargins(0, 0, 0, 2)
        self.loc_view_col_label = QLabel(self.location_view_col_label_container)
        self.loc_view_col_label.setObjectName(u"loc_view_col_label")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.loc_view_col_label.sizePolicy().hasHeightForWidth())
        self.loc_view_col_label.setSizePolicy(sizePolicy11)
        self.loc_view_col_label.setMinimumSize(QSize(211, 46))
        self.loc_view_col_label.setMaximumSize(QSize(212, 46))
        self.loc_view_col_label.setFont(font2)
        self.loc_view_col_label.setLineWidth(0)

        self.location_view_col_container.addWidget(self.loc_view_col_label)

        self.location_view_col_wrapper.setWidget(self.location_view_col_label_container)

        self.location_view_collapsed_container.addWidget(self.location_view_col_wrapper)

        self.location_expand_button = QPushButton(self.location_view_collapsed)
        self.location_expand_button.setObjectName(u"location_expand_button")
        sizePolicy7.setHeightForWidth(self.location_expand_button.sizePolicy().hasHeightForWidth())
        self.location_expand_button.setSizePolicy(sizePolicy7)
        self.location_expand_button.setMinimumSize(QSize(40, 50))
        self.location_expand_button.setMaximumSize(QSize(40, 50))
        icon20 = QIcon()
        icon20.addFile(u":/icons/calendar/events/location/location_edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon20.addFile(u":/icons/calendar/events/location/location_lock_dark.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.location_expand_button.setIcon(icon20)
        self.location_expand_button.setIconSize(QSize(30, 30))
        self.location_expand_button.setCheckable(True)
        self.location_expand_button.setChecked(True)

        self.location_view_collapsed_container.addWidget(self.location_expand_button)


        self.location_view_container.addWidget(self.location_view_collapsed)

        self.location_view_expanded = QWidget(self.location_view)
        self.location_view_expanded.setObjectName(u"location_view_expanded")
        sizePolicy1.setHeightForWidth(self.location_view_expanded.sizePolicy().hasHeightForWidth())
        self.location_view_expanded.setSizePolicy(sizePolicy1)
        self.location_view_expanded.setMinimumSize(QSize(252, 0))
        self.location_view_expanded.setMaximumSize(QSize(290, 16777215))
        self.location_view_expanded_container = QHBoxLayout(self.location_view_expanded)
        self.location_view_expanded_container.setSpacing(0)
        self.location_view_expanded_container.setObjectName(u"location_view_expanded_container")
        self.location_view_expanded_container.setContentsMargins(0, 0, 0, 0)
        self.location_view_exp_labels = QWidget(self.location_view_expanded)
        self.location_view_exp_labels.setObjectName(u"location_view_exp_labels")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.location_view_exp_labels.sizePolicy().hasHeightForWidth())
        self.location_view_exp_labels.setSizePolicy(sizePolicy12)
        self.location_view_exp_labels.setMinimumSize(QSize(207, 0))
        self.location_view_exp_labels.setMaximumSize(QSize(16777215, 300))
        self.location_view_exp_labels.setStyleSheet(u"")
        self.location_view_exp_labels_container = QVBoxLayout(self.location_view_exp_labels)
        self.location_view_exp_labels_container.setSpacing(5)
        self.location_view_exp_labels_container.setObjectName(u"location_view_exp_labels_container")
        self.location_view_exp_labels_container.setContentsMargins(0, 0, 0, 0)
        self.loc_address_line_1_label = QLabel(self.location_view_exp_labels)
        self.loc_address_line_1_label.setObjectName(u"loc_address_line_1_label")
        self.loc_address_line_1_label.setMinimumSize(QSize(0, 40))
        self.loc_address_line_1_label.setMaximumSize(QSize(16777215, 40))
        self.loc_address_line_1_label.setFont(font)
        self.loc_address_line_1_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_address_line_1_label)

        self.loc_address_line_2_label = QLabel(self.location_view_exp_labels)
        self.loc_address_line_2_label.setObjectName(u"loc_address_line_2_label")
        self.loc_address_line_2_label.setMinimumSize(QSize(0, 40))
        self.loc_address_line_2_label.setFont(font)
        self.loc_address_line_2_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_address_line_2_label)

        self.loc_address_line_3_label = QLabel(self.location_view_exp_labels)
        self.loc_address_line_3_label.setObjectName(u"loc_address_line_3_label")
        self.loc_address_line_3_label.setMinimumSize(QSize(0, 40))
        self.loc_address_line_3_label.setMaximumSize(QSize(16777215, 40))
        self.loc_address_line_3_label.setFont(font)
        self.loc_address_line_3_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_address_line_3_label)

        self.loc_county_label = QLabel(self.location_view_exp_labels)
        self.loc_county_label.setObjectName(u"loc_county_label")
        self.loc_county_label.setMinimumSize(QSize(0, 40))
        self.loc_county_label.setMaximumSize(QSize(16777215, 40))
        self.loc_county_label.setFont(font)
        self.loc_county_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_county_label)

        self.loc_city_label = QLabel(self.location_view_exp_labels)
        self.loc_city_label.setObjectName(u"loc_city_label")
        self.loc_city_label.setMinimumSize(QSize(0, 40))
        self.loc_city_label.setMaximumSize(QSize(16777215, 40))
        self.loc_city_label.setFont(font)
        self.loc_city_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_city_label)

        self.loc_postcode_label = QLabel(self.location_view_exp_labels)
        self.loc_postcode_label.setObjectName(u"loc_postcode_label")
        self.loc_postcode_label.setMinimumSize(QSize(0, 40))
        self.loc_postcode_label.setMaximumSize(QSize(16777215, 40))
        self.loc_postcode_label.setFont(font)
        self.loc_postcode_label.setWordWrap(True)

        self.location_view_exp_labels_container.addWidget(self.loc_postcode_label)


        self.location_view_expanded_container.addWidget(self.location_view_exp_labels)

        self.location_view_exp_options = QWidget(self.location_view_expanded)
        self.location_view_exp_options.setObjectName(u"location_view_exp_options")
        sizePolicy7.setHeightForWidth(self.location_view_exp_options.sizePolicy().hasHeightForWidth())
        self.location_view_exp_options.setSizePolicy(sizePolicy7)
        self.location_view_exp_options.setMinimumSize(QSize(40, 0))
        self.location_view_exp_options.setMaximumSize(QSize(40, 16777215))
        self.location_view_exp_options_container = QVBoxLayout(self.location_view_exp_options)
        self.location_view_exp_options_container.setSpacing(10)
        self.location_view_exp_options_container.setObjectName(u"location_view_exp_options_container")
        self.location_view_exp_options_container.setContentsMargins(0, 0, 0, 0)
        self.location_finish_button = QPushButton(self.location_view_exp_options)
        self.location_finish_button.setObjectName(u"location_finish_button")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.location_finish_button.sizePolicy().hasHeightForWidth())
        self.location_finish_button.setSizePolicy(sizePolicy13)
        self.location_finish_button.setMinimumSize(QSize(40, 50))
        self.location_finish_button.setMaximumSize(QSize(40, 50))
        icon21 = QIcon()
        icon21.addFile(u":/icons/calendar/events/location/location_back_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon21.addFile(u":/icons/calendar/events/location/location_tick1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.location_finish_button.setIcon(icon21)
        self.location_finish_button.setIconSize(QSize(30, 30))
        self.location_finish_button.setCheckable(True)
        self.location_finish_button.setChecked(True)

        self.location_view_exp_options_container.addWidget(self.location_finish_button)

        self.location_view_exp_options_spacer = QSpacerItem(10, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.location_view_exp_options_container.addItem(self.location_view_exp_options_spacer)

        self.location_edit_button = QPushButton(self.location_view_exp_options)
        self.location_edit_button.setObjectName(u"location_edit_button")
        sizePolicy13.setHeightForWidth(self.location_edit_button.sizePolicy().hasHeightForWidth())
        self.location_edit_button.setSizePolicy(sizePolicy13)
        self.location_edit_button.setMinimumSize(QSize(40, 50))
        self.location_edit_button.setMaximumSize(QSize(40, 50))
        icon22 = QIcon()
        icon22.addFile(u":/icons/calendar/events/location/location_remove1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon22.addFile(u":/icons/calendar/events/location/location_add1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.location_edit_button.setIcon(icon22)
        self.location_edit_button.setIconSize(QSize(30, 30))
        self.location_edit_button.setCheckable(True)
        self.location_edit_button.setChecked(True)

        self.location_view_exp_options_container.addWidget(self.location_edit_button)


        self.location_view_expanded_container.addWidget(self.location_view_exp_options)


        self.location_view_container.addWidget(self.location_view_expanded)


        self.location_container.addWidget(self.location_view)

        self.location_edit_combobox = QComboBox(self.location)
        self.location_edit_combobox.setObjectName(u"location_edit_combobox")
        sizePolicy4.setHeightForWidth(self.location_edit_combobox.sizePolicy().hasHeightForWidth())
        self.location_edit_combobox.setSizePolicy(sizePolicy4)
        self.location_edit_combobox.setMinimumSize(QSize(252, 50))
        self.location_edit_combobox.setMaximumSize(QSize(290, 50))
        self.location_edit_combobox.setFont(font2)
        self.location_edit_combobox.setEditable(True)
        self.location_edit_combobox.setIconSize(QSize(30, 30))

        self.location_container.addWidget(self.location_edit_combobox)


        self.details_form_container.setWidget(4, QFormLayout.ItemRole.FieldRole, self.location)

        self.layer = QWidget(self.details_form)
        self.layer.setObjectName(u"layer")
        sizePolicy2.setHeightForWidth(self.layer.sizePolicy().hasHeightForWidth())
        self.layer.setSizePolicy(sizePolicy2)
        self.layer.setMinimumSize(QSize(0, 0))
        self.layer.setMaximumSize(QSize(290, 16777215))
        self.layer.setAutoFillBackground(False)
        self.layer.setStyleSheet(u"QWidget#layer {\n"
"	border: 2px solid rgba(60,60,60,1);\n"
"	border-radius: 10px;\n"
"}")
        self.layer_container = QVBoxLayout(self.layer)
        self.layer_container.setSpacing(10)
        self.layer_container.setObjectName(u"layer_container")
        self.layer_container.setContentsMargins(3, 3, 3, 3)
        self.layers_header = QLabel(self.layer)
        self.layers_header.setObjectName(u"layers_header")
        sizePolicy2.setHeightForWidth(self.layers_header.sizePolicy().hasHeightForWidth())
        self.layers_header.setSizePolicy(sizePolicy2)
        self.layers_header.setMinimumSize(QSize(248, 40))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(24)
        self.layers_header.setFont(font7)
        self.layers_header.setStyleSheet(u"border-radius: 6px;\n"
"padding-left: 5px;")
        self.layers_header.setLineWidth(0)

        self.layer_container.addWidget(self.layers_header)

        self.layer_edit = QWidget(self.layer)
        self.layer_edit.setObjectName(u"layer_edit")
        sizePolicy2.setHeightForWidth(self.layer_edit.sizePolicy().hasHeightForWidth())
        self.layer_edit.setSizePolicy(sizePolicy2)
        self.layer_edit.setMinimumSize(QSize(247, 0))
        self.layer_edit.setMaximumSize(QSize(290, 16777215))
        self.layer_edit.setStyleSheet(u"QWidget#layer_edit {\n"
"	border-radius: 6px;\n"
"}")
        self.layer_edit_container = QVBoxLayout(self.layer_edit)
        self.layer_edit_container.setSpacing(10)
        self.layer_edit_container.setObjectName(u"layer_edit_container")
        self.layer_edit_container.setContentsMargins(0, 0, 0, 0)
        self.layer_header_wrapper = QScrollArea(self.layer_edit)
        self.layer_header_wrapper.setObjectName(u"layer_header_wrapper")
        sizePolicy2.setHeightForWidth(self.layer_header_wrapper.sizePolicy().hasHeightForWidth())
        self.layer_header_wrapper.setSizePolicy(sizePolicy2)
        self.layer_header_wrapper.setMinimumSize(QSize(247, 70))
        self.layer_header_wrapper.setMaximumSize(QSize(290, 70))
        self.layer_header_wrapper.setAutoFillBackground(False)
        self.layer_header_wrapper.setStyleSheet(u"QScrollBar:horizontal {\n"
"   	background: rgba(40,40,40,0.9);\n"
"    	height: 20px;\n"
"	padding: 0px 25px\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(120,120,120,1);\n"
"	min-width: 50px;\n"
"	min-height: 20px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    	background: rgba(20,20,20,1);\n"
"    	width: 25px;\n"
"	padding: 0px;\n"
"    	border: 0px solid rgba(0,0,0,0);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   	subcontrol-origin: margin;\n"
"    	subcontrol-position: left;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: right;\n"
"	border-bottom-right-ra"
                        "dius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_left_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_left_red.svg\")\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_right_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_right_red.svg\")\n"
"}")
        self.layer_header_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.layer_header_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.layer_header_wrapper.setLineWidth(0)
        self.layer_header_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layer_header_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.layer_header_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.layer_header_wrapper.setWidgetResizable(True)
        self.layer_header = QWidget()
        self.layer_header.setObjectName(u"layer_header")
        self.layer_header.setGeometry(QRect(0, 0, 440, 40))
        self.layer_header.setMaximumSize(QSize(16777215, 40))
        self.layer_header_container = QHBoxLayout(self.layer_header)
        self.layer_header_container.setSpacing(10)
        self.layer_header_container.setObjectName(u"layer_header_container")
        self.layer_header_container.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.layer_header_container.setContentsMargins(0, 0, 0, 20)
        self.layer_finish_button = QPushButton(self.layer_header)
        self.layer_finish_button.setObjectName(u"layer_finish_button")
        self.layer_finish_button.setMinimumSize(QSize(90, 40))
        self.layer_finish_button.setMaximumSize(QSize(90, 40))
        self.layer_finish_button.setFont(font4)
        icon23 = QIcon()
        icon23.addFile(u":/icons/util/back_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon23.addFile(u":/icons/util/back_square1_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon23.addFile(u":/icons/util/back_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon23.addFile(u":/icons/util/back_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.layer_finish_button.setIcon(icon23)
        self.layer_finish_button.setIconSize(QSize(20, 20))
        self.layer_finish_button.setCheckable(True)
        self.layer_finish_button.setAutoExclusive(False)

        self.layer_header_container.addWidget(self.layer_finish_button)

        self.layer_add_button = QPushButton(self.layer_header)
        self.layer_add_button.setObjectName(u"layer_add_button")
        self.layer_add_button.setMinimumSize(QSize(80, 40))
        self.layer_add_button.setMaximumSize(QSize(80, 40))
        self.layer_add_button.setFont(font4)
        icon24 = QIcon()
        icon24.addFile(u":/icons/util/add_2_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon24.addFile(u":/icons/util/add_2_red.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.layer_add_button.setIcon(icon24)
        self.layer_add_button.setIconSize(QSize(20, 20))
        self.layer_add_button.setCheckable(True)
        self.layer_add_button.setAutoExclusive(False)

        self.layer_header_container.addWidget(self.layer_add_button)

        self.layer_remove_button = QPushButton(self.layer_header)
        self.layer_remove_button.setObjectName(u"layer_remove_button")
        self.layer_remove_button.setMinimumSize(QSize(110, 40))
        self.layer_remove_button.setMaximumSize(QSize(110, 40))
        self.layer_remove_button.setFont(font4)
        icon25 = QIcon()
        icon25.addFile(u":/icons/util/minus_square_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon25.addFile(u":/icons/util/minus_square_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon25.addFile(u":/icons/util/minus_square_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon25.addFile(u":/icons/util/minus_square_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon25.addFile(u":/icons/util/minus_square_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon25.addFile(u":/icons/util/minus_square_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon25.addFile(u":/icons/util/minus_square_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.layer_remove_button.setIcon(icon25)
        self.layer_remove_button.setIconSize(QSize(20, 20))
        self.layer_remove_button.setCheckable(True)
        self.layer_remove_button.setAutoExclusive(False)

        self.layer_header_container.addWidget(self.layer_remove_button)

        self.layer_edit_button = QPushButton(self.layer_header)
        self.layer_edit_button.setObjectName(u"layer_edit_button")
        self.layer_edit_button.setMinimumSize(QSize(80, 40))
        self.layer_edit_button.setMaximumSize(QSize(80, 40))
        self.layer_edit_button.setFont(font4)
        icon26 = QIcon()
        icon26.addFile(u":/icons/util/edit_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon26.addFile(u":/icons/util/edit_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon26.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon26.addFile(u":/icons/util/edit_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.layer_edit_button.setIcon(icon26)
        self.layer_edit_button.setIconSize(QSize(20, 20))
        self.layer_edit_button.setCheckable(True)
        self.layer_edit_button.setAutoExclusive(False)

        self.layer_header_container.addWidget(self.layer_edit_button)

        self.spacer_widget = QWidget(self.layer_header)
        self.spacer_widget.setObjectName(u"spacer_widget")
        sizePolicy1.setHeightForWidth(self.spacer_widget.sizePolicy().hasHeightForWidth())
        self.spacer_widget.setSizePolicy(sizePolicy1)
        self.spacer_widget_layout = QHBoxLayout(self.spacer_widget)
        self.spacer_widget_layout.setSpacing(0)
        self.spacer_widget_layout.setObjectName(u"spacer_widget_layout")
        self.spacer_widget_layout.setContentsMargins(0, 10, 0, 0)
        self.layer_header_spacer = QSpacerItem(40, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.spacer_widget_layout.addItem(self.layer_header_spacer)


        self.layer_header_container.addWidget(self.spacer_widget)

        self.layer_header_wrapper.setWidget(self.layer_header)

        self.layer_edit_container.addWidget(self.layer_header_wrapper)

        self.layer_header_expanded = QWidget(self.layer_edit)
        self.layer_header_expanded.setObjectName(u"layer_header_expanded")
        self.layer_header_expanded_container = QVBoxLayout(self.layer_header_expanded)
        self.layer_header_expanded_container.setSpacing(0)
        self.layer_header_expanded_container.setObjectName(u"layer_header_expanded_container")
        self.layer_header_expanded_container.setContentsMargins(0, 0, 0, 0)
        self.layer_header_exp_finish = QWidget(self.layer_header_expanded)
        self.layer_header_exp_finish.setObjectName(u"layer_header_exp_finish")
        sizePolicy2.setHeightForWidth(self.layer_header_exp_finish.sizePolicy().hasHeightForWidth())
        self.layer_header_exp_finish.setSizePolicy(sizePolicy2)
        self.layer_header_exp_finish.setMinimumSize(QSize(247, 40))
        self.layer_header_exp_finish.setMaximumSize(QSize(290, 40))
        self.finish_options_container = QHBoxLayout(self.layer_header_exp_finish)
        self.finish_options_container.setSpacing(10)
        self.finish_options_container.setObjectName(u"finish_options_container")
        self.finish_options_container.setContentsMargins(0, 0, 0, 0)
        self.layer_save_changes_button = QPushButton(self.layer_header_exp_finish)
        self.layer_save_changes_button.setObjectName(u"layer_save_changes_button")
        self.layer_save_changes_button.setMinimumSize(QSize(90, 40))
        self.layer_save_changes_button.setMaximumSize(QSize(90, 50))
        self.layer_save_changes_button.setFont(font4)
        icon27 = QIcon()
        icon27.addFile(u":/icons/util/tick_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon27.addFile(u":/icons/util/tick_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon27.addFile(u":/icons/util/tick_square1_green.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon27.addFile(u":/icons/util/tick_square1_green.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.layer_save_changes_button.setIcon(icon27)
        self.layer_save_changes_button.setIconSize(QSize(20, 20))

        self.finish_options_container.addWidget(self.layer_save_changes_button)

        self.layer_cancel_changes_button = QPushButton(self.layer_header_exp_finish)
        self.layer_cancel_changes_button.setObjectName(u"layer_cancel_changes_button")
        self.layer_cancel_changes_button.setMinimumSize(QSize(100, 40))
        self.layer_cancel_changes_button.setMaximumSize(QSize(100, 50))
        self.layer_cancel_changes_button.setFont(font4)
        icon28 = QIcon()
        icon28.addFile(u":/icons/util/close_square1_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon28.addFile(u":/icons/util/close_square1_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon28.addFile(u":/icons/util/close_square1_red.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon28.addFile(u":/icons/util/close_square1_red.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.layer_cancel_changes_button.setIcon(icon28)
        self.layer_cancel_changes_button.setIconSize(QSize(20, 20))

        self.finish_options_container.addWidget(self.layer_cancel_changes_button)

        self.layer_finish_options_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.finish_options_container.addItem(self.layer_finish_options_spacer)


        self.layer_header_expanded_container.addWidget(self.layer_header_exp_finish)

        self.layer_header_exp_add_wrapper = QScrollArea(self.layer_header_expanded)
        self.layer_header_exp_add_wrapper.setObjectName(u"layer_header_exp_add_wrapper")
        sizePolicy2.setHeightForWidth(self.layer_header_exp_add_wrapper.sizePolicy().hasHeightForWidth())
        self.layer_header_exp_add_wrapper.setSizePolicy(sizePolicy2)
        self.layer_header_exp_add_wrapper.setMinimumSize(QSize(190, 0))
        self.layer_header_exp_add_wrapper.setMaximumSize(QSize(16777215, 40))
        self.layer_header_exp_add_wrapper.setStyleSheet(u"QScrollBar:horizontal {\n"
"   	background: rgba(40,40,40,0.9);\n"
"    	height: 20px;\n"
"	padding: 0px 25px\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(120,120,120,1);\n"
"	min-width: 50px;\n"
"	min-height: 20px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    	background: rgba(20,20,20,1);\n"
"    	width: 25px;\n"
"	padding: 0px;\n"
"    	border: 0px solid rgba(0,0,0,0);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   	subcontrol-origin: margin;\n"
"    	subcontrol-position: left;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: right;\n"
"	border-bottom-right-ra"
                        "dius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_left_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_left_red.svg\")\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_right_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_right_red.svg\")\n"
"}")
        self.layer_header_exp_add_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.layer_header_exp_add_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.layer_header_exp_add_wrapper.setLineWidth(0)
        self.layer_header_exp_add_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layer_header_exp_add_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layer_header_exp_add_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.layer_header_exp_add_wrapper.setWidgetResizable(True)
        self.layer_header_exp_add = QWidget()
        self.layer_header_exp_add.setObjectName(u"layer_header_exp_add")
        self.layer_header_exp_add.setGeometry(QRect(0, 0, 247, 40))
        self.layer_header_exp_add.setMinimumSize(QSize(190, 0))
        self.layer_header_exp_add.setMaximumSize(QSize(16777215, 40))
        self.layer_header_exp_add_container = QHBoxLayout(self.layer_header_exp_add)
        self.layer_header_exp_add_container.setSpacing(10)
        self.layer_header_exp_add_container.setObjectName(u"layer_header_exp_add_container")
        self.layer_header_exp_add_container.setContentsMargins(0, 0, 0, 0)
        self.layer_add_task_button = QPushButton(self.layer_header_exp_add)
        self.layer_add_task_button.setObjectName(u"layer_add_task_button")
        self.layer_add_task_button.setMinimumSize(QSize(90, 40))
        self.layer_add_task_button.setMaximumSize(QSize(90, 40))
        self.layer_add_task_button.setFont(font4)
        icon29 = QIcon()
        icon29.addFile(u":/icons/calendar/events/description/description_add_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon29.addFile(u":/icons/calendar/events/description/description_add_blue.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon29.addFile(u":/icons/calendar/events/description/description_add_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.layer_add_task_button.setIcon(icon29)
        self.layer_add_task_button.setIconSize(QSize(20, 20))
        self.layer_add_task_button.setCheckable(True)
        self.layer_add_task_button.setAutoExclusive(False)

        self.layer_header_exp_add_container.addWidget(self.layer_add_task_button)

        self.layer_add_note_button = QPushButton(self.layer_header_exp_add)
        self.layer_add_note_button.setObjectName(u"layer_add_note_button")
        self.layer_add_note_button.setMinimumSize(QSize(90, 40))
        self.layer_add_note_button.setMaximumSize(QSize(90, 40))
        self.layer_add_note_button.setFont(font4)
        icon30 = QIcon()
        icon30.addFile(u":/icons/calendar/events/todo/todo_add_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon30.addFile(u":/icons/calendar/events/todo/todo_add_green.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.layer_add_note_button.setIcon(icon30)
        self.layer_add_note_button.setIconSize(QSize(20, 20))
        self.layer_add_note_button.setCheckable(True)
        self.layer_add_note_button.setAutoExclusive(False)

        self.layer_header_exp_add_container.addWidget(self.layer_add_note_button)

        self.layer_add_options_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layer_header_exp_add_container.addItem(self.layer_add_options_spacer)

        self.layer_header_exp_add_wrapper.setWidget(self.layer_header_exp_add)

        self.layer_header_expanded_container.addWidget(self.layer_header_exp_add_wrapper)


        self.layer_edit_container.addWidget(self.layer_header_expanded)

        self.layer_view_display_ebody = EBodySingleDisplay(self.layer_edit)
        self.layer_view_display_ebody.setObjectName(u"layer_view_display_ebody")
        self.layer_view_display_ebody.setMinimumSize(QSize(0, 0))

        self.layer_edit_container.addWidget(self.layer_view_display_ebody)

        self.layer_object_edit = QWidget(self.layer_edit)
        self.layer_object_edit.setObjectName(u"layer_object_edit")
        sizePolicy2.setHeightForWidth(self.layer_object_edit.sizePolicy().hasHeightForWidth())
        self.layer_object_edit.setSizePolicy(sizePolicy2)
        self.layer_object_edit.setMinimumSize(QSize(247, 0))
        self.layer_object_edit.setMaximumSize(QSize(290, 16777215))
        self.layer_object_edit_container = QVBoxLayout(self.layer_object_edit)
        self.layer_object_edit_container.setSpacing(10)
        self.layer_object_edit_container.setObjectName(u"layer_object_edit_container")
        self.layer_object_edit_container.setContentsMargins(1, 0, 1, 0)
        self.layer_current_label = QLabel(self.layer_object_edit)
        self.layer_current_label.setObjectName(u"layer_current_label")
        sizePolicy2.setHeightForWidth(self.layer_current_label.sizePolicy().hasHeightForWidth())
        self.layer_current_label.setSizePolicy(sizePolicy2)
        self.layer_current_label.setMinimumSize(QSize(248, 30))
        self.layer_current_label.setMaximumSize(QSize(16777215, 30))
        self.layer_current_label.setFont(font6)
        self.layer_current_label.setLineWidth(0)

        self.layer_object_edit_container.addWidget(self.layer_current_label)

        self.layer_obj_edit_task_form = QWidget(self.layer_object_edit)
        self.layer_obj_edit_task_form.setObjectName(u"layer_obj_edit_task_form")
        self.layer_obj_edit_task_form.setMinimumSize(QSize(252, 82))
        self.layer_obj_edit_task_form.setMaximumSize(QSize(290, 82))
        self.layer_obj_edit_task_form.setStyleSheet(u"QWidget#layer_obj_edit_task_form {\n"
"	background-color: rgba(20,20,20,1);\n"
"	border-radius: 4px;\n"
"	border: 2px solid rgba(80, 160, 100, 1);\n"
"}\n"
"\n"
"QWidget#layer_obj_edit_task_form > * {\n"
"	border-radius: 0px;\n"
"	border: 0px;\n"
"}")
        self.layer_obj_edit_task_form_container = QVBoxLayout(self.layer_obj_edit_task_form)
        self.layer_obj_edit_task_form_container.setSpacing(0)
        self.layer_obj_edit_task_form_container.setObjectName(u"layer_obj_edit_task_form_container")
        self.layer_obj_edit_task_form_container.setContentsMargins(2, 0, 2, 0)
        self.layer_task_edit_header = QWidget(self.layer_obj_edit_task_form)
        self.layer_task_edit_header.setObjectName(u"layer_task_edit_header")
        sizePolicy4.setHeightForWidth(self.layer_task_edit_header.sizePolicy().hasHeightForWidth())
        self.layer_task_edit_header.setSizePolicy(sizePolicy4)
        self.layer_task_edit_header.setMinimumSize(QSize(0, 44))
        self.layer_task_edit_header.setMaximumSize(QSize(290, 44))
        self.layer_task_edit_header.setStyleSheet(u"border-bottom: 2px solid rgba(80, 160, 100, 1);")
        self.task_edit_header_container = QHBoxLayout(self.layer_task_edit_header)
        self.task_edit_header_container.setSpacing(0)
        self.task_edit_header_container.setObjectName(u"task_edit_header_container")
        self.task_edit_header_container.setContentsMargins(0, 0, 0, 0)
        self.task_line_edit = QLineEdit(self.layer_task_edit_header)
        self.task_line_edit.setObjectName(u"task_line_edit")
        sizePolicy11.setHeightForWidth(self.task_line_edit.sizePolicy().hasHeightForWidth())
        self.task_line_edit.setSizePolicy(sizePolicy11)
        self.task_line_edit.setMinimumSize(QSize(212, 40))
        self.task_line_edit.setMaximumSize(QSize(250, 40))
        self.task_line_edit.setFont(font7)
        self.task_line_edit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.task_line_edit.setStyleSheet(u"QLineEdit {\n"
"	border: 0px solid transparent;\n"
"	padding-left: 5px;\n"
"	border-top-left-radius: 0px;\n"
"}")
        self.task_line_edit.setClearButtonEnabled(True)

        self.task_edit_header_container.addWidget(self.task_line_edit)

        self.task_checkbox = QCheckBox(self.layer_task_edit_header)
        self.task_checkbox.setObjectName(u"task_checkbox")
        self.task_checkbox.setMinimumSize(QSize(0, 40))
        self.task_checkbox.setMaximumSize(QSize(40, 40))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(19)
        self.task_checkbox.setFont(font8)
        self.task_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.task_checkbox.setStyleSheet(u"QCheckBox {\n"
"border-bottom: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	height: 36px; width: 36px;\n"
"}")
        self.task_checkbox.setIconSize(QSize(30, 30))
        self.task_checkbox.setChecked(False)
        self.task_checkbox.setTristate(False)

        self.task_edit_header_container.addWidget(self.task_checkbox)


        self.layer_obj_edit_task_form_container.addWidget(self.layer_task_edit_header)

        self.layer_task_edit_footer = QWidget(self.layer_obj_edit_task_form)
        self.layer_task_edit_footer.setObjectName(u"layer_task_edit_footer")
        self.layer_task_edit_footer.setMinimumSize(QSize(248, 40))
        self.layer_task_edit_footer.setMaximumSize(QSize(290, 40))
        self.layer_task_edit_footer.setStyleSheet(u"background-color: rgba(20,20,20,1);\n"
"margin: 2px;\n"
"padding: 4px;\n"
"border-radius: 5px;")
        self.task_edit_footer_container = QHBoxLayout(self.layer_task_edit_footer)
        self.task_edit_footer_container.setSpacing(0)
        self.task_edit_footer_container.setObjectName(u"task_edit_footer_container")
        self.task_edit_footer_container.setContentsMargins(0, 0, 0, 0)
        self.task_edit_footer_spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.task_edit_footer_container.addItem(self.task_edit_footer_spacer)

        self.task_edit_confirm = QPushButton(self.layer_task_edit_footer)
        self.task_edit_confirm.setObjectName(u"task_edit_confirm")
        sizePolicy6.setHeightForWidth(self.task_edit_confirm.sizePolicy().hasHeightForWidth())
        self.task_edit_confirm.setSizePolicy(sizePolicy6)
        self.task_edit_confirm.setMinimumSize(QSize(90, 40))
        self.task_edit_confirm.setMaximumSize(QSize(90, 40))
        self.task_edit_confirm.setFont(font4)
        self.task_edit_confirm.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(30, 30, 30, 1);\n"
"    border: 1px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"                           \n"
"QPushButton:pressed {\n"
"    /* Pressed state */\n"
"    background: rgba(140, 255, 140, 1);\n"
"}")
        self.task_edit_confirm.setIconSize(QSize(20, 20))
        self.task_edit_confirm.setCheckable(True)

        self.task_edit_footer_container.addWidget(self.task_edit_confirm)

        self.task_keyboard_button = QPushButton(self.layer_task_edit_footer)
        self.task_keyboard_button.setObjectName(u"task_keyboard_button")
        sizePolicy13.setHeightForWidth(self.task_keyboard_button.sizePolicy().hasHeightForWidth())
        self.task_keyboard_button.setSizePolicy(sizePolicy13)
        self.task_keyboard_button.setMinimumSize(QSize(40, 40))
        self.task_keyboard_button.setMaximumSize(QSize(40, 40))
        self.task_keyboard_button.setStyleSheet(u"border-left: 1px solid white;\n"
"border-radius: 0px;")
        icon31 = QIcon()
        icon31.addFile(u":/icons/util/keyboard_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon31.addFile(u":/icons/util/keyboard_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon31.addFile(u":/icons/util/keyboard_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon31.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon31.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon31.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon31.addFile(u":/icons/util/keyboard_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.task_keyboard_button.setIcon(icon31)
        self.task_keyboard_button.setIconSize(QSize(30, 30))

        self.task_edit_footer_container.addWidget(self.task_keyboard_button)


        self.layer_obj_edit_task_form_container.addWidget(self.layer_task_edit_footer)


        self.layer_object_edit_container.addWidget(self.layer_obj_edit_task_form)

        self.layer_obj_edit_note_form = QWidget(self.layer_object_edit)
        self.layer_obj_edit_note_form.setObjectName(u"layer_obj_edit_note_form")
        self.layer_obj_edit_note_form.setMinimumSize(QSize(247, 280))
        self.layer_obj_edit_note_form.setMaximumSize(QSize(16777215, 280))
        self.layer_obj_edit_note_form_container = QVBoxLayout(self.layer_obj_edit_note_form)
        self.layer_obj_edit_note_form_container.setSpacing(10)
        self.layer_obj_edit_note_form_container.setObjectName(u"layer_obj_edit_note_form_container")
        self.layer_obj_edit_note_form_container.setContentsMargins(0, 0, 0, 0)
        self.layer_note_edit_header_wrapper = QScrollArea(self.layer_obj_edit_note_form)
        self.layer_note_edit_header_wrapper.setObjectName(u"layer_note_edit_header_wrapper")
        sizePolicy4.setHeightForWidth(self.layer_note_edit_header_wrapper.sizePolicy().hasHeightForWidth())
        self.layer_note_edit_header_wrapper.setSizePolicy(sizePolicy4)
        self.layer_note_edit_header_wrapper.setMinimumSize(QSize(247, 40))
        self.layer_note_edit_header_wrapper.setMaximumSize(QSize(290, 70))
        self.layer_note_edit_header_wrapper.setStyleSheet(u"QScrollBar:horizontal {\n"
"   	background: rgba(40,40,40,0.9);\n"
"    	height: 20px;\n"
"	padding: 0px 25px\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgba(120,120,120,1);\n"
"	min-width: 50px;\n"
"	min-height: 20px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::groove:horizontal {\n"
"    background: transparent;\n"
"    height: 20px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal, QScrollBar::add-page:horizontal {\n"
"    background: rgba(40,40,40,1);\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    	background: rgba(20,20,20,1);\n"
"    	width: 25px;\n"
"	padding: 0px;\n"
"    	border: 0px solid rgba(0,0,0,0);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   	subcontrol-origin: margin;\n"
"    	subcontrol-position: left;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-top-left-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: right;\n"
"	border-bottom-right-ra"
                        "dius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_left_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_left_red.svg\")\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"	image: url(\":/icons/arrows/arrow_right_dark.svg\");\n"
"	width: 20px;\n"
"	height: 20px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"	image: url(\":/icons/arrows/arrow_right_red.svg\")\n"
"}")
        self.layer_note_edit_header_wrapper.setFrameShape(QFrame.Shape.NoFrame)
        self.layer_note_edit_header_wrapper.setFrameShadow(QFrame.Shadow.Plain)
        self.layer_note_edit_header_wrapper.setLineWidth(0)
        self.layer_note_edit_header_wrapper.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.layer_note_edit_header_wrapper.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.layer_note_edit_header_wrapper.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.layer_note_edit_header_wrapper.setWidgetResizable(True)
        self.note_edit_header = QWidget()
        self.note_edit_header.setObjectName(u"note_edit_header")
        self.note_edit_header.setGeometry(QRect(0, 0, 340, 40))
        sizePolicy2.setHeightForWidth(self.note_edit_header.sizePolicy().hasHeightForWidth())
        self.note_edit_header.setSizePolicy(sizePolicy2)
        self.note_edit_header.setMinimumSize(QSize(0, 40))
        self.note_edit_header.setMaximumSize(QSize(16777215, 40))
        self.note_edit_header_container = QHBoxLayout(self.note_edit_header)
        self.note_edit_header_container.setSpacing(10)
        self.note_edit_header_container.setObjectName(u"note_edit_header_container")
        self.note_edit_header_container.setContentsMargins(0, 0, 0, 10)
        self.bold_selected = QPushButton(self.note_edit_header)
        self.bold_selected.setObjectName(u"bold_selected")
        self.bold_selected.setMinimumSize(QSize(90, 40))
        self.bold_selected.setMaximumSize(QSize(90, 40))
        self.bold_selected.setFont(font4)
        icon32 = QIcon()
        icon32.addFile(u":/icons/util/text/text_bold_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon32.addFile(u":/icons/util/text/text_bold_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.bold_selected.setIcon(icon32)
        self.bold_selected.setIconSize(QSize(20, 20))

        self.note_edit_header_container.addWidget(self.bold_selected)

        self.underline_selected = QPushButton(self.note_edit_header)
        self.underline_selected.setObjectName(u"underline_selected")
        self.underline_selected.setMinimumSize(QSize(120, 40))
        self.underline_selected.setMaximumSize(QSize(120, 40))
        self.underline_selected.setFont(font4)
        icon33 = QIcon()
        icon33.addFile(u":/icons/util/text/text_underline_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon33.addFile(u":/icons/util/text/text_underline_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.underline_selected.setIcon(icon33)
        self.underline_selected.setIconSize(QSize(20, 20))

        self.note_edit_header_container.addWidget(self.underline_selected)

        self.italicise_selected = QPushButton(self.note_edit_header)
        self.italicise_selected.setObjectName(u"italicise_selected")
        self.italicise_selected.setMinimumSize(QSize(110, 40))
        self.italicise_selected.setMaximumSize(QSize(110, 40))
        self.italicise_selected.setFont(font4)
        icon34 = QIcon()
        icon34.addFile(u":/icons/util/text/text_italic_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon34.addFile(u":/icons/util/text/text_italic_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.italicise_selected.setIcon(icon34)
        self.italicise_selected.setIconSize(QSize(20, 20))

        self.note_edit_header_container.addWidget(self.italicise_selected)

        self.layer_note_edit_header_wrapper.setWidget(self.note_edit_header)

        self.layer_obj_edit_note_form_container.addWidget(self.layer_note_edit_header_wrapper)

        self.layer_note_text_edit = QTextEdit(self.layer_obj_edit_note_form)
        self.layer_note_text_edit.setObjectName(u"layer_note_text_edit")
        sizePolicy6.setHeightForWidth(self.layer_note_text_edit.sizePolicy().hasHeightForWidth())
        self.layer_note_text_edit.setSizePolicy(sizePolicy6)
        self.layer_note_text_edit.setMinimumSize(QSize(247, 150))
        self.layer_note_text_edit.setMaximumSize(QSize(290, 150))
        self.layer_note_text_edit.setFont(font4)
        self.layer_note_text_edit.setStyleSheet(u"QTextEdit{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(30,30,30,1);\n"
"	border: 2px solid rgba(75,150,255,1);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border-left: 2px solid rgba(70,150,255,1);\n"
"    background: rgba(40,40,40,0.9);\n"
"    width:  24px;\n"
"    padding: 25px 0;\n"
"}\n"
"\n"
"QScrollBar::groove:vertical {\n"
"    background: transparent;\n"
"    width: 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    	background: rgba(120,120,120,1);\n"
"    	min-height: 50px;\n"
"	min-width: 20px;\n"
"	max-width: 20px;\n"
"    	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {\n"
"    	background: rgba(40,40,40,1);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"    	width: 20px;\n"
"    	height: 25px;             \n"
"    	background: rgba(20,20,20,1);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    	subcontrol-origin: margin;\n"
"    	subcontrol-position: top;\n"
"    	border-top-left-radius: 4px;\n"
""
                        "    	border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: bottom;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"    image: url(\":/icons/arrows/arrow_up_dark.svg\");\n"
"    width:  20px;   height: 20px;\n"
"}\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"    image: url(\":/icons/arrows/arrow_up_blue.svg\");\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    image: url(\":/icons/arrows/arrow_down_dark.svg\");\n"
"    width:  20px;   height: 20px;\n"
"}\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"    image: url(\":/icons/arrows/arrow_down_blue.svg\");\n"
"}\n"
"")
        self.layer_note_text_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self.layer_note_text_edit.setFrameShadow(QFrame.Shadow.Plain)
        self.layer_note_text_edit.setLineWidth(0)
        self.layer_note_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.layer_note_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.layer_note_text_edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.layer_note_text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)

        self.layer_obj_edit_note_form_container.addWidget(self.layer_note_text_edit)

        self.layer_note_edit_footer = QWidget(self.layer_obj_edit_note_form)
        self.layer_note_edit_footer.setObjectName(u"layer_note_edit_footer")
        sizePolicy6.setHeightForWidth(self.layer_note_edit_footer.sizePolicy().hasHeightForWidth())
        self.layer_note_edit_footer.setSizePolicy(sizePolicy6)
        self.layer_note_edit_footer.setMinimumSize(QSize(252, 40))
        self.layer_note_edit_footer.setMaximumSize(QSize(16777215, 40))
        self.note_edit_footer_container = QHBoxLayout(self.layer_note_edit_footer)
        self.note_edit_footer_container.setSpacing(10)
        self.note_edit_footer_container.setObjectName(u"note_edit_footer_container")
        self.note_edit_footer_container.setContentsMargins(0, 0, 0, 0)
        self.undo_button = QPushButton(self.layer_note_edit_footer)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setMinimumSize(QSize(40, 40))
        self.undo_button.setMaximumSize(QSize(40, 40))
        self.undo_button.setFont(font4)
        icon35 = QIcon()
        icon35.addFile(u":/icons/arrows/arrow_redo_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon35.addFile(u":/icons/arrows/arrow_redo_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon35.addFile(u":/icons/arrows/arrow_redo_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon35.addFile(u":/icons/arrows/arrow_redo_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.undo_button.setIcon(icon35)
        self.undo_button.setIconSize(QSize(20, 20))

        self.note_edit_footer_container.addWidget(self.undo_button)

        self.redo_button = QPushButton(self.layer_note_edit_footer)
        self.redo_button.setObjectName(u"redo_button")
        self.redo_button.setMinimumSize(QSize(40, 40))
        self.redo_button.setMaximumSize(QSize(40, 40))
        self.redo_button.setFont(font4)
        icon36 = QIcon()
        icon36.addFile(u":/icons/arrows/arrow_undo_grey.svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon36.addFile(u":/icons/arrows/arrow_undo_blue.svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon36.addFile(u":/icons/arrows/arrow_undo_blue.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        self.redo_button.setIcon(icon36)
        self.redo_button.setIconSize(QSize(20, 20))

        self.note_edit_footer_container.addWidget(self.redo_button)

        self.note_edit_footer_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.note_edit_footer_container.addItem(self.note_edit_footer_spacer)

        self.note_edit_confirm = QPushButton(self.layer_note_edit_footer)
        self.note_edit_confirm.setObjectName(u"note_edit_confirm")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(40)
        sizePolicy14.setHeightForWidth(self.note_edit_confirm.sizePolicy().hasHeightForWidth())
        self.note_edit_confirm.setSizePolicy(sizePolicy14)
        self.note_edit_confirm.setMinimumSize(QSize(90, 40))
        self.note_edit_confirm.setMaximumSize(QSize(90, 40))
        self.note_edit_confirm.setFont(font4)
        self.note_edit_confirm.setIconSize(QSize(20, 20))

        self.note_edit_footer_container.addWidget(self.note_edit_confirm)


        self.layer_obj_edit_note_form_container.addWidget(self.layer_note_edit_footer)


        self.layer_object_edit_container.addWidget(self.layer_obj_edit_note_form)


        self.layer_edit_container.addWidget(self.layer_object_edit)


        self.layer_container.addWidget(self.layer_edit)

        self.layer_view = QWidget(self.layer)
        self.layer_view.setObjectName(u"layer_view")
        self.layer_view.setMinimumSize(QSize(248, 0))
        self.layer_view.setMaximumSize(QSize(290, 16777215))
        self.layer_view.setAutoFillBackground(False)
        self.layer_view_container = QVBoxLayout(self.layer_view)
        self.layer_view_container.setSpacing(10)
        self.layer_view_container.setObjectName(u"layer_view_container")
        self.layer_view_container.setContentsMargins(0, 0, 0, 0)
        self.layer_view_empty_label = QLabel(self.layer_view)
        self.layer_view_empty_label.setObjectName(u"layer_view_empty_label")
        self.layer_view_empty_label.setMinimumSize(QSize(80, 50))
        self.layer_view_empty_label.setFont(font)
        self.layer_view_empty_label.setStyleSheet(u"border: 2px solid rgba(120,120,120,1);\n"
"border-radius: 7px;")
        self.layer_view_empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layer_view_container.addWidget(self.layer_view_empty_label)

        self.layer_view_list_ebody = EBody(self.layer_view)
        self.layer_view_list_ebody.setObjectName(u"layer_view_list_ebody")
        self.layer_view_list_ebody.setMinimumSize(QSize(0, 50))

        self.layer_view_container.addWidget(self.layer_view_list_ebody)


        self.layer_container.addWidget(self.layer_view)


        self.details_form_container.setWidget(3, QFormLayout.ItemRole.FieldRole, self.layer)

        self.form_wrapper.setWidget(self.details_form)

        self.page_details_container.addWidget(self.form_wrapper)

        self.details_container.addWidget(self.page_details)

        self.event_view_container.addWidget(self.details_container)


        self.retranslateUi(event_view)
        self.time_button.toggled.connect(self.time_view.setHidden)
        self.time_button.toggled.connect(self.time_edit.setVisible)
        self.layer_button.toggled.connect(self.layer_view.setHidden)
        self.layer_button.toggled.connect(self.layer_edit.setVisible)
        self.layer_view_list_ebody.hasItems.connect(self.layer_view_empty_label.setHidden)
        self.layer_view_list_ebody.hasItems.connect(self.layer_view_list_ebody.setVisible)
        self.layer_add_button.toggled.connect(self.layer_header_expanded.setVisible)
        self.layer_add_button.toggled.connect(self.layer_header_exp_add_wrapper.setVisible)
        self.layer_finish_button.toggled.connect(self.layer_header_exp_finish.setVisible)
        self.layer_add_note_button.toggled.connect(self.layer_obj_edit_task_form.setVisible)
        self.layer_add_task_button.toggled.connect(self.layer_obj_edit_note_form.setVisible)
        self.layer_add_task_button.toggled.connect(self.layer_object_edit.setVisible)
        self.layer_add_note_button.toggled.connect(self.layer_object_edit.setVisible)
        self.undo_button.clicked.connect(self.layer_note_text_edit.undo)
        self.redo_button.clicked.connect(self.layer_note_text_edit.redo)
        self.note_edit_confirm.clicked.connect(self.layer_add_note_button.toggle)
        self.title_edit_button.toggled.connect(self.title_edit.setVisible)
        self.title_line_edit.returnPressed.connect(self.title_edit_button.toggle)
        self.title_edit_button.toggled.connect(self.title_view.setHidden)
        self.title_line_edit.textChanged.connect(self.title_label.setText)
        self.layer_finish_button.toggled.connect(self.layer_header_expanded.setVisible)
        self.simple_button.toggled.connect(self.layer_button.setHidden)
        self.simple_button.toggled.connect(self.layer.setHidden)
        self.task_button.toggled.connect(self.layer_add_button.setHidden)
        self.task_button.toggled.connect(self.layer_remove_button.setHidden)
        self.note_button.toggled.connect(self.layer_add_button.setHidden)
        self.note_button.toggled.connect(self.layer_remove_button.setHidden)
        self.layer_add_button.toggled.connect(self.layer_object_edit.hide)
        self.task_edit_confirm.clicked.connect(self.layer_add_note_button.toggle)
        self.note_button.toggled.connect(self.spacer_widget.setVisible)
        self.task_button.toggled.connect(self.spacer_widget.setVisible)
        self.complex_button.toggled.connect(self.spacer_widget.setHidden)
        self.task_button.toggled.connect(self.location_button.setHidden)
        self.task_button.toggled.connect(self.location.setHidden)
        self.note_button.toggled.connect(self.location.setHidden)
        self.note_button.toggled.connect(self.location_button.setHidden)
        self.simple_button.toggled.connect(self.location.setVisible)
        self.simple_button.toggled.connect(self.location_button.setVisible)
        self.complex_button.toggled.connect(self.location.setVisible)
        self.complex_button.toggled.connect(self.location_button.setVisible)
        self.layer_finish_button.toggled.connect(self.layer_header_exp_add_wrapper.setHidden)
        self.layer_add_button.toggled.connect(self.layer_header_exp_finish.setHidden)
        self.location_button.toggled.connect(self.location_edit_combobox.setHidden)
        self.location_button.toggled.connect(self.location_view_expanded.setHidden)
        self.location_button.toggled.connect(self.location_view_collapsed.setVisible)
        self.location_expand_button.toggled.connect(self.location_view_expanded.setVisible)
        self.location_expand_button.toggled.connect(self.location_view_collapsed.setHidden)
        self.location_finish_button.toggled.connect(self.location_expand_button.toggle)
        self.location_edit_button.clicked["bool"].connect(self.location_view_expanded.hide)
        self.location_edit_combobox.currentIndexChanged.connect(self.location_view_expanded.show)
        self.layer_finish_button.toggled.connect(self.layer_object_edit.hide)
        self.time_start_select.dateTimeChanged.connect(self.time_end_select.setMinimumDateTime)

        self.details_container.setCurrentIndex(3)
        self.preset_button.setDefault(False)
        self.simple_button.setDefault(False)
        self.save_button.setDefault(False)


        QMetaObject.connectSlotsByName(event_view)
    # setupUi

    def retranslateUi(self, event_view):
        event_view.setWindowTitle(QCoreApplication.translate("event_view", u"Form", None))
        self.prev_day.setText("")
        self.next_day.setText("")
        self.date_label.setText(QCoreApplication.translate("event_view", u"TextLabel", None))
        self.calendar_view.setText("")
        self.filter_button.setText("")
        self.user1.setText(QCoreApplication.translate("event_view", u"user1", None))
        self.user2.setText(QCoreApplication.translate("event_view", u"user2", None))
        self.user3.setText(QCoreApplication.translate("event_view", u"user3", None))
        self.printsql.setText(QCoreApplication.translate("event_view", u"proposedSQL", None))
        self.load.setText(QCoreApplication.translate("event_view", u"PushButton", None))
        self.next.setText(QCoreApplication.translate("event_view", u"next", None))
        self.prev.setText(QCoreApplication.translate("event_view", u"prev", None))
        self.add_event_button.setText("")
        self.cancel_button.setText("")
        self.title_label.setText(QCoreApplication.translate("event_view", u"Event", None))
        self.title_edit_button.setText("")
        self.title_line_edit.setText("")
        self.title_line_edit.setPlaceholderText(QCoreApplication.translate("event_view", u"Title", None))
        self.title_keyboard_button.setText("")
        self.preset_button.setText("")
        self.note_button.setText(QCoreApplication.translate("event_view", u"Note", None))
        self.task_button.setText(QCoreApplication.translate("event_view", u"Task", None))
        self.simple_button.setText(QCoreApplication.translate("event_view", u"Simple", None))
        self.complex_button.setText(QCoreApplication.translate("event_view", u"Complex", None))
        self.time_button.setText("")
        self.time_allday_label.setText(QCoreApplication.translate("event_view", u"All-day", None))
        self.time_start_label.setText(QCoreApplication.translate("event_view", u"Starts", None))
        self.time_end_label.setText(QCoreApplication.translate("event_view", u"Ends", None))
        self.time_schedule_label.setText(QCoreApplication.translate("event_view", u"Schedule", None))
        self.time_allday_checkbox.setText("")
        self.time_schedule_label_button.setText(QCoreApplication.translate("event_view", u" Add schedule", None))
        self.layer_button.setText("")
        self.location_button.setText("")
        self.invitees_button.setText("")
        self.tags_button.setText("")
        self.save_button.setText(QCoreApplication.translate("event_view", u"Save", None))
        self.loc_view_col_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.location_expand_button.setText("")
        self.loc_address_line_1_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.loc_address_line_2_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.loc_address_line_3_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.loc_county_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.loc_city_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.loc_postcode_label.setText(QCoreApplication.translate("event_view", u"None", None))
        self.location_finish_button.setText("")
        self.location_edit_button.setText("")
        self.location_edit_combobox.setCurrentText("")
        self.location_edit_combobox.setPlaceholderText(QCoreApplication.translate("event_view", u"Address...", None))
        self.layers_header.setText(QCoreApplication.translate("event_view", u"Layers", None))
        self.layer_finish_button.setText(QCoreApplication.translate("event_view", u"Finish", None))
        self.layer_add_button.setText(QCoreApplication.translate("event_view", u"Add", None))
        self.layer_remove_button.setText(QCoreApplication.translate("event_view", u"Remove", None))
        self.layer_edit_button.setText(QCoreApplication.translate("event_view", u"Edit", None))
        self.layer_save_changes_button.setText(QCoreApplication.translate("event_view", u"Save", None))
        self.layer_cancel_changes_button.setText(QCoreApplication.translate("event_view", u"Cancel", None))
        self.layer_add_task_button.setText(QCoreApplication.translate("event_view", u"Note", None))
        self.layer_add_note_button.setText(QCoreApplication.translate("event_view", u"Task", None))
        self.layer_current_label.setText(QCoreApplication.translate("event_view", u"Currently editing:", None))
        self.task_line_edit.setText("")
        self.task_line_edit.setPlaceholderText(QCoreApplication.translate("event_view", u"Task", None))
        self.task_checkbox.setText("")
        self.task_edit_confirm.setText(QCoreApplication.translate("event_view", u"Confirm", None))
        self.task_keyboard_button.setText("")
        self.bold_selected.setText(QCoreApplication.translate("event_view", u"Bold", None))
        self.underline_selected.setText(QCoreApplication.translate("event_view", u"Underline", None))
        self.italicise_selected.setText(QCoreApplication.translate("event_view", u"Italicise", None))
        self.layer_note_text_edit.setPlaceholderText(QCoreApplication.translate("event_view", u"Enter your note here...", None))
        self.undo_button.setText("")
        self.redo_button.setText("")
        self.note_edit_confirm.setText(QCoreApplication.translate("event_view", u"Confirm", None))
        self.layer_view_empty_label.setText(QCoreApplication.translate("event_view", u"No objects", None))
    # retranslateUi

