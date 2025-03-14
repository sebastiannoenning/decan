# This Python file uses the following encoding: utf-8
import os
import sys

# Get the project root (assuming client is directly under the root)
"""project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)"""

from PySide6.QtWidgets import QApplication, QMainWindow

from views.main_view import MainView

class decan(QApplication):
    def __init__(self, sys_arg):
        super(decan, self).__init__(sys_arg)
        self.main_view = MainView()
        self.main_view.show()

if __name__ == "__main__":
    app = decan(sys.argv)
    app.setStyle("Fusion")
    sys.exit(app.exec())