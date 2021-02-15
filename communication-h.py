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


# 通讯及控制类
class Communication(object):

	def broadcastConfirm(self):
		Raw802Device = digi.xbee.devices.Raw802Device("COM3", 115200)
		Raw802Device.open()
		Raw802Device.send_data_broadcast("u")#帧别码广播，0x75，十进制117
		Raw802Device.close()

	def terminalSignal(self):
		pass

	def refreshSystem(self):
		pass

	def getmodule(self):
		pass

	def refreshModule(self):
		pass

Communication()
Communication.broadcastConfirm(self=None)

