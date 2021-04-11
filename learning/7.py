#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/3/2 20:26
# Author  : RummySaltyfish
from digi.xbee.devices import RemoteXBeeDevice, Raw802Device
from digi.xbee.models.address import XBee64BitAddress

Device802 = Raw802Device("COM3", 115200)
Device802.open()


def data_receive_callback(xbee_message):
	print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(), xbee_message.data.decode()))


Device802.add_data_received_callback(data_receive_callback)
Device802.close()
