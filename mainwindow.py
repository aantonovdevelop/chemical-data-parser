# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lstFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lstFiles.setObjectName("lstFiles")
        self.verticalLayout.addWidget(self.lstFiles)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtResult = QtWidgets.QTextEdit(self.centralwidget)
        self.txtResult.setObjectName("txtResult")
        self.verticalLayout.addWidget(self.txtResult)
        self.btnOpenDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenDirectory.setObjectName("btnOpenDirectory")
        self.verticalLayout.addWidget(self.btnOpenDirectory)
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setEnabled(False)
        self.btnExport.setObjectName("btnExport")
        self.verticalLayout.addWidget(self.btnExport)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Opened files:"))
        self.label.setText(_translate("MainWindow", "Result:"))
        self.btnOpenDirectory.setText(_translate("MainWindow", "Open Directory"))
        self.btnExport.setText(_translate("MainWindow", "Export"))

