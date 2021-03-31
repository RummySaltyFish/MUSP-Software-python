#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:57
# @Author  : RummySaltyfish
# @File    : main.py
# @Software: PyCharm

import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindowtest import Ui_MainWindow
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import digi


def switch_case(xbee_message):
	dict = {
		"7500": ReceiveSignal
		"7501": ReceiveSignal
		"7502": ReceiveSignal
		"75ff": ReceiveSignal.establish_connection(ReceiveSignal, xbee_message.data.hex())
	}
	return dict.get(xbee_message.data.hex()[0:4], 'No such method')


class ReceiveSignal(QThread):
	def __init__(self):
		super(ReceiveSignal, self).__init__(parent)

	comport = self.ui.comportchoose.currentText()
	Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)

	def establish_connection(self, address):
		self.remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string(address))
		Raw802Device.open()
		Raw802Device.send_data("\x75\xff" + Raw802Device.get_64bit_addr(), self.remote_device)
		Raw802Device.close()
	def terminal_signal_get(self,terminal_data):
		terminal_dict = {
			'01':
		}
		return terminal_dict.get()
	def run(self):
		try:
			Raw802Device.open()
			Raw802Device.add_data_received_callback(switch_case)
			print("Waiting for data...\n")
			input()

		finally:
			if Raw802Device is not None and device.is_open():
				Raw802Device.close()


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def broadcast_confirm_send(self):  # 广播帧别码
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data_broadcast("\x75")  # 帧别码广播，0x75，十进制117 ，二进制：0111 0101
		Raw802Device.close()

	def terminal_signal_send(self):  # 用于获取平台本身的信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data(ReceiveSignal.remote_device, "\x75\x01")  # 二进制：0000 0001,接收平台当前除模组信息外的信息，如电量等
		Raw802Device.close()

	def refresh_system_send(self):  # 用于刷新全部系统信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data(ReceiveSignal.remote_device, "\x75\x00")  # 二进制：0000 0000,接收平台所有信息
		Raw802Device.close()

	def get_module_send(self):  # 要求平台发送模组信息，用于获得及刷新模组信息
		comport = self.ui.comportchoose.currentText()
		Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)
		Raw802Device.open()
		Raw802Device.send_data(ReceiveSignal.remote_device, "\x75\x02")  # 二进制：0000 0010,接收平台当前模组数量及种类信息
		Raw802Device.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
