#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/1/6 21:01
# Author  : RummySaltyfish

class Myclass:
	count = 0
	name = 'DefaultName'

	def __init__(self, name):
		self.name = name
		print('类的变量是%s\n对象的变量是%s' % (Myclass.name, self.name))

	def setCount(self, count):
		self.count = count

	def getCount(self):
		return self.count


if __name__ == "__main__":
	cls = Myclass('lisi')
	cls.setCount(10)
	print('count=%d' % cls.getCount())
