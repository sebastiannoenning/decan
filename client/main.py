# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication

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