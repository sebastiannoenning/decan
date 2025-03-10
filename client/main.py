# This Python file uses the following encoding: utf-8
import os
import sys

# Get the project root (assuming client is directly under the root)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic main_window.ui -o ui_main_window.py, or
#     pyside2-uic main_window.ui -o ui_main_window.py
from views.main_window import MainWindow

class decan(QApplication):
    def __init__(self, sys_arg):
        super(decan, self).__init__(sys_arg)
        self.main_view = MainWindow()
        self.main_view.show()

if __name__ == "__main__":
    app = decan(sys.argv)
    sys.exit(app.exec())