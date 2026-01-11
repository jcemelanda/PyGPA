# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Wed Aug 31 10:42:37 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureWidget
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as Navbar
from matplotlib.figure import Figure
from PyQt4 import QtCore, QtGui

from about import ui_sobre

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ui_janela_principal(object):
    '''
    class ui_janela_principal
    
    Classe que define a interfacegráfica do programa PyGPA
    
    Métodos:
        setup_ui -> None
        retranslate_ui -> None
    '''
    def __init__(self, controle):
        self.controle = controle


    def setup_ui(self, janela_principal):
        '''
        setup_ui -> None
        
        Configura a interface gráfica, seus elementos e faz a ligação entre
        elementos gráficos e métodos do controle.
        '''
        janela_principal.setObjectName(_fromUtf8("janela_principal"))
        janela_principal.setWindowModality(QtCore.Qt.ApplicationModal)
        janela_principal.resize(800, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/icon.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela_principal.setWindowIcon(icon)
        janela_principal.setUnifiedTitleAndToolBarOnMac(True)
        self.widget_central = QtGui.QWidget(janela_principal)
        self.widget_central.setObjectName(_fromUtf8("widget_central"))
        self.grid = QtGui.QGridLayout(self.widget_central)
        self.grid.setObjectName(_fromUtf8("grid"))
        self.fig = Figure(dpi = 120)
        self.widget_desenho = FigureWidget(self.fig)
        self.widget_desenho.setObjectName(_fromUtf8("widget_desenho"))
        self.widget_desenho.setParent(self.widget_central)
        self.axes = self.fig.add_subplot(111, aspect = 'equal')

        self.navbar = Navbar(self.widget_desenho, self.widget_central)

        self.grid.addWidget(self.widget_desenho, 0, 0, 1, 1)
        self.grid.addWidget(self.navbar, 1, 0, 1, 1)

        janela_principal.setCentralWidget(self.widget_central)
        self.menubar = QtGui.QMenuBar(janela_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_arquivo = QtGui.QMenu(self.menubar)
        self.menu_arquivo.setObjectName(_fromUtf8("menu_arquivo"))
        self.menu_sobre = QtGui.QMenu(self.menubar)
        self.act_sobre_PyGPA = QtGui.QAction(janela_principal)
        self.act_sobre_PyGPA.setObjectName(_fromUtf8("act_sobre_PyGPA"))
        self.menu_sobre.addAction(self.act_sobre_PyGPA)
        self.menu_arquivo.setObjectName(_fromUtf8("menu_sobre"))
        self.menu_ferramentas = QtGui.QMenu(self.menubar)
        self.menu_ferramentas.setObjectName(_fromUtf8("menu_ferramentas"))
        janela_principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(janela_principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        janela_principal.setStatusBar(self.statusbar)
        self.toolbar = QtGui.QToolBar(janela_principal)
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        janela_principal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.act_abrir_arquivo = QtGui.QAction(janela_principal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/document-open.png")),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_abrir_arquivo.setIcon(icon2)
        self.act_abrir_arquivo.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.act_abrir_arquivo.setPriority(QtGui.QAction.HighPriority)
        self.act_abrir_arquivo.setObjectName(_fromUtf8("act_abrir_arquivo"))
        self.act_gerar_vetores = QtGui.QAction(janela_principal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/vector.png")),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_gerar_vetores.setIcon(icon4)
        self.act_gerar_vetores.setObjectName(_fromUtf8("act_gerar_vetores"))
        self.act_anular = QtGui.QAction(janela_principal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/anula.png")),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_anular.setIcon(icon5)
        self.act_anular.setObjectName(_fromUtf8("act_anular"))
        self.act_triangular = QtGui.QAction(janela_principal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/delauney.png")),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_triangular.setIcon(icon6)
        self.act_triangular.setObjectName(_fromUtf8("act_triangular"))
        self.menu_arquivo.addAction(self.act_abrir_arquivo)
        self.menu_arquivo.addSeparator()
        self.menu_ferramentas.addAction(self.act_gerar_vetores)
        self.menu_ferramentas.addAction(self.act_anular)
        self.menu_ferramentas.addAction(self.act_triangular)
        self.menubar.addAction(self.menu_arquivo.menuAction())
        self.menubar.addAction(self.menu_ferramentas.menuAction())
        self.menubar.addAction(self.menu_sobre.menuAction())
        self.toolbar.addAction(self.act_abrir_arquivo)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.act_gerar_vetores)
        self.toolbar.addAction(self.act_anular)
        self.toolbar.addAction(self.act_triangular)
        self.act_gerar_vetores.setEnabled(False)
        self.act_anular.setEnabled(False)
        self.act_triangular.setEnabled(False)

        self.retranslate_ui(janela_principal)
        QtCore.QObject.connect(self.act_abrir_arquivo, QtCore.SIGNAL(
                                    'triggered()'), self.controle.abrir_arquivo)
        QtCore.QObject.connect(self.act_gerar_vetores, QtCore.SIGNAL(
                                    'triggered()'), self.controle.gerar_vetores)
        QtCore.QObject.connect(self.act_anular, QtCore.SIGNAL(
                                    'triggered()'), self.controle.anular)
        QtCore.QObject.connect(self.act_triangular, QtCore.SIGNAL(
                                'triggered()'), self.controle.triangular)
        QtCore.QObject.connect(self.act_sobre_PyGPA, QtCore.SIGNAL(
                                'triggered()'), self.mostrar_sobre)
        QtCore.QMetaObject.connectSlotsByName(janela_principal)
        self.janela = janela_principal

    def retranslate_ui(self, JanelaPrincipal):
        '''
        retranslate_ui -> None
        
        Ajusta as Strings da interface gráfica.
        Método permite internacionalização de forma simples.
        '''
        JanelaPrincipal.setWindowTitle(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "PyGPA",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.menu_arquivo.setTitle(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Arquivo",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.menu_ferramentas.setTitle(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Ferramentas",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.menu_sobre.setTitle(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Sobre",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.toolbar.setWindowTitle(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "toolbar",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_abrir_arquivo.setText(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Abrir",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_sobre_PyGPA.setText(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Sobre o PyGPA",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_abrir_arquivo.setStatusTip(QtGui.QApplication.translate(
                                "JanelaPrincipal", "Abre um arquivo de matriz",
                                None, QtGui.QApplication.UnicodeUTF8))
        self.act_abrir_arquivo.setShortcut(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "Ctrl+O",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_gerar_vetores.setText(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Gerar Vetores",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_gerar_vetores.setShortcut(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+V",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_anular.setText(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Anular",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_anular.setShortcut(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+A",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_triangular.setText(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "&Triangular",
                                        None, QtGui.QApplication.UnicodeUTF8))
        self.act_triangular.setShortcut(QtGui.QApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+T",
                                        None, QtGui.QApplication.UnicodeUTF8))

    def mostrar_sobre(self):
        sobre = QtGui.QDialog(self.janela)
        ui = ui_sobre()
        pix = QtGui.QPixmap(_fromUtf8("icons/icon.png"))
        text = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'\
'<html><head><meta name="qrichtext" content="1" /><style type="text/css">'\
'p, li { white-space: pre-wrap; }'\
'</style></head><body style=" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;">'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">PyGPA</span></p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Versão 0.2</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Copyleft Julio Cesar Eiras Melanda, 2011</p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Este software é distribuído sob a GPL v3.</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">http://www.gnu.org/licenses/gpl-3.0.txt</p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Para mais informações acesse a página do projeto</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;"> </span><span style=" color:#000000;">http://gitorious.org/pygpa/pages/Home</span></a></p></body></html>'
        ui.setup_ui(sobre, pix, text)
        sobre.show()
