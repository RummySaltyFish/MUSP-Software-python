#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 20:46
# @Author  : RummySaltyfish
import serial.tools.list_ports
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
import digi
ports = serial.tools.list_ports.comports()
result = []
for port in ports:
	try:
		s = serial.Serial(str(port)[0:4])
		s.close()
		Raw802Device=digi.xbee.devices.Raw802Device(str(port)[0:4],115200)
		Raw802Device.close()
	except (OSError, serial.SerialException):
		pass
