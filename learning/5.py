#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2021/1/6 23:28
# Author  : RummySaltyfish

class MyCounter:
	__secretCount = 0
	publicCount = 0

	def __privateCountFun(self):
		print('This is a private method')
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)

	def publicCountFun(self):
		print('This is a public method')
		self.__privateCountFun()


if __name__ == '__main__':
	counter = MyCounter()
	counter.publicCountFun()
	counter.publicCountFun()
	print('instance publicCount=%d' % counter.publicCount)
	print('Class publicCount=%d' % MyCounter.publicCount)
