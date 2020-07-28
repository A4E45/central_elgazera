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
#from central_elgazera import Ui_MainWindow

MainUI,_ = loadUiType("central_elgazera.ui")
emp_id = 0


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
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_28.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_32.setEnabled(False)
        self.setWindowIcon(QIcon('img/central_elgazera.png'))

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
        self.pushButton_55.clicked.connect(self.add_new_cards_values)
        self.pushButton_41.clicked.connect(self.add_employee)
        self.pushButton_24.clicked.connect(self.display_emp)
        self.pushButton_43.clicked.connect(self.edit_employee)
        self.pushButton_52.clicked.connect(self.reports)
        self.pushButton_53.clicked.connect(self.export_reports)
        self.pushButton_25.clicked.connect(self.daily_movement_search)
        self.pushButton_26.clicked.connect(self.export_daiymovments)
        self.pushButton_31.clicked.connect(self.login)
        self.pushButton_44.clicked.connect(self.display_permission)
        self.pushButton_45.clicked.connect(self.permissions)
        self.checkBox_16.stateChanged.connect(self.charge_groupbox)
        self.checkBox_17.stateChanged.connect(self.accessories_groupbox)
        self.checkBox_18.stateChanged.connect(self.tobacco_groupbox)
        self.checkBox_19.stateChanged.connect(self.other_groupbox)
        self.checkBox_20.stateChanged.connect(self.wanted_groupbox)
        self.checkBox_24.stateChanged.connect(self.settings_groupbox)
        self.checkBox_29.stateChanged.connect(self.admin_groupbox)
        self.pushButton_42.clicked.connect(self.update_charge)

    def admin_groupbox(self):
        if self.checkBox_29.isChecked():
            self.groupBox_16.setEnabled(False)
            self.groupBox_17.setEnabled(False)
            self.groupBox_18.setEnabled(False)
            self.groupBox_24.setEnabled(False)
            self.groupBox_19.setEnabled(False)
            self.groupBox_21.setEnabled(False)
            self.groupBox_20.setEnabled(False)
        else:
            self.groupBox_20.setEnabled(True)

    def charge_groupbox(self):
        if self.checkBox_16.isChecked():
            self.groupBox_16.setEnabled(True)
        else:
            self.groupBox_16.setEnabled(False)
            self.checkBox_15.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)

    def accessories_groupbox(self):
        if self.checkBox_17.isChecked():
            self.groupBox_17.setEnabled(True)
        else:
            self.groupBox_17.setEnabled(False)
            self.checkBox_32.setChecked(False)
            self.checkBox_9.setChecked(False)
            self.checkBox_10.setChecked(False)

    def tobacco_groupbox(self):
        if self.checkBox_18.isChecked():
            self.groupBox_18.setEnabled(True)
        else:
            self.groupBox_18.setEnabled(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_22.setChecked(False)
            self.checkBox_13.setChecked(False)

    def other_groupbox(self):
        if self.checkBox_19.isChecked():
            self.groupBox_24.setEnabled(True)
        else:
            self.groupBox_24.setEnabled(False)
            self.checkBox_23.setChecked(False)
            self.checkBox_30.setChecked(False)
            self.checkBox_31.setChecked(False)

    def wanted_groupbox(self):
        if self.checkBox_20.isChecked():
            self.groupBox_19.setEnabled(True)
        else:
            self.groupBox_19.setEnabled(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_14.setChecked(False)

    def settings_groupbox(self):
        if self.checkBox_24.isChecked():
            self.groupBox_21.setEnabled(True)
        else:
            self.groupBox_21.setEnabled(False)
            self.checkBox_25.setChecked(False)
            self.checkBox_26.setChecked(False)
            self.checkBox_52.setChecked(False)
            self.checkBox_27.setChecked(False)
            self.checkBox_55.setChecked(False)
            self.checkBox_53.setChecked(False)
            self.checkBox_54.setChecked(False)
            self.checkBox_28.setChecked(False)

    def load_date(self):
        date = datetime.datetime.now().date()
        return str(date)

    def load_date_time(self):
        date = datetime.datetime.now()
        return date

    def load_time(self):
        _time = datetime.datetime.now().time()
        return _time

    def info_message(self, total, total2):
        msg = QMessageBox()
        msg.setWindowTitle(" معلومات")
        msg.setWindowIcon(QIcon('img/central_elgazera.png'))
        msg.setText(f"""
          اجمالي مبيعات اليوم : {total}
          اجمالي مبيعات الموظف : {total2}
          """)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def empty_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("تحذير")
        msg.setWindowIcon(QIcon('img/central_elgazera.png'))
        msg.setText(f"{message}")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def open_login_tab(self):
        self.tabWidget.setCurrentIndex(0)
        global emp_id
        emp_id = 0
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_10.setRowCount(0)
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_28.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_32.setEnabled(False)

    def daily_movement(self, m):
        #emp_id = 1
        message = f"""{m}"""
        self.cur.execute("""
                INSERT INTO dailymoment(EmployeeID, _move, _date, _time)
                VALUES (%s, %s, %s, %s)
        """, (emp_id, message, self.load_date(), self.load_time()))
        self.db.commit()

    ########################################################################
    ###########################Charge Zone##################################
    ########################################################################

    def open_charge_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.daily_movement("قام بفتح صفحة تحويل الرصيد")

    def show_machine(self):
        self.cur.execute(
            "SELECT machine_name FROM machines ORDER BY MachineID")
        machines = self.cur.fetchall()
        for machine in machines:
            for m in machine:
                self.comboBox.addItem(m)
                self.comboBox_17.addItem(m)
                self.comboBox_18.addItem(m)

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
							WHERE _date=%s AND charge.EmployeeID=%s
							ORDER BY order_id
			""", (self.load_date(), emp_id))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget.resizeColumnsToContents()

    def add_charge(self):
        try:
            phone_number = self.lineEdit.text()
            if phone_number == "":
                self.empty_message("برجاء ادخال رقم المحمول")
            else:
                value = float(self.lineEdit_2.text())
                self.cur.execute("""
						SELECT * FROM machines WHERE machine_name=%s
					""", (self.comboBox.currentText(),))
                machine_id = int(self.cur.fetchall()[0][0])
                self.cur.execute(
                    "SELECT stored_charge FROM machines WHERE MachineID=%s", (machine_id,))
                stored_value = float(self.cur.fetchall()[0][0])
                if stored_value < value:
                    self.empty_message(
                        """لقد نفذ الرصيد من هذه الماكينة او ان قيمة التحويل غير كافية""")
                else:
                    self.cur.execute("""
                            SELECT * FROM services WHERE service_name=%s
                        """, (self.comboBox_14.currentText(),)
                    )
                    service_id = int(self.cur.fetchall()[0][0])
                    sql = """
                        INSERT INTO charge(phone_number, value, _date, serviceID, EmployeeID, MachineID, _time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    data_inserted = [
                        (phone_number),
                        (value),
                        (self.load_date()),
                        (service_id),
                        (emp_id),
                        (machine_id),
                        (self.load_time())
                    ]
                    self.cur.execute(sql, data_inserted)
                    self.db.commit()
                    final_value = stored_value - value
                    self.cur.execute(
                        """UPDATE machines SET stored_charge=%s WHERE MachineID=%s""", (final_value, machine_id))
                    self.db.commit()
                    self.tableWidget.setRowCount(0)
                    self.show_charge()
                    self.daily_movement(
                        f""" بقيمة {value} {phone_number}تم اضافة عملية تحويل""")

        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")
        except Exception:
            self.empty_message("حدث خطأ")

    def del_charge(self):
        try:
            info = []
            for currentQTableWidgetItem in self.tableWidget.selectedItems():
                info.append(currentQTableWidgetItem.text())
            order_num = int(info[3])
            value = float(info[1])
            machine_name = info[5]
            self.cur.execute(
                """SELECT stored_charge FROM machines WHERE machine_name=%s""", (machine_name,))
            final = float(self.cur.fetchall()[0][0]) + value
            self.cur.execute(
                """UPDATE machines SET stored_charge=%s WHERE machine_name=%s""", (final, machine_name))
            self.db.commit()
            self.cur.execute("""
					DELETE FROM charge WHERE order_id=%s
				""", (order_num,))
            self.db.commit()
            self.tableWidget.setRowCount(0)
            self.show_charge()
            self.daily_movement(f"""{info[1]} {info[0]}تم حذف عملية تحويل""")
        except Exception as e:
            self.empty_message("""حدث خطأ""")

    def charge_info(self):
        self.cur.execute("""
			SELECT value FROM charge WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0.0
        for value in values:
            total += value[0]
        self.cur.execute("""
			SELECT value FROM charge WHERE _date=%s AND EmployeeID=%s
			""", (self.load_date(), emp_id))
        values2 = self.cur.fetchall()
        total2 = 0.0
        for value2 in values2:
            total2 += value2[0]
        self.info_message(total, total2)
        self.daily_movement(""" تم عرض معلومات عن تحويل الرصيد""")

    ########################################################################
    #############################accessories zone###########################
    ########################################################################

    def open_mobile_accessories_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.daily_movement("""تم فتح صفحة الاكسسوارات""")

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
            self.comboBox_2.addItem(accessories_name[1])
            self.comboBox_10.addItem(accessories_name[1])

    def accessories_bayment(self):
        self.cur.execute("""
				SELECT accessories.name, accessories.quantity, value,  _date, accessories.order_id, employee.name  FROM accessories
				INNER JOIN employee ON accessories.EmployeeID=employee.EmployeeID
				WHERE _date=%s AND accessories.EmployeeID = %s
				ORDER BY order_id
			""", (self.load_date(), emp_id))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget_2.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_2.setItem(
                    row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_2.resizeColumnsToContents()

    def add_accessories(self):
        try:
            accessories_name = self.comboBox_2.currentText()
            quantity = int(self.spinBox.text())
            #emp_id = 1
            sql = """
                    SELECT * FROM accessories_stored WHERE name=%s
            """
            self.cur.execute(sql, [(accessories_name)])
            data = self.cur.fetchall()
            value = quantity * data[0][2]
            stored_accessories = data[0][3] - quantity
            if stored_accessories < 0:
                self.empty_message(
                    " لقد نفذت الكمية من هذا المنتج او الكمية غير كافية")
            else:
                self.cur.execute("""
                        INSERT INTO accessories(name, value, quantity, _date, _time, EmployeeID)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (accessories_name, value, quantity, self.load_date(), self.load_time(), emp_id))

                self.cur.execute("""
                        UPDATE accessories_stored SET quantity=%s WHERE name=%s
                    """, (stored_accessories, accessories_name))
                self.db.commit()
                self.tableWidget_2.setRowCount(0)
                self.accessories_bayment()
                self.daily_movement(
                    f""" {value} {accessories_name}تم اضافة اكسسوار""")
        except:
            self.empty_message("""حدث خطأ""")

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
            self.daily_movement(f"""تم حذف اكسسوار {info[0]} {info[2]}""")
        except:
            self.empty_message("""حدث خطأ""")

    def info_accessories(self):
        self.cur.execute("""
				SELECT value FROM accessories WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            for v in value:
                total += v
        self.cur.execute("""
				SELECT value FROM accessories WHERE _date=%s AND EmployeeID=%s
			""", (self.load_date(), emp_id))
        values2 = self.cur.fetchall()
        total2 = 0
        for value2 in values2:
            for v2 in value2:
                total2 += v
        self.info_message(total, total2)
        self.daily_movement(""" تم عرض معلومات عن اكسسوار""")

    ########################################################################
    #############################tobacco zone###############################
    ########################################################################

    def open_tobacoo_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.daily_movement("""تم فتح صفحة السجاير""")

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
				WHERE _date=%s AND tobacco.EmployeeID=%s
				ORDER BY tobacco.order_id
			""", (self.load_date(), emp_id))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget_3.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_3.setItem(
                    row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_3.resizeColumnsToContents()

    def add_tobacco(self):
        try:
            tobacco_name = self.comboBox_3.currentText()
            quantity = int(self.spinBox_2.text())
            self.cur.execute("""
                    SELECT quantity, price FROM tobacco_stored WHERE name=%s
                """, (tobacco_name,))
            data = self.cur.fetchall()
            stored_tobacco = data[0][0] - quantity
            total_value = data[0][1] * quantity
            #emp_id = 1
            _datetime = self.load_date_time()
            if stored_tobacco < 0:
                self.empty_message(
                    " لقد نفذت الكمية من هذا المنتج او الكمية غير كافية")

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
                self.daily_movement(
                    f""" تم اضافة علبة سجاير {tobacco_name} {total_value}""")
        except:
            self.empty_message("""حدث خطأ""")

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
            self.daily_movement(
                f"""تم حذف علبة سجاير {tobacco_name} {info[1]}""")
        except:
            self.empty_message("""حدث خطأ""")

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

        self.cur.execute("""
				SELECT value, num FROM tobacco WHERE _date=%s AND EmployeeID=%s
			""", (self.load_date(), emp_id))
        data2 = self.cur.fetchall()
        total_value2 = 0
        for da2 in data2:
            total_value2 += float(da2[0])

        msg = QMessageBox()
        msg.setWindowTitle("سجاير")
        msg.setText(f"""
اجمالي مبيعات اليوم : {total_value}
اجمالى مبيعات الموظف : {total_value2}
اجمالى عدد العلب : {total_num}
			""")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.daily_movement("""تم عرض معلومات عن السجاير""")

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
        self.comboBox_4.addItem(all_company[0], vodafone)
        self.comboBox_4.addItem(all_company[1], orange)
        self.comboBox_4.addItem(all_company[2], etisalat)
        self.comboBox_4.addItem(all_company[3], WE)
        self.comboBox_4.currentIndexChanged.connect(self.indexChanged)
        self.indexChanged(self.comboBox_4.currentIndex())

    def indexChanged(self, index):
        self.comboBox_5.clear()
        data = self.comboBox_4.itemData(index)
        if data is not None:
            self.comboBox_5.addItems(data)

    def add_cards(self):
        try:
            card_name = self.comboBox_4.currentText()
            card_value = float(self.comboBox_5.currentText())
            card_quantity = int(self.spinBox_3.text())
            final_value = card_value * card_quantity
            self.cur.execute("""
                    SELECT * FROM machines WHERE machine_name=%s
                """, (self.comboBox_18.currentText(),))
            machine_id = int(self.cur.fetchall()[0][0])
            self.cur.execute(
                "SELECT stored_charge FROM machines WHERE MachineID=%s", (machine_id,))
            stored_value = float(self.cur.fetchall()[0][0])
            if stored_value < final_value:
                self.empty_message("""لقد نفذ الرصيد من هذه الماكينة او ان قيمة التحويل غير كافية""")
            else:
                self.cur.execute("""
                        INSERT INTO charge(phone_number, value, _date, EmployeeID, MachineID, _time)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (card_name, final_value, self.load_date(), emp_id, machine_id, self.load_time()))
                self.db.commit()
                final = stored_value - final_value
                self.cur.execute(
                        """UPDATE machines SET stored_charge=%s WHERE MachineID=%s""", (final, machine_id))
                self.db.commit()
                self.daily_movement(
                    f"""تم اضافة كرت {card_name} {card_quantity * card_value}""")
                self.statusBar().showMessage("تم اضافة قيمة الكرت بنجاح",3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
        except Exception as e:
            print(e)
            self.empty_message("""حدث خطأ""")

    def cards_info(self):
        self.cur.execute("""
				SELECT value FROM phone_cards WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            total += float(value[0])

        self.cur.execute("""
				SELECT value FROM phone_cards WHERE _date=%s AND EmployeeID=%s
			""", (self.load_date(), emp_id))
        values2 = self.cur.fetchall()
        total2 = 0
        for value2 in values2:
            total2 += float(value2[0])
        self.info_message(total, total2)
        self.daily_movement("""  تم اظهار معلومات عن الكروت الشحن""")

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
				WHERE _date=%s AND other.EmployeeID=%s
				ORDER BY other.order_id
			""", (self.load_date(), emp_id))
        data = self.cur.fetchall()
        for row_index, row_data in enumerate(data):
            self.tableWidget_5.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_5.setItem(
                    row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_5.resizeColumnsToContents()

    def add_other(self):
        try:
            name = self.comboBox_6.currentText()
            quantity = int(self.spinBox_4.text())
            self.cur.execute("""
                    SELECT price, quantity FROM other_stored WHERE other_name=%s
                """, (name,))
            data = self.cur.fetchall()
            price = data[0][0]
            quantity_stored = data[0][1] - quantity
            total_value = quantity * price
            #emp = 1
            if quantity_stored < 0:
                self.empty_message(
                    " لقد نفذت الكمية من هذا المنتج او الكمية غير كافية")
            else:
                self.cur.execute("""
                        INSERT INTO other(name, num, value, _date, _time, EmployeeID)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (name, quantity, total_value, self.load_date(), self.load_time(), emp_id))
                self.cur.execute("""
                        UPDATE other_stored SET quantity=%s WHERE other_name=%s
                    """, (quantity_stored, name))
                self.db.commit()
                self.tableWidget_5.setRowCount(0)
                self.other_payment()
                self.daily_movement(f"""تم اضافة {name} {total_value}""")
        except:
            self.empty_message("""حدث خطأ""")

    def del_other(self):
        try:
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
            self.daily_movement(f"""تم حذف  {other_name} {info[2]}""")
        except:
            self.empty_message("""حدث خطأ""")

    def info_other(self):
        self.cur.execute("""
				SELECT value FROM other WHERE _date=%s
			""", (self.load_date(),))
        values = self.cur.fetchall()
        total = 0
        for value in values:
            total += float(value[0])
        self.cur.execute("""
				SELECT value FROM other WHERE _date=%s AND EmployeeID=%s
			""", (self.load_date(), emp_id))
        values2 = self.cur.fetchall()
        total2 = 0
        for value2 in values2:
            total2 += float(value2[0])
        self.info_message(total, total2)
        self.daily_movement(f"""تم اظهار معلومات عن المنتجات الاخرى""")

    def open_other_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.daily_movement("""تم فتح صفحة المنتجات الاخرى""")

    ########################################################################
    ##############################wanted zone###############################
    ########################################################################

    def open_wanted_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.daily_movement("""تم فتح صفحة المستحقات""")

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
                self.tableWidget_4.setItem(
                    row_index, colm_index, QTableWidgetItem(str(colm_data)))
        self.tableWidget_4.resizeColumnsToContents()

    def add_wanted(self):
        try:
            name = self.lineEdit_4.text()
            if name == "":
                self.empty_message("رجاء ادخال اسم العميل")
            else:
                value = float(self.lineEdit_5.text())
                # emp = 1
                self.cur.execute("""
						INSERT INTO wanted(client_name, value, _date, _time, EmployeeID)
						VALUES (%s, %s, %s, %s, %s)
					""", (name, value, self.load_date(), self.load_time(), emp_id))
                self.db.commit()
                self.tableWidget_4.setRowCount(0)
                self.show_wanted()
                self.daily_movement(
                    f"""تم اضافة {name} {value} الى المستحقات""")

        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")
        except:
            self.empty_message("""حدث خطأ""")

    def del_wanted(self):
        try:
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
            self.daily_movement(f""" تم حذف {name} {info[1]} من المستحقات""")
        except:
            self.empty_message("""حدث خطأ""")
    ########################################################################
    ##############################op zone###################################
    ########################################################################

    def show_op(self):
        try:
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
                    self.daily_movement(
                        f"""تم البحث عن عملية مخصصة {number}""")
        except:
            self.empty_message("""حدث خطأ""")

    def all_op(self):
        try:
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
                self.daily_movement("""تم ابحث عن عمليات من فترة الى اخرى""")
        except:
            self.empty_message("""حدث خطأ""")

    def open_search_for_opration_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.daily_movement(f"""تم فتح صفحة البحث عن عمليات""")
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
        self.daily_movement(f"""تم اضافة {name} {quantity} """)
        self.statusBar().showMessage("تم اضافة المنتج بنجاح", 3000)
        self.statusBar().setStyleSheet("font-size: 17px;")

    def update_charge(self):
        try:
            machine_name = self.comboBox_17.currentText()
            value = float(self.lineEdit_6.text())
            self.cur.execute("""
                SELECT stored_charge FROM machines WHERE machine_name=%s
            """, (machine_name,))
            stored_value = float(self.cur.fetchall()[0][0])
            final_value = stored_value + value
            self.cur.execute("""
                UPDATE machines SET stored_charge=%s WHERE machine_name=%s
            """, (final_value, machine_name))
            self.db.commit()
            self.statusBar().showMessage("تم اضافة الرصيد بنجاح", 3000)
            self.statusBar().setStyleSheet("font-size: 17px;")
        except ValueError:
            self.empty_message("""يجب ادخال ارقام فقط""")
        except:
            self.empty_message("""حدث خطأ""")

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
        self.daily_movement(f"""تم اضافة {name} {quantity} """)
        self.statusBar().showMessage("تم اضافة المنتج بنجاح", 3000)
        self.statusBar().setStyleSheet("font-size: 17px;")

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
        self.daily_movement(f"""تم اضافة {name} {quantity} """)
        self.statusBar().showMessage("تم اضافة المنتج بنجاح", 3000)
        self.statusBar().setStyleSheet("font-size: 17px;")

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
                self.daily_movement(
                    f"""تم اضافة نوع جديد من السجاير {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم اضافة المنتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 20px;")
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")
            except:
                self.empty_message("""حدث خطأ""")

    def add_new_machine(self):
        try:
            name = self.lineEdit_12.text()
            value = int(self.lineEdit_27.text())
            if name == "":
                self.empty_message("برجاء ادخال اسم الماكينة")
            else:
                try:
                    self.cur.execute("""
                        INSERT INTO machines(machine_name, stored_charge)
                        VALUES (%s, %s);
                    """, (name, value))
                    self.db.commit()
                    self.comboBox.clear()
                    self.comboBox_17.clear()
                    self.show_machine()
                    self.daily_movement(f"""تم اضافة ماكينة جديدة {name}""")
                    self.statusBar().showMessage("تم اضافة اسم الماكينة بنجاح", 3000)
                    self.statusBar().setStyleSheet("font-size: 20px;")
                except mysql.connector.errors.IntegrityError:
                    self.empty_message("هذه الماكينة موجودة من قبل")
        except ValueError:
            self.empty_message("""برجاء ادخال ارقام فقط""")
        except mysql.connector.errors.IntegrityError:
            self.empty_message("هذه الماكينة موجودة من قبل")
        except:
            self.empty_message("""حدث خطأ""")

    def add_new_service(self):
        try:
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
                    self.daily_movement(f"""تم اضافة خدمة جديدة {name}""")
                    self.statusBar().showMessage("تم اضافة نوع الخدمة بنجاح", 3000)
                    self.statusBar().setStyleSheet("font-size: 17px;")
                except mysql.connector.errors.IntegrityError:
                    self.empty_message("هذه الخدمة موجودة من قبل")
        except:
            self.empty_message(""" حدث خطأ""")

    def add_new_cards_values(self):
        try:
            value = float(self.lineEdit_21.text())
            company_name = self.comboBox_7.currentText()
            self.daily_movement(
                f""" تم اضافة نوع جديد من كروت الشحن {company_name} {value}""")
            if company_name == "فودافون":
                self.cur.execute("""
                    INSERT INTO vodafone_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
                self.db.commit()
                self.statusBar().showMessage("تم اضافة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif company_name == "اورنج":
                self.cur.execute("""
                    INSERT INTO orange_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
                self.db.commit()
                self.statusBar().showMessage("تم اضافة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif company_name == "اتصالات":
                self.cur.execute("""
                    INSERT INTO etisalat_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
                self.db.commit()
                self.statusBar().showMessage("تم اضافة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif company_name == "WE":
                self.cur.execute("""
                    INSERT INTO WE_cards_values(card_value)
                    VALUES (%s)
                """, (value,))
                self.db.commit()
                self.statusBar().showMessage("تم اضافة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            self.show_cards()
        except ValueError:
            self.empty_message("برجاء ادخال ارقام فقط")
        except:
            self.empty_message("""حدث خطأ""")

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
                self.daily_movement(
                    f"""تم اضافة نوع جديد من الاكسسوارات {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم اضافة النتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")
            except:
                self.empty_message("""حدث خطأ""")

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
                self.daily_movement(
                    f"""تم اضافة منتج اخر {name} بسعر {price} {quantity}""")
                self.statusBar().showMessage("تم اضافة امنتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            except mysql.connector.errors.IntegrityError:
                self.empty_message("هذا المنتج موجود من قبل")
            except ValueError:
                self.empty_message("برجاء ادخال ارقام فقط")
            except:
                self.empty_message("""حدث خطأ""")

    def show_edit(self):
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectRows)
        category = self.comboBox_15.currentText()
        if category == "سجاير":
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["اسم المنتج", "سعر المنتج", "المخزون"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["اسم المنتج", "سعر المنتج", "المخزون"])
            self.cur.execute("""
                    SELECT name, price, quantity FROM accessories_stored
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["اسم المنتج", "سعر المنتج", "المخزون"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["كود الكرت", "سعر الكرت"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["كود الكرت", "سعر الكرت"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["كود الكرت", "سعر الكرت"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["كود الكرت", "سعر الكرت"])
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
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["كود الخدمة", "اسم الخدمة"])
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
        elif category == "رصيد":
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setHorizontalHeaderLabels(
                ["الرقم التعريفي", "اسم الماكينة", "الرصيد"])
            self.cur.execute("""
                    SELECT * FROM machines ORDER BY MachineID
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
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم التعديل على النتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "اكسسوارات محمول":
                quantity = info[2]
                self.cur.execute("""
                    UPDATE accessories_stored SET name=%s, price=%s, quantity=%s WHERE name=%s
                """, (name, price, quantity, name))
                self.db.commit()
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم التعديل على النتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "اخرى":
                quantity = info[2]
                self.cur.execute("""
                    UPDATE other_stored SET other_name=%s, price=%s, quantity=%s WHERE other_name=%s
                """, (name, price, quantity, name))
                self.db.commit()
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم التعديل على النتج بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "كروت فودافون":
                self.cur.execute("""
                    UPDATE vodafone_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} بكمية {quantity}""")
                self.statusBar().showMessage("تم التعديل على قيمة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "كروت اورنج":
                self.cur.execute("""
                    UPDATE orange_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} """)
                self.statusBar().showMessage("تم التعديل على قيمة الكرت بنجاح",3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "كروت اتصالات":
                self.cur.execute("""
                    UPDATE etisalat_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
                self.daily_movement(f""" تم التعديل على {name} بسعر {price}""")
                self.statusBar().showMessage("تم التعديل على قيمة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "كروت WE":
                self.cur.execute("""
                    UPDATE WE_cards_values SET card_value=%s WHERE cardID=%s
                """, (price, name))
                self.db.commit()
                self.show_cards()
                self.daily_movement(
                    f""" تم التعديل على {name} بسعر {price} """)
                self.statusBar().showMessage("تم التعديل على قيمة الكرت بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "خدمات":
                self.cur.execute("""
                    UPDATE services SET service_name=%s WHERE serviceID=%s
                """, (price, name))
                self.db.commit()
                self.show_servies()
                self.daily_movement(f""" تم التعديل على {name} """)
                self.statusBar().showMessage("تم التعديل على اسم الخدمة بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            elif category == "رصيد":
                self.cur.execute("""
                    UPDATE machines SET stored_charge=%s WHERE MachineID=%s
                """, (info[2], name))
                self.db.commit()
                self.show_servies()
                self.daily_movement(
                    f""" تم التعديل على {info[1]} بقيمة {info[2]} """)
                self.statusBar().showMessage("تم التعديل على اسم الخدمة بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
            else:
                pass
        except:
            self.empty_message("برجاء تحديد القيمة المراد تعديلها")

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
            self.comboBox_21.addItem(d[0])

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
        try:
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
                self.daily_movement(f""" تم التعديل على بيانات {name}""")
                self.statusBar().showMessage("تم التعديل على بيانات الموظف بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
        except:
            self.empty_message("""حدث خطأ""")

    def add_employee(self):
        try:
            name = self.lineEdit_17.text()
            username = self.lineEdit_26.text()
            mail = self.lineEdit_25.text()
            national_id = self.lineEdit_18.text()
            phone_number = self.lineEdit_19.text()
            address = self.lineEdit_23.text()
            password = self.encrypt(self.lineEdit_24.text(), "md5")
            if name == "" or username == "" or mail == "" or national_id == "" or phone_number == "" or address == "" or password == "":
                self.empty_message("بيانات الموظف غير كاملة")
            else:
                self.cur.execute("""
                        INSERT INTO employee(name, username, mail, national_id, phone, address, password)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (name, username, mail, national_id, phone_number, address, password))
                self.cur.execute(
                    "SELECT EmployeeID FROM employee WHERE username=%s", (username, ))
                _id = self.cur.fetchall()[0][0]
                self.cur.execute("""
                INSERT INTO permissions (EmployeeID, is_admin, charge_tab, charge_add, charge_del, charge_info, accessories_tab, accessories_add, accessories_del, accessories_info, tobacco_tab, tobacco_add, tobacco_del, tobacco_info, other_tab, other_add, other_del, other_info, wanted_tab, wanted_add, wanted_del, search_op, settings_tab, setting_add_brand, setting_add_new_brand, setting_edit_brand, add_employee, edit_employee, reports, dailymoment, add_permissions)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (_id, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False))
                self.db.commit()
                self.statusBar().showMessage("تم اضافة المعلومات بنجاح", 3000)
                self.statusBar().setStyleSheet("font-size: 17px;")
                self.daily_movement(f"""تم اضافة موظف {name}""")
                self.show_emp()
        except mysql.connector.errors.IntegrityError as e:
            self.empty_message("بيانات هذا الموظف موجودة من قبل")
        except Exception as e:
            self.empty_message("حدث خطأ في ادخال بيانات الموظف")

    def show_tobacco_reports(self):
        _from = self.dateEdit_14.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_15.date().toString("yyyy-MM-dd")
        self.cur.execute(
            """ SELECT * FROM tobacco_stored ORDER BY tobaccoID""")
        stored_toba = self.cur.fetchall()
        total_values = []
        total_pay = 0
        total_stored = 0
        for stored in range(len(stored_toba)):
            self.cur.execute("""
                SELECT num, value FROM tobacco WHERE (name=%s) AND (_date BETWEEN %s AND %s)
            """, (stored_toba[stored][1], _from, _to))
            values = self.cur.fetchall()
            tobacco = 0
            tobacco_values = 0
            total_stored += stored_toba[stored][2] * stored_toba[stored][3]
            for value in values:
                tobacco += value[0]
                tobacco_values += value[1]
            total_values.append(
                [stored_toba[stored][1], stored_toba[stored][3], stored_toba[stored][2], stored_toba[stored][2] * stored_toba[stored][3], tobacco, stored_toba[stored][3] * tobacco])
            total_pay += tobacco_values
        return total_pay, total_stored, total_values

    def tobacco_reports(self):
        total_pay, total_stored,  data = self.show_tobacco_reports()
        for row_index, row_data in enumerate(data):
            self.tableWidget_10.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_10.setItem(row_index, colm_index,
                                            QTableWidgetItem(str(colm_data)))
        self.tableWidget_10.resizeColumnsToContents()
        return total_pay, total_stored

    def show_accessories_reports(self):
        _from = self.dateEdit_14.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_15.date().toString("yyyy-MM-dd")
        self.cur.execute(
            """ SELECT * FROM accessories_stored ORDER BY accessoriesID""")
        stored_ac = self.cur.fetchall()
        total_values = []
        total_pay = 0
        total_stored = 0
        for stored in range(len(stored_ac)):
            self.cur.execute("""
                SELECT quantity, value FROM accessories WHERE (name=%s) AND (_date BETWEEN %s AND %s)
            """, (stored_ac[stored][1], _from, _to))
            values = self.cur.fetchall()
            ac = 0
            ac_values = 0
            total_stored += stored_ac[stored][2] * stored_ac[stored][3]
            for value in values:
                ac += value[0]
                ac_values += value[1]
            total_values.append(
                [stored_ac[stored][1], stored_ac[stored][2], stored_ac[stored][3], stored_ac[stored][3] * stored_ac[stored][2], ac, stored_ac[stored][2] * ac])
            total_pay += ac_values
        return total_pay, total_stored, total_values

    def accessories_reports(self):
        total_pay, total_stored, data = self.show_accessories_reports()
        for row_index, row_data in enumerate(data):
            self.tableWidget_10.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_10.setItem(row_index, colm_index,
                                            QTableWidgetItem(str(colm_data)))
        self.tableWidget_10.resizeColumnsToContents()
        return total_pay, total_stored

    def show_other_reports(self):
        _from = self.dateEdit_14.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_15.date().toString("yyyy-MM-dd")
        self.cur.execute(
            """ SELECT * FROM other_stored ORDER BY otherID""")
        stored_ot = self.cur.fetchall()
        total_values = []
        total_pay = 0
        total_stored = 0
        for stored in range(len(stored_ot)):
            self.cur.execute("""
                SELECT num, value FROM other WHERE (name=%s) AND (_date BETWEEN %s AND %s)
            """, (stored_ot[stored][1], _from, _to))
            values = self.cur.fetchall()
            ot = 0
            ot_values = 0
            total_stored += stored_ot[stored][2] * stored_ot[stored][3]
            for value in values:
                ot += value[0]
                ot_values += value[1]
            total_values.append(
                [stored_ot[stored][1], stored_ot[stored][2], stored_ot[stored][3], stored_ot[stored][3] * stored_ot[stored][2], ot, stored_ot[stored][2] * ot])
            total_pay += ot_values
        return total_pay, total_stored, total_values

    def other_reports(self):
        total_pay, total_stored, data = self.show_other_reports()
        for row_index, row_data in enumerate(data):
            self.tableWidget_10.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_10.setItem(row_index, colm_index,
                                            QTableWidgetItem(str(colm_data)))
        self.tableWidget_10.resizeColumnsToContents()
        return total_pay, total_stored

    def show_charge_reports(self):
        _from = self.dateEdit_14.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_15.date().toString("yyyy-MM-dd")
        self.cur.execute("""SELECT * FROM machines ORDER BY MachineID""")
        data = self.cur.fetchall()
        total_values = []
        total_pay = 0
        total_stored = 0
        for stored in range(len(data)):
            self.cur.execute("""
                SELECT value FROM charge WHERE (MachineID=%s) AND (_date BETWEEN %s AND %s)
            """, (data[stored][0], _from, _to))
            values = self.cur.fetchall()
            total_stored += data[stored][2]
            charge_values = 0
            for value in values:
                charge_values += value[0]
            total_values.append([data[stored][1], "---------", data[stored]
                                 [2], "---------", charge_values, "---------"])
            total_pay += charge_values
        return total_pay, total_stored, total_values

    def charge_reports(self):
        total_pay, total_stored, data = self.show_charge_reports()
        for row_index, row_data in enumerate(data):
            self.tableWidget_10.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_10.setItem(row_index, colm_index,
                                            QTableWidgetItem(str(colm_data)))
        self.tableWidget_10.resizeColumnsToContents()
        return total_pay, total_stored

    def reports(self):
        category = self.comboBox_16.currentText()
        self.tableWidget_10.setRowCount(0)
        self.label_20.setText("")
        self.label_18.setText("")
        if category == "سجاير":
            payment, stored = self.tobacco_reports()
            self.label_20.setText("{:.2f}".format(payment))
            self.label_18.setText("{:.2f}".format(stored))
        elif category == "اكسسوارات":
            payment, stored = self.accessories_reports()
            self.label_20.setText("{:.2f}".format(payment))
            self.label_18.setText("{:.2f}".format(stored))
        elif category == "اخرى":
            payment, stored = self.other_reports()
            self.label_20.setText("{:.2f}".format(payment))
            self.label_18.setText("{:.2f}".format(stored))
        elif category == "الكل":
            payment_ch, stored_ch = self.charge_reports()
            payment_ot, stored_ot = self.other_reports()
            payment_ac, stored_ac = self.accessories_reports()
            payment_to, stored_to = self.tobacco_reports()
            total = payment_to + payment_ac + payment_ot + payment_ch
            total_stored = stored_to + stored_ac + stored_ot + stored_ch
            self.label_20.setText("{:.2f}".format(total))
            self.label_18.setText("{:.2f}".format(total_stored))
        elif category == "رصيد":
            payment, stored = self.charge_reports()
            self.label_20.setText("{:.2f}".format(payment))
            self.label_18.setText("{:.2f}".format(stored))
        else:
            pass
        self.daily_movement(f"""تم اظهار تقاير عن {category}""")
        self.report_cards()

    def func_export(self, category):
            data = category
            wb = Workbook(f'تقارير/{self.load_date()}.xlsx')
            sheet1 = wb.add_worksheet()
            sheet1.write(0, 0, 'اسم المنتج')
            sheet1.write(0, 1, 'سعر المنتج')
            sheet1.write(0, 2, 'المجزون')
            sheet1.write(0, 3, 'قيمة المخزون')
            sheet1.write(0, 4, 'المباع')
            sheet1.write(0, 5, 'قيمة المباع')
            row_number = 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet1.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1
            wb.close()

    def export_reports(self):
        category = self.comboBox_16.currentText()
        if category == "سجاير":
            self.func_export(self.show_tobacco_reports()[2])
        elif category == "اكسسوارات":
            self.func_export(self.show_accessories_reports()[2])
        elif category == "اخرى":
            self.func_export(self.show_other_reports()[2])
        elif category == "الكل":
            total = self.show_tobacco_reports(
            )[2] + self.show_accessories_reports()[2] + self.show_other_reports()[2]
            self.func_export(total)
        elif category == "رصيد":
            self.func_export(self.show_charge_reports()[2])
        else:
            pass
        self.daily_movement(f"""تم تصدير تقارير عن {category}""")
        self.statusBar().showMessage("تم تصدير البيانات بنجاح", 3000)
        self.statusBar().setStyleSheet("font-size: 17px;")

    def show_daily_movment_for_one(self):
        username = self.comboBox_21.currentText()
        _from = self.dateEdit_7.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_6.date().toString("yyyy-MM-dd")
        self.cur.execute(
            """SELECT name, EmployeeID FROM employee WHERE username=%s""", (username,))
        info = self.cur.fetchall()[0]
        name = info[0]
        emp_id = info[1]
        self.cur.execute("""
            SELECT employee.name, _move, _date, _time FROM dailymoment
            INNER JOIN employee ON dailymoment.EmployeeID=employee.EmployeeID
            WHERE employee.EmployeeID=%s AND _date BETWEEN %s AND %s
            ORDER BY moveID
        """, (emp_id, _from, _to))
        data = self.cur.fetchall()
        return data, name

    def show_all_daily_movements(self):
        username = self.comboBox_21.currentText()
        _from = self.dateEdit_7.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_6.date().toString("yyyy-MM-dd")
        self.cur.execute("""
            SELECT employee.name, _move, _date, _time FROM dailymoment
            INNER JOIN employee ON dailymoment.EmployeeID=employee.EmployeeID
            WHERE _date BETWEEN %s AND %s
            ORDER BY moveID
        """, (_from, _to))
        data = self.cur.fetchall()
        return data

    def daily_movement_search(self):
        self.textBrowser.clear()
        username = self.comboBox_21.currentText()
        _from = self.dateEdit_7.date().toString("yyyy-MM-dd")
        _to = self.dateEdit_6.date().toString("yyyy-MM-dd")
        if username == "الكل":
            data = self.show_all_daily_movements()
            self.textBrowser.append(
                f"""التحركات داخل البرنامج لكل الموظفين : """)
            for i in data:
                self.textBrowser.append(
                    f"""قام {i[0]} {i[1]} التاريخ {i[2]} التوقيت {i[3]}""")
        else:
            data, name = self.show_daily_movment_for_one()
            self.textBrowser.append(f"""التحركات  ل {name} داخل البرنامج : """)
            for i in data:
                self.textBrowser.append(
                    f"""{i[1]} التاريخ {i[2]} التوقيت {i[3]}""")

    def export_daiymovments(self):
        username = self.comboBox_21.currentText()
        if username == "الكل":
            with open(f"التحركات/{self.load_date()}.txt", "a", encoding="utf-8") as file:
                data = self.show_all_daily_movements()
                for i in data:
                    file.write(
                        f"""قام {i[0]} {i[1]} التاريخ {i[2]} التوقيت {i[3]} \n""")
        else:
            with open(f"التحركات/{self.load_date()}.txt", "a", encoding="utf-8") as file:
                data = self.show_daily_movment_for_one()[0]
                for i in data:
                    file.write(
                        f"""قام {i[0]} {i[1]} التاريخ {i[2]} التوقيت {i[3]} \n""")
        self.statusBar().showMessage("تم تصدير البيانات بنجاح", 3000)
        self.statusBar().setStyleSheet("font-size: 17px;")

    def login(self):
        try:
            username = self.lineEdit_7.text()
            password = self.encrypt(self.lineEdit_8.text(), "md5")
            self.cur.execute(
                """ SELECT EmployeeID, username, password FROM employee WHERE username=%s""", (username,))
            data = self.cur.fetchall()
            if password == data[0][2] and username == data[0][1]:
                global emp_id
                emp_id = data[0][0]
                self.tabWidget.setCurrentIndex(1)
                self.show_charge()
                self.accessories_bayment()
                self.tobacco_payment()
                self.other_payment()
                self.lineEdit_7.setText("")
                self.lineEdit_8.setText("")
                self.pushButton_32.setEnabled(True)
                self.cur.execute("""
                    SELECT * FROM permissions WHERE EmployeeID=%s
                """, (emp_id,))
                data = self.cur.fetchall()[0]
                if data[2] == 1:
                    self.pushButton_6.setEnabled(True)
                    self.pushButton.setEnabled(True)
                    self.pushButton_2.setEnabled(True)
                    self.pushButton_5.setEnabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    self.pushButton_4.setEnabled(True)
                    self.pushButton_13.setEnabled(True)
                    self.pushButton_11.setEnabled(True)
                    self.pushButton_10.setEnabled(True)
                    self.pushButton_34.setEnabled(True)
                    self.pushButton_9.setEnabled(True)
                    self.pushButton_12.setEnabled(True)
                    self.pushButton_14.setEnabled(True)
                    self.pushButton_22.setEnabled(True)
                    self.pushButton_49.setEnabled(True)
                    self.pushButton_15.setEnabled(True)
                    self.pushButton_16.setEnabled(True)
                    self.pushButton_19.setEnabled(True)
                    self.pushButton_20.setEnabled(True)
                    self.pushButton_16.setEnabled(True)
                    self.pushButton_28.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
                    self.tabWidget_2.setTabEnabled(0, True)
                    self.tabWidget_2.setTabEnabled(1, True)
                    self.tabWidget_2.setTabEnabled(2, True)
                    self.tabWidget_2.setTabEnabled(3, True)
                    self.tabWidget_2.setTabEnabled(4, True)
                    self.tabWidget_2.setTabEnabled(5, True)
                    self.tabWidget_2.setTabEnabled(6, True)
                    self.tabWidget_2.setTabEnabled(7, True)
                else:
                    if data[3] == 1:
                        self.pushButton_6.setEnabled(True)
                        if data[4] == 1:
                            self.pushButton.setEnabled(True)
                        else:
                            self.pushButton.setEnabled(False)
                        if data[5] == 1:
                            self.pushButton_2.setEnabled(True)
                        else:
                            self.pushButton_2.setEnabled(False)
                        if data[6] == 1:
                            self.pushButton_5.setEnabled(True)
                        else:
                            self.pushButton_5.setEnabled(False)
                    else:
                        self.pushButton_6.setEnabled(False)
                    if data[7] == 1:
                        self.pushButton_7.setEnabled(True)
                        if data[8] == 1:
                            self.pushButton_3.setEnabled(True)
                        else:
                            self.pushButton_3.setEnabled(False)
                        if data[9] == 1:
                            self.pushButton_4.setEnabled(True)
                        else:
                            self.pushButton_4.setEnabled(False)
                        if data[10] == 1:
                            self.pushButton_13.setEnabled(True)
                        else:
                            self.pushButton_13.setEnabled(False)
                    else:
                        self.pushButton_7.setEnabled(False)
                    if data[11] == 1:
                        self.pushButton_11.setEnabled(True)
                        if data[12] == 1:
                            self.pushButton_10.setEnabled(True)
                        else:
                            self.pushButton_10.setEnabled(False)
                        if data[13] == 1:
                            self.pushButton_34.setEnabled(True)
                        else:
                            self.pushButton_34.setEnabled(False)
                        if data[14] == 1:
                            self.pushButton_9.setEnabled(True)
                        else:
                            self.pushButton_9.setEnabled(False)
                    else:
                        self.pushButton_11.setEnabled(False)
                    if data[15] == 1:
                        self.pushButton_12.setEnabled(True)
                        if data[16] == 1:
                            self.pushButton_14.setEnabled(True)
                            self.pushButton_22.setEnabled(True)
                        else:
                            self.pushButton_14.setEnabled(False)
                            self.pushButton_22.setEnabled(False)
                        if data[17] == 1:
                            self.pushButton_49.setEnabled(True)
                        else:
                            self.pushButton_49.setEnabled(False)
                        if data[18] == 1:
                            self.pushButton_15.setEnabled(True)
                            self.pushButton_21.setEnabled(True)
                        else:
                            self.pushButton_15.setEnabled(False)
                            self.pushButton_21.setEnabled(False)
                    else:
                        self.pushButton_12.setEnabled(False)

                    if data[19] == 1:
                        self.pushButton_16.setEnabled(True)
                        if data[20] == 1:
                            self.pushButton_19.setEnabled(True)
                        else:
                            self.pushButton_19.setEnabled(False)
                        if data[21] == 1:
                            self.pushButton_20.setEnabled(True)
                        else:
                            self.pushButton_20.setEnabled(False)
                    else:
                        self.pushButton_16.setEnabled(False)

                    if data[22] == 1:
                        self.pushButton_28.setEnabled(True)
                    else:
                        self.pushButton_28.setEnabled(False)

                    if data[23] == 1:
                        self.pushButton_8.setEnabled(True)
                        if data[24] == 1:
                            self.tabWidget_2.setTabEnabled(0, True)
                        else:
                            self.tabWidget_2.setTabEnabled(0, False)
                        if data[25] == 1:
                            self.tabWidget_2.setTabEnabled(1, True)
                        else:
                            self.tabWidget_2.setTabEnabled(1, False)
                        if data[26] == 1:
                            self.tabWidget_2.setTabEnabled(2, True)
                        else:
                            self.tabWidget_2.setTabEnabled(2, False)
                        if data[27] == 1:
                            self.tabWidget_2.setTabEnabled(3, True)
                        else:
                            self.tabWidget_2.setTabEnabled(3, False)
                        if data[28] == 1:
                            self.tabWidget_2.setTabEnabled(4, True)
                        else:
                            self.tabWidget_2.setTabEnabled(4, False)
                        if data[29] == 1:
                            self.tabWidget_2.setTabEnabled(5, True)
                        else:
                            self.tabWidget_2.setTabEnabled(5, False)
                        if data[30] == 1:
                            self.tabWidget_2.setTabEnabled(6, True)
                        else:
                            self.tabWidget_2.setTabEnabled(6, False)
                        if data[31] == 1:
                            self.tabWidget_2.setTabEnabled(7, True)
                        else:
                            self.tabWidget_2.setTabEnabled(7, False)
                    else:
                        self.pushButton_8.setEnabled(False)

            else:
                self.empty_message(
                    "برجاء الخال اسم المستخدم و الكلمة المرور بشكل صحيح")
        except:
            self.empty_message(
                "برجاء الخال اسم المستخدم و الكلمة المرور بشكل صحيح")

    def display_permission(self):
        try:
            self.groupBox_20.setEnabled(True)
            self.checkBox_16.setChecked(False)
            self.checkBox_17.setChecked(False)
            self.checkBox_18.setChecked(False)
            self.checkBox_19.setChecked(False)
            self.checkBox_20.setChecked(False)
            self.checkBox_21.setChecked(False)
            self.checkBox_24.setChecked(False)
            self.checkBox_29.setChecked(False)
            self.groupBox_16.setEnabled(False)
            self.checkBox_15.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.groupBox_17.setEnabled(False)
            self.checkBox_32.setChecked(False)
            self.checkBox_9.setChecked(False)
            self.checkBox_10.setChecked(False)
            self.groupBox_18.setEnabled(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_22.setChecked(False)
            self.checkBox_13.setChecked(False)
            self.groupBox_24.setEnabled(False)
            self.checkBox_23.setChecked(False)
            self.checkBox_30.setChecked(False)
            self.checkBox_31.setChecked(False)
            self.groupBox_19.setEnabled(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_14.setChecked(False)
            self.groupBox_21.setEnabled(False)
            self.checkBox_25.setChecked(False)
            self.checkBox_26.setChecked(False)
            self.checkBox_52.setChecked(False)
            self.checkBox_27.setChecked(False)
            self.checkBox_55.setChecked(False)
            self.checkBox_53.setChecked(False)
            self.checkBox_54.setChecked(False)
            self.checkBox_28.setChecked(False)
            username = self.comboBox_12.currentText()
            self.cur.execute(
                """ SELECT EmployeeID FROM employee WHERE username=%s""", (username,))
            _id = self.cur.fetchall()[0][0]
            self.cur.execute(
                """ SELECT * FROM permissions WHERE EmployeeID=%s""", (_id,))
            data = self.cur.fetchall()[0]
            is_admin = data[2]
            charge_tab = data[3]
            add_charge = data[4]
            del_charge = data[5]
            info_charge = data[6]
            accessories_tab = data[7]
            add_accessories = data[8]
            del_accessories = data[9]
            info_accessories = data[10]
            tobacco_tab = data[11]
            add_tobacco = data[12]
            del_tobacco = data[13]
            info_tobacco = data[14]
            other_tab = data[15]
            add_other = data[16]
            del_other = data[17]
            info_other = data[18]
            wanted_tab = data[19]
            add_wanted = data[20]
            del_wanted = data[21]
            search_op = data[22]
            settings_tab = data[23]
            add_brand = data[24]
            add_new_brand = data[25]
            edit_brand = data[26]
            add_emp = data[27]
            info_emp = data[28]
            reports = data[29]
            dailymovments = data[30]
            add_permissions = data[31]
            if is_admin == 1:
                self.checkBox_29.setChecked(True)
            else:
                if charge_tab == 1:
                    self.checkBox_16.setChecked(True)
                if add_charge == 1:
                    self.checkBox_15.setChecked(True)
                if del_charge == 1:
                    self.checkBox_2.setChecked(True)
                if info_charge == 1:
                    self.checkBox_3.setChecked(True)
                if accessories_tab == 1:
                    self.checkBox_17.setChecked(True)
                if add_accessories == 1:
                    self.checkBox_32.setChecked(True)
                if del_accessories == 1:
                    self.checkBox_9.setChecked(True)
                if info_accessories == 1:
                    self.checkBox_10.setChecked(True)
                if tobacco_tab == 1:
                    self.checkBox_18.setChecked(True)
                if add_tobacco == 1:
                    self.checkBox_11.setChecked(True)
                if del_tobacco == 1:
                    self.checkBox_22.setChecked(True)
                if info_tobacco == 1:
                    self.checkBox_13.setChecked(True)
                if other_tab == 1:
                    self.checkBox_19.setChecked(True)
                if add_other == 1:
                    self.checkBox_23.setChecked(True)
                if del_other == 1:
                    self.checkBox_30.setChecked(True)
                if info_other == 1:
                    self.checkBox_31.setChecked(True)
                if wanted_tab == 1:
                    self.checkBox_20.setChecked(True)
                if add_wanted == 1:
                    self.checkBox_12.setChecked(True)
                if del_wanted == 1:
                    self.checkBox_14.setChecked(True)
                if search_op == 1:
                    self.checkBox_21.setChecked(True)
                if settings_tab == 1:
                    self.checkBox_24.setChecked(True)
                if add_brand == 1:
                    self.checkBox_25.setChecked(True)
                if add_new_brand == 1:
                    self.checkBox_26.setChecked(True)
                if edit_brand == 1:
                    self.checkBox_52.setChecked(True)
                if add_emp == 1:
                    self.checkBox_27.setChecked(True)
                if info_emp == 1:
                    self.checkBox_55.setChecked(True)
                if reports == 1:
                    self.checkBox_53.setChecked(True)
                if dailymovments == 1:
                    self.checkBox_54.setChecked(True)
                if add_permissions == 1:
                    self.checkBox_28.setChecked(True)
        except:
            self.empty_message(
                """هذا الموظف ليس لديه صلاحيات برجاء اضافة صلاحيات له""")

    def permissions(self):
        try:
            username = self.comboBox_12.currentText()
            self.cur.execute("""
                    SELECT EmployeeID FROM employee WHERE username=%s
            """, (username,))
            _id = self.cur.fetchall()[0][0]
            is_admin = self.checkBox_29.isChecked()
            charge_tab = self.checkBox_16.isChecked()
            add_charge = self.checkBox_15.isChecked()
            del_charge = self.checkBox_2.isChecked()
            info_charge = self.checkBox_3.isChecked()
            accessories_tab = self.checkBox_17.isChecked()
            add_accessories = self.checkBox_32.isChecked()
            del_accessories = self.checkBox_9.isChecked()
            info_accessories = self.checkBox_10.isChecked()
            tobacco_tab = self.checkBox_18.isChecked()
            add_tobacco = self.checkBox_11.isChecked()
            del_tobacco = self.checkBox_22.isChecked()
            info_tobacco = self.checkBox_13.isChecked()
            other_tab = self.checkBox_19.isChecked()
            add_other = self.checkBox_23.isChecked()
            del_other = self.checkBox_30.isChecked()
            info_other = self.checkBox_31.isChecked()
            wanted_tab = self.checkBox_20.isChecked()
            add_wanted = self.checkBox_12.isChecked()
            del_wanted = self.checkBox_14.isChecked()
            search_op = self.checkBox_21.isChecked()
            settings_tab = self.checkBox_24.isChecked()
            add_brand = self.checkBox_25.isChecked()
            add_new_brand = self.checkBox_26.isChecked()
            edit_brand = self.checkBox_52.isChecked()
            add_emp = self.checkBox_27.isChecked()
            info_emp = self.checkBox_55.isChecked()
            reports = self.checkBox_53.isChecked()
            dailymovments = self.checkBox_54.isChecked()
            add_permissions = self.checkBox_28.isChecked()
            self.cur.execute("""
                    UPDATE permissions SET is_admin=%s, charge_tab=%s, charge_add=%s, charge_del=%s, charge_info=%s, accessories_tab=%s, accessories_add=%s, accessories_del=%s, accessories_info=%s, tobacco_tab=%s, tobacco_add=%s, tobacco_del=%s, tobacco_info=%s, other_tab=%s, other_add=%s, other_del=%s, other_info=%s, wanted_tab=%s, wanted_add=%s, wanted_del=%s, search_op=%s, settings_tab=%s, setting_add_brand=%s, setting_add_new_brand=%s, setting_edit_brand=%s, add_employee=%s, edit_employee=%s, reports=%s, dailymoment=%s, add_permissions=%s
                    WHERE EmployeeID=%s
            """, (is_admin, charge_tab, add_charge, del_charge, info_charge, accessories_tab, add_accessories, del_accessories, info_accessories, tobacco_tab, add_tobacco, del_tobacco, info_tobacco, other_tab, add_other, del_other, info_other, wanted_tab, add_wanted, del_wanted, search_op, settings_tab, add_brand, add_new_brand, edit_brand, add_emp, info_emp, reports, dailymovments, add_permissions, _id))
            self.db.commit()
            self.statusBar().showMessage("تم تعديل صلاحيات الموظف بنجاح", 3000)
            self.statusBar().setStyleSheet("font-size: 17px;")
        except:
            self.empty_message("""حدث خطأ""")

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.daily_movement("""تم فتح صفحة الاعدادات""")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
