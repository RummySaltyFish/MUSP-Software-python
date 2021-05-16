#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/5/16 12:53
# Author  : RummySaltyfish
from digi.xbee.devices import Raw802Device, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress


# 平台端发送信息的内容格式为：帧头75，后接模式01或02或03，
# 若模式为01，则后接\x02表示有两种数据，随后接具体数据，01后为电量，02后为模组数
# 若模式为02，则后接模组数，再接具体模组编号，模组对应编号看module_signal_get函数
# 若模式为03，则直接后跟平台端地址

def switch_case(xbee_message):  # 根据发送的信息选择接收数据的内容
	case_dict = {
		'7501': terminal_signal_get(xbee_message.data.hex()[4:]),
		'7502': module_signal_get(xbee_message.data.hex()[4:]),
		'7503': establish_connection(xbee_message.data.hex()[4:])
	}
	return case_dict.get(xbee_message.data.hex()[0:4], 'No such method')


def establish_connection(address):  # 首次建立连接时使用，平台端接收到电脑端的地址即成功，但是python的16进制实在操蛋，字符串先将就着用用
	remote_device = RemoteXBeeDevice(Raw802Device, XBee64BitAddress.from_hex_string(address))
	Raw802Device.send_data(remote_device,
						   "\x75\x03" + str(Raw802Device.get_64bit_addr()))


def terminal_signal_get(terminal_data):  # 获得并显示系统当前的信息，默认电量信息在前，模组数量信息在后
	for i in range(0, int(terminal_data[0:2], 16)):
		if terminal_data[(2 + 4 * i):(4 + 4 * i)] == '01':  # ‘01’表示平台电量，默认其在前
			print('电量：' + str(int(terminal_data[4 + 4 * i:6 + 4 * i])))
		elif terminal_data[(2 + 4 * i):(4 + 4 * i)] == '02':  # ‘02’表示模组数量，默认在后
			print('现加载的模组数：' + str(int(terminal_data[4 + 4 * i:6 + 4 * i])))


def module_signal_get(module_data):
	module_type = {
		"01": "空气质量检测",
		"02": "环境温度检测"
	}
	for i in range(0, int(module_data[0:2], 16)):
		print(module_type.get(module_data[(2 + 4 * i):(4 + 4 * i)]))


mode_choose = 2333
while mode_choose != -1:
	com = input('给我自己输入接的哪个usb口，记得大写：')
	Raw802Device = Raw802Device(com, 115200)
	try:
		Raw802Device.open()
		Raw802Device.add_data_received_callback(switch_case)
		Raw802Device.close()
	finally:
		pass
	mode_choose = input('输入-1退出，不退出的话就随便输个数：')
