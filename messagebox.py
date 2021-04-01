#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- messagebox.py ---

Sample messagebox.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self._init_gui()

    def _init_gui(self):
        self.setWindowTitle('MessageBoxes')
        self.setFixedSize(300, 200)
        self._add_widgets()
        self.show()

    def _add_widgets(self):
        h1 = QFont('Roboto', 12)
        h1.setBold(True)
        b1 = QFont('Roboto', 10)

        some_label = QLabel('Press buttons below:', self)
        some_label.setFont(h1)
        some_label.move(20, 20)

        info_button = QPushButton('Information', self)
        info_button.setFont(b1)
        info_button.move(40, 40)
        info_button.clicked.connect(self._show_msg)

        question_button = QPushButton('Question', self)
        question_button.setFont(b1)
        question_button.move(120, 40)
        question_button.clicked.connect(self._show_msg)

    def _show_msg(self):
        button_text = self.sender().text()
        if button_text == 'Information':
            msgbox = QMessageBox().information(
                self, 'Information', 'Some information.\nBaby.', QMessageBox.Ok,
                QMessageBox.Ok)
        elif button_text == 'Question':
            msgbox = QMessageBox().question(
                self, 'Question', 'Continue?', QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
            if msgbox == QMessageBox.Yes:
                print('Choice: continue')
            else:
                print('Choice: exit')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
