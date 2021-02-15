#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:57
# @Author  : RummySaltyfish
# @File    : main.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindowtest import Ui_MainWindow
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import digi


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def broadcastConfirm(self):
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data_broadcast("u")  # 帧别码广播，0x75，十进制117
		Raw802Device.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win=MainWindow()
	win.show()
	sys.exit(app.exec_())
