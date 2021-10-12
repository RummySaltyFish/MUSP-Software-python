#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:57
# @Author  : RummySaltyfish
# @File    : main.py
# @Software: PyCharm

import serial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainwindowtest import Ui_MainWindow
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import digi
from serial.tools.list_ports import *
from serial import Serial


class MainWindow(QMainWindow, QApplication):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.thread = ReceiveSignal()

	threadComport = '???'

	def broadcast_confirm_send(self):  # 广播帧别码
		self.Comport = 'COM3'
		self.threadComport = self.Comport
		self.thread.start()


class ReceiveSignal(QThread, MainWindow):

	def __init__(self, parent=None):
		super(ReceiveSignal, self).__init__(parent)
		self.working = True

	def __del__(self):
		self.working = False
		self.wait()

	def run(self):
		while self.working:
			print(MainWindow.threadComport)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
