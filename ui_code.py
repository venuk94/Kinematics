# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kinematics.ui'
#
# Created: Wed May 17 20:19:03 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(978, 717)
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.Theta1_1 = QtGui.QTabWidget(self.widget)
        self.Theta1_1.setGeometry(QtCore.QRect(0, 0, 979, 691))
        self.Theta1_1.setObjectName(_fromUtf8("Theta1_1"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.f_plot = MatplotlibWidget(self.tab)
        self.f_plot.setGeometry(QtCore.QRect(150, 5, 811, 641))
        self.f_plot.setObjectName(_fromUtf8("f_plot"))
        self.f_x = QtGui.QSpinBox(self.tab)
        self.f_x.setGeometry(QtCore.QRect(6, 45, 139, 22))
        self.f_x.setObjectName(_fromUtf8("f_x"))
        self.f_y = QtGui.QSpinBox(self.tab)
        self.f_y.setGeometry(QtCore.QRect(6, 95, 139, 22))
        self.f_y.setObjectName(_fromUtf8("f_y"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(66, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(66, 80, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.f_th1_1 = QtGui.QLineEdit(self.tab)
        self.f_th1_1.setGeometry(QtCore.QRect(18, 180, 113, 20))
        self.f_th1_1.setObjectName(_fromUtf8("f_th1_1"))
        self.f_th2_1 = QtGui.QLineEdit(self.tab)
        self.f_th2_1.setGeometry(QtCore.QRect(18, 225, 113, 20))
        self.f_th2_1.setObjectName(_fromUtf8("f_th2_1"))
        self.f_th1_2 = QtGui.QLineEdit(self.tab)
        self.f_th1_2.setGeometry(QtCore.QRect(18, 315, 113, 20))
        self.f_th1_2.setObjectName(_fromUtf8("f_th1_2"))
        self.f_th2_2 = QtGui.QLineEdit(self.tab)
        self.f_th2_2.setGeometry(QtCore.QRect(18, 360, 113, 20))
        self.f_th2_2.setObjectName(_fromUtf8("f_th2_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(54, 155, 55, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(54, 210, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(54, 290, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(54, 340, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.f_calc = QtGui.QPushButton(self.tab)
        self.f_calc.setGeometry(QtCore.QRect(0, 425, 145, 36))
        self.f_calc.setObjectName(_fromUtf8("f_calc"))
        self.Theta1_1.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.i_plot = MatplotlibWidget(self.tab_2)
        self.i_plot.setGeometry(QtCore.QRect(150, 0, 811, 641))
        self.i_plot.setObjectName(_fromUtf8("i_plot"))
        self.Theta1_1.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Theta1_1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "X", None))
        self.label_2.setText(_translate("MainWindow", "Y", None))
        self.label_3.setText(_translate("MainWindow", "Theta1_1", None))
        self.label_4.setText(_translate("MainWindow", "Theta2_1", None))
        self.label_5.setText(_translate("MainWindow", "Theta1_2", None))
        self.label_6.setText(_translate("MainWindow", "Theta2_2", None))
        self.f_calc.setText(_translate("MainWindow", "Calculate", None))
        self.Theta1_1.setTabText(self.Theta1_1.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.Theta1_1.setTabText(self.Theta1_1.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

from matplotlibwidget import MatplotlibWidget
