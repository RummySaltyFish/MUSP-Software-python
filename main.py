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
import communicationFunc


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def broadcastconfirmsend(self):  # 广播帧别码
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data_broadcast("u")  # 帧别码广播，0x75，十进制117 ，二进制：0111 0101
		Raw802Device.close()

	def terminalsignalsend(self):  # 用于获取平台本身的信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, "!")  # 二进制：0010 0001,0010为每次发送时的帧别信息，0001为接收平台当前除模组信息外的信息
		Raw802Device.close()

	def refreshsystemsend(self):  # 用于刷新全部系统信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, " ")  # 二进制：0010 0000,0000为每次发送时的帧别信息，0000为接收平台所有信息
		Raw802Device.close()

	def getmodulesend(self):  # 要求平台发送模组信息，用于获得及刷新模组信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, "\"")  # 二进制：0010 0010,前0010为每次发送时的帧别信息，后0010为接收平台当前模组信息
		Raw802Device.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
