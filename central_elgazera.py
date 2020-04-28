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
import hashlib


MainUI, _ = loadUiType("central_elgazera.ui")


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
        self.show_cards()
        self.show_other()
        self.other_payment()
        self.show_wanted()
        self.show_emp()

    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    def db_connect(self):
        self.db = mysql.connector.connect(host="localhost", port=3306, user="root",
                                          passwd="htmlhtml", database="central_elgazera", use_unicode=True, charset="utf8")
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
        self.pushButton_14.clicked.connect(self.add_cards)
        self.pushButton_15.clicked.connect(self.cards_info)
        self.pushButton_18.clicked.connect(self.add_ele_cards)
        self.pushButton_17.clicked.connect(self.info_elec_cards)
        self.pushButton_22.clicked.connect(self.add_other)
        self.pushButton_49.clicked.connect(self.del_other)
        self.pushButton_21.clicked.connect(self.info_other)
        self.pushButton_19.clicked.connect(self.add_wanted)
        self.pushButton_20.clicked.connect(self.del_wanted)
        self.pushButton_54.clicked.connect(self.show_op)
        self.pushButton_51.clicked.connect(self.all_op)
        self.pushButton_33.clicked.connect(self.update_tobacco)
        self.pushButton_35.clicked.connect(self.update_accessories)
        self.pushButton_36.clicked.connect(self.update_other)
        self.pushButton_37.clicked.connect(self.add_new_tobacco)
        self.pushButton_38.clicked.connect(self.add_new_machine)
        self.pushButton_50.clicked.connect(self.add_new_service)
        self.pushButton_39.clicked.connect(self.add_new_accessories)
        self.pushButton_40.clicked.connect(self.add_new_other)
        self.comboBox_15.currentIndexChanged.connect(self.show_edit)
        self.pushButton_47.clicked.connect(self.edit)
        self.pushButton_48.clicked.connect(self.delete)
        self.pushButton_55.clicked.connect(self.add_new_cards_values)
        self.pushButton_41.clicked.connect(self.add_employee)
        self.pushButton_24.clicked.connect(self.display_emp)
        self.pushButton_43.clicked.connect(self.edit_employee)
        self.pushButton_52.clicked.connect(self.reports)

    def load_date(self):
        date = datetime.datetime.now().date()
        return str(date)

    def load_date_time(self):
        date = datetime.datetime.now()
        return date

    def load_time(self):
        _time = datetime.datetime.now().time()
        return _time

    def info_message(self, total):
        msg = QMessageBox()
        msg.setWindowTitle(" معلومات")
        msg.setText(f"  اجمالي مبيعات اليوم : {total}")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def empty_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("تحذير")
        msg.setText(f"{message}")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def open_login_tab(self):
        self.tabWidget.setCurrentIndex(0)

    ########################################################################
    ###########################Charge Zone##################################
    ########################################################################

    def open_charge_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def show_machine(self):
        self.cur.execute("SELECT machine_name FROM machines ORDER BY MachineID")
        machines = self.cur.fetchall()
        for machine in machines:
            for m in machine:
                self.comboBox.addItem(m)
                self.comboBox_9.addItem(m)

    def show_servies(self):
        self.comboBox_14.clear()
        self.cur.execute("""
				SELECT service_name FROM services ORDER BY serviceID
			""")
        services = self.cur.fetchall()
        for service in services:
            for s in service:
                self.comboBox_14.addItem(s)

    def show_charge(self):
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cur.execute("""SELECT phone_number, value, _date, charge.order_id, services.service_name, machines.machine_name, employee.name FROM charge
							INNER JOIN employee ON charge.EmployeeID=employee.EmployeeID
							INNER JOIN machines ON charge.MachineID=machines.MachineID
							INNER JOIN services ON charge.serviceID=services.serviceID
							WHERE _date=%s
							ORDER BY order_id
			""", (self.load_date(),))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget.resizeColumnsToContents()

    def add_charge(self):
        try:
            phone_number = self.lineEdit.text()
            if phone_number == "":
                self.empty_message("برجاء ادخال رقم المحمول")
            else:
                value = float(self.lineEdit_2.text())
                self.cur.execute("""
						SELECT * FROM services WHERE service_name=%s
					""", (self.comboBox_14.currentText(),)
                )
                service_id = int(self.cur.fetchall()[0][0])
                date = self.load_date_time()
                emp_id = 1

                self.cur.execute("""
						SELECT * FROM machines WHERE machine_name=%s
					""", (self.comboBox.currentText(),)
                )
                machine_id = int(self.cur.fetchall()[0][0])
                sql = """
					INSERT INTO charge(phone_number, value, _date, serviceID, EmployeeID, MachineID, _time)
					VALUES (%s, %s, %s, %s, %s, %s, %s)
				"""
                data_inserted = [
                    (phone_number),
                    (value),
                    (date),
                    (service_id),
                    (emp_id),
                    (machine_id),
                    (self.load_time())
                ]
                self.cur.execute(sql, data_inserted)
                self.db.commit()
                self.tableWidget.setRowCount(0)
                self.show_charge()
        except ValueError as e:
            self.empty_message("برجاء ادخال ارقام فقط")
            print(e)

    def del_charge(self):
        try:
            info = []
            for currentQTableWidgetItem in self.tableWidget.selectedItems():
                info.append(currentQTableWidgetItem.text())
            order_num = int(info[3])
            self.cur.execute("""
					DELETE FROM charge WHERE order_id=%s
				""", (order_num,))
            self.db.commit()
            self.tableWidget.setRowCount(0)
            self.show_charge()
        except:
            pass

    def charge_info(self):
        self.cur.execute("""
			SELECT value FROM charge WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0.0
        for value in values:
            total += value[0]
        self.info_message(total)

    ########################################################################
    #############################accessories zone###########################
    ########################################################################

    def open_mobile_accessories_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def show_all_accessories(self):
        self.comboBox_2.clear()
        self.comboBox_10.clear()
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        sql = """
			SELECT * FROM accessories_stored
		"""
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for accessories_name in data:
            self.comboBox_2.addItem(accessories_name[0])
            self.comboBox_10.addItem(accessories_name[0])

    def accessories_bayment(self):
        self.cur.execute("""
				SELECT accessories.name, accessories.quantity, value,  _date, accessories.order_id, employee.name  FROM accessories
				INNER JOIN employee ON accessories.EmployeeID=employee.EmployeeID
				WHERE _date=%s
				ORDER BY order_id
			""", (self.load_date(),))
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
        value = quantity * data[0][1]
        stored_accessories = data[0][2] - quantity
        date = self.load_date_time()
        if stored_accessories < 0:
            self.empty_message("لقد نفذت الكمية من هذا المنتج")
        else:
            self.cur.execute("""
					INSERT INTO accessories(name, value, quantity, _date, EmployeeID, _time)
					VALUES (%s, %s, %s, %s, %s, %s)
				""", (accessories_name, value, quantity, date, emp_id, self.load_time()))

            self.cur.execute("""
					UPDATE accessories_stored SET quantity=%s WHERE name=%s
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
            order_id = info[4]
            quantity_back = int(info[1])
            self.cur.execute("""
					DELETE FROM accessories WHERE order_id=%s
				""", (order_id,))
            self.cur.execute("""
					SELECT quantity FROM accessories_stored WHERE name=%s
				""", (accessories_name,))
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
				SELECT value FROM accessories WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            for v in value:
                total += v
        self.info_message(total)

    ########################################################################
    #############################tobacco zone###############################
    ########################################################################

    def open_tobacoo_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def show_all_tobacoo(self):
        self.comboBox_3.clear()
        self.comboBox_8.clear()
        self.cur.execute("""
				SELECT name FROM tobacco_stored
			""")
        tobacco_name = self.cur.fetchall()
        for toba in tobacco_name:
            self.comboBox_3.addItem(toba[0])
            self.comboBox_8.addItem(toba[0])

    def tobacco_payment(self):
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cur.execute("""
				SELECT tobacco.name, value, num, _date, tobacco.order_id, employee.name
				FROM tobacco
				INNER JOIN employee ON tobacco.EmployeeID=employee.EmployeeID
				WHERE _date=%s
				ORDER BY tobacco.order_id
			""", (self.load_date(),))
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
			""", (tobacco_name,))
        data = self.cur.fetchall()
        stored_tobacco = data[0][0] - quantity
        total_value = data[0][1] * quantity
        emp_id = 1
        _datetime = self.load_date_time()
        if stored_tobacco < 0:
            self.empty_message("لقد نفذت الكمية من هذا المنتج")

        else:
            self.cur.execute("""
					INSERT INTO tobacco(name, value, num , _date, EmployeeID, _time)
					VALUES (%s, %s, %s, %s, %s, %s)
				""", (tobacco_name, total_value, quantity, _datetime, emp_id, self.load_time()))
            self.cur.execute("""
					UPDATE tobacco_stored SET quantity=%s WHERE name=%s
				""", (stored_tobacco, tobacco_name))
            self.db.commit()
            self.tableWidget_3.setRowCount(0)
            self.tobacco_payment()

    def del_tobacco(self):
        try:
            info = []
            for currentQTableWidgetItem in self.tableWidget_3.selectedItems():
                info.append(currentQTableWidgetItem.text())
            tobacco_name = info[0]
            order_id = info[4]
            quantity_back = int(info[2])
            self.cur.execute("""
					DELETE FROM tobacco WHERE order_id=%s
				""", (order_id,))

            self.cur.execute("""
					SELECT quantity FROM tobacco_stored WHERE name=%s
				""", (tobacco_name,))

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
				SELECT value, num FROM tobacco WHERE _date=%s
			""", (self.load_date(),))
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

    ########################################################################
    ##############################other zone################################
    ########################################################################
    def show_cards(self):
        self.comboBox_4.clear()
        self.comboBox_5.clear()
        self.cur.execute("""
			SELECT * FROM company_names
			""")
        company_names = self.cur.fetchall()
        all_company = []
        for name in company_names:
            all_company.append(str(name[1]))
        self.cur.execute("""
			SELECT * FROM vodafone_cards_values
			""")
        vodafone_values = self.cur.fetchall()
        vodafone = []
        for v in vodafone_values:
            vodafone.append(str(v[1]))
        self.cur.execute("""
			SELECT * FROM orange_cards_values
			""")
        orange_values = self.cur.fetchall()
        orange = []
        for o in orange_values:
            orange.append(str(o[1]))
        self.cur.execute("""
			SELECT * FROM etisalat_cards_values
			""")
        etisalat_values = self.cur.fetchall()
        etisalat = []
        for e in etisalat_values:
            etisalat.append(str(e[1]))
        self.cur.execute("""
			SELECT * FROM WE_cards_values
			""")
        WE_values = self.cur.fetchall()
        WE = []
        for w in WE_values:
            WE.append(str(w[1]))
        self.comboBox_4.addItem(all_company[0], WE)
        self.comboBox_4.addItem(all_company[1], etisalat)
        self.comboBox_4.addItem(all_company[2], orange)
        self.comboBox_4.addItem(all_company[3], vodafone)
        self.comboBox_4.currentIndexChanged.connect(self.indexChanged)
        self.indexChanged(self.comboBox_4.currentIndex())

    def indexChanged(self, index):
        self.comboBox_5.clear()
        data = self.comboBox_4.itemData(index)
        if data is not None:
            self.comboBox_5.addItems(data)

    def add_cards(self):
        card_name = self.comboBox_4.currentText()
        card_value = float(self.comboBox_5.currentText())
        card_quantity = int(self.spinBox_3.text())
        emp = 1
        machine = 1
        self.cur.execute("""
				INSERT INTO phone_cards (company_name, value, quantity, EmployeeID, MachineID, _date, _time)
				VALUES (%s, %s, %s, %s, %s, %s, %s)
			""", (card_name, card_value, card_quantity, emp, machine, self.load_date(), self.load_time()))
        self.db.commit()

    def cards_info(self):
        self.cur.execute("""
				SELECT value FROM phone_cards WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            total += float(value[0])
        self.info_message(total)

    def add_ele_cards(self):
        try:
            client_number = self.lineEdit_9.text()
            value = float(self.lineEdit_3.text())
            machine_name = self.comboBox_9.currentText()
            if client_number == "":
                self.empty_message("ربجاء ادخال رقم العميل")
            else:
                op_type = "شحن كرت كهربا"
                self.cur.execute("""
						SELECT MachineID FROM machines WHERE machine_name=%s
					""", (machine_name, ))
                machine_id = self.cur.fetchall()[0][0]
                emp = 1
                self.cur.execute("""
						INSERT INTO elec_cards(client_number, value, type, _date, EmployeeID, MachineID, _time)
						VALUES (%s, %s, %s, %s, %s, %s, %s)
					""", (client_number, value, op_type, self.load_date(), emp, machine_id, self.load_time()))
                self.db.commit()
        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")

    def info_elec_cards(self):
        self.cur.execute("""
			SELECT value FROM elec_cards WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            total += float(value[0])
        self.info_message(total)

    def show_other(self):
        self.comboBox_11.clear()
        self.comboBox_6.clear()
        self.cur.execute("""
				SELECT other_name FROM other_stored ORDER BY otherID
			""")
        names = self.cur.fetchall()
        for name in names:
            self.comboBox_6.addItem(name[0])
            self.comboBox_11.addItem(name[0])

    def other_payment(self):
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cur.execute("""
				SELECT other.name, value, num, _date, other.order_id, employee.name
				FROM other
				INNER JOIN employee ON other.EmployeeID=employee.EmployeeID
				WHERE _date=%s
				ORDER BY other.order_id
			""", (self.load_date(), ))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget_5.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_5.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_5.resizeColumnsToContents()

    def add_other(self):
        name = self.comboBox_6.currentText()
        quantity = int(self.spinBox_4.text())
        self.cur.execute("""
				SELECT price, quantity FROM other_stored WHERE other_name=%s
			""", (name,))
        data = self.cur.fetchall()
        price = data[0][0]
        quantity_stored = data[0][1] - quantity
        total_value = quantity * price
        emp = 1
        if quantity_stored < 0:
            self.empty_message("لقد نفذت الكمية من هذا المنتج")
        else:
            self.cur.execute("""
					INSERT INTO other(name, num, value, _date, _time, EmployeeID)
					VALUES (%s, %s, %s, %s, %s, %s)
				""", (name, quantity, total_value, self.load_date(), self.load_time(), emp))
            self.cur.execute("""
					UPDATE other_stored SET quantity=%s WHERE other_name=%s
				""", (quantity_stored, name))
            self.db.commit()
            self.tableWidget_5.setRowCount(0)
            self.other_payment()

    def del_other(self):
        info = []
        for currentQTableWidgetItem in self.tableWidget_5.selectedItems():
            info.append(currentQTableWidgetItem.text())
        other_name = info[0]
        order_id = info[4]
        quantity_back = int(info[2])
        self.cur.execute("""
				DELETE FROM other WHERE order_id=%s
			""", (order_id,))

        self.cur.execute("""
				SELECT quantity FROM other_stored WHERE other_name=%s
			""", (other_name,))

        final = self.cur.fetchall()[0][0] + quantity_back

        self.cur.execute("""
				UPDATE other_stored SET quantity=%s WHERE other_name=%s
			""", (final, other_name))
        self.db.commit()
        self.tableWidget_5.setRowCount(0)
        self.other_payment()

    def info_other(self):
        self.cur.execute("""
				SELECT value FROM other WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            total += float(value[0])
        self.info_message(total)

    def open_other_tab(self):
        self.tabWidget.setCurrentIndex(4)

    ########################################################################
    ##############################wanted zone###############################
    ########################################################################

    def open_wanted_tab(self):
        self.tabWidget.setCurrentIndex(5)

    def show_wanted(self):
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cur.execute("""
				SELECT client_name, value, order_id, _date, TIME_FORMAT(_time, "%H:%i  %p"), employee.name
				FROM wanted
				INNER JOIN employee ON wanted.EmployeeID=employee.EmployeeID
				ORDER BY order_id
			""")
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget_4.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_4.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_4.resizeColumnsToContents()

    def add_wanted(self):
        try:
            name = self.lineEdit_4.text()
            if name == "":
                self.empty_message("رجاء ادخال اسم العميل")
            else:
                value = float(self.lineEdit_5.text())
                emp = 1
                self.cur.execute("""
						INSERT INTO wanted(client_name, value, _date, _time, EmployeeID)
						VALUES (%s, %s, %s, %s, %s)
					""", (name, value, self.load_date(), self.load_time(), emp))
                self.db.commit()
                self.tableWidget_4.setRowCount(0)
                self.show_wanted()

        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")

    def del_wanted(self):
        info = []
        for currentQTableWidgetItem in self.tableWidget_4.selectedItems():
            info.append(currentQTableWidgetItem.text())
        order_id = info[2]
        name = info[0]
        self.cur.execute("""
			DELETE FROM wanted WHERE order_id=%s AND client_name=%s
			""", (order_id, name))
        self.db.commit()
        self.tableWidget_4.setRowCount(0)
        self.show_wanted()
    ########################################################################
    ##############################op zone###################################
    ########################################################################

    def show_op(self):
        self.tableWidget_11.setRowCount(0)
        number = self.lineEdit_22.text()
        if number == "":
            self.empty_message("رجاء ادخال اسم العميل")
        else:
            _from = self.dateEdit_11.date().toString("yyyy-MM-dd")
            _to = self.dateEdit_10.date().toString("yyyy-MM-dd")
            self.cur.execute("""
    				SELECT phone_number, value, _date, TIME_FORMAT(_time, "%H:%i  %p"), services.service_name, employee.name, machines.machine_name
    				FROM charge
    				INNER JOIN employee ON charge.EmployeeID=employee.EmployeeID
    				INNER JOIN services ON charge.serviceID=services.serviceID
    				INNER JOIN machines ON charge.MachineID=machines.MachineID
    				WHERE phone_number=%s AND _date BETWEEN %s AND %s
    				ORDER BY _time
    			""", (number, _from, _to))
            data = self.cur.fetchall()
            if data == []:
                self.empty_message("العملية غير موجودة")
            else:
                for row_index, row_data in enumerate(data):
                    self.tableWidget_11.insertRow(row_index)
                    for colm_index, colm_data in enumerate(row_data):
                        self.tableWidget_11.setItem(row_index, colm_index,
                                                    QTableWidgetItem(str(colm_data)))
                self.tableWidget_11.resizeColumnsToContents()

    def all_op(self):
        self.tableWidget_9.setRowCount(0)
        _from = self.dateEdit_12.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_13.date().toString("yyyy-MM-dd")
        self.cur.execute("""
				SELECT phone_number, value, _date, TIME_FORMAT(_time, "%H:%i  %p"), services.service_name, employee.name, machines.machine_name
				FROM charge
				INNER JOIN employee ON charge.EmployeeID=employee.EmployeeID
				INNER JOIN services ON charge.serviceID=services.serviceID
				INNER JOIN machines ON charge.MachineID=machines.MachineID
				WHERE _date BETWEEN %s AND %s
				ORDER BY _time
			""", (_from, _to))
        data = self.cur.fetchall()
        if data == []:
            self.empty_message("العمليات غير موجودة")
        else:
            for row_index, row_data in enumerate(data):
                self.tableWidget_9.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_9.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_9.resizeColumnsToContents()

    def open_search_for_opration_tab(self):
        self.tabWidget.setCurrentIndex(6)
    ########################################################################
    ##############################settings zone#############################
    ########################################################################

    def update_tobacco(self):
        name = self.comboBox_8.currentText()
        quantity = int(self.spinBox_5.text())
        self.cur.execute("""
			SELECT quantity FROM tobacco_stored WHERE name=%s
		""", (name,))
        new_stored = self.cur.fetchall()[0][0] + quantity
        self.cur.execute("""
			UPDATE tobacco_stored SET quantity=%s WHERE name=%s
		""", (new_stored, name))
        self.db.commit()

    def update_accessories(self):
        name = self.comboBox_10.currentText()
        quantity = int(self.spinBox_6.text())
        self.cur.execute("""
			SELECT quantity FROM accessories_stored WHERE name=%s
		""", (name,))
        new_stored = self.cur.fetchall()[0][0] + quantity
        self.cur.execute("""
			UPDATE accessories_stored SET quantity=%s WHERE name=%s
		""", (new_stored, name))
        self.db.commit()

    def update_other(self):
        name = self.comboBox_11.currentText()
        quantity = int(self.spinBox_7.text())
        self.cur.execute("""
			SELECT quantity FROM other_stored WHERE other_name=%s
		""", (name,))
        new_stored = self.cur.fetchall()[0][0] + quantity
        self.cur.execute("""
			UPDATE other_stored SET quantity=%s WHERE other_name=%s
		""", (new_stored, name))
        self.db.commit()

    def add_new_tobacco(self):
        name = self.lineEdit_10.text()
        if name == "":
            self.empty_message("برجاء ادخال اسم المنتج")
        else:
            try:
                price = float(self.lineEdit_11.text())
                quantity = int(self.spinBox_8.text())
                self.cur.execute("""
                		INSERT INTO tobacco_stored(name, quantity, price)
                		VALUES (%s, %s, %s);
                	""", (name, quantity, price))
                self.db.commit()
                self.comboBox_8.clear()
                self.comboBox_3.clear()
                self.show_all_tobacoo()
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")

    def add_new_machine(self):
        name = self.lineEdit_12.text()
        if name == "":
            self.empty_message("برجاء ادخال اسم الماكينة")
        else:
            try:
                self.cur.execute("""
    				INSERT INTO machines(machine_name)
    				VALUES (%s);
    			""", (name,))
                self.db.commit()
                self.comboBox.clear()
                self.comboBox_9.clear()
                self.show_machine()
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذه الماكينة موجودة من قبل")

    def add_new_service(self):
        name = self.lineEdit_20.text()
        if name == "":
            self.empty_message("برجاء الدخال اسم الخدمة")
        else:
            try:
                self.cur.execute("""
    				INSERT INTO services(service_name)
    				VALUES (%s);
    			""", (name,))
                self.db.commit()
                self.comboBox_14.clear()
                self.show_servies()
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذه الخدمة موجودة من قبل")

    def add_new_cards_values(self):
        try:
            value = float(self.lineEdit_21.text())
            company_name = self.comboBox_7.currentText()
            if company_name == "فودافون":
                self.cur.execute("""
                    INSERT INTO vodafone_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
                self.db.commit()
            elif company_name == "اورنج":
                self.cur.execute("""
                    INSERT INTO orange_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
            elif company_name == "اتصالات":
                self.cur.execute("""
                    INSERT INTO etisalat_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
            elif company_name == "WE":
                self.cur.execute("""
                    INSERT INTO WE_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
            self.show_cards()
        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")

    def add_new_accessories(self):
        name = self.lineEdit_14.text()
        if name == "":
            self.empty_message("ربجاء ادخال اسم المنتج")
        else:
            try:
                price = int(self.lineEdit_13.text())
                quantity = int(self.spinBox_9.text())
                self.cur.execute("""
        				INSERT INTO accessories_stored(name, price, quantity)
        				VALUES (%s, %s, %s);
        			""", (name, price, quantity))
                self.db.commit()
                self.comboBox_2.clear()
                self.comboBox_10.clear()
                self.show_all_accessories()
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")

    def add_new_other(self):
        name = self.lineEdit_16.text()
        if name == "":
            self.empty_message("برجاء ادخال اسم المنتج")
        else:
            try:
                price = float(self.lineEdit_15.text())
                quantity = int(self.spinBox_10.text())
                self.cur.execute("""
        				INSERT INTO other_stored(other_name, price, quantity)
        				VALUES (%s, %s, %s);
        			""", (name, price, quantity))
                self.db.commit()
                self.comboBox_6.clear()
                self.comboBox_11.clear()
                self.show_other()
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")

    def show_edit(self):
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectRows)
        category = self.comboBox_15.currentText()
        if category == "سجاير":
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setHorizontalHeaderLabels(["اسم المنتج", "سعر المنتج", "المخزون"])
            self.cur.execute("""
                    SELECT name, price, quantity FROM tobacco_stored
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "اكسسوارات محمول":
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setHorizontalHeaderLabels(["اسم المنتج", "سعر المنتج", "المخزون"])
            self.cur.execute("""
                    SELECT * FROM accessories_stored
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "اخرى":
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setHorizontalHeaderLabels(["اسم المنتج", "سعر المنتج", "المخزون"])
            self.cur.execute("""
                    SELECT other_name, price, quantity FROM other_stored
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "كروت فودافون":
            self.tableWidget_6.setColumnCount(2)
            self.tableWidget_6.setHorizontalHeaderLabels(["كود الكرت", "سعر الكرت"])
            self.cur.execute("""
                    SELECT * FROM vodafone_cards_values
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "كروت اورنج":
            self.tableWidget_6.setColumnCount(2)
            self.tableWidget_6.setHorizontalHeaderLabels(["كود الكرت", "سعر الكرت"])
            self.cur.execute("""
                    SELECT * FROM orange_cards_values
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "كروت اتصالات":
            self.tableWidget_6.setColumnCount(2)
            self.tableWidget_6.setHorizontalHeaderLabels(["كود الكرت", "سعر الكرت"])
            self.cur.execute("""
                    SELECT * FROM etisalat_cards_values
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "كروت WE":
            self.tableWidget_6.setColumnCount(2)
            self.tableWidget_6.setHorizontalHeaderLabels(["كود الكرت", "سعر الكرت"])
            self.cur.execute("""
                    SELECT * FROM WE_cards_values
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        elif category == "خدمات":
            self.tableWidget_6.setColumnCount(2)
            self.tableWidget_6.setHorizontalHeaderLabels(["كود الخدمة", "اسم الخدمة"])
            self.cur.execute("""
                    SELECT serviceID, service_name FROM services ORDER BY serviceID
            """)
            data = self.cur.fetchall()
            for row_index, row_data in enumerate(data):
                self.tableWidget_6.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget_6.setItem(row_index, colm_index,
                                               QTableWidgetItem(str(colm_data)))
            self.tableWidget_6.resizeColumnsToContents()
        else:
            pass

    def edit(self):
        try:
            category = self.comboBox_15.currentText()
            info = []
            for currentQTableWidgetItem in self.tableWidget_6.selectedItems():
                info.append(currentQTableWidgetItem.text())
            name = info[0]
            price = info[1]
            if category == "سجاير":
                quantity = info[2]
                self.cur.execute("""
                    UPDATE tobacco_stored SET name=%s, price=%s, quantity=%s WHERE name=%s
                """, (name, price, quantity, name))
                self.db.commit()
            elif category == "اكسسوارات محمول":
                quantity = info[2]
                self.cur.execute("""
                    UPDATE accessories_stored SET name=%s, price=%s, quantity=%s WHERE name=%s
                """, (name, price, quantity, name))
                self.db.commit()
            elif category == "اخرى":
                quantity = info[2]
                self.cur.execute("""
                    UPDATE other_stored SET other_name=%s, price=%s, quantity=%s WHERE other_name=%s
                """, (name, price, quantity, name))
                self.db.commit()
            elif category == "كروت فودافون":
                self.cur.execute("""
                    UPDATE vodafone_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
            elif category == "كروت اورنج":
                self.cur.execute("""
                    UPDATE orange_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
            elif category == "كروت اتصالات":
                self.cur.execute("""
                    UPDATE etisalat_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
            elif category == "كروت WE":
                self.cur.execute("""
                    UPDATE WE_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
            elif category == "خدمات":
                self.cur.execute("""
                    UPDATE services SET service_name=%s WHERE serviceID=%s
                """, (price, name))
                self.db.commit()
                self.show_servies()
            else:
                pass
        except:
            self.empty_message("برجاء تحديد القيمة المراد تعديلها")

    def delete(self):
        try:
            category = self.comboBox_15.currentText()
            info = []
            for currentQTableWidgetItem in self.tableWidget_6.selectedItems():
                info.append(currentQTableWidgetItem.text())
            name = info[0]
            if category == "سجاير":
                self.cur.execute("""
                    DELETE FROM tobacco_stored WHERE name=%s
                """, (name,))
                self.db.commit()
                self.show_all_tobacoo()
            elif category == "اكسسوارات محمول":
                self.cur.execute("""
                    DELETE FROM accessories_stored WHERE name=%s
                """, (name,))
                self.db.commit()
                self.show_all_accessories()
            elif category == "اخرى":
                self.cur.execute("""
                    DELETE FROM other_stored WHERE other_name=%s
                """, (info[0],))
                self.db.commit()
                self.show_other()
            elif category == "كروت فودافون":
                self.cur.execute("""
                    DELETE FROM vodafone_cards_values WHERE cardID=%s
                """, (info[0],))
                self.db.commit()
                self.show_cards()
            elif category == "كروت اورنج":
                self.cur.execute("""
                    DELETE FROM orange_cards_values WHERE cardID=%s
                """, (info[0],))
                self.db.commit()
                self.show_cards()
            elif category == "كروت اتصالات":
                self.cur.execute("""
                    DELETE FROM etisalat_cards_values WHERE cardID=%s
                """, (info[0],))
                self.db.commit()
                self.show_cards()
            elif category == "كروت WE":
                self.cur.execute("""
                    DELETE FROM WE_cards_values WHERE cardID=%s
                """, (info[0],))
                self.db.commit()
                self.show_cards()
            elif category == "خدمات":
                self.cur.execute("""
                    DELETE FROM services WHERE serviceID=%s
                """, (info[0],))
                self.db.commit()
                self.show_servies()
            else:
                pass

            self.show_edit()
        except:
            self.empty_message("برجاء تحديد المنتج المراد حذفه")

    def encrypt(self, text, hashtype):
        text = text.encode("utf-8")
        hash_hash = hashlib.new(hashtype)
        hash_hash.update(text)
        return hash_hash.hexdigest()

    def show_emp(self):
        self.comboBox_13.clear()
        self.comboBox_12.clear()
        self.comboBox_13.addItem("")
        self.cur.execute("""
                SELECT username FROM employee ORDER BY EmployeeID
        """)
        data = self.cur.fetchall()
        for d in data:
            self.comboBox_13.addItem(d[0])
            self.comboBox_12.addItem(d[0])

    def display_emp(self):
        try:
            username = self.comboBox_13.currentText()
            self.cur.execute("""
                    SELECT name, mail, national_id, phone, address  FROM employee WHERE username=%s
            """, (username,))
            data = self.cur.fetchall()[0]
            name = data[0]
            mail = data[1]
            national_id = data[2]
            phone = data[3]
            address = data[4]
            self.lineEdit_30.setText(name)
            self.lineEdit_29.setText(mail)
            self.lineEdit_28.setText(national_id)
            self.lineEdit_32.setText(phone)
            self.lineEdit_33.setText(address)
        except IndexError:
            self.empty_message("برجاء اختيار اسم الموظف")
        except:
            self.empty_message("برجاء اختيار اسم الموظف")

    def edit_employee(self):
        username = self.comboBox_13.currentText()
        name = self.lineEdit_30.text()
        mail = self.lineEdit_29.text()
        national_id = self.lineEdit_28.text()
        phone = self.lineEdit_32.text()
        address = self.lineEdit_33.text()
        if name == "":
            self.empty_message("برجاء ادخال بيانات الموظف بشكل كامل")
        elif self.lineEdit_31.text() == "":
            self.empty_message("برجاء اخدال كلمة السر")
        else:
            password = self.encrypt(self.lineEdit_31.text(), "md5")
            self.cur.execute("""
                UPDATE employee SET name=%s, mail=%s, national_id=%s, phone=%s, address=%s, password=%s
                WHERE username=%s
            """, (name, mail, national_id, phone, address, password, username))
            self.db.commit()
            self.statusBar().showMessage("تم تعديل بيانات الموظف بنجاح")
            self.lineEdit_30.setText("")
            self.lineEdit_29.setText("")
            self.lineEdit_28.setText("")
            self.lineEdit_32.setText("")
            self.lineEdit_33.setText("")
            self.lineEdit_31.setText("")

    def add_employee(self):
        try:
            name = self.lineEdit_17.text()
            username = self.lineEdit_26.text()
            mail = self.lineEdit_25.text()
            national_id = self.lineEdit_18.text()
            phone_number = self.lineEdit_19.text()
            address = self.lineEdit_23.text()
            password = self.encrypt(self.lineEdit_24.text(), "md5")
            self.cur.execute("""
                    INSERT INTO employee(name, username, mail, national_id, phone, address, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (name, username, mail, national_id, phone_number, address, password))
            self.db.commit()
            self.statusBar().showMessage("تم اضافة المعلومات بنجاح")
        except mysql.connector.errors.IntegrityError:
            self.empty_message("بيانات هذا الموظف موجودة من قبل")
        except:
            self.empty_message("حدث خطأ في ادخال بيانات الموظف")

    def reports(self):
        category = self.comboBox_16.currentText()
        _from = self.dateEdit_14.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_15.date().toString("yyyy-MM-dd")
        self.cur.execute("SELECT * FROM tobacco")
        data = self.cur.fetchall()
        self.cur.execute(""" SELECT * FROM tobacco_stored""")
        stored_toba = self.cur.fetchall()
        for stored in range(len(stored_toba)):
            print(stored_toba[stored][0])

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(7)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()