#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 19:37
# @Author  : RummySaltyfish
# @File    : defines.py
# @Software: PyCharm
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import digi


# 通讯及控制类，暂时无用，功能均移至主线程
class Communication(object):
	def terminalSignal(self):  # 用于获取平台本身的信息
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, "!")  # 二进制：0010 0001,0010为每次发送时的帧别信息，0001为接收平台当前除模组信息外的信息
		Raw802Device.close()

	def refreshSystem(self):  # 用于刷新全部系统信息
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, " ")  # 二进制：0010 0000,0000为每次发送时的帧别信息，0000为接收平台所有信息
		Raw802Device.close()

	def getmodule(self):  # 要求平台发送模组信息，用于获得及刷新模组信息
		Raw802Device.open()
		remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
		Raw802Device.send_data(remote_device, "“")  # 二进制：0010 0010,前0010为每次发送时的帧别信息，后0010为接收平台当前模组信息
		Raw802Device.close()
