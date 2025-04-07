from PySide6 import QtCore
from PySide6.QtWidgets import QWidget


# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/pages/user_view.ui -o client/views/pages/user_view_ui.py, or
#       pyside6-uic --from-imports pages/user_view.ui -o ../client/views/pages/user_view_ui.py
#       
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o resources/assets/rss.py
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py 

from .user_view_ui import Ui_user_view
from modules.touchdatetime.tdateedit import DateSelect

class UserView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_user_view()
        self._ui.setupUi(self)