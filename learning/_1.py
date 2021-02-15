#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/1/28 12:57
# Author  : RummySaltyfish

from digi.xbee.devices import RemoteXBeeDevice, Raw802Device
from digi.xbee.models.address import XBee64BitAddress

Raw802Device = Raw802Device("COM3", 115200)
Raw802Device.open()
remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string("0013A200415D2430"))
Raw802Device.send_data(remote_device, bin(117))
Raw802Device.close()
