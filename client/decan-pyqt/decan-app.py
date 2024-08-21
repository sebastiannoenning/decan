# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

from views.main_window import MainWindow


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        #self.main_model() = Model()
        #self.main_controller = MainController(self.model)
        self.main_view = MainWindow()#self.main_model, self.main_controller)
        self.main_view.show()
        #self load ui components


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
    