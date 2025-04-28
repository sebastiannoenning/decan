# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic --from-imports resources/ui/main_view.ui -o client/views/main_view_ui.py

from .main_view_ui import Ui_main_view
from .pages.user_view import UserView
from .pages.event_view import EventView


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_main_view()
        self._ui.setupUi(self)
        self._ui.collapsed.hide()

        self.setup_connections()

        self._ui.pages.addWidget(UserView(self))
        self._ui.pages.addWidget(EventView(self))

    def setup_connections(self):
        self._ui.col_toggle.clicked.connect(lambda: self.toggle_nav())
        self._ui.exp_toggle.clicked.connect(lambda: self.toggle_nav())

        self._ui.exp_p1_user.clicked.connect(lambda: self._ui.pages.setCurrentIndex(0))
        self._ui.exp_p3_events.clicked.connect(lambda: self._ui.pages.setCurrentIndex(1))

        self._ui.col_p1_user.clicked.connect(lambda: self._ui.pages.setCurrentIndex(0))
        self._ui.col_p3_events.clicked.connect(lambda: self._ui.pages.setCurrentIndex(1))

        self._ui.col_p4_pref.clicked.connect(lambda: print(f"""
            Family: {self._ui.col_p4_pref.fontInfo().family()}
            PixelSize: {self._ui.col_p4_pref.fontInfo().pixelSize()}
            PointSize: {self._ui.col_p4_pref.fontInfo().pointSize()}
            WidgetSize: {self._ui.col_p4_pref.size()}
            """)
                                             )

    def toggle_nav(self):
        if self._ui.collapsed.isVisible():
            self._ui.expanded.show()
            self._ui.collapsed.hide()
        else:
            self._ui.collapsed.show()
            self._ui.expanded.hide()
