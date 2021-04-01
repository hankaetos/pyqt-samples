#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- appointment.py ---

Sample medical appointment GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init()

    def init(self):
        self.setWindowTitle("Medical Appointment")
        self.setFixedSize(450, 400)
        self.add_widgets()
        self.show()

    def add_widgets(self):
        # Defines fonts.
        f1 = QFont('Consolas', 12)
        f1.setBold(True)
        f2 = QFont('Consolas', 10)
        f3 = QFont('Consolas', 8)
        self.setFont(f2)

        # Sets layout.
        layout = QFormLayout()
        layout.setLabelAlignment(Qt.AlignRight)
        self.setLayout(layout)

        # Adds title row.
        title_label = QLabel('Appointment Submission')
        title_label.setFont(f1)
        title_label.setContentsMargins(10, 10, 10, 10)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addRow(title_label)

        # Adds Name row.
        name_label = QLabel('Name:')
        name_label.setFont(f2)
        name_edit = QLineEdit()
        name_edit.setFont(f3)
        name_edit.setPlaceholderText('First Last')
        layout.addRow(name_label, name_edit)

        # Adds Address row.
        address_label = QLabel('Address:')
        address_label.setFont(f2)
        address_edit = QLineEdit()
        address_edit.setFont(f3)
        layout.addRow(address_label, address_edit)

        # Adds Phone row.
        phone_label = QLabel('Phone:')
        phone_label.setFont(f2)
        phone_edit = QLineEdit()
        phone_edit.setFont(f3)
        phone_edit.setInputMask('000-000-0000;')
        layout.addRow(phone_label, phone_edit)

        # Adds Age, Height, Weight row.
        age_label = QLabel('       Age:')
        age_label.setFont(f2)
        age_spinbox = QSpinBox()
        age_spinbox.setFont(f3)
        age_spinbox.setRange(0, 130)

        height_label = QLabel('  Height:')
        height_label.setFont(f2)
        height_edit = QLineEdit()
        height_edit.setFont(f3)
        height_edit.setPlaceholderText('ft')

        weight_label = QLabel('  Weight:')
        weight_label.setFont(f2)
        weight_edit = QLineEdit()
        weight_edit.setFont(f3)
        weight_edit.setPlaceholderText('lbs')

        age_hbox = QHBoxLayout()
        age_hbox.addWidget(age_label)
        age_hbox.addWidget(age_spinbox)
        age_hbox.addWidget(height_label)
        age_hbox.addWidget(height_edit)
        age_hbox.addWidget(weight_label)
        age_hbox.addWidget(weight_edit)
        layout.addRow(age_hbox)

        # Adds Gender row.
        gender_label = QLabel('Gender:')
        gender_label.setFont(f2)
        gender_combobox = QComboBox()
        gender_combobox.setFixedWidth(80)
        gender_combobox.addItems(['Male', 'Female'])
        layout.addRow(gender_label, gender_combobox)

        # Adds Past Surgeries row.
        past_surgeries_label = QLabel('Past Surgeries:')
        past_surgeries_label.setFont(f2)
        past_surgeries_edit = QTextEdit()
        past_surgeries_edit.setFont(f3)
        past_surgeries_edit.setPlaceholderText('Separate by ;')
        layout.addRow('', past_surgeries_label)
        layout.addRow('', past_surgeries_edit)

        # Adds Blood Type row.
        blood_type_label = QLabel('Blood Type:')
        blood_type_label.setFont(f2)
        blood_type_combobox = QComboBox()
        blood_type_combobox.addItems(['A', 'AB', 'B', 'O'])
        blood_type_combobox.setFixedWidth(80)
        layout.addRow(blood_type_label, blood_type_combobox)

        # Adds Appointment Time row.
        time_label = QLabel('Time:')
        time_label.setFont(f2)
        time_label.setAlignment(Qt.AlignRight)

        hour_spinbox = QSpinBox()
        hour_spinbox.setFont(f3)
        hour_spinbox.setRange(1, 12)
        hour_spinbox.setValue(8)
        hour_spinbox.setFixedWidth(60)

        minutes_combobox = QComboBox()
        minutes_combobox.setFont(f3)
        minutes_combobox.addItems([':00', ':30'])
        minutes_combobox.setFixedWidth(60)

        ampm_combobox = QComboBox()
        ampm_combobox.setFont(f3)
        ampm_combobox.addItems(['AM', 'PM'])
        ampm_combobox.setFixedWidth(60)

        time_hbox = QHBoxLayout()
        time_hbox.addWidget(hour_spinbox)
        time_hbox.addWidget(minutes_combobox)
        time_hbox.addWidget(ampm_combobox)

        layout.addRow(time_label, time_hbox)

        # Adds Submit row.
        submit_button = QPushButton('Submit')
        submit_button.setFont(f2)
        submit_button.setFixedWidth(80)
        submit_button.clicked.connect(self._on_submit)
        submit_hbox = QHBoxLayout()
        submit_hbox.setAlignment(Qt.AlignCenter)
        submit_hbox.addWidget(submit_button)
        layout.addRow(submit_hbox)

    def _on_submit(self):
        print('\tSubmitted.')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
