from PyQt6.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QGridLayout, QLabel, QTextBrowser, QDialogButtonBox, QFrame

class ui_sobre(object):
    def setup_ui(self, Sobre, pix, text):
        Sobre.setObjectName("Sobre")
        Sobre.resize(400, 300)
        self.gridLayout = QGridLayout(Sobre)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(Sobre)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setPixmap(pix)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser = QTextBrowser(Sobre)
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Plain)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(text)
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.buttonBox = QDialogButtonBox(Sobre)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslate_ui(Sobre)
        self.buttonBox.accepted.connect(Sobre.accept)
        self.buttonBox.rejected.connect(Sobre.reject)
        QMetaObject.connectSlotsByName(Sobre)

    def retranslate_ui(self, Sobre):
        Sobre.setWindowTitle(QCoreApplication.translate("Sobre", "Sobre"))

