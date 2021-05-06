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


class MainWindow(QMainWindow, QApplication):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def closeDevice(self):
		self.Raw802Device.close()

	def broadcast_confirm_send(self):  # 广播帧别码
		QApplication.processEvents()
		self.comport = self.ui.comportchoose.currentText()
		self.Raw802Device = digi.xbee.devices.Raw802Device(self.comport, 115200)
		try:
			self.Raw802Device.open()
		finally:
			pass
		self.Raw802Device.send_data_broadcast(data='\x75')  # 帧别码广播，0x75，十进制117 ，二进制：0111 0101
		try:
			self.Raw802Device.add_data_received_callback(self.switch_case)
			input()
		finally:
			pass

	def terminal_signal_send(self):  # 用于获取平台本身的信息
		QApplication.processEvents()
		self.Raw802Device.send_data(self.remote_device, "\x75\x01")  # 二进制：0000 0001,接收平台当前除模组信息外的信息，如电量等
		try:
			self.Raw802Device.add_data_received_callback(self.switch_case)
			input()
		finally:
			pass

	def refresh_system_send(self):  # 用于刷新全部系统信息
		QApplication.processEvents()
		self.Raw802Device.send_data(self.remote_device, "\x75\x00")  # 二进制：0000 0000,接收平台所有信息
		try:
			self.Raw802Device.add_data_received_callback(self.switch_case)
			input()
		finally:
			pass

	def get_module_send(self):  # 要求平台发送模组信息，用于获得及刷新模组信息
		QApplication.processEvents()
		self.Raw802Device.send_data(self.remote_device,
									"\x75\x02")  # 二进制：0000 0010,接收平台当前模组数量及种类信息
		try:
			self.Raw802Device.add_data_received_callback(self.switch_case)
		finally:
			pass

	def switch_case(self, xbee_message):
		case_dict = {
			"7501": self.terminal_signal_get(terminal_data=xbee_message.data.hex()[4:]),
			"7502": self.module_signal_get(module_data=xbee_message.data.hex()[4:]),
			"75ff": self.establish_connection(address=xbee_message.data.hex()[4:])
		}
		return case_dict.get(xbee_message.data.hex()[0:4], 'No such method')

	def establish_connection(self, address):
		self.remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string(address))
		self.Raw802Device.send_data(self.remote_device,
									"\x75\xff" + hex(int(str(self.Raw802Device.get_64bit_addr()), 16)))

	def terminal_signal_get(self, terminal_data):  # 获得并显示系统当前的信息，默认电量信息在前，模组数量信息在后
		terminal_dict = {
			'电量': '???',
			'现有模组数': '???'
		}
		for i in range(0, int(terminal_data[0:2], 16)):
			if terminal_data[(2 + 4 * i):(4 + 4 * i)] == '01':  # ‘01’表示平台电量，默认其在前
				terminal_dict['电量'] = str(int(terminal_data[4 + 4 * i:6 + 4 * i]))
			elif terminal_data[(2 + 4 * i):(4 + 4 * i)] == '02':  # ‘02’表示模组数量，默认在后
				terminal_dict['现有模组数'] = str(int(terminal_data[4 + 4 * i:6 + 4 * i]))
		self.ui.label.setText('电量：' + '\n现加载的模组数：')
		QApplication.processEvents()

	def module_signal_get(self, module_data):
		module_type = {
			"01": "空气质量检测",
			"02": "环境温度检测"
		}
		for i in range(0, int(module_data[0:2], 16)):
			self.ui.modulechoose.addItems(module_type.get(module_data[(2 + 4 * i):(4 + 4 * i)]))
			QApplication.processEvents()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
