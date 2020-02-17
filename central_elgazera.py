from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import MySQLdb
import datetime
from xlsxwriter import *
from xlrd import *

MainUI,_ = loadUiType("central_elgazera.ui")
class Main(QMainWindow, MainUI):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.tabWidget.setCurrentIndex(0)
		self.handel_buttons()
		self.UI_Changes()

	def UI_Changes(self):
		self.tabWidget.tabBar().setVisible(False)

	def db_connect(self):
		pass

	def handel_buttons(self):
		self.pushButton_32.clicked.connect(self.open_login_tab)
		self.pushButton_6.clicked.connect(self.open_charge_tab)
		self.pushButton_7.clicked.connect(self.open_mobile_accessories_tab)
		self.pushButton_11.clicked.connect(self.open_tobacoo_tab)
		self.pushButton_12.clicked.connect(self.open_other_tab)
		self.pushButton_16.clicked.connect(self.open_wanted_tab)
		self.pushButton_28.clicked.connect(self.open_search_for_opration_tab)
		self.pushButton_8.clicked.connect(self.open_settings_tab)

	def open_login_tab(self):
		self.tabWidget.setCurrentIndex(0)

	def open_charge_tab(self):
		self.tabWidget.setCurrentIndex(1)

	def open_mobile_accessories_tab(self):
		self.tabWidget.setCurrentIndex(2)

	def open_tobacoo_tab(self):
		self.tabWidget.setCurrentIndex(3)

	def open_other_tab(self):
		self.tabWidget.setCurrentIndex(4)

	def open_wanted_tab(self):
		self.tabWidget.setCurrentIndex(5)

	def open_search_for_opration_tab(self):
		self.tabWidget.setCurrentIndex(6)

	def open_settings_tab(self):
		self.tabWidget.setCurrentIndex(7)



def main():
	app = QApplication(sys.argv)
	window = Main()
	window.show()
	app.exec_()

if __name__ == "__main__":
	main()
