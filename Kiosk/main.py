# Import Libraries and Packages

import sys
import datetime

from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFrame
from PyQt6 import QtWidgets
import pyodbc

from reference import Ui_dialog_ref
from ui_home import Ui_kiosk_window
from preview_certificate import Ui_preview_certificate
from preview_clearance import Ui_dialog_clearance
from preview_indigency import Ui_dialog_indigency
from preview_ftjs import Ui_Dialog
from preview_permit import Ui_dialog_permit
from login_window import Ui_win_login
from dialog_createacc import Ui_create_Dialog
# Connect to ODBC
server = 'mssql-157657-0.cloudclusters.net, 16555'
database = 'db_system'
username = 'root_db'
password = 'newUser09112001'
# Create a connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)


# Window Class for Login Page
class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.loginUI = Ui_win_login()
        self.loginUI.setupUi(self)
        self.loginUI.btn_login.clicked.connect(self.login)
        self.loginUI.btn_register.clicked.connect(self.register)



# Functions
    def register(self):
        self.hide()
        self.registerwin = QtWidgets.QDialog()
        self.registerUI = Ui_create_Dialog()
        self.registerUI.setupUi(self.registerwin)
        self.registerUI.to_login.clicked.connect(self.showurself)
        self.registerUI.submit_account.clicked.connect(self.input_register)
        self.registerwin.show()

    def login(self):
        global email
        email = self.loginUI.line_editemail.text()
        self.password = self.loginUI.line_editpassword.text()
        c = connection.cursor()
        try:
            query = "SELECT password FROM tbl_users WHERE email LIKE '" + email + "'"
            c.execute(query)
            pword = c.fetchone()[0]
            if pword == self.password:
                quer = "SELECT verification FROM tbl_users WHERE email LIKE '" + email + "'"
                c.execute(quer)
                verif = c.fetchone()[0]
                if verif == "Verified":
                    home_page = MainWindow()
                    home_page.show()
                    self.close()
                else:
                    self.show_error_message("Not Yet Verified")
            else:
                self.show_error_message("Wrong Email or Password")
        except:
            self.show_error_message("Wrong Email or Password!")



    def show_error_message(self, message):
        # Show an error message dialog
        error_dialog = QMessageBox(self)
        error_dialog.setStyleSheet("color: white; font: 16px 'Roboto';")
        error_dialog.setIcon(QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()





    def input_register(self):
        self.name = self.registerUI.create_name.text()
        self.address = self.registerUI.create_address.text()
        self.bday = self.registerUI.create_birthday.text()
        self.bplace = self.registerUI.create_birthplace.text()
        self.cstatus = self.registerUI.create_cs.text()
        self.ctzn = self.registerUI.create_ctzn.text()
        self.cremail = self.registerUI.create_email.text()
        self.password = self.registerUI.create_password.text()
        self.confirm = self.registerUI.confirm_password.text()
        self.verification = "Not Verified"
        self.sex = None
        if self.registerUI.rbtn_male.isChecked():
            self.sex = "Male"
        elif self.registerUI.rbtn_female.isChecked():
            self.sex = "Female"
        print(self.sex)
        c = connection.cursor()
        if self.password == "" and self.confirm == "":
            self.show_error_message("Fill it all up")
        elif self.password != self.confirm:
            self.show_error_message("Passwords are not the same!!")
        else:
            c.execute("INSERT INTO tbl_users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                self.cremail, self.password, self.name, self.sex, self.address, self.bday, self.bplace, self.cstatus,
                self.ctzn, self.verification,))
            self.show_message("Have you brought your Barangay ID? You might need it for Verification of your Account")
        connection.commit()

    def show_error_message(self, message):
        # Show an error message dialog
        error_dialog = QMessageBox(self)
        error_dialog.setStyleSheet("color: white; font: 16px 'Roboto';")
        error_dialog.setIcon(QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()

    def show_message(self, message):
        # Show an error message dialog
        error_dialog = QMessageBox(self)
        error_dialog.setStyleSheet("color: white; font: 16px 'Roboto';")
        error_dialog.setIcon(QMessageBox.Icon.Information)
        error_dialog.setWindowTitle("Note")
        error_dialog.setText(message)
        error_dialog.exec()

    def showurself(self):
        self.registerwin.close()
        self.show()

# Window Class for Home Page

class MainWindow(QMainWindow):
    login_instance = None
    def __init__(self):
        QMainWindow.__init__(self)
        self.MainUI = Ui_kiosk_window()
        self.MainUI.setupUi(self)

        # From Current Page to Home
        self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home)
        self.MainUI.btn_home2.clicked.connect(lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))
        self.MainUI.btn_home2_2.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))
        self.MainUI.btn_home2_3.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))
        self.MainUI.btn_home2_4.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))
        self.MainUI.btn_home2_5.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))
        self.MainUI.btn_home2_6.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.page_home))

        # From Current Page to Request Page
        self.MainUI.btn_request.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_request.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_2.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_3.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_4.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_5.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_6.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_toRequest_7.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.select_doc))
        self.MainUI.btn_years.clicked.connect(lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.form_ftjs))

        # From Request Page to Selected Document Form
        self.MainUI.btn_ftjsOath.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.form_ftjs))
        self.MainUI.btn_permit.clicked.connect(lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.form_bp))
        self.MainUI.btn_clearance.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.form_clearance))
        self.MainUI.btn_indigency.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.form_indigency))
        self.MainUI.btn_editacc.clicked.connect(
            lambda: self.MainUI.stackedWidget.setCurrentWidget(self.MainUI.edit_acc))
        self.MainUI.btn_certificate.clicked.connect(self.certificate_preview)

        # Submit Request Button Click Events
        self.MainUI.submit_ca.clicked.connect(self.edit_account)
        self.MainUI.submit_bc.clicked.connect(self.clearance_preview)
        self.MainUI.submit_idg.clicked.connect(self.indigency_preview)
        self.MainUI.btn_years.clicked.connect(self.ftjs_preview)
        self.MainUI.submit_bp.clicked.connect(self.permit_preview)
        self.MainUI.edit_email.insert(email)
        self.MainUI.btn_logout.clicked.connect(self.logout)

    def logout(self):
        if not MainWindow.login_instance:
            MainWindow.login_instance = Login()

        MainWindow.login_instance.show()
        self.hide()




    # Dialog Buttons
    def certificate_preview(self):
        self.certificate = QtWidgets.QDialog()
        self.uiA = Ui_preview_certificate()
        self.uiA.setupUi(self.certificate)
        c = connection.cursor()
        dbq = "SELECT name FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.certname = c.fetchone()[0]
        self.uiA.lbl_certifname.setText(self.certname)
        dbqa = "SELECT address FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbqa)
        self.certaddress = c.fetchone()[0]
        self.uiA.lbl_certifaddress.setText(self.certaddress)
        dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "certification" + "'"
        c.execute(dbqa)
        self.certprice = c.fetchone()[0]
        self.uiA.cert_price.setText(self.certprice)
        self.uiA.btnbox_certificate.accepted.connect(self.cert_insert)
        self.uiA.btnbox_certificate.rejected.connect(self.certificate.destroy)
        self.certificate.show()

    def clearance_preview(self):
        self.clearance = QtWidgets.QDialog()
        self.uiB = Ui_dialog_clearance()
        self.uiB.setupUi(self.clearance)
        self.bcpurpose = self.MainUI.cBox_clearance.currentText()
        c = connection.cursor()
        dbq = "SELECT name FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bcname = c.fetchone()[0]
        self.uiB.lbl_clrname.setText(self.bcname)
        dbq = "SELECT address FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bcaddress = c.fetchone()[0]
        self.uiB.lbl_clraddress.setText(self.bcaddress)
        dbq = "SELECT bday FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bcbday = c.fetchone()[0]
        self.uiB.lbl_clrbirthday.setText(self.bcbday)
        dbq = "SELECT bplace FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bcbplace = c.fetchone()[0]
        self.uiB.lbl_clrbirthplace.setText(self.bcbplace)
        dbq = "SELECT sex FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bcsex = c.fetchone()[0]
        self.uiB.lbl_clrsex.setText(self.bcsex)
        dbq = "SELECT cstatus FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bccstatus = c.fetchone()[0]
        self.uiB.lbl_clrcivilstatus.setText(self.bccstatus)
        dbq = "SELECT citizenship FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bccitizenship = c.fetchone()[0]
        self.uiB.lbl_clrcitizenship.setText(self.bccitizenship)
        self.uiB.lbl_clrpurpose.setText(self.bcpurpose)

        if self.bcpurpose == "Local Employment":
            dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "employment" + "'"
            c.execute(dbqa)
            self.bcprice = c.fetchone()[0]
            self.uiB.clearance_price.setText(self.bcprice)
            self.uiB.buttonBox.accepted.connect(self.clearance_insert)
            self.clearance.show()
        elif self.bcpurpose == "Motor Loan":
            dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "loan" + "'"
            c.execute(dbqa)
            self.bcprice = c.fetchone()[0]
            self.uiB.clearance_price.setText(self.bcprice)
            self.uiB.buttonBox.accepted.connect(self.clearance_insert)
            self.clearance.show()
        elif self.bcpurpose == "Police Clearance":
            dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "employment" + "'"
            c.execute(dbqa)
            self.bcprice = c.fetchone()[0]
            self.uiB.clearance_price.setText(self.bcprice)
            self.uiB.buttonBox.accepted.connect(self.clearance_insert)
            self.clearance.show()
        elif self.bcpurpose == "Loan":
            dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "loan" + "'"
            c.execute(dbqa)
            self.bcprice = c.fetchone()[0]
            self.uiB.clearance_price.setText(self.bcprice)
            self.uiB.buttonBox.accepted.connect(self.clearance_insert)
            self.clearance.show()
        elif self.bcpurpose == "Bank Requirement":
            dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "employment" + "'"
            c.execute(dbqa)
            self.bcprice = c.fetchone()[0]
            self.uiB.clearance_price.setText(self.bcprice)
            self.uiB.buttonBox.accepted.connect(self.clearance_insert)
            self.clearance.show()
        else:
            msg_box = QMessageBox()

            # Set the title and text of the message box
            msg_box.setWindowTitle('WARNING')
            msg_box.setText("What's your purpose?")

            # Set the type of the message box (Information, Warning, Critical, etc.)
            msg_box.setIcon(QMessageBox.Icon.Warning)

            # Add standard buttons to the message box
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            # You can also customize the buttons or add your own buttons
            # msg_box.addButton('Custom Button', QMessageBox.ButtonRole.ActionRole)

            # Execute the message box and handle the result

            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Ok:
                print('OK clicked')
            elif result == QMessageBox.StandardButton.Cancel:
                print('Cancel clicked')
            else:
                print('Custom button clicked')

    def indigency_preview(self):
        self.indigency = QtWidgets.QDialog()
        self.uiC = Ui_dialog_indigency()
        self.uiC.setupUi(self.indigency)
        c = connection.cursor()
        self.idgpurpose = self.MainUI.cBox_indigency.currentText()
        dbq = "SELECT name FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.idgname = c.fetchone()[0]
        self.uiC.lbl_indname.setText(self.idgname)
        dbq = "SELECT address FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.idgaddress = c.fetchone()[0]
        self.uiC.lbl_indaddress.setText(self.idgaddress)
        self.uiC.lbl_indpurpose.setText(self.idgpurpose)
        self.uiC.buttonBox.accepted.connect(self.idg_insert)
        self.indigency.show()

    def ftjs_preview(self):
        self.ftjs = QtWidgets.QDialog()
        self.uiD = Ui_Dialog()
        self.uiD.setupUi(self.ftjs)
        self.ftjsage = self.MainUI.line_editage.text()
        self.ftjsyears = self.MainUI.line_editstay.text()
        c = connection.cursor()
        dbq = "SELECT name FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.ftjsname = c.fetchone()[0]
        self.uiD.lbl_ftjsname.setText(self.ftjsname)
        dbq = "SELECT address FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.ftjsaddress = c.fetchone()[0]
        dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "ftjs" + "'"
        c.execute(dbqa)
        self.ftjsprice = c.fetchone()[0]
        self.uiD.lbl_ftjsadrdress.setText(self.ftjsaddress)
        self.uiD.lbl_ftjsage.setText(self.ftjsage)
        self.uiD.lbl_ftjsyears.setText(self.ftjsyears)
        self.uiD.ftjs_price.setText(self.ftjsprice)
        self.uiD.buttonBox.accepted.connect(self.ftjs_insert)
        self.ftjs.show()

    def permit_preview(self):
        self.permit = QtWidgets.QDialog()
        self.uiE = Ui_dialog_permit()
        self.uiE.setupUi(self.permit)
        c = connection.cursor()
        self.bpbname = self.MainUI.bp_bname.text()
        self.bpbaddress = self.MainUI.bp_badress.text()
        dbq = "SELECT name FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bpname = c.fetchone()[0]
        self.uiE.lbl_permitname.setText(self.bpname)
        dbq = "SELECT address FROM tbl_users WHERE email LIKE '" + email + "'"
        c.execute(dbq)
        self.bpaddress = c.fetchone()[0]
        dbqa = "SELECT price FROM doc_price WHERE doc_type LIKE '" + "permit" + "'"
        c.execute(dbqa)
        self.bpprice = c.fetchone()[0]
        self.uiE.permit_price.setText(self.bpprice)
        self.uiE.lbl_permitadress.setText(self.bpaddress)
        self.uiE.lbl_businessname.setText(self.bpbname)
        self.uiE.lbl_businessaddress.setText(self.bpbaddress)
        self.uiE.buttonBox.accepted.connect(self.permit_insert)
        self.permit.show()

    def edit_account(self):
        c = connection.cursor()
        new_name = self.MainUI.edit_name.text()
        new_address = self.MainUI.edit_address.text()
        if self.MainUI.rbtn_female.isChecked():
            new_sex = "Female"
        elif self.MainUI.rbtn_male.isChecked():
            new_sex = "Male"
        new_birthday = self.MainUI.edit_birthday.text()
        new_birthplace = self.MainUI.edit_birthplace.text()
        new_cstatus = self.MainUI.edit_cs.text()
        new_ctzn = self.MainUI.edit_ctzn.text()
        new_email = self.MainUI.edit_email.text()
        new_password = self.MainUI.edit_password.text()
        query = ("UPDATE tbl_users SET email = '" + new_email + "', password = '" + new_password + "', name = '" + new_name + "', sex = '" + new_sex +
                 "', address = '" + new_address + "', bday = '" + new_birthday + "', bplace = '" + new_birthplace + "', cstatus = '" + new_cstatus + "', citizenship = '" + new_ctzn + "' WHERE email LIKE '" + email + "'")
        c.execute(query)
        connection.commit()


    def cert_insert(self):
        try:
            c = connection.cursor()
            req = "Not Yet Paid"
            sp = "None"
            c1 = 1
            c.execute("SELECT * FROM doc_requests")
            for row in c:
                if c1 > int(row[0]):
                    print(c1)
                    break
                elif c1 == int(row[0]):
                    c1 += 1
            print(c1)
            doc = "Certification"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO doc_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (c1, date, doc, self.certprice, self.certname, sp, sp, self.certaddress, req, sp, sp, sp, sp, sp,
                       sp, sp, sp))
            connection.commit()
            self.ref = QtWidgets.QDialog()
            self.refUI4 = Ui_dialog_ref()
            self.refUI4.setupUi(self.ref)
            self.refUI4.lbl_ref.setText(str(c1))
            self.ref.show()
        except Exception as e:
            # Handle any exceptions that may occur during connection
            print(f"Error connecting to the database: {e}")

    def idg_insert(self):
        try:
            c = connection.cursor()
            req = "Free"
            sp = "None"
            c1 = 1
            c.execute("SELECT * FROM doc_requests")
            for row in c:
                if c1 > int(row[0]):
                    print(c1)
                    break
                elif c1 == int(row[0]):
                    c1 += 1
            print(c1)
            doc = "Indigency"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO doc_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (c1, date, doc, self.idgprice, self.certname, sp, sp, self.certaddress, req, sp, sp, sp, sp, sp,
                       sp, sp, sp))
            connection.commit()
            self.ref = QtWidgets.QDialog()
            self.refUI3 = Ui_dialog_ref()
            self.refUI3.setupUi(self.ref)
            self.refUI3.lbl_ref.setText(str(c1))
            self.ref.show()
        except Exception as e:
            # Handle any exceptions that may occur during connection
            print(f"Error connecting to the database: {e}")

    def permit_insert(self):
        try:
            c = connection.cursor()
            req = "Not Yet Paid"
            sp = "None"
            c1 = 1
            c.execute("SELECT * FROM doc_requests")
            for row in c:
                if c1 > int(row[0]):
                    print(c1)
                    break
                elif c1 == int(row[0]):
                    c1 += 1
            print(c1)
            doc = "Business Permit"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO doc_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (c1, date, doc, self.bpprice, self.bpname, sp, sp, self.bpaddress, req, sp, sp, sp, sp, sp,
                       self.bpbname, self.bpbaddress, sp))
            connection.commit()
            self.ref = QtWidgets.QDialog()
            self.refUI2 = Ui_dialog_ref()
            self.refUI2.setupUi(self.ref)
            self.refUI2.lbl_ref.setText(str(c1))
            self.ref.show()
        except Exception as e:
            # Handle any exceptions that may occur during connection
            print(f"Error connecting to the database: {e}")

    def clearance_insert(self):
        try:
            c = connection.cursor()
            req = "Not Yet Paid"
            sp = "None"
            c1 = 1
            c.execute("SELECT * FROM doc_requests")
            for row in c:
                if c1 > int(row[0]):
                    print(c1)
                    break
                elif c1 == int(row[0]):
                    c1 += 1
            print(c1)
            doc = "Barangay Clearance"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO doc_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (c1, date, doc, self.bcprice, self.bcname, sp, self.bcsex, self.bcaddress, req, self.bcbday, self.bcbplace, self.bccstatus, self.bccitizenship, self.bcpurpose,
                       sp, sp, sp))
            connection.commit()
            self.ref = QtWidgets.QDialog()
            self.refUI1 = Ui_dialog_ref()
            self.refUI1.setupUi(self.ref)
            self.refUI1.lbl_ref.setText(str(c1))
            self.ref.show()
        except Exception as e:
            # Handle any exceptions that may occur during connection
            print(f"Error connecting to the database: {e}")

    def ftjs_insert(self):
        try:
            c = connection.cursor()
            req = "Not Yet Paid"
            sp = "None"
            c1 = 1
            c.execute("SELECT * FROM doc_requests")
            for row in c:
                if c1 > int(row[0]):
                    print(c1)
                    break
                elif c1 == int(row[0]):
                    c1 += 1
            print(c1)
            self.ref = QtWidgets.QDialog()
            self.refUI = Ui_dialog_ref()
            self.refUI.setupUi(self.ref)
            self.refUI.lbl_ref.setText(str(c1))
            self.ref.show()
            doc = "Certification"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            c.execute("INSERT INTO doc_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (c1, date, doc, self.ftjsprice, self.ftjsname, self.ftjsage, sp, self.ftjsaddress, req, sp, sp, sp, sp, sp,
                       sp, sp, self.ftjsyears))
            connection.commit()

        except Exception as e:
            # Handle any exceptions that may occur during connection
            print(f"Error connecting to the database: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Login()
    mainWin.show()
    sys.exit(app.exec())
