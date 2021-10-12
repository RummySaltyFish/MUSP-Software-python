#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.thread = ReceiveSignal()
		self.thread.module_out.connect(self.add_modules_list)
		self.thread.terminal_out.connect(self.show_terminal)
		self.thread.remote_address_out.connect(self.get_remote_device)

	comport = 'COM3'
	Raw802Device = digi.xbee.devices.Raw802Device(comport, 115200)

	def show_terminal(self, terminal_dict):
		self.ui.label.setText(self=self, str=terminal_dict)
		QApplication.processEvents()

	def add_modules_list(self, module_list):
		self.ui.modulechoose.addItems(module_list)

	def get_remote_device(self, remote_address):
		self.remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string(remote_address))
		self.Raw802Device.open()
		self.Raw802Device.send_data(self.remote_device,
										   "\x75" + "\x03" + str(self.Raw802Device.get_64bit_addr()))
		self.thread_Raw802Device.close()

	def close_device(self):
		for port in comports():
			try:
				s = Serial(str(port)[0:4])
				s.close()
				device_close = digi.xbee.devices.Raw802Device(str(port)[0:4], 115200)
				device_close.close()
			except (OSError, serial.SerialException):
				pass

	def broadcast_confirm_send(self):  # 广播帧别码
		QApplication.processEvents()
		self.comport = self.ui.comportchoose.currentText()
		self.Raw802Device = digi.xbee.devices.Raw802Device(self.comport, 115200)
		try:
			self.Raw802Device.open()
			self.Raw802Device.send_data_broadcast('\x75')
			self.Raw802Device.close()
		finally:
			pass
		QApplication.processEvents()
		self.thread.start()

	def terminal_signal_send(self):  # 用于获取平台本身的信息
		QApplication.processEvents()
		self.Raw802Device.open()
		self.Raw802Device.send_data(self.remote_device, "\x75\x01")  # 二进制：0000 0001,接收平台当前除模组信息外的信息，如电量等
		self.Raw802Device.close()
		self.thread.start()

	def refresh_system_send(self):  # 用于刷新全部系统信息
		QApplication.processEvents()
		self.Raw802Device.open()
		self.Raw802Device.send_data(self.remote_device, "\x75\x00")  # 二进制：0000 0000,接收平台所有信息
		self.Raw802Device.close()
		self.thread.start()

	def get_module_send(self):  # 要求平台发送模组信息，用于获得及刷新模组信息
		QApplication.processEvents()
		self.Raw802Device.open()
		self.Raw802Device.send_data(self.remote_device, "\x75\x02")  # 二进制：0000 0010,接收平台当前模组数量及种类信息
		self.Raw802Device.close()
		self.thread.start()


class ReceiveSignal(QThread, MainWindow):
	terminal_out = pyqtSignal(dict)
	module_out = pyqtSignal(list)
	remote_address_out = pyqtSignal(str)

	def __init__(self, parent=None):
		super(ReceiveSignal, self).__init__(parent)
		self.modules = []
		self.terminal_dict = {'电量': '???', '现加载模组数': '???'}
		self.working = True
		self.sinoutmode = -1
		self.thread_Raw802Device = digi.xbee.devices.Raw802Device('COM3', 115200)

	def __del__(self):
		self.working = False
		self.wait()

	def switch_case(self, xbee_message):

		print(xbee_message.data.hex()[4:])
		return case_dict.get(xbee_message.data.hex()[0:4], 'No such method')

	def get_remote_device(self, address):
		self.remote_address = address
		self.thread_remote_device = RemoteXBeeDevice(self.thread_Raw802Device,
													 XBee64BitAddress.from_hex_string(address))
		self.sinoutmode = 3
		self.working = False

	def terminal_signal_get(self, terminal_data):  # 获得并显示系统当前的信息，默认电量信息在前，模组数量信息在后
		for i in range(0, int(terminal_data[0:2], 16)):
			if terminal_data[(2 + 4 * i):(4 + 4 * i)] == '01':  # ‘01’表示平台电量，默认其在前
				self.terminal_dict['电量'] = str(int(terminal_data[4 + 4 * i:6 + 4 * i]))
			elif terminal_data[(2 + 4 * i):(4 + 4 * i)] == '02':  # ‘02’表示模组数量，默认在后
				self.terminal_dict['现加载模组数'] = str(int(terminal_data[4 + 4 * i:6 + 4 * i]))
		self.terminal_signal = '电量：' + self.terminal_dict['电量'] + '\n现加载模组数：' + self.terminal_dict['现加载模组数']
		self.sinoutmode = 1
		self.working = False

	def module_signal_get(self, module_data):
		module_type = {
			"01": "空气质量检测",
			"02": "环境温度检测"
		}
		for i in range(0, int(module_data, 16)):
			self.modules.append(module_type.get(module_data[(2 + 4 * i):(4 + 4 * i)]))
		self.sinoutmode = 2
		self.working = False

	def run(self):
		self.working = True
		while self.working:
			self.thread_Raw802Device = digi.xbee.devices.Raw802Device(MainWindow.comport, 115200)
			try:
				self.thread_Raw802Device.open()
				self.thread_Raw802Device.send_data_broadcast("\x75\x00")
				self.xbee_message = self.thread_Raw802Device.read_data()
				print(self.xbee_message)
				self.case_dict = {
					"7501": self.terminal_signal_get(terminal_data=self.xbee_message.data.hex()[4:]),
					"7502": self.module_signal_get(module_data=self.xbee_message.data.hex()[4:]),
					"7503": self.get_remote_device(address=self.xbee_message.data.hex()[4:])
				}
				self.case_dict.get(self.xbee_message.data.hex()[0:4], 'No such method')
				self.thread_Raw802Device.close()
			finally:
				pass
			if self.sinoutmode == 1:
				self.terminal_out.emit(self.terminal_dict)
				self.sinoutmode = -1
			elif self.sinoutmode == 2:
				self.module_out.emit(self.modules)
				self.sinoutmode = -1
			elif self.sinoutmode == 3:
				self.remote_address_out.emit(self.remote_address)
				self.sinoutmode = -1


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
