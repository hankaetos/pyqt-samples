#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- photoeditor.py ---

Sample photo editor GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMenu, QAction, QToolBar, QDockWidget,
    QStatusBar, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QFileDialog,
    QMessageBox)
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QTransform


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(650, 650)
        self.setWindowTitle('Photo Editor')
        self.create_actions()
        self.add_menubar()
        self.add_toolbar()
        self.add_central_widget()
        self.add_dock()
        self.setStatusBar(QStatusBar())
        self.show()

    def create_actions(self):
        # Create Open action.
        open_action = QAction(QIcon('resources/open_file.png'), 'Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open image')
        open_action.triggered.connect(self.on_open)

        # Create Save action.
        save_action = QAction(QIcon('resources/save_file.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save image')
        save_action.triggered.connect(self.on_save)
        save_action.setEnabled(False)

        # Create Print action.
        print_action = QAction(QIcon('resources/print.png'), 'Print', self)
        print_action.setShortcut('Ctrl+P')
        print_action.setStatusTip('Print image')
        print_action.triggered.connect(self.on_print)
        print_action.setEnabled(False)

        # Create Exit action.
        exit_action = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Quit program')
        exit_action.triggered.connect(self.close)

        # Create Rotate 90° action.
        rotate_90_action = QAction('Rotate 90°')
        rotate_90_action.setStatusTip('Rotates image by 90° clockwise')
        rotate_90_action.triggered.connect(self.on_rotate_90)
        rotate_90_action.setEnabled(False)

        # Create Rotate 180° action.
        rotate_180_action = QAction('Rotate 180°')
        rotate_180_action.setStatusTip('Rotates image by 180° clockwise')
        rotate_180_action.triggered.connect(self.on_rotate_180)
        rotate_180_action.setEnabled(False)

        # Create Vertical Flip
        vflip_action = QAction('Flip Vertical', self)
        vflip_action.triggered.connect(self.on_vflip)
        vflip_action.setEnabled(False)

        # Create Horizontal Flip
        hflip_action = QAction('Flip Horizontal', self)
        hflip_action.triggered.connect(self.on_hflip)
        hflip_action.setEnabled(False)

        # Create Resize Half action.
        resize_action = QAction('Resize Half', self)
        resize_action.triggered.connect(self.on_resize)
        resize_action.setEnabled(False)

        # Create Clear action.
        clear_action = QAction(QIcon('resources/clear.png'), 'Clear', self)
        clear_action.setShortcut('Ctrl+D')
        clear_action.setStatusTip('Clear image')
        clear_action.triggered.connect(self.on_clear)
        clear_action.setEnabled(False)

        # Create Edit Image Tools checkable action.
        toggle_dock_action = QAction('Edit Image Tools', self, checkable=True)
        toggle_dock_action.setChecked(True)
        toggle_dock_action.triggered.connect(self.on_toggle_dock)

        # Set actions as attributes.
        self.open_action = open_action
        self.save_action = save_action
        self.print_action = print_action
        self.exit_action = exit_action
        self.rotate_90_action = rotate_90_action
        self.rotate_180_action = rotate_180_action
        self.vflip_action = vflip_action
        self.hflip_action = hflip_action
        self.resize_action = resize_action
        self.clear_action = clear_action
        self.toggle_dock_action = toggle_dock_action

    def add_menubar(self):
        """Adds menubar with associated menus and actions."""
        menubar = self.menuBar()

        # Create menus.
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        view_menu = menubar.addMenu('View')

        # Add actions to File menu.
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.print_action)
        file_menu.addAction(self.clear_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # Add actions to Edit menu.
        edit_menu.addAction(self.rotate_90_action)
        edit_menu.addAction(self.rotate_180_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.vflip_action)
        edit_menu.addAction(self.hflip_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_action)

        # Add actions to View menu.
        view_menu.addAction(self.toggle_dock_action)

    def add_toolbar(self):
        # Add toolbar.
        toolbar = QToolBar(self)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Add actions.
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.print_action)
        toolbar.addAction(self.clear_action)
        toolbar.addAction(self.exit_action)

    def add_central_widget(self):
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)

    def add_dock(self):
        # Create dock.
        self.dock = QDockWidget('Edit Image Tools', self)
        self.dock.setMinimumWidth(150)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # Set dock content layout.
        widget = QWidget()
        vbox_layout = QVBoxLayout()
        vbox_layout.setContentsMargins(8, 8, 8 ,8)
        widget.setLayout(vbox_layout)
        self.dock.setWidget(widget)

        # Add Rotate 90 button.
        self.rotate_90_button = QPushButton('Rotate 90°')
        self.rotate_90_button.setStatusTip('Rotate image 90° clockwise')
        self.rotate_90_button.clicked.connect(self.on_rotate_90)
        self.rotate_90_button.setEnabled(False)
        vbox_layout.addWidget(self.rotate_90_button)

        # Add Rotate 180 button.
        self.rotate_180_button = QPushButton('Rotate 180°')
        self.rotate_180_button.setStatusTip('Rotate image 180° clockwise')
        self.rotate_180_button.clicked.connect(self.on_rotate_180)
        self.rotate_180_button.setEnabled(False)
        vbox_layout.addWidget(self.rotate_180_button)
        vbox_layout.addStretch(1)

        # Add Vertical Flip button.
        self.vflip_button = QPushButton('Flip Vertical')
        self.vflip_button.setStatusTip('Flip image across vertical axis')
        self.vflip_button.clicked.connect(self.on_vflip)
        self.vflip_button.setEnabled(False)
        vbox_layout.addWidget(self.vflip_button)

        # Add Horizontal Flip button.
        self.hflip_button = QPushButton('Flip Horizontal')
        self.hflip_button.setStatusTip('Flip image across horizontal axis')
        self.hflip_button.clicked.connect(self.on_hflip)
        self.hflip_button.setEnabled(False)
        vbox_layout.addWidget(self.hflip_button)
        vbox_layout.addStretch(1)

        # Add Resize Half button.
        self.resize_button = QPushButton('Resize Half')
        self.resize_button.setStatusTip('Resize image to 1/2 the original size')
        self.resize_button.clicked.connect(self.on_resize)
        self.resize_button.setEnabled(False)
        vbox_layout.addWidget(self.resize_button)
        vbox_layout.addStretch(8)

    @pyqtSlot()
    def on_open(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Open Image', 'resources', 'JPG Files (*.jpeg *.jpg);;\
            PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)')

        if fname:
            self.image = QPixmap(fname)
            self.image_label.setPixmap(
                self.image.scaled(
                    self.image_label.size(), Qt.KeepAspectRatio,
                    Qt.SmoothTransformation))

        else:
            QMessageBox.warning(
                self, 'Open Image', 'Could not open image!', QMessageBox.Ok)

        # Activate/Deactivate image editing widgets.
        self.toggle_widgets(bool(fname))

    def toggle_widgets(self, flag):
        self.save_action.setEnabled(flag)
        self.print_action.setEnabled(flag)
        self.clear_action.setEnabled(flag)
        self.rotate_90_action.setEnabled(flag)
        self.rotate_180_action.setEnabled(flag)
        self.vflip_action.setEnabled(flag)
        self.hflip_action.setEnabled(flag)
        self.resize_action.setEnabled(flag)
        self.rotate_90_button.setEnabled(flag)
        self.rotate_180_button.setEnabled(flag)
        self.vflip_button.setEnabled(flag)
        self.hflip_button.setEnabled(flag)
        self.resize_button.setEnabled(flag)

    @pyqtSlot()
    def on_save(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save File', 'resources',
            'JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;\
            Bitmap Files (*.bmp);;GIF Files (*.gif)')

        if fname and (not self.image.isNull()):
            self.image.save(fname)
        else:
            QMessageBox.warning(
                self, 'Save Image', 'Cound not save image!', QMessageBox.Ok)

    @pyqtSlot()
    def on_print(self):
        print('\tPrint image')
        pass

    @pyqtSlot()
    def on_vflip(self):
        pass

    @pyqtSlot()
    def on_hflip(self):
        print('\tFlip image horizontally')
        pass

    @pyqtSlot()
    def on_resize(self):
        print('\tResize image')
        pass

    @pyqtSlot()
    def on_clear(self):
        self.image_label.clear()
        self.toggle_widgets(False)

    @pyqtSlot()
    def on_toggle_dock(self):
        if self.dock.isVisible():
            self.dock.setVisible(False)
        else:
            self.dock.setVisible(True)

    @pyqtSlot()
    def on_rotate_90(self):
        rotate90 = QTransform().rotate(90)
        pixmap = QPixmap(self.image)
        rotated = pixmap.transformed(rotate90, Qt.SmoothTransformation)
        self.image_label.setPixmap(
            rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio,
                           Qt.SmoothTransformation))
        self.image = QPixmap(rotated)
        self.image_label.repaint()

    @pyqtSlot()
    def on_rotate_180(self):
        rotate180 = QTransform().rotate(180)
        pixmap = QPixmap(self.image)
        rotated = pixmap.transformed(rotate180, Qt.SmoothTransformation)
        self.image_label.setPixmap(
            rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio,
                           Qt.SmoothTransformation))
        self.image = QPixmap(rotated)
        self.image_label.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
