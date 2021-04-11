#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/1/28 12:57
# Author  : RummySaltyfish

from digi.xbee.devices import RemoteXBeeDevice, Raw802Device
from digi.xbee.models.address import XBee64BitAddress

data_send = bin(25)
# Instantiate an XBee device object.
local_xbee = Raw802Device("COM3", 115200)
local_xbee.open()
remote_xbee = RemoteXBeeDevice(local_xbee, XBee64BitAddress.from_hex_string("0013A200415D2430"))
local_xbee.send_data(remote_xbee, data_send)
local_xbee.close()
