
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal, QSize, QByteArray, QModelIndex
from PySide6.QtWidgets import (QWidget, QPushButton, QGridLayout, QDataWidgetMapper,
                               QGraphicsView, QGraphicsWidget, QGraphicsScene,
                               QDialog)
from PySide6.QtGui import QIcon, QPixmap, QValidator
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtSql import QSqlDatabase

# Important:
# You need to run the following command to generate the ui_form.py file
#       pyside6-uic --from-imports resources/ui/pages/user_view.ui -o client/views/pages/user_view_ui.py, or
#       pyside6-uic --from-imports pages/user_view.ui -o ../client/views/pages/user_view_ui.py
#       
# For icons:
#       pyside6-rcc resources/assets/rss.qrc -o resources/assets/rss.py
#       pyside6-rcc resources/assets/rss.qrc -o client/views/rss_rc.py 

from .user_view_ui import Ui_user_view
from models.user_model import UserModel
from modules.touchdatetime.tdateedit import DateSelect
from views.dialogs.icon_picker_dialog import IconPicker
from client.modules.validators_qt import PasswordValidator, UsernameValidator

from views import rss_rc

class UserView(QWidget):

    userChanged = Signal(QModelIndex)

    def __init__(self, parent, db: QSqlDatabase):
        super().__init__(parent)
        self._database = db

        self._Ui = Ui_user_view()
        self._Ui.setupUi(self)

        self.cur_iconpicker = IconPicker(self)
        self.cur_scene = QGraphicsScene(self)
        self.cur_svg_renderer = QSvgRenderer()
        self.cur_svg = QGraphicsSvgItem()

        self.new_iconpicker = IconPicker(self)
        self.new_scene = QGraphicsScene(self)
        self.new_svg_renderer = QSvgRenderer()
        self.new_svg = QGraphicsSvgItem()

        self.usermodel = UserModel(self, db=self._database)

        self.usermapper = QDataWidgetMapper(self)
        self.userprofilemapper = QDataWidgetMapper(self)

        self._Ui.user_list.setModel(self.usermodel)

        self.usermodel.select()

        self.setupConnections()

    def setupConnections(self):
        self._Ui.new_icon_change_pushbutton.toggled.connect(lambda toggled: self._openDialog(toggled, self.new_iconpicker))
        self.new_iconpicker.iconSelected.connect(lambda file_name: self.setIconInView(file_name,
                                                                                      self.new_svg_renderer,
                                                                                      self.new_svg,
                                                                                      self.new_scene,
                                                                                      self._Ui.new_icon_view))
        self.new_svg.setSharedRenderer(self.new_svg_renderer)
        self._Ui.new_icon_view.setScene(self.new_scene)
        self.new_iconpicker.accepted.connect(lambda: self._Ui.new_icon_change_pushbutton.toggle())

        self._Ui.cur_icon_change_pushbutton.toggled.connect(lambda toggled: self._openDialog(toggled, self.cur_iconpicker))
        self.cur_iconpicker.iconSelected.connect(lambda file_name: self.setIconInView(file_name,
                                                                                      self.cur_svg_renderer,
                                                                                      self.cur_svg,
                                                                                      self.cur_scene,
                                                                                      self._Ui.cur_icon_view))
        self.cur_svg.setSharedRenderer(self.cur_svg_renderer)
        self._Ui.cur_icon_view.setScene(self.cur_scene)
        self.cur_iconpicker.accepted.connect(lambda: self._Ui.cur_icon_change_pushbutton.toggle())

        self.usermapper.setModel(self.usermodel.underlyingUserModel())
        self.usermapper.addMapping(self._Ui.cur_username_label, 1, QByteArray('text'))
        self.usermapper.addMapping(self._Ui.cur_username_lineedit, 1, QByteArray('text'))

        self._Ui.user_list.userChanged.connect(lambda index: self.userChanged.emit(index))

    @staticmethod
    def _openDialog(o: bool, dialog: QDialog):
        if not o: return
        dialog.show()

    @staticmethod
    def setIconInView(file_name: str,
                      svg_renderer: QSvgRenderer,
                      svg_item: QGraphicsSvgItem,
                      icon_scene: QGraphicsScene,
                      graphics_view: QGraphicsView):
        path_to_icon = f":/icons/user/options/{file_name}.svg"
        svg_renderer.load(path_to_icon)

        icon_scene.removeItem(svg_item)
        svg_item.setSharedRenderer(svg_renderer)
        icon_scene.addItem(svg_item)

        bounds = svg_item.boundingRect()
        icon_scene.setSceneRect(bounds)
        graphics_view.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    def userModel(self) -> UserModel: return self.usermodel
