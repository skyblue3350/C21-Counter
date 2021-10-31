# -*- coding: utf-8 -*-

"""



"""

import sip
sip.setapi('QString', 2)

import os
import sys
import glob
import time

import datetime
import ConfigParser
import collections

import res_rc

from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow

class logWalker(QtCore.QThread):
	finish = QtCore.pyqtSignal(collections.OrderedDict)

	def __init__(self, parent=None):
		super(logWalker, self).__init__(parent)
		self.stopped = False
		self.mutex = QtCore.QMutex()

	def stop(self):
		with QtCore.QMutexLocker(self.mutex):
			self.stopped = True

	def load(self,mode):
		#モード
		self.mode = mode
		#検索系
		self.DUNGEON = u"定義/遺跡.txt"
		self.MISSION = u"定義/基地ミッション.txt"
		self.SUDDEN  = u"定義/突発ミッション.txt"
		self.count_search  = []
		self.count_text    = []
		self.count_counter = []
		#返り値統一
		self.countDic = collections.OrderedDict()

		#定義リスト読み込み
		if self.mode == u"遺跡":
			for text in open(self.DUNGEON,"r"):
				text = text.rstrip().decode("cp932").encode("utf-8").split("|")
				self.count_search.append(text[1])
				self.count_text.append(text[0])
				self.count_counter.append(0)
		elif self.mode == u"基地":
			for text in open(self.MISSION,"r"):
				text = text.rstrip().decode("cp932").encode("utf-8").split("|")
				self.count_search.append(text[1])
				self.count_text.append(text[0])
				self.count_counter.append(0)
		elif self.mode == u"突発":
			for text in open(self.SUDDEN,"r"):
				text = text.rstrip().decode("cp932").encode("utf-8").split("|")
				self.count_search.append(text[1])
				self.count_text.append(text[0])
				self.count_counter.append(0)


	def run(self):
		for file in self.filelist:
			self.count(file)
		self.finish.emit(self.countDic)

	def count(self, file):
		for text in open(file):
			text = text.decode("cp932").rstrip().encode("utf-8")
			textSplit = text.split()
			#エラー要因
			if len(textSplit) < 3:
				pass
			#遺跡
			elif self.mode == u"遺跡":
				if not textSplit[2] == "[INFO]":
					try:
						number = self.count_search.index(text[20:])
						self.count_counter[number] = self.count_counter[number] + 1
					except: pass
				for i in range(len(self.count_text)):
					self.countDic[self.count_text[i]] = self.count_counter[i]

			#撃破
			elif self.mode == u"撃破":
				if textSplit[2] == "[INFO]":
					if "を撃破した！" in text:
						mob = text[27:text.rfind("を撃破した！")]
						if not "が" in mob:
							if self.countDic.has_key(mob):
								self.countDic[mob] += 1
							else:
								self.countDic[mob]  = 1
			#取得/アイテム
			elif self.mode == u"取得/アイテム":
				if textSplit[2] == "[INFO]":
					if "取得した！" in text and "個" in text and not "が" in text:
						item = text[text.rfind("[")+1:text.rfind("]")]
						if self.countDic.has_key(item):
							self.countDic[item] += int(textSplit[5].replace("個","").decode("utf-8"))
						else:
							self.countDic[item]  = int(textSplit[5].replace("個","").decode("utf-8"))

			#取得/パーツ
			elif self.mode == u"取得/パーツ":
				if textSplit[2] == "[INFO]":
					if "を取得した！" in text:
						item = text[text.rfind("[")+1:text.rfind("を取得した！")-2]
						if self.countDic.has_key(item):
							self.countDic[item] += 1
						else:
							self.countDic[item]  = 1

			#取得/ギルドポイント
			elif self.mode == u"取得/ギルドポイント":
				if textSplit[2] == "[INFO]":
					if "ダンジョン成功報酬－ギルドポイント" in text:
						point = "ギルドポイント"
						if self.countDic.has_key(point):
							self.countDic[point] += int(textSplit[4].replace("+","").decode("utf-8"))
						else:
							self.countDic[point]  = int(textSplit[4].replace("+","").decode("utf-8"))

			#報酬/アイテム・パーツ
			elif self.mode == u"報酬/アイテム・パーツ":
				if textSplit[2] == "[INFO]":
					if "報酬－" in text and "x" in text and not "ダンジョン" in text:
						if textSplit[6] == "x":
							reward = textSplit[4] + " " + textSplit[5]
						else:
							reward = textSplit[4]

						if self.countDic.has_key(reward):
							if textSplit[6] == "x":
								self.countDic[reward] += int(textSplit[7])
							else:
								self.countDic[reward] += int(textSplit[6])
						else:
							if textSplit[6] == "x":
								self.countDic[reward]  = int(textSplit[7])
							else:
								self.countDic[reward]  = int(textSplit[6])

			#ガチャ
			elif self.mode == u"ガチャ":
				if textSplit[2] == "[INFO]":
					if "が当たりました！" in text:
						reward = text[text.rfind("[")+1:text.rfind("]")]
						if self.countDic.has_key(reward):
							self.countDic[reward] += 1
						else:
							self.countDic[reward]  = 1

			#基地
			elif self.mode == u"基地":
				if not textSplit[2] == "[INFO]":
					try:
						number = self.count_search.index(text[20:])
						self.count_counter[number] = self.count_counter[number] + 1
					except: pass
				for i in range(len(self.count_text)):
					self.countDic[self.count_text[i]] = self.count_counter[i]
			#突発
			elif self.mode == u"突発":
				if not textSplit[2] == "[INFO]":
					try:
						number = self.count_search.index(text[20:])
						self.count_counter[number] = self.count_counter[number] + 1
					except: pass
				for i in range(len(self.count_text)):
					self.countDic[self.count_text[i]] = self.count_counter[i]
			#ラボ
			elif self.mode == u"ラボ":
				if len(text.split()) < 6:
					pass
				elif textSplit[2] == "[INFO]":
					if "×" in text:
						labo = textSplit[3]
						num = 5
						if textSplit[5] == "×":
							labo = textSplit[3]+ " " + textSplit[4]
							num = 6
						if "を倒した！" in text:
							pass
						elif "取得した！" in text:
							pass
						elif self.countDic.has_key(labo):
							self.countDic[labo]+=int(textSplit[num].decode("utf-8"))
						else:
							print labo.decode("utf-8")
							print textSplit[5].decode("utf-8")
							print text.decode("utf-8")
							self.countDic[labo] = int(textSplit[num].decode("utf-8"))

			#検索
			elif self.mode == u"検索":
				skip = False

				#[INFO]をスキップ
				if self.checkInfo:
					if textSplit[2] == "[INFO]":
						skip = True

				#Userをスキップ
				if self.checkUser:
					if not textSplit[2] == "[INFO]":
						skip = True

				#スキップしないなら検索
				if not skip:
					if self.word in text:
						day = text[:20]
						word = text[20:]
						self.countDic[day] = word.decode("utf-8")

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.pushCount, QtCore.SIGNAL("clicked()"), self.pushCount)
		QtCore.QObject.connect(self.ui.pushSearch, QtCore.SIGNAL("clicked()"), self.pushCount)
		QtCore.QObject.connect(self.ui.radioGroup, QtCore.SIGNAL("buttonClicked(QAbstractButton*)"), self.radioGroup)
		QtCore.QObject.connect(self.ui.pushOption, QtCore.SIGNAL("clicked()"), self.pushOption)
		QtCore.QObject.connect(self.ui.lineSearch, QtCore.SIGNAL("textChanged(QString)"), self.textChanged)
		QtCore.QObject.connect(self.ui.pushOutput, QtCore.SIGNAL("clicked()"), self.pushOutput)
		QtCore.QObject.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.pushAbout)
		QtCore.QObject.connect(self.ui.actionHelp, QtCore.SIGNAL("triggered()"), self.pushHelp)
		QtCore.QObject.connect(self.ui.actionCopy, QtCore.SIGNAL("triggered()"), self.clipbord)
		QtCore.QObject.connect(self.ui.pushCapture, QtCore.SIGNAL("clicked()"), self.pushCapture)

		#UIの初期化
		self.ui.frameOption.hide()
		self.radioGroup()
		self.setupTarget()
		self.ui.treeResult.setColumnWidth(0,300)
		self.ui.treeSearch.setColumnWidth(0,200)

		#ソフトバージョン
		self.SOFTVER = u"β1.1"
		test = "aaa"
		test.decode("cp932").encode("utf-8")

	def setupTarget(self):
		self.ui.comboStart.clear()
		self.ui.comboEnd.clear()
		# { "日付":[ファイルURL,ファイルURL] }
		self.filelist = {}

		ini = ConfigParser.SafeConfigParser()

		#設定読み込み
		if os.path.isfile(u"設定.ini"):
			f = open(u"設定.ini", "r")
			ini.readfp(f)
			f.close()
			pathlist = ini.get('path','path').split(",")

		else:
			pathlist = ["C:\CyberStep\C21_Hangame\chat", "C:\CyberStep\C21\chat"]
			ini.add_section("path")
			ini.set("path","path","C:\CyberStep\C21_Hangame\chat,C:\CyberStep\C21\chat")
			f = open(u"設定.ini", "w")
			ini.write(f)

		for url in pathlist:
			for i in glob.glob(url+"\*.log"):
				day = i[i.rfind("\\")+1:]
				day = day[4:11].replace(u"_", u"年") + u"月" + day[11:13] + u"日"
				if self.filelist.has_key(day):
					self.filelist[day].append(i)
				else:
					self.filelist[day] = [i]

		for k,v in sorted(self.filelist.items()):
			self.ui.comboStart.insertItem(0,k)
			self.ui.comboEnd.insertItem(0,k)

	def textChanged(self, text):
		if text.strip() == u"":
			self.ui.pushSearch.setEnabled(False)
		else:
			self.ui.pushSearch.setEnabled(True)
			self.ui.labelText.setText(u"検索文字列　：　"+text)

	def clipbord(self):
		if self.ui.tabWidget.currentIndex() == 0:
			items = self.ui.treeResult.selectedItems()
		elif self.ui.tabWidget.currentIndex() == 1:
			items = self.ui.treeSearch.selectedItems()
		clip = ""
		for i in items:
			clip += i.text(0) + "\t" + i.text(1) + "\n"
		QtGui.qApp.clipboard().setText(clip)

	def pushCapture(self):
		d = datetime.datetime.now()
		day = d.strftime("%Y年%m月%d日")
		filename = day.decode("utf-8")+u".png"
		p = QtGui.QPixmap.grabWindow(self.winId())
		p.save(filename, 'png')

	def pushCount(self):
		self.parseList = []
		self.ui.treeResult.clear()
		self.ui.treeSearch.clear()

		start = self.ui.comboStart.currentText()
		end = self.ui.comboEnd.currentText()
		startTime =  datetime.datetime( int(start[0:4]), int(start[5:7]), int(start[8:10]) )
		endTime   =  datetime.datetime( int(end[0:4]),   int(end[5:7]),   int(end[8:10])   )

		#対象ファイル選定
		if self.ui.radioGroup.checkedButton().text() == u"すべて":
			for k,v in sorted(self.filelist.items()):
				self.parseList.extend(v)
		elif self.ui.radioGroup.checkedButton().text() == u"今日":
			d = datetime.datetime.now()
			day = d.strftime("%Y年%m月%d日").decode("utf-8")
			if self.filelist.has_key(day):
				self.parseList.extend(self.filelist[day])
			else:
				QtGui.QMessageBox.warning(self, u"エラー", u"ファイルが存在しません。")
				return
		elif self.ui.radioGroup.checkedButton().text() == u"指定した日":
			self.parseList.extend(self.filelist[self.ui.comboStart.currentText()])
		elif self.ui.radioGroup.checkedButton().text() == u"指定した期間":
			radioText = self.ui.radioGroup.checkedButton().text()
			if radioText == u"指定した期間":
				if startTime == endTime:
					QtGui.QMessageBox.warning(self, u"エラー", u"日付が同じです。")
					return
				elif start > end:
					QtGui.QMessageBox.warning(self, u"エラー", u"指定した期間が逆です。")
					return
				else:
					flag = None
					for k,v in sorted(self.filelist.items()):
						if k == self.ui.comboStart.currentText():
							flag = "start"
						elif k == self.ui.comboEnd.currentText():
							flag = "end"

						if flag == "start":
							for i in v:
								self.parseList.append(i)
						elif flag == "end":
							flag = None
							for i in v:
								self.parseList.append(i)

		#選択
		if self.ui.tabWidget.currentIndex() == 0 :
			self.select = self.ui.comboBox.currentText()
		elif self.ui.tabWidget.currentIndex() == 1 :
			self.select = u"検索"
			self.word = self.ui.lineSearch.text()

		#ボタン無効
		self.ui.pushCount.setEnabled(False)
		self.ui.pushSearch.setEnabled(False)
		self.ui.pushOutput.setEnabled(False)

		#結果リスト
		self.result = collections.OrderedDict()

		self.walker = logWalker()
		self.walker.load(self.select)
		self.walker.finish.connect(self.finish)
		self.walker.filelist = self.parseList
		if self.select == u"検索":
			self.walker.word = self.word.encode("utf-8")
			self.walker.checkInfo = self.ui.checkInfo.isChecked()
			self.walker.checkUser = self.ui.checkUser.isChecked()
		self.walker.start()

	def finish(self, result):
		self.result = result
		#ソート
		if not (self.select == u"遺跡" or self.select == u"基地" or self.select == u"突発"):
			self.ui.treeResult.setSortingEnabled(True)
		else:
			self.ui.treeResult.setSortingEnabled(False)

		#結果描画
		if self.select == u"検索":
			resultTarget = self.ui.treeSearch
			self.ui.labelSearch.setText(u"合致数　：　"+str(len(result)))
			self.ui.labelFile.setText(u"対象ファイル数　：　"+str(len(self.parseList)))
		else:
			resultTarget = self.ui.treeResult

		self.ui.pushCount.setEnabled(True)
		self.ui.pushSearch.setEnabled(True)
		self.ui.pushOutput.setEnabled(True)

		for k,v in result.items():
			if type(v) == int:v = str(v)
			list = QtGui.QTreeWidgetItem(resultTarget)
			list.setText(0, k.decode("utf-8"))
			list.setText(1, v)

	def radioGroup(self):
		text = self.ui.radioGroup.checkedButton().text()
		if (text == u"すべて") or (text == u"今日"):
			self.ui.comboStart.setEnabled(False)
			self.ui.comboEnd.setEnabled(False)
			self.ui.labelOption.setText(u"から")
		elif text == u"指定した日":
			self.ui.comboStart.setEnabled(True)
			self.ui.comboEnd.setEnabled(False)
			self.ui.labelOption.setText(u"の")
		elif text == u"指定した期間":
			self.ui.comboStart.setEnabled(True)
			self.ui.comboEnd.setEnabled(True)
			self.ui.labelOption.setText(u"から")

	def pushOption(self):
		if self.ui.frameOption.isHidden():
			self.ui.frameOption.show()
			self.setupTarget()
		else:
			self.ui.frameOption.hide()

	def pushOutput(self):

		d = datetime.datetime.now()
		day = d.strftime("%Y年%m月%d日")
		filename = day.decode("utf-8")+u"_"+self.select.replace("/","_")+u".txt"
		f = open(filename,"w")

		for k,v in self.result.items():
			if type(v) == int:v = str(v)
			f.write(k)
			f.write("\t")
			f.write(v.encode("utf-8"))
			f.write("\n")
		
		f.close

		self.ui.pushOutput.setEnabled(False)

	def pushHelp(self):
		QtGui.QMessageBox.about(self, u"ヘルプ",
				u"<b>使用方法</b><br>"
				u"カウントしたい対象を選択し、「カウント開始」を押すと計測を始めます。<br>"
				u"ログの量が多いと時間がかかりますがしばらくすると結果が表示されます。<br>"
				u"書き出す場合は右下にある「書き出し」を押すとこのソフト実行フォルダと同階層に今日の日付でテキストファイルが出力されます。"
				u"動作で問題があった場合は終了時にC21counter.exe.logが出力されますので、お手数ですがご報告お願いします。<br><br>"
				u"<b>ご意見・ご要望・不具合報告</b><br>"
				u"<a href='http://www.c21-online.jp/sns/?m=pc&a=page_f_home&target_c_member_id=12794'>鋼鉄戦記C21 SNS -戦場の突撃兵</a> までどうぞ"
				)

	def pushAbout(self):
		QtGui.QMessageBox.about(self, u"ソフトについて",
				u"<b>ソフト名：</b>C21Counter（名称なし）<br>"
				u"<b>作成者：</b>戦場の突撃兵<br>"
				u"<b>バージョン：</b>"+self.SOFTVER+"<br>"
				u"<b>問い合わせ：</b><a href='http://www.c21-online.jp/sns/?m=pc&a=page_f_home&target_c_member_id=12794'>鋼鉄戦記C21 SNS -戦場の突撃兵</a>"
				)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
	myapp = MainWindow()
	myapp.show()
	sys.exit(app.exec_())