from PyQt6 import QtCore, QtGui, QtWidgets

class ui_sobre(object):
    def setup_ui(self, Sobre, pix, text):
        Sobre.setObjectName("Sobre")
        Sobre.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Sobre)
        self.gridLayout.setObjectName("gridLayout")
        self.GPALabel = QtWidgets.QLabel(Sobre)
        self.GPALabel.setText("")
        self.GPALabel.setObjectName("GPALabel")
        self.GPALabel.setPixmap(pix)
        self.gridLayout.addWidget(self.GPALabel, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Sobre)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setHtml(text)
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Sobre)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslate_ui(Sobre)
        self.buttonBox.accepted.connect(Sobre.accept)
        self.buttonBox.rejected.connect(Sobre.reject)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslate_ui(self, Sobre):
        Sobre.setWindowTitle(QtWidgets.QApplication.translate("Sobre", "Sobre", None))


