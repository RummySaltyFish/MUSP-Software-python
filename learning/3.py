#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 20:46
# @Author  : RummySaltyfish

import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
	def __init__(self, parent=None):
		super(WinForm, self).__init__(parent)
		self.setGeometry(300, 300, 350, 350)
		self.setWindowTitle('2123432')
		close = QPushButton('Close', self)
		close.setGeometry(10, 10, 60, 35)
		close.setStyleSheet("background-color:red")
		close.clicked.connect(self.close)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
