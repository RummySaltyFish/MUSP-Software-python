#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 20:46
# @Author  : RummySaltyfish
# @File    : 3.py
# @Software: PyCharm
# !/usr/bin/env python
#  -*- coding:utf-8 -*-

from PyQt5 import QtGui, Qt, QtCore


class GetIconDemo(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(GetIconDemo, self).__init__(parent)

        self.setWindowTitle(u"获取图标")
        self.setIconSize(Qt.QSize(50, 50))
        self.clicked.connect(self.getIconClick)

    def getIconClick(self):
        filename = unicode(QtGui.QFileDialog.getOpenFileName(self, u" 获取文件... " , '',  u'所有类型(*)'))
        if filename:
            icon, name = self.getFileInfo(filename)
            self.setIcon(icon)
            self.setText(name)

    def getFileInfo(self, filename):
        """获取文件的图片和名字"""
        fileInfo = Qt.QFileInfo(filename)
        fileIcon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(fileIcon.icon(fileInfo))
        name = QtCore.QFileInfo(filename).fileName()
        return icon, name


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = GetIconDemo()
    frm.show()
    sys.exit(app.exec_())