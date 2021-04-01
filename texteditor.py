#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- texteditor.py ---

Sample rich text editor GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu, QAction, QMessageBox, QTextEdit,
    QFileDialog, QInputDialog, QFontDialog, QColorDialog)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Rich Text Editor')
        self.setGeometry(100, 100, 400, 500)
        self.add_central_widget()
        self.add_menubar_widget()
        self.show()

    def add_central_widget(self):
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)

    def add_menubar_widget(self):
        # Add menubar.
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)  # For MacOS.

        # Add File menu.
        file_menu = menubar.addMenu('File')

        # Add New action to File menu.
        new_action = QAction(QIcon('resources/new_file.png'), 'New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.on_new)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        # Add Open action to File menu.
        open_action = QAction(QIcon('resources/open_file.png'), 'Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.on_open)
        file_menu.addAction(open_action)

        # Add Save action to File menu.
        save_action = QAction(QIcon('resources/save_file.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.on_save)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        # Add Exit action to File menu.
        exit_action = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Add Edit menu to menubar.
        edit_menu = menubar.addMenu('Edit')

        # Add Undo action to Edit menu.
        undo_action = QAction(QIcon('resources/undo.png'), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.textedit.undo)
        edit_menu.addAction(undo_action)

        # Add Redo action to Edit menu.
        redo_action = QAction(QIcon('resources/redo.png'), 'Redo', self)
        redo_action.setShortcut('Ctrl+Shift+Z')
        redo_action.triggered.connect(self.textedit.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        # Add Cut action to Edit menu.
        cut_action = QAction(QIcon('resources/cut.png'), 'Cut', self)
        cut_action.setShortcut('Ctlr+X')
        cut_action.triggered.connect(self.textedit.cut)
        edit_menu.addAction(cut_action)

        # Add Copy action to Edit menu.
        copy_action = QAction(QIcon('resources/copy.png'), 'Copy', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.textedit.copy)
        edit_menu.addAction(copy_action)

        # Add Paste action to Edit menu.
        paste_action = QAction(QIcon('resources/paste.png'), 'Paste', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.textedit.paste)
        edit_menu.addAction(paste_action)

        edit_menu.addSeparator()

        # Add Find action to Edit menu.
        find_action = QAction(QIcon('resources/find.png'), 'Find', self)
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(self.on_find)
        edit_menu.addAction(find_action)

    def on_find(self):
        token, ok = QInputDialog.getText(self, 'Find Text', 'Find:')
        extra_selections = []

        if ok and not self.textedit.isReadOnly():
            self.textedit.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)

            while(self.textedit.find(token)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                selection.cursor = self.textedit.textCursor()
                extra_selections.append(selection)

            for i in extra_selections:
                self.textedit.setExtraSelections(extra_selections)

    def on_new(self):
        choice = QMessageBox.question(self, 'New File', 'Clear all text?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            self.textedit.clear()

    def on_open(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Open File', './resources',
            'Text Files (*.txt);;HTML Files (*.html)')

        if fname:
            with open(fname, 'r') as f:
                self.textedit.setText(f.read())
        else:
            QMessageBox.warning(
                self, 'Warning', 'Unable to open file!', QMessageBox.Ok)

    def on_save(self):
        fname, _ = QFileDialog.getSaveFileName(
            self, 'Save File', './resources',
            'Text Files (*.txt);;HTML Files (*.html')

        if fname.endswith('.txt'):
            with open(fname, 'w') as f:
                f.write(self.textedit.toPlainText())
        elif fname.endswith('.html'):
            with open(fname, 'w') as f:
                f.write(self.textedit.toHtml())
        else:
            QMessageBox.warning(
                self, 'Warning', 'Unable to save file!', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
