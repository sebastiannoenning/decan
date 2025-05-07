import json
from enum import Enum
from typing import List, Dict, Tuple, Union

# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import (Qt, QObject, Signal,
                            QByteArray, QModelIndex, Property, QPersistentModelIndex,
                            QSize)
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout,
                               QWidget, QSizePolicy, QDataWidgetMapper,
                               QGraphicsView, QGraphicsWidget, QGraphicsScene,
                               QStyleOption, QStyle)
from PySide6.QtGui import (QFont, QMouseEvent, QPainter)
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtSvg import QSvgRenderer

from models.event_model import UserModel

from modules.userlist.user_tab_ui import Ui_user_tab

from views import rss_rc

# pyside6-uic --from-imports resources/modules/user_tab.ui -o client/modules/userlist/user_tab_ui.py

class IconParser(QWidget):
    pathChanged = Signal(str)
    def __init__(self, parent):
        super().__init__(parent)
        self.hide()
        self._icon: str = ''

    @Property(str)
    def Icon(self): return self._icon

    @Icon.setter
    def Icon(self, Icon: str):
        if self._icon != Icon:
            self._icon = Icon
            self.pathChanged.emit(Icon)

class UserTab(QWidget):
    trySelected = Signal(int)
    signInRequested = Signal(int)

    def __init__(self, parent=None, model=None, index=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        self._Ui = Ui_user_tab()
        self._Ui.setupUi(self)

        self._mapper    :QDataWidgetMapper      = QDataWidgetMapper(parent=self)
        if model is not None: self._mapper.setModel(model)

        self._iconParser = IconParser(self)
        self._icon_scene = QGraphicsScene(self)
        self._icon_svg_render = QSvgRenderer()
        self._icon_svg = QGraphicsSvgItem()

        self.connections()
        self._setupMappings()

        self._index     :int           = index
        if index is not None:
            self._mapper.setCurrentModelIndex(index)

        self._active = False
        self._signed_in = False
        self._selected = False

        self.hideAll()

    def hideAll(self):
        self._Ui.active.hide()
        self._Ui.status.hide()
        self._Ui.options.hide()

    def showSignIn(self, ):
        self._Ui.sign_in_button.show()
        self._Ui.sign_out_button.hide()

    def showSignOut(self):
        self._Ui.sign_out_button.show()
        self._Ui.sign_in_button.hide()

    def toggleOptions(self, visible: bool):
        if visible: self._Ui.options.show()
        else: self._Ui.options.hide()

    def toggleActive(self, visible: bool):
        if visible: self._Ui.active.show()
        else: self._Ui.active.hide()

    def toggleStatus(self, visible: bool):
        if visible: self._Ui.status.show()
        else: self._Ui.status.hide()

    def isSignedIn(self) -> bool: return self._Ui.status.isVisible()

    def setModel(self, model: UserModel):              self._mapper.setModel(model)
    def setCurrentModelIndex(self, index: QModelIndex): self._mapper.setCurrentModelIndex(index)
    def setCurrentIndex(self, row: int):                self._mapper.setCurrentIndex(row)
    def currentIndex(self):                             self._mapper.currentIndex()

    def _setupMappings(self, test_en: bool = False): # Sets mappings to each ui object generated via the _setup_Ui
        self._mapper.addMapping(self._Ui.name, 2, QByteArray("text"))
        if test_en: print(f'{self.objectName()}_{hex(id(self))} added mapping to _Ui.name')
        self._mapper.addMapping(self._iconParser, 5, QByteArray("Icon"))
        if test_en: print(f'{self.objectName()}_{hex(id(self))} added mapping to _iconParser')

        self._mapper.setSubmitPolicy(QDataWidgetMapper.SubmitPolicy.AutoSubmit)

    def connections(self):
        self._iconParser.pathChanged.connect(lambda path: self.setIconInView(path,
                                                                              self._icon_svg_render,
                                                                              self._icon_svg,
                                                                              self._icon_scene,
                                                                              self._Ui.icon))
        self._icon_svg.setSharedRenderer(self._icon_svg_render)
        self._Ui.icon.setScene(self._icon_scene)
        self._Ui.sign_in_button.clicked.connect(lambda: self.signInRequested.emit(self))

    @staticmethod
    def setIconInView(file_name: str,
                      svg_renderer: QSvgRenderer,
                      svg_item: QGraphicsSvgItem,
                      icon_scene: QGraphicsScene,
                      graphics_view: QGraphicsView):
        sql_file_name = file_name.strip("'\"")
        path_to_icon = f":/icons/user/options/{sql_file_name}.svg"
        svg_renderer.load(path_to_icon)

        icon_scene.removeItem(svg_item)
        svg_item.setSharedRenderer(svg_renderer)
        icon_scene.addItem(svg_item)

        bounds = svg_item.boundingRect()
        icon_scene.setSceneRect(bounds)
        vp = graphics_view.viewport().size()
        print(f"[DEBUG] bounds = {bounds},  viewport = {vp}")
        graphics_view.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    def mousePressEvent(self, event):
        # Check if the left mouse button was pressed
        if event.button() == Qt.MouseButton.LeftButton:
            # Change the background color to a new color
            self.trySelected.emit(self._mapper.currentIndex())
            #print('mouse pressed!')

        # Call the base class implementation to ensure the event is handled correctly
        super().mousePressEvent(event)

    def setObjectName(self, name, /):
        self.setStyleSheet(f"""
        QWidget#{name} {{
            border-radius: 4px;
            background-color: rgba(30,30,30,1);
        }}""")
        return super().setObjectName(name)

    def paintEvent(self, pe):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)