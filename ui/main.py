# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(652, 538)
        self.guitar = QtWidgets.QPushButton(widget)
        self.guitar.setGeometry(QtCore.QRect(90, 190, 121, 131))
        self.guitar.setObjectName("guitar")
        self.piano1 = QtWidgets.QPushButton(widget)
        self.piano1.setGeometry(QtCore.QRect(260, 190, 141, 131))
        self.piano1.setObjectName("piano1")
        self.piano2 = QtWidgets.QPushButton(widget)
        self.piano2.setGeometry(QtCore.QRect(430, 190, 141, 131))
        self.piano2.setObjectName("piano2")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.guitar.setText(_translate("widget", "吉他"))
        self.piano1.setText(_translate("widget", "C2_钢琴"))
        self.piano2.setText(_translate("widget", "C4_钢琴"))
