#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- area_calculator.py ---

Sample area calculator GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGroupBox, QVBoxLayout,
    QFormLayout, QPushButton, QHBoxLayout)
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QDoubleValidator


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.setWindowTitle('Area Calculator')
        self.setFixedSize(250, 175)
        self.add_widgets()
        self.show()

    def add_widgets(self):
        # Create root layout.
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(8, 8, 8, 8)
        root_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(root_layout)

        # Create "Width" widgets.
        width_label = QLabel('Width:', self)
        double_validator = QDoubleValidator(self)
        self.width_entry = QLineEdit(self)
        self.width_entry.setPlaceholderText('0.0')
        self.width_entry.setValidator(double_validator)

        # Create "Length" widgets.
        length_label = QLabel('Length:', self)
        self.length_entry = QLineEdit(self)
        self.length_entry.setPlaceholderText('0.0')
        self.length_entry.setValidator(double_validator)

        # Create "Input" groupbox and add "Length" and "Width" widgets.
        input_layout = QFormLayout(self)
        input_layout.setContentsMargins(8, 8, 8, 8)
        input_layout.setLabelAlignment(Qt.AlignRight)
        input_layout.addRow(width_label, self.width_entry)
        input_layout.addRow(length_label, self.length_entry)
        input_groupbox = QGroupBox('Input', self)
        input_groupbox.setLayout(input_layout)
        root_layout.addWidget(input_groupbox)
        root_layout.addStretch()

        # Create "Area" widget.
        area_label = QLabel('   Area:', self)
        self.area_entry = QLineEdit(self)
        self.area_entry.setPlaceholderText('0.0')
        self.area_entry.setEnabled(False)

        # Create "Output" groupbox and add "Area" widget.
        output_layout = QFormLayout(self)
        output_layout.setContentsMargins(8, 8, 8, 8)
        output_layout.setLabelAlignment(Qt.AlignRight)
        output_layout.addRow(area_label, self.area_entry)
        output_groupbox = QGroupBox('Output', self)
        output_groupbox.setLayout(output_layout)
        root_layout.addWidget(output_groupbox)
        root_layout.addStretch()

        # Create "Calculate" button.
        calculate_button = QPushButton('Calculate', self)
        calculate_button.setFixedWidth(80)
        calculate_button.clicked.connect(self.on_calculate)
        calculate_layout = QHBoxLayout(self)
        calculate_layout.setAlignment(Qt.AlignCenter)
        calculate_layout.addWidget(calculate_button)
        root_layout.addLayout(calculate_layout)

    @pyqtSlot()
    def on_calculate(self):
        if not (self.width_entry.text() and self.length_entry.text()):
            return
        width = float(self.width_entry.text())
        length = float(self.length_entry.text())
        area = width * length
        self.area_entry.setText(str(area))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())
