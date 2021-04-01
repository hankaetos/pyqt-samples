#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""--- profile.py ---

Sample user profile information GUI.

@author   hank.aetos@gmail.com
@version  0.1.0
@license  MIT

--- Copyright (C) 2020 Hank Aetos ---
"""


import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QLabel, QRadioButton, QGroupBox,
    QLineEdit, QHBoxLayout, QVBoxLayout)


class ContactForm(QWidget):
    def __init__(self):
        super(ContactForm, self).__init__()
        self.setFixedSize(400, 250)
        self.setWindowTitle('User Profile Information')
        self.add_tabs()
        self.show()

    def add_tabs(self):
        tabs = QTabWidget(self)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.addWidget(tabs)

        details_widget = QWidget(self)
        tabs.addTab(details_widget, 'Details')

        details_layout = QVBoxLayout(self)
        details_layout.setContentsMargins(8, 8, 8, 8)
        details_widget.setLayout(details_layout)

        name_label = QLabel('Name', self)
        name_edit = QLineEdit(self)
        details_layout.addWidget(name_label)
        details_layout.addWidget(name_edit)
        details_layout.addStretch(1)

        address_label = QLabel('Address', self)
        address_edit = QLineEdit(self)
        details_layout.addWidget(address_label)
        details_layout.addWidget(address_edit)
        details_layout.addStretch(1)

        gender_groupbox = QGroupBox('Gender')
        gender_layout = QHBoxLayout(self)
        gender_groupbox.setLayout(gender_layout)
        details_layout.addWidget(gender_groupbox)

        male_radiobutton = QRadioButton('Male', gender_groupbox)
        female_radiobutton = QRadioButton('Female', gender_groupbox)
        gender_layout.addWidget(male_radiobutton)
        gender_layout.addWidget(female_radiobutton)
        details_layout.addStretch(4)

        background_widget = QWidget(self)
        tabs.addTab(background_widget, 'Background')

        background_layout = QVBoxLayout(self)
        background_layout.setContentsMargins(8, 8, 8, 8)
        background_widget.setLayout(background_layout)

        education_groupbox = QGroupBox('Education')
        education_layout = QVBoxLayout(self)
        education_groupbox.setLayout(education_layout)
        background_layout.addWidget(education_groupbox)

        highschool_radiobutton = QRadioButton(
            'High School Diploma', education_groupbox)
        associate_radiobutton = QRadioButton(
            "Associate's Degree", education_groupbox)
        bachelor_radiobutton = QRadioButton(
            "Bachelor's Degree", education_groupbox)
        master_radiobutton = QRadioButton(
            "Master's Degree", education_groupbox)
        doctorate_radiobutton = QRadioButton(
            "Doctorate or Higher", education_groupbox)

        education_layout.addWidget(highschool_radiobutton)
        education_layout.addWidget(associate_radiobutton)
        education_layout.addWidget(bachelor_radiobutton)
        education_layout.addWidget(master_radiobutton)
        education_layout.addWidget(doctorate_radiobutton)
        education_layout.addStretch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ContactForm()
    sys.exit(app.exec_())
