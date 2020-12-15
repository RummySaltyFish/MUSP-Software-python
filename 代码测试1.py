# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 166)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("YaHei Consolas Hybrid")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "对话框"))
        self.pushButton.setText(_translate("Form", "弹出对话框"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMsg)

    def showMsg(self):
        QMessageBox.information(self, '信息提示对话框','前方右拐到达目的地',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        QMessageBox.question(self, "提问对话框", "你要继续搞测试吗？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.warning(self, "警告对话框", "继续执行会导致系统重启，你确定要继续？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.critical(self, "严重错误对话框", "数组越界，程序异常退出", QMessageBox.Yes | QMessageBox.No,)
        QMessageBox.about(self, "关于对话框", "你的Windows系统是DOS1.0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())