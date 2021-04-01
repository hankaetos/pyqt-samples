#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- notepad.py ---

Sample notepad GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QStatusBar, QAction,
                             QTextEdit, QToolBar, QDockWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Notepad')
        self.setCentralWidget(QTextEdit())
        self.add_menubar()
        self.add_toolbar()
        self.add_dock()
        self.show()

    def add_menubar(self):
        # Add menubar and menus.
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        view_menu = menubar.addMenu('View')

        # Add Exit action to File menu.
        exit_action = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Quit Progam')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Add Fullscreen action to View menu.
        appearance_submenu = view_menu.addMenu('Appearance')
        fullscreen_action = QAction('Fullscreen', self, checkable=True)
        fullscreen_action.setStatusTip('Switch to fullscreen mode')
        fullscreen_action.triggered.connect(self.on_fullscreen)
        appearance_submenu.addAction(fullscreen_action)

        # Add statusbar.
        self.setStatusBar(QStatusBar(self))

    def on_fullscreen(self, checked):
        if checked:
            self.showFullScreen()
        else:
            self.showNormal()

    def add_toolbar(self):
        toolbar = QToolBar('Main Toolbar', self)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

    def add_dock(self):
        dock = QDockWidget('Main Dock', self)
        dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock.setWidget(QTextEdit())
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
