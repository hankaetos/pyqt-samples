#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- main_window.py ---

SpinWheel GUI; randomly selects an item from a list.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2021 MAI Enterprises ---
"""

import os
import random
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QTabWidget, QTextEdit, QScrollBar, QMessageBox, QHBoxLayout, QSpinBox,
    QFormLayout, QPushButton, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap, QTransform
from PyQt5.QtCore import pyqtSlot, Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.items = []

        self.setFixedSize(400, 420)
        self.setWindowTitle('SpinWheel')
        self.setWindowIcon(QIcon('resources/mai_v0.1.0.png'))
        self.create_actions()
        self.add_menubar()
        self.add_central_widget()
        self.add_statusbar()
        self.show()

    def create_actions(self):
        # Import
        self.import_action = QAction('Import...', self)
        self.import_action.setStatusTip('Import items from *.txt')
        self.import_action.setShortcut('Ctrl+I')
        self.import_action.triggered.connect(self.on_import)

        # Export
        self.export_action = QAction('Export...', self)
        self.export_action.setStatusTip('Export items to *.txt')
        self.export_action.setShortcut('Ctrl+E')
        self.export_action.triggered.connect(self.on_export)
        self.export_action.setEnabled(False)

        # Exit
        self.exit_action = QAction('Exit', self)
        self.exit_action.setStatusTip('Quit application')
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

        # About
        self.about_action = QAction('About')
        self.about_action.setStatusTip('Show application information')
        self.about_action.setShortcut('Ctrl+?')
        self.about_action.triggered.connect(self.on_about)

    @pyqtSlot()
    def on_import(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Import TXT', 'resources', 'Text Files (*.txt)')

        if fname:
            with open(fname, 'r') as f:
                self.items = f.readlines()
                self.items_edit.setText(''.join(self.items))

    @pyqtSlot()
    def on_export(self):
        text = '\n'.join(self.items)
        fname, _ = QFileDialog.getSaveFileName(
            self, 'Export TXT', 'resources', 'Text Files (*.txt)')
        if fname:
            with open(fname, 'w') as f:
                f.write(text)

    @pyqtSlot()
    def on_about(self):
        text = (
            'SpinWheel v0.1.0\n'
            '\n'
            'Authors:\n'
            '    hank.aetos@gmail.com\n'
            '\n'
            'Copyright (c) MAI Enterprises 2021')
        QMessageBox.about(self, 'About', text)

    def add_menubar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addActions([self.import_action, self.export_action])
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)
        help_menu = menubar.addMenu('Help')
        help_menu.addAction(self.about_action)

    def add_central_widget(self):
        central_widget = QTabWidget(self)
        self.setCentralWidget(central_widget)

        self.input_widget = QWidget(self)
        self.add_input_subwidgets()
        central_widget.addTab(self.input_widget, 'Input')

        self.select_widget = QWidget(self)
        self.add_select_subwidgets()
        self.select_widget.setEnabled(False)
        central_widget.addTab(self.select_widget, 'Select')

    def add_input_subwidgets(self):
        # Set layout.
        input_layout = QFormLayout(self)
        input_layout.setContentsMargins(16, 16, 16, 16)
        self.input_widget.setLayout(input_layout)

        # Add widgets.
        items_label = QLabel('Enter items separated by newlines:', self)
        self.items_edit = QTextEdit(self)
        self.items_edit.setFixedHeight(265)
        self.items_edit.addScrollBarWidget(QScrollBar(), Qt.AlignRight)
        self.items_edit.textChanged.connect(self.on_items)
        input_layout.addRow(items_label)
        input_layout.addRow(self.items_edit)

        count_label = QLabel('Items count:', self)
        self.count_edit = QLineEdit(self)
        self.count_edit.setFixedWidth(40)
        self.count_edit.setText('0')
        self.count_edit.setDisabled(True)
        input_layout.addRow(count_label, self.count_edit)

    @pyqtSlot()
    def on_items(self):
        self.items = self.items_edit.toPlainText().split('\n')
        items_count = len(self.items)

        if self.items != [''] and items_count > 0:
            self.export_action.setEnabled(True)
            self.select_widget.setEnabled(True)
            self.count_edit.setText(str(items_count))
            self.nspin_spinbox.setRange(1, items_count)
            self.plot_spinwheel()
        else:
            self.export_action.setEnabled(False)
            self.select_widget.setEnabled(False)
            self.count_edit.setText('0')

    def plot_spinwheel(self):
        items_count = len(self.items)
        if self.items != [''] and items_count > 0:
            n_items = len(self.items)
            angle = 360 / n_items
            y = np.repeat(angle, repeats=n_items)

            plt.clf()
            plt.pie(y, labels=self.items, labeldistance=0.5, rotatelabels=45,
                    startangle=90 - angle / 2)
            plt.savefig('resources/spinwheel.svg', transparent=True,
                        bbox_inches='tight', pad_inches=0)

            self.wheel_pixmap = QPixmap('resources/spinwheel.svg').scaled(
                QSize(300, 300), Qt.KeepAspectRatio,
                Qt.SmoothTransformation)
            self.wheel_label.setPixmap(self.wheel_pixmap)
            self.wheel_label.repaint()

            self.angle = angle
        else:
            self.wheel_pixmap = QPixmap('resources/default_wheel.png')
            self.wheel_label.setPixmap(self.wheel_pixmap)
            self.wheel_label.repaint()

    def add_select_subwidgets(self):
        # Set layout.
        select_layout = QVBoxLayout()
        select_layout.setAlignment(Qt.AlignCenter)
        select_layout.setContentsMargins(8, 8, 8, 8)
        self.select_widget.setLayout(select_layout)

        # Add widgets.
        nspin_label = QLabel('Spin Repetitions:', self)
        self.nspin_spinbox = QSpinBox(self)

        self.nspin_spinbox.setRange(1, len(self.items))
        self.nspin_spinbox.setFixedWidth(40)

        nspin_layout = QHBoxLayout(self)
        select_layout.addLayout(nspin_layout)

        nspin_layout.addWidget(nspin_label)
        nspin_layout.addWidget(self.nspin_spinbox)
        nspin_layout.addStretch()

        pointer_pixmap = QPixmap('resources/pointer.png')
        pointer_label = QLabel(self)
        pointer_label.setAlignment(Qt.AlignCenter)
        pointer_label.setPixmap(pointer_pixmap)
        select_layout.addWidget(pointer_label)

        self.wheel_label = QLabel(self)
        self.plot_spinwheel()
        wheel_layout = QHBoxLayout(self)
        wheel_layout.setAlignment(Qt.AlignCenter)
        wheel_layout.addWidget(self.wheel_label)
        select_layout.addLayout(wheel_layout)

        spin_button = QPushButton('Spin', self)
        spin_button.setFixedWidth(80)
        spin_button.clicked.connect(self.on_spin)
        spin_button_layout = QHBoxLayout(self)
        spin_button_layout.setAlignment(Qt.AlignCenter)
        spin_button_layout.addWidget(spin_button)
        select_layout.addLayout(spin_button_layout)

    def on_spin(self):
        self.winner = Selector.random_select(self.items)
        deg_winner = self.items.index(self.winner) * self.angle

        secs = 3
        deg_step = 10
        frames = secs * deg_step

        deg = 0
        for i in range(frames):
            self.wheel_label.setPixmap(self.wheel_pixmap.transformed(
                QTransform().rotate(deg), mode=Qt.SmoothTransformation))
            self.wheel_label.setAlignment(Qt.AlignCenter)
            self.wheel_label.repaint()

            deg = (deg + deg_step) % 360
            time.sleep(secs / frames)

        while(True):
            if abs(deg_winner - deg) > deg_step:
                deg = (deg + deg_step) % 360

                self.wheel_label.setPixmap(self.wheel_pixmap.transformed(
                QTransform().rotate(deg), mode=Qt.SmoothTransformation))
                self.wheel_label.setAlignment(Qt.AlignCenter)
                self.wheel_label.repaint()

                time.sleep(secs / frames)
            else:
                break

        print(f'Winner: {self.winner}')

        if self.nspin_spinbox.value() > 1:
            print('Re-spinning in', end=' ')
            for i in range(3, 0, -1):
                print(i, end=' ')
                time.sleep(1)
            print()
            self.items.remove(self.winner)
            self.items_edit.setText('\n'.join(self.items))
            self.nspin_spinbox.setValue(self.nspin_spinbox.value() - 1)

            self.on_spin()

    def add_statusbar(self):
        self.statusBar()


class Selector:
    @staticmethod
    def random_select(items: list):
        if not isinstance(items, list):
            raise ValueError(f'items={items} must be a list of strings!')
        return random.choice(items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
