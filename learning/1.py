#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = PyQt5.QtWidgets.QLCDNumber(self)
        sld = PyQt5.QtWidgets.QSlider(Qt.Horizontal, self)

        vbox = PyQt5.QtWidgets.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
1