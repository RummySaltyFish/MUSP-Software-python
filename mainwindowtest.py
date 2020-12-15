# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import defines

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 2, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 3, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuModule = QtWidgets.QMenu(self.menubar)
        self.menuModule.setObjectName("menuModule")
        self.menusystem = QtWidgets.QMenu(self.menubar)
        self.menusystem.setObjectName("menusystem")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.actionsystem = QtWidgets.QAction(MainWindow)
        self.actionsystem.setObjectName("actionsystem")
        self.actionmodule = QtWidgets.QAction(MainWindow)
        self.actionmodule.setObjectName("actionmodule")
        self.actionrefreshsytem = QtWidgets.QAction(MainWindow)
        self.actionrefreshsytem.setObjectName("actionrefreshsytem")
        self.actionsystemgetsignal = QtWidgets.QAction(MainWindow)
        self.actionsystemgetsignal.setObjectName("actionsystemgetsignal")
        self.actionsystemrefresh = QtWidgets.QAction(MainWindow)
        self.actionsystemrefresh.setObjectName("actionsystemrefresh")
        self.actiongetmodule = QtWidgets.QAction(MainWindow)
        self.actiongetmodule.setObjectName("actiongetmodule")
        self.actionrefreshmodule = QtWidgets.QAction(MainWindow)
        self.actionrefreshmodule.setObjectName("actionrefreshmodule")
        self.actionNothing_Here = QtWidgets.QAction(MainWindow)
        self.actionNothing_Here.setObjectName("actionNothing_Here")
        self.menuFiles.addAction(self.Exit)
        self.menuModule.addAction(self.actiongetmodule)
        self.menuModule.addAction(self.actionrefreshmodule)
        self.menusystem.addAction(self.actionsystemgetsignal)
        self.menusystem.addAction(self.actionsystemrefresh)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menusystem.menuAction())
        self.menubar.addAction(self.menuModule.menuAction())

        self.retranslateUi(MainWindow)
        self.Exit.triggered.connect(MainWindow.close)

        """self.actionsystemgetsignal.triggered.connect(defines.terminalsignal())
        self.actionsystemrefresh.triggered.connect(defines.refreshsystem())
        self.actiongetmodule.triggered.connect(defines.getmodule())
        self.actionrefreshmodule.triggered.connect(defines.refreshmodule())"""
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "AllRefresh"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuModule.setTitle(_translate("MainWindow", "Module"))
        self.menusystem.setTitle(_translate("MainWindow", "system"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.actionsystem.setText(_translate("MainWindow", "system"))
        self.actionmodule.setText(_translate("MainWindow", "module"))
        self.actionrefreshsytem.setText(_translate("MainWindow", "refreshsytem"))
        self.actionsystemgetsignal.setText(_translate("MainWindow", "getsignal"))
        self.actionsystemrefresh.setText(_translate("MainWindow", "refresh"))
        self.actiongetmodule.setText(_translate("MainWindow", "Get"))
        self.actionrefreshmodule.setText(_translate("MainWindow", "refresh"))
        self.actionNothing_Here.setText(_translate("MainWindow", "Nothing Here!"))
