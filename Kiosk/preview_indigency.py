# Form implementation generated from reading ui file 'preview_indigency.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dialog_indigency(object):
    def setupUi(self, dialog_indigency):
        dialog_indigency.setObjectName("dialog_indigency")
        dialog_indigency.resize(489, 525)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_indigency)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=dialog_indigency)
        self.frame.setMinimumSize(QtCore.QSize(0, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 468, 361))
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lbl_indname = QtWidgets.QLabel(parent=self.frame)
        self.lbl_indname.setGeometry(QtCore.QRect(180, 40, 131, 61))
        self.lbl_indname.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_indname.setObjectName("lbl_indname")
        self.lbl_indaddress = QtWidgets.QLabel(parent=self.frame)
        self.lbl_indaddress.setGeometry(QtCore.QRect(100, 70, 111, 51))
        self.lbl_indaddress.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_indaddress.setObjectName("lbl_indaddress")
        self.lbl_indpurpose = QtWidgets.QLabel(parent=self.frame)
        self.lbl_indpurpose.setGeometry(QtCore.QRect(250, 260, 161, 51))
        self.lbl_indpurpose.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_indpurpose.setObjectName("lbl_indpurpose")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=dialog_indigency)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.indigency_price = QtWidgets.QLabel(parent=self.frame_2)
        self.indigency_price.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.indigency_price.setObjectName("indigency_price")
        self.verticalLayout_2.addWidget(self.indigency_price)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=dialog_indigency)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_indigency)
        self.buttonBox.accepted.connect(dialog_indigency.accept) # type: ignore
        self.buttonBox.rejected.connect(dialog_indigency.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog_indigency)

    def retranslateUi(self, dialog_indigency):
        _translate = QtCore.QCoreApplication.translate
        dialog_indigency.setWindowTitle(_translate("dialog_indigency", "Dialog"))
        self.label.setText(_translate("dialog_indigency", "To Whom It May Concern:\n"
"\n"
"This is to certify that _________ is bonafide \n"
"resident of ___________ Barangay San Rafael \n"
"III City of San Jose Del Monte, Bulacan\n"
"\n"
"This is also certified that the name stated above \n"
"is belong to the Indigent families based on \n"
"barangay record and considered belong to \n"
"poverty level.\n"
"\n"
"This certification is issued for ______________\n"
"Given this 23rd day of October, 2023 at the \n"
"Office of Punong Barangay of Barangay San \n"
"Rafael III, City of San Jose Del Monte, Bulacan."))
        self.lbl_indname.setText(_translate("dialog_indigency", "s"))
        self.lbl_indaddress.setText(_translate("dialog_indigency", "s"))
        self.lbl_indpurpose.setText(_translate("dialog_indigency", "s"))
        self.indigency_price.setText(_translate("dialog_indigency", "TextLabel"))
