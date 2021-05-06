#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/5/6 20:04
# Author  : RummySaltyfish
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
import digi

Raw802Device = Raw802Device('COM3', 115200)
Raw802Device.open()
address=hex(int(str(Raw802Device.get_64bit_addr()), 16))
print(len(str(Raw802Device.get_64bit_addr())))
print(address)
Raw802Device.close()
