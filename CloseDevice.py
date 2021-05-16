#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 20:46
# @Author  : RummySaltyfish
import serial.tools.list_ports
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
import digi

for port in serial.tools.list_ports.comports():
	try:
		s = serial.Serial(str(port)[0:4])
		s.close()
		Deviceclose = digi.xbee.devices.Raw802Device(str(port)[0:4], 115200)
		Deviceclose.close()
	except (OSError, serial.SerialException):
		pass
