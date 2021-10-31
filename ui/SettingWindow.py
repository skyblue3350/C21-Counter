# -*- coding: utf-8 -*-

"""



"""

import sip
sip.setapi('QString', 2)

import os
import sys
import glob

import datetime
import ConfigParser

from PyQt4 import QtCore, QtGui
from ui import Ui_SettingForm

global APPPATH
APPPATH = os.path.dirname(os.path.abspath(sys.argv[0]))+"\\"

class SettingWindow(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		#初期化処理
		self.ui = Ui_SettingForm()
		self.ui.setupUi(self)
		self.ini = ConfigParser.SafeConfigParser()
		self.result = None
		self.PATH = ["C:\CyberStep\C21_Hangame\chat","C:\CyberStep\C21\chat"]

		#初期設定
		self.select = 0
		self.update = 180

		#アイコン
		#self.setWindowIcon(QtGui.QIcon(u"定義/mid.png"))

		#シグナル
		QtCore.QObject.connect(self.ui.Button_reset,QtCore.SIGNAL("clicked()"), self.reset)
		QtCore.QObject.connect(self.ui.Box_select,QtCore.SIGNAL("currentIndexChanged(QString)"), self.set)
		QtCore.QObject.connect(self.ui.Button_save,QtCore.SIGNAL("clicked()"), self.save)

		self.setup()

	def setup(self):
		#設定ファイルの存在確認　あったらパスを読み込む
		if os.path.isfile(APPPATH+"setting.ini"):
			f = open(APPPATH+"setting.ini", "r")
			self.ini.readfp(f)
			f.close()
			path = self.ini.get("path", "path")
			select = int(self.ini.get("setting", "select"))
			update = int(self.ini.get("setting", "update"))

			self.ui.Line_path.setText(path)
			self.ui.Box_select.setCurrentIndex(select)
			self.ui.Spin_update.setValue(update)

		#無ければ初期設定で書き出し
		else:
			self.ini.add_section("path")
			self.ini.add_section("setting")

			self.ini.set("path", "path",  self.pathlist())
			self.ini.set("setting", "select", str(self.select).encode("utf-8"))
			self.ini.set("setting", "update", str(self.update).encode("utf-8"))
			f = open(APPPATH+"setting.ini", "w")
			self.ini.write(f)
			f.close

			self.reset()

		self.check()

	#初期設定パスの存在確認する関数
	def pathlist(self,list=None):
		result = ""
		if list == None: list = self.PATH
		for i in list:
			if os.path.isdir(i):
				result += "," + i
		return result[1:]

	#初期化用関数
	def reset(self):
		self.ui.Box_select.setCurrentIndex(self.select)
		self.ui.Spin_update.setValue(self.update)
		result = self.pathlist()
		self.ui.Line_path.setText(result)

	def set(self,select):
		self.check()

	def check(self):
		select = self.ui.Box_select.currentText()
		if select == u"すべて":
			self.ui.Box_start.hide()
			self.ui.Box_end.hide()
			self.ui.Label_from.hide()
			self.ui.Label_end.hide()
		elif select == u"今日":
			self.ui.Box_start.hide()
			self.ui.Box_end.hide()
			self.ui.Label_from.hide()
			self.ui.Label_end.hide()
		elif select == u"特定の１日":
			self.ui.Box_end.hide()
			self.ui.Label_end.hide()
			self.ui.Box_start.show()
			self.ui.Label_from.show()
			self.ui.Label_from.setText(u"のログ")
		elif select == u"特定の期間":
			self.ui.Box_start.show()
			self.ui.Box_end.show()
			self.ui.Label_from.show()
			self.ui.Label_end.show()
			self.ui.Label_from.setText(u"から")
			self.ui.Label_end.setText(u"まで")

	def save(self):
		self.ini = ConfigParser.SafeConfigParser()
		self.ini.add_section("path")
		self.ini.add_section("setting")

		self.ini.set("path", "path",  self.ui.Line_path.text())
		self.ini.set("setting", "select", str(self.ui.Box_select.currentIndex()))
		self.ini.set("setting", "update", str(self.ui.Spin_update.value()))
		f = open(APPPATH+"setting.ini", "w")
		self.ini.write(f)
		f.close

		self.path = self.ui.Line_path.text()
		self.select = self.ui.Box_select.currentText()
		self.update = self.ui.Spin_update.value()

		self.result = "save"