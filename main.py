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
from serial.tools.list_ports import *
from serial import Serial


class MainWindow(QMainWindow, QApplication):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def close_device(self):
		for port in comports():
			try:
				s = Serial(str(port)[0:4])
				s.close()
				Deviceclose = digi.xbee.devices.Raw802Device(str(port)[0:4], 115200)
				Deviceclose.close()
			except (OSError, serial.SerialException):
				pass

	def into_hex(self, goalstr):
		hex_dict = {'00': '\x00', '01': '\x01', '02': '\x02', '03': '\x03', '04': '\x04', '05': '\x05', '06': '\x06',
					'07': '\x07', '08': '\x08', '09': '\x09', '0a': '\x0a', '0b': '\x0b', '0c': '\x0c', '0d': '\x0d',
					'0e': '\x0e', '0f': '\x0f',
					'10': '\x10', '11': '\x11', '12': '\x12', '13': '\x13', '14': '\x14', '15': '\x15', '16': '\x16',
					'17': '\x17', '18': '\x18', '19': '\x19', '1a': '\x1a', '1b': '\x1b', '1c': '\x1c', '1d': '\x1d',
					'1e': '\x1e', '1f': '\x1f',

					'20': '\x20', '21': '\x21', '22': '\x22', '23': '\x23', '24': '\x24', '25': '\x25', '26': '\x26',
					'27': '\x27', '28': '\x28', '29': '\x29', '2a': '\x2a', '2b': '\x2b', '2c': '\x2c', '2d': '\x2d',
					'2e': '\x2e', '2f': '\x2f',

					'30': '\x30', '31': '\x31', '32': '\x32', '33': '\x33', '34': '\x34', '35': '\x35', '36': '\x36',
					'37': '\x37', '38': '\x38', '39': '\x39', '3a': '\x3a', '3b': '\x3b', '3c': '\x3c', '3d': '\x3d',
					'3e': '\x3e', '3f': '\x3f',

					'40': '\x40', '41': '\x41', '42': '\x42', '43': '\x43', '44': '\x44', '45': '\x45', '46': '\x46',
					'47': '\x47', '48': '\x48', '49': '\x49', '4a': '\x4a', '4b': '\x4b', '4c': '\x4c', '4d': '\x4d',
					'4e': '\x4e', '4f': '\x4f',

					'50': '\x50', '51': '\x51', '52': '\x52', '53': '\x53', '54': '\x54', '55': '\x55', '56': '\x56',
					'57': '\x57', '58': '\x58', '59': '\x59', '5a': '\x5a', '5b': '\x5b', '5c': '\x5c', '5d': '\x5d',
					'5e': '\x5e', '5f': '\x5f',

					'60': '\x60', '61': '\x61', '62': '\x62', '63': '\x63', '64': '\x64', '65': '\x65', '66': '\x66',
					'67': '\x67', '68': '\x68', '69': '\x69', '6a': '\x6a', '6b': '\x6b', '6c': '\x6c', '6d': '\x6d',
					'6e': '\x6e', '6f': '\x6f',

					'70': '\x70', '71': '\x71', '72': '\x72', '73': '\x73', '74': '\x74', '75': '\x75', '76': '\x76',
					'77': '\x77', '78': '\x78', '79': '\x79', '7a': '\x7a', '7b': '\x7b', '7c': '\x7c', '7d': '\x7d',
					'7e': '\x7e', '7f': '\x7f',

					'80': '\x80', '81': '\x81', '82': '\x82', '83': '\x83', '84': '\x84', '85': '\x85', '86': '\x86',
					'87': '\x87', '88': '\x88', '89': '\x89', '8a': '\x8a', '8b': '\x8b', '8c': '\x8c', '8d': '\x8d',
					'8e': '\x8e', '8f': '\x8f',

					'90': '\x90', '91': '\x91', '92': '\x92', '93': '\x93', '94': '\x94', '95': '\x95', '96': '\x96',
					'97': '\x97', '98': '\x98', '99': '\x99', '9a': '\x9a', '9b': '\x9b', '9c': '\x9c', '9d': '\x9d',
					'9e': '\x9e', '9f': '\x9f',

					'a0': '\xa0', 'a1': '\xa1', 'a2': '\xa2', 'a3': '\xa3', 'a4': '\xa4', 'a5': '\xa5', 'a6': '\xa6',
					'a7': '\xa7', 'a8': '\xa8', 'a9': '\xa9', 'aa': '\xaa', 'ab': '\xab', 'ac': '\xac', 'ad': '\xad',
					'ae': '\xae', 'af': '\xaf',

					'b0': '\xb0', 'b1': '\xb1', 'b2': '\xb2', 'b3': '\xb3', 'b4': '\xb4', 'b5': '\xb5', 'b6': '\xb6',
					'b7': '\xb7', 'b8': '\xb8', 'b9': '\xb9', 'ba': '\xba', 'bb': '\xbb', 'bc': '\xbc', 'bd': '\xbd',
					'be': '\xbe', 'bf': '\xbf',

					'c0': '\xc0', 'c1': '\xc1', 'c2': '\xc2', 'c3': '\xc3', 'c4': '\xc4', 'c5': '\xc5', 'c6': '\xc6',
					'c7': '\xc7', 'c8': '\xc8', 'c9': '\xc9', 'ca': '\xca', 'cb': '\xcb', 'cc': '\xcc', 'cd': '\xcd',
					'ce': '\xce', 'cf': '\xcf',

					'd0': '\xd0', 'd1': '\xd1', 'd2': '\xd2', 'd3': '\xd3', 'd4': '\xd4', 'd5': '\xd5', 'd6': '\xd6',
					'd7': '\xd7', 'd8': '\xd8', 'd9': '\xd9', 'da': '\xda', 'db': '\xdb', 'dc': '\xdc', 'dd': '\xdd',
					'de': '\xde', 'df': '\xdf',

					'e0': '\xe0', 'e1': '\xe1', 'e2': '\xe2', 'e3': '\xe3', 'e4': '\xe4', 'e5': '\xe5', 'e6': '\xe6',
					'e7': '\xe7', 'e8': '\xe8', 'e9': '\xe9', 'ea': '\xea', 'eb': '\xeb', 'ec': '\xec', 'ed': '\xed',
					'ee': '\xee', 'ef': '\xef',

					'f0': '\xf0', 'f1': '\xf1', 'f2': '\xf2', 'f3': '\xf3', 'f4': '\xf4', 'f5': '\xf5', 'f6': '\xf6',
					'f7': '\xf7', 'f8': '\xf8', 'f9': '\xf9', 'fa': '\xfa', 'fb': '\xfb', 'fc': '\xfc', 'fd': '\xfd',
					'fe': '\xfe', 'ff': '\xff',

					'0A': '\x0A', '0B': '\x0B', '0C': '\x0C', '0D': '\x0D', '0E': '\x0E', '0F': '\x0F',

					'1A': '\x1A', '1B': '\x1B', '1C': '\x1C', '1D': '\x1D', '1E': '\x1E', '1F': '\x1F',

					'2A': '\x2A', '2B': '\x2B', '2C': '\x2C', '2D': '\x2D', '2E': '\x2E', '2F': '\x2F',

					'3A': '\x3A', '3B': '\x3B', '3C': '\x3C', '3D': '\x3D', '3E': '\x3E', '3F': '\x3F',

					'4A': '\x4A', '4B': '\x4B', '4C': '\x4C', '4D': '\x4D', '4E': '\x4E', '4F': '\x4F',

					'5A': '\x5A', '5B': '\x5B', '5C': '\x5C', '5D': '\x5D', '5E': '\x5E', '5F': '\x5F',

					'6A': '\x6A', '6B': '\x6B', '6C': '\x6C', '6D': '\x6D', '6E': '\x6E', '6F': '\x6F',

					'7A': '\x7A', '7B': '\x7B', '7C': '\x7C', '7D': '\x7D', '7E': '\x7E', '7F': '\x7F',

					'8A': '\x8A', '8B': '\x8B', '8C': '\x8C', '8D': '\x8D', '8E': '\x8E', '8F': '\x8F',

					'9A': '\x9A', '9B': '\x9B', '9C': '\x9C', '9D': '\x9D', '9E': '\x9E', '9F': '\x9F',

					'A0': '\xA0', 'A1': '\xA1', 'A2': '\xA2', 'A3': '\xA3', 'A4': '\xA4', 'A5': '\xA5', 'A6': '\xA6',
					'A7': '\xA7', 'A8': '\xA8', 'A9': '\xA9', 'AA': '\xAA', 'AB': '\xAB', 'AC': '\xAC', 'AD': '\xAD',
					'AE': '\xAE', 'AF': '\xAF',

					'B0': '\xB0', 'B1': '\xB1', 'B2': '\xB2', 'B3': '\xB3', 'B4': '\xB4', 'B5': '\xB5', 'B6': '\xB6',
					'B7': '\xB7', 'B8': '\xB8', 'B9': '\xB9', 'BA': '\xBA', 'BB': '\xBB', 'BC': '\xBC', 'BD': '\xBD',
					'BE': '\xBE', 'BF': '\xBF',

					'C0': '\xC0', 'C1': '\xC1', 'C2': '\xC2', 'C3': '\xC3', 'C4': '\xC4', 'C5': '\xC5', 'C6': '\xC6',
					'C7': '\xC7', 'C8': '\xC8', 'C9': '\xC9', 'CA': '\xCA', 'CB': '\xCB', 'CC': '\xCC', 'CD': '\xCD',
					'CE': '\xCE', 'CF': '\xCF',

					'D0': '\xD0', 'D1': '\xD1', 'D2': '\xD2', 'D3': '\xD3', 'D4': '\xD4', 'D5': '\xD5', 'D6': '\xD6',
					'D7': '\xD7', 'D8': '\xD8', 'D9': '\xD9', 'DA': '\xDA', 'DB': '\xDB', 'DC': '\xDC', 'DD': '\xDD',
					'DE': '\xDE', 'DF': '\xDF',

					'E0': '\xE0', 'E1': '\xE1', 'E2': '\xE2', 'E3': '\xE3', 'E4': '\xE4', 'E5': '\xE5', 'E6': '\xE6',
					'E7': '\xE7', 'E8': '\xE8', 'E9': '\xE9', 'EA': '\xEA', 'EB': '\xEB', 'EC': '\xEC', 'ED': '\xED',
					'EE': '\xEE', 'EF': '\xEF',

					'F0': '\xF0', 'F1': '\xF1', 'F2': '\xF2', 'F3': '\xF3', 'F4': '\xF4', 'F5': '\xF5', 'F6': '\xF6',
					'F7': '\xF7', 'F8': '\xF8', 'F9': '\xF9', 'FA': '\xFA', 'FB': '\xFB', 'FC': '\xFC', 'FD': '\xFD',
					'FE': '\xFE', 'FF': '\xFF'}
		hexget = 'str'
		for i in range(0, len(goalstr), 2):
			try:
				if i == 0:
					hexget = hex_dict.get(goalstr[[i, i + 1]])
				else:
					hexget = hexget + hex_dict.get(goalstr[[i, i + 1]])
			except:
				pass
		return hexget

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
		QApplication.processEvents()
		case_dict = {
			"7501": self.terminal_signal_get(terminal_data=xbee_message.data.hex()[4:]),
			"7502": self.module_signal_get(module_data=xbee_message.data.hex()[4:]),
			"7503": self.establish_connection(address=xbee_message.data.hex()[4:])
		}
		return case_dict.get(xbee_message.data.hex()[0:4], 'No such method')

	def establish_connection(self, address):
		self.remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string(address))
		self.Raw802Device.send_data(self.remote_device,
									"\x75" + "\x03" + str(self.Raw802Device.get_64bit_addr()))
		QApplication.processEvents()

	def terminal_signal_get(self, terminal_data):  # 获得并显示系统当前的信息，默认电量信息在前，模组数量信息在后
		terminal_dict = {
			'电量': '???',
			'现有模组数': '???'
		}
		QApplication.processEvents()
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
		QApplication.processEvents()
		for i in range(0, int(module_data[0:2], 16)):
			self.ui.modulechoose.addItems(module_type.get(module_data[(2 + 4 * i):(4 + 4 * i)]))
			QApplication.processEvents()
		QApplication.processEvents()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
