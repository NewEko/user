# Form implementation generated from reading ui file 'preview_certificate.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_preview_certificate(object):
    def setupUi(self, preview_certificate):
        preview_certificate.setObjectName("preview_certificate")
        preview_certificate.resize(506, 346)
        preview_certificate.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(preview_certificate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=preview_certificate)
        self.frame.setMinimumSize(QtCore.QSize(0, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 29, 468, 151))
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.lbl_certifname = QtWidgets.QLabel(parent=self.frame)
        self.lbl_certifname.setGeometry(QtCore.QRect(250, 20, 171, 41))
        self.lbl_certifname.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_certifname.setObjectName("lbl_certifname")
        self.lbl_certifaddress = QtWidgets.QLabel(parent=self.frame)
        self.lbl_certifaddress.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.lbl_certifaddress.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.lbl_certifaddress.setObjectName("lbl_certifaddress")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=preview_certificate)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cert_price = QtWidgets.QLabel(parent=self.frame_2)
        self.cert_price.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.cert_price.setObjectName("cert_price")
        self.verticalLayout_2.addWidget(self.cert_price)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.btnbox_certificate = QtWidgets.QDialogButtonBox(parent=preview_certificate)
        self.btnbox_certificate.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnbox_certificate.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnbox_certificate.setObjectName("btnbox_certificate")
        self.verticalLayout.addWidget(self.btnbox_certificate)

        self.retranslateUi(preview_certificate)
        self.btnbox_certificate.accepted.connect(preview_certificate.accept) # type: ignore
        self.btnbox_certificate.rejected.connect(preview_certificate.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(preview_certificate)

    def retranslateUi(self, preview_certificate):
        _translate = QtCore.QCoreApplication.translate
        preview_certificate.setWindowTitle(_translate("preview_certificate", "Dialog"))
        self.label.setText(_translate("preview_certificate", "This is to certify that Mr./Ms __________ a resident of \n"
"_____________ Brgy. San Rafael III, CSJDM, Bulacan, \n"
"SINCE BIRTH his/her rights, including the duties and\n"
"Responsibilities accorded by RA 11261 through the \n"
"Oath of Undertaking he/she has signed and \n"
"executed in the Presence of our Barangay Official."))
        self.lbl_certifname.setText(_translate("preview_certificate", "s"))
        self.lbl_certifaddress.setText(_translate("preview_certificate", "s"))
        self.cert_price.setText(_translate("preview_certificate", "TextLabel"))
