# Form implementation generated from reading ui file 'preview_permit.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dialog_permit(object):
    def setupUi(self, dialog_permit):
        dialog_permit.setObjectName("dialog_permit")
        dialog_permit.resize(490, 596)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_permit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=dialog_permit)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 468, 361))
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lbl_permitname = QtWidgets.QLabel(parent=self.frame)
        self.lbl_permitname.setGeometry(QtCore.QRect(120, 62, 101, 21))
        self.lbl_permitname.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_permitname.setObjectName("lbl_permitname")
        self.lbl_permitadress = QtWidgets.QLabel(parent=self.frame)
        self.lbl_permitadress.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.lbl_permitadress.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_permitadress.setObjectName("lbl_permitadress")
        self.lbl_businessname = QtWidgets.QLabel(parent=self.frame)
        self.lbl_businessname.setGeometry(QtCore.QRect(170, 170, 221, 41))
        self.lbl_businessname.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_businessname.setObjectName("lbl_businessname")
        self.lbl_businessaddress = QtWidgets.QLabel(parent=self.frame)
        self.lbl_businessaddress.setGeometry(QtCore.QRect(200, 190, 221, 51))
        self.lbl_businessaddress.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_businessaddress.setObjectName("lbl_businessaddress")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=dialog_permit)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.permit_price = QtWidgets.QLabel(parent=self.frame_2)
        self.permit_price.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.permit_price.setObjectName("permit_price")
        self.verticalLayout_2.addWidget(self.permit_price, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=dialog_permit)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_permit)
        self.buttonBox.accepted.connect(dialog_permit.accept) # type: ignore
        self.buttonBox.rejected.connect(dialog_permit.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog_permit)

    def retranslateUi(self, dialog_permit):
        _translate = QtCore.QCoreApplication.translate
        dialog_permit.setWindowTitle(_translate("dialog_permit", "Dialog"))
        self.label.setText(_translate("dialog_permit", "To Whom It May Concern:\n"
"This is to certify that undersigned approved herein \n"
"application of __________, with the address of \n"
"____________, Barangay San Rafael III, CSJDM, \n"
"Bulacan for a permit and license to operate/ renew \n"
"a business.\n"
"\n"
"BUSINESS NAME: \n"
"BUSINESS ADDRESS: \n"
"\n"
"It is further certified that the subject business is not \n"
"a nuisance to public safety and order. Moreover, the \n"
"above name applicant pledge to abide with the existing \n"
"laws, ordinances, rules and regulations pertaining to \n"
"said activity."))
        self.lbl_permitname.setText(_translate("dialog_permit", "TextLabel"))
        self.lbl_permitadress.setText(_translate("dialog_permit", "TextLabel"))
        self.lbl_businessname.setText(_translate("dialog_permit", "TextLabel"))
        self.lbl_businessaddress.setText(_translate("dialog_permit", "TextLabel"))
        self.permit_price.setText(_translate("dialog_permit", "TextLabel"))
