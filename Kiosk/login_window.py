# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit


class Ui_win_login(object):
    def setupUi(self, win_login):
        win_login.setObjectName("win_login")
        win_login.resize(633, 277)
        win_login.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.517045, x2:1, y2:0.511364, stop:0 rgba(17, 21, 28, 255), stop:1 rgba(33, 45, 64, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=win_login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 30pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.line_editemail = QtWidgets.QLineEdit(parent=self.frame_2)
        self.line_editemail.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    font: 22pt \"Helvetica Neue\";\n"
"    background-color: #1974D2;\n"
"border: none;")
        self.line_editemail.setText("")
        self.line_editemail.setObjectName("line_editemail")
        self.verticalLayout_4.addWidget(self.line_editemail)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 30pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.line_editpassword = QtWidgets.QLineEdit(parent=self.frame_2)
        self.line_editpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_editpassword.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    font: 22pt \"Helvetica Neue\";\n"
"    background-color: #1974D2;\n"
"border: none;")
        self.line_editpassword.setText("")
        self.line_editpassword.setObjectName("line_editpassword")
        self.verticalLayout_4.addWidget(self.line_editpassword)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_register = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_register.setStyleSheet("QPushButton{\n"
"background-color: rgb(229, 228, 226);\n"
"    font: 25 15pt \"Roboto Light\";\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(195, 195, 195);\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout.addWidget(self.btn_register)
        self.btn_login = QtWidgets.QPushButton(parent=self.frame_3)
        self.btn_login.setStyleSheet("QPushButton{\n"
"background-color: rgb(229, 228, 226);\n"
"    font: 25 15pt \"Roboto Light\";\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(195, 195, 195);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        win_login.setCentralWidget(self.centralwidget)

        self.retranslateUi(win_login)
        QtCore.QMetaObject.connectSlotsByName(win_login)

    def retranslateUi(self, win_login):
        _translate = QtCore.QCoreApplication.translate
        win_login.setWindowTitle(_translate("win_login", "MainWindow"))
        self.label_2.setText(_translate("win_login", "Email:"))
        self.line_editemail.setPlaceholderText(_translate("win_login", "xxxx@yyyy.com"))
        self.label_3.setText(_translate("win_login", "Password:"))
        self.line_editpassword.setPlaceholderText(_translate("win_login", "Password"))
        self.btn_register.setText(_translate("win_login", "Register"))
        self.btn_login.setText(_translate("win_login", "Enter"))
