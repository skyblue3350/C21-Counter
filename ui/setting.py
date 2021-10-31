# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created: Thu Feb 07 11:45:03 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingForm(object):
    def setupUi(self, SettingForm):
        SettingForm.setObjectName(_fromUtf8("SettingForm"))
        SettingForm.resize(433, 145)
        SettingForm.setMinimumSize(QtCore.QSize(433, 145))
        SettingForm.setMaximumSize(QtCore.QSize(433, 145))
        self.gridLayout = QtGui.QGridLayout(SettingForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Spin_update = QtGui.QSpinBox(SettingForm)
        self.Spin_update.setMinimum(30)
        self.Spin_update.setMaximum(180)
        self.Spin_update.setSingleStep(5)
        self.Spin_update.setObjectName(_fromUtf8("Spin_update"))
        self.gridLayout.addWidget(self.Spin_update, 3, 2, 1, 1)
        self.Label_logpath = QtGui.QLabel(SettingForm)
        self.Label_logpath.setObjectName(_fromUtf8("Label_logpath"))
        self.gridLayout.addWidget(self.Label_logpath, 4, 0, 1, 1)
        self.Line_path = QtGui.QLineEdit(SettingForm)
        self.Line_path.setObjectName(_fromUtf8("Line_path"))
        self.gridLayout.addWidget(self.Line_path, 4, 2, 1, 4)
        self.Button_save = QtGui.QPushButton(SettingForm)
        self.Button_save.setObjectName(_fromUtf8("Button_save"))
        self.gridLayout.addWidget(self.Button_save, 5, 4, 1, 1)
        self.Label_end = QtGui.QLabel(SettingForm)
        self.Label_end.setObjectName(_fromUtf8("Label_end"))
        self.gridLayout.addWidget(self.Label_end, 2, 5, 1, 1)
        self.Label_second = QtGui.QLabel(SettingForm)
        self.Label_second.setObjectName(_fromUtf8("Label_second"))
        self.gridLayout.addWidget(self.Label_second, 3, 3, 1, 1)
        self.Label_update = QtGui.QLabel(SettingForm)
        self.Label_update.setObjectName(_fromUtf8("Label_update"))
        self.gridLayout.addWidget(self.Label_update, 3, 0, 1, 1)
        self.Button_cancel = QtGui.QPushButton(SettingForm)
        self.Button_cancel.setObjectName(_fromUtf8("Button_cancel"))
        self.gridLayout.addWidget(self.Button_cancel, 5, 5, 1, 1)
        self.Box_start = QtGui.QComboBox(SettingForm)
        self.Box_start.setObjectName(_fromUtf8("Box_start"))
        self.gridLayout.addWidget(self.Box_start, 2, 2, 1, 1)
        self.Label_from = QtGui.QLabel(SettingForm)
        self.Label_from.setObjectName(_fromUtf8("Label_from"))
        self.gridLayout.addWidget(self.Label_from, 2, 3, 1, 1)
        self.Box_end = QtGui.QComboBox(SettingForm)
        self.Box_end.setObjectName(_fromUtf8("Box_end"))
        self.gridLayout.addWidget(self.Box_end, 2, 4, 1, 1)
        self.Box_select = QtGui.QComboBox(SettingForm)
        self.Box_select.setObjectName(_fromUtf8("Box_select"))
        self.Box_select.addItem(_fromUtf8(""))
        self.Box_select.addItem(_fromUtf8(""))
        self.Box_select.addItem(_fromUtf8(""))
        self.Box_select.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Box_select, 0, 2, 1, 1)
        self.Label_log = QtGui.QLabel(SettingForm)
        self.Label_log.setObjectName(_fromUtf8("Label_log"))
        self.gridLayout.addWidget(self.Label_log, 0, 0, 1, 1)
        self.Button_reset = QtGui.QPushButton(SettingForm)
        self.Button_reset.setObjectName(_fromUtf8("Button_reset"))
        self.gridLayout.addWidget(self.Button_reset, 5, 0, 1, 1)

        self.retranslateUi(SettingForm)
        QtCore.QObject.connect(self.Button_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingForm.close)
        QtCore.QObject.connect(self.Button_save, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingForm.close)
        QtCore.QMetaObject.connectSlotsByName(SettingForm)
        SettingForm.setTabOrder(self.Box_select, self.Box_start)
        SettingForm.setTabOrder(self.Box_start, self.Box_end)
        SettingForm.setTabOrder(self.Box_end, self.Spin_update)
        SettingForm.setTabOrder(self.Spin_update, self.Line_path)
        SettingForm.setTabOrder(self.Line_path, self.Button_save)
        SettingForm.setTabOrder(self.Button_save, self.Button_cancel)
        SettingForm.setTabOrder(self.Button_cancel, self.Button_reset)
        SettingForm.setTabOrder(self.Button_reset, self.Line_path)
        SettingForm.setTabOrder(self.Line_path, self.Box_select)
        SettingForm.setTabOrder(self.Box_select, self.Box_end)
        SettingForm.setTabOrder(self.Box_end, self.Spin_update)
        SettingForm.setTabOrder(self.Spin_update, self.Box_start)
        SettingForm.setTabOrder(self.Box_start, self.Button_cancel)
        SettingForm.setTabOrder(self.Button_cancel, self.Button_save)

    def retranslateUi(self, SettingForm):
        SettingForm.setWindowTitle(QtGui.QApplication.translate("SettingForm", "設定", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_logpath.setText(QtGui.QApplication.translate("SettingForm", "ログファイルパス　：　", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_save.setText(QtGui.QApplication.translate("SettingForm", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_end.setText(QtGui.QApplication.translate("SettingForm", "まで", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_second.setText(QtGui.QApplication.translate("SettingForm", "秒ごと", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_update.setText(QtGui.QApplication.translate("SettingForm", "自動更新　：　", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_cancel.setText(QtGui.QApplication.translate("SettingForm", "キャンセル", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_from.setText(QtGui.QApplication.translate("SettingForm", "から", None, QtGui.QApplication.UnicodeUTF8))
        self.Box_select.setItemText(0, QtGui.QApplication.translate("SettingForm", "すべて", None, QtGui.QApplication.UnicodeUTF8))
        self.Box_select.setItemText(1, QtGui.QApplication.translate("SettingForm", "今日", None, QtGui.QApplication.UnicodeUTF8))
        self.Box_select.setItemText(2, QtGui.QApplication.translate("SettingForm", "特定の１日", None, QtGui.QApplication.UnicodeUTF8))
        self.Box_select.setItemText(3, QtGui.QApplication.translate("SettingForm", "特定の期間", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_log.setText(QtGui.QApplication.translate("SettingForm", "対象ログファイル　：　", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_reset.setText(QtGui.QApplication.translate("SettingForm", "初期設定", None, QtGui.QApplication.UnicodeUTF8))

