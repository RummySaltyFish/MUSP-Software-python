#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/2/28 20:29
# Author  : RummySaltyfish
from digi.xbee.devices import RemoteXBeeDevice, Raw802Device
from digi.xbee.models.address import XBee64BitAddress

# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM3"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 115200


def main():
    print(" +-----------------------------------------+")
    print(" | XBee Python Library Receive Data Sample |")
    print(" +-----------------------------------------+\n")

    device = Raw802Device(PORT, BAUD_RATE)


    try:
        device.open()

        def data_receive_callback(xbee_message):
            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                     type(xbee_message.data.hex())))

        device.add_data_received_callback(data_receive_callback)

        print("Waiting for data...\n")
        input()

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
