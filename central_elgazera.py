from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import mysql.connector
import datetime
from xlsxwriter import *
from xlrd import *
import humanize

MainUI,_ = loadUiType("central_elgazera.ui")
class Main(QMainWindow, MainUI):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.tabWidget.setCurrentIndex(0)
		self.handel_buttons()
		self.UI_Changes()
		self.db_connect()
		self.show_all_accessories()
		self.show_charge()
		self.show_machine()
		self.show_servies()
		self.accessories_bayment()
		self.show_all_tobacoo()
		self.tobacco_payment()

	def UI_Changes(self):
		self.tabWidget.tabBar().setVisible(False)

	def db_connect(self):
		self.db = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="htmlhtml", database="central_elgazera", use_unicode=True, charset="utf8")
		self.cur = self.db.cursor()

	def handel_buttons(self):
		self.pushButton_32.clicked.connect(self.open_login_tab)
		self.pushButton_6.clicked.connect(self.open_charge_tab)
		self.pushButton_7.clicked.connect(self.open_mobile_accessories_tab)
		self.pushButton_11.clicked.connect(self.open_tobacoo_tab)
		self.pushButton_12.clicked.connect(self.open_other_tab)
		self.pushButton_16.clicked.connect(self.open_wanted_tab)
		self.pushButton_28.clicked.connect(self.open_search_for_opration_tab)
		self.pushButton_8.clicked.connect(self.open_settings_tab)
		self.pushButton.clicked.connect(self.add_charge)
		self.pushButton_3.clicked.connect(self.add_accessories)
		self.pushButton_2.clicked.connect(self.del_charge)
		self.pushButton_5.clicked.connect(self.charge_info)
		self.pushButton_4.clicked.connect(self.del_accessories)
		self.pushButton_13.clicked.connect(self.info_accessories)
		self.pushButton_10.clicked.connect(self.add_tobacco)
		self.pushButton_34.clicked.connect(self.del_tobacco)
		self.pushButton_9.clicked.connect(self.info_tobacco)

	def load_date(self):
		date = datetime.datetime.now().date()
		return str(date)

	def load_date_time(self):
		date = datetime.datetime.now()
		return date

	def open_login_tab(self):
		self.tabWidget.setCurrentIndex(0)

	########################################################################
	###########################Charge Zone##################################
	########################################################################

	def open_charge_tab(self):
		self.tabWidget.setCurrentIndex(1)

	def show_machine(self):
		self.cur.execute("SELECT machine_name FROM machines")
		machines = self.cur.fetchall()
		for machine in machines:
			for m in machine:
				self.comboBox.addItem(m)

	def show_servies(self):
		self.cur.execute("""
				SELECT services_name FROM services
			""")
		services = self.cur.fetchall()
		for service in services:
			for s in service:
				self.comboBox_14.addItem(s)

	def show_charge(self):
		self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.cur.execute("""SELECT phone_number, value, _date, charge.order_id, services.services_name, machines.machine_name, employee.name FROM charge
							INNER JOIN employee ON charge.EmployeeID=employee.EmployeeID
							INNER JOIN machines ON charge.MachineID=machines.MachineID
							INNER JOIN services ON charge.serviceID=services.serviceID
							ORDER BY _date
			""")
		data = self.cur.fetchall()
		for row_index, row_data in enumerate(data):
			self.tableWidget.insertRow(row_index)
			for colm_index, colm_data in enumerate(row_data):
				self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
		self.tableWidget.resizeColumnsToContents()

	def add_charge(self):
		phone_number = self.lineEdit.text()
		value = float(self.lineEdit_2.text())
		self.cur.execute("""
				SELECT * FROM services WHERE services_name=%s
			""", (self.comboBox_14.currentText(),)
			)
		service_id = int(self.cur.fetchall()[0][0])
		date = self.load_date_time()
		emp_id = 1

		self.cur.execute("""
				SELECT * FROM machines WHERE machine_name=%s
			""",(self.comboBox.currentText(),)
			)
		machine_id = int(self.cur.fetchall()[0][0])
		sql = """
			INSERT INTO charge(phone_number, value, _date, serviceID, EmployeeID, MachineID)
			VALUES (%s, %s, %s, %s, %s, %s)
		"""
		data_inserted = [
			(phone_number),
			(value),
			(date),
			(service_id),
			(emp_id),
			(machine_id)
		]
		self.cur.execute(sql, data_inserted)
		self.db.commit()
		self.tableWidget.setRowCount(0)
		self.show_charge()

	def del_charge(self):
		try:
			info = []
			for currentQTableWidgetItem in self.tableWidget.selectedItems():
				info.append(currentQTableWidgetItem.text())
			number = info[0]
			order_num = int(info[3])
			self.cur.execute("""
					DELETE FROM charge WHERE phone_number=%s AND charge.order_id=%s
				""", (number, order_num))
			self.db.commit()
			self.tableWidget.setRowCount(0)
			self.show_charge()
		except:
			pass

	def charge_info(self):
		self.cur.execute("""
			SELECT value FROM charge
			""")
		values = self.cur.fetchall()
		total = 0
		for value in values:
			for v in value:
				total+= float(v)
		msg = QMessageBox()
		msg.setWindowTitle(" معلومات عن التحويلات")
		msg.setText(f"اجمالي تحويلات اليوم : {humanize.intword(total)}")
		msg.setIcon(QMessageBox.Information)
		msg.exec_()

	########################################################################
	#############################accessories zone###########################
	########################################################################

	def open_mobile_accessories_tab(self):
		self.tabWidget.setCurrentIndex(2)

	def show_all_accessories(self):
		self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
		sql = """
			SELECT * FROM accessories_stored
		"""
		self.cur.execute(sql)
		data = self.cur.fetchall()
		for accessories_name in data:
			self.comboBox_2.addItem(accessories_name[0])

	def accessories_bayment(self):
		self.cur.execute("""
				SELECT accessories.name, accessories.quantity, value, _date, accessories.order_id,employee.name  FROM accessories
				INNER JOIN employee ON accessories.EmployeeID=employee.EmployeeID
				ORDER BY _date
			""")
		data = self.cur.fetchall()
		for row_index, row_data in enumerate(data):
			self.tableWidget_2.insertRow(row_index)
			for colm_index, colm_data in enumerate(row_data):
				self.tableWidget_2.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
		self.tableWidget_2.resizeColumnsToContents()


	def add_accessories(self):
		accessories_name = self.comboBox_2.currentText()
		quantity = int(self.spinBox.text())
		emp_id = 1
		sql = """
				SELECT * FROM accessories_stored WHERE name=%s
		"""
		self.cur.execute(sql, [(accessories_name)])
		data = self.cur.fetchall()
		accessories_id = data[0][0]
		value = quantity * data[0][2]
		stored_accessories = data[0][3]- quantity
		date = self.load_date_time()
		if stored_accessories < 0:
			msg = QMessageBox()
			msg.setWindowTitle("اكسسوار")
			msg.setText(f"لقد نفذت الكمية من هذا المنتج")
			msg.setIcon(QMessageBox.Critical)
			msg.exec_()
		else:
			self.cur.execute("""
					INSERT INTO accessories(name, value, quantity, _date, EmployeeID)
					VALUES (%s, %s, %s, %s, %s)
				""",(accessories_name, value, quantity, date, emp_id))

			self.cur.execute("""
					UPDATE accessories_stored SET quantity=%s WHERE name=%s AND
				""", (stored_accessories, accessories_name))
			self.db.commit()
			self.tableWidget_2.setRowCount(0)
			self.accessories_bayment()

	def del_accessories(self):
		try:
			info = []
			for currentQTableWidgetItem in self.tableWidget_2.selectedItems():
				info.append(currentQTableWidgetItem.text())
			accessories_name = info[0]
			_datetime = info[3]
			quantity_back = int(info[1])
			self.cur.execute("""
					DELETE FROM accessories WHERE name=%s AND _date=%s
				""", (accessories_name, _datetime))
			self.cur.execute("""
					SELECT quantity FROM accessories_stored WHERE name=%s
				""",(accessories_name,))
			final = self.cur.fetchall()[0][0] + quantity_back
			self.cur.execute("""
					UPDATE accessories_stored SET quantity=%s WHERE name=%s
				""", (final, accessories_name))
			self.db.commit()
			self.tableWidget_2.setRowCount(0)
			self.accessories_bayment()
		except:
			pass

	def info_accessories(self):
		self.cur.execute("""
				SELECT value FROM accessories
			""")
		values = self.cur.fetchall()
		total = 0
		for value in values:
			for v in value:
				total +=v
		msg = QMessageBox()
		msg.setWindowTitle(" معلومات عن التحويلات")
		msg.setText(f"  اجمالي مبيعات اليوم : {humanize.intword(total)}")
		msg.setIcon(QMessageBox.Information)
		msg.exec_()

	########################################################################
	#############################tobacco zone###############################
	########################################################################

	def open_tobacoo_tab(self):
		self.tabWidget.setCurrentIndex(3)

	def show_all_tobacoo(self):
		self.cur.execute("""
				SELECT name FROM tobacco_stored
			""")
		tobacco_name = self.cur.fetchall()
		for toba in tobacco_name:
			self.comboBox_3.addItem(toba[0])

	def tobacco_payment(self):
		self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.cur.execute("""
				SELECT tobacco.name, value, num, _date, employee.name
				FROM tobacco
				INNER JOIN employee ON tobacco.EmployeeID=employee.EmployeeID
			""")
		data = self.cur.fetchall()
		for row_index, row_data in enumerate(data):
			self.tableWidget_3.insertRow(row_index)
			for colm_index, colm_data in enumerate(row_data):
				self.tableWidget_3.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
		self.tableWidget_3.resizeColumnsToContents()

	def add_tobacco(self):
		tobacco_name = self.comboBox_3.currentText()
		quantity = int(self.spinBox_2.text())
		self.cur.execute("""
				SELECT quantity, price FROM tobacco_stored WHERE name=%s
			""",(tobacco_name,))
		data = self.cur.fetchall()
		stored_tobacco = data[0][0] - quantity
		total_value = data[0][1] * quantity
		emp_id = 1
		_datetime = self.load_date_time()
		if stored_tobacco < 0:
			msg = QMessageBox()
			msg.setWindowTitle("سجاير")
			msg.setText(f"لقد نفذت الكمية من هذا المنتج")
			msg.setIcon(QMessageBox.Critical)
			msg.exec_()

		else:
			self.cur.execute("""
					INSERT INTO tobacco(name, value, num , _date, EmployeeID)
					VALUES (%s, %s, %s, %s, %s)
				""",(tobacco_name, total_value, quantity, _datetime, emp_id))
			self.cur.execute("""
					UPDATE tobacco_stored SET quantity=%s WHERE name=%s
				""",(stored_tobacco, tobacco_name) )
			self.db.commit()
			self.tableWidget_3.setRowCount(0)
			self.tobacco_payment()

	def del_tobacco(self):
		try:
			info = []
			for currentQTableWidgetItem in self.tableWidget_3.selectedItems():
				info.append(currentQTableWidgetItem.text())
			tobacco_name = info[0]
			_datetime = info[3]
			quantity_back = int(info[2])
			self.cur.execute("""
					DELETE FROM tobacco WHERE name=%s AND _date=%s
				""", (tobacco_name, _datetime))

			self.cur.execute("""
					SELECT quantity FROM tobacco_stored WHERE name=%s
				""",(tobacco_name,))

			final = self.cur.fetchall()[0][0] + quantity_back

			self.cur.execute("""
					UPDATE tobacco_stored SET quantity=%s WHERE name=%s
				""", (final, tobacco_name))
			self.db.commit()
			self.tableWidget_3.setRowCount(0)
			self.tobacco_payment()
		except:
			pass

	def info_tobacco(self):
		self.cur.execute("""
				SELECT value, num FROM tobacco
			""")
		data = self.cur.fetchall()
		total_num = 0
		total_value = 0
		for da in data:
			total_value += float(da[0])
			total_num += int(da[1])
		msg = QMessageBox()
		msg.setWindowTitle("سجاير")
		msg.setText(f"""
اجمالي مبيعات اليوم : {total_value}
اجمالى عدد العلب : {total_num}
			""")
		msg.setIcon(QMessageBox.Information)
		msg.exec_()

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
