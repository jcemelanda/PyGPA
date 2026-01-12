from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureWidget
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as Navbar
from matplotlib.figure import Figure
from PyQt6.QtCore import Qt, QRect, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QWidget, QGridLayout, QMenuBar, QMenu, QStatusBar, QToolBar, QLabel, QTextBrowser, QDialogButtonBox, QDialog
from PyQt6.QtGui import QIcon, QPixmap, QAction

from about import ui_sobre


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
        janela_principal.setObjectName("janela_principal")
        janela_principal.setWindowModality(Qt.WindowModality.ApplicationModal)
        janela_principal.resize(800, 800)
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/icon.png"),
                       QIcon.Mode.Normal, QIcon.State.Off)
        janela_principal.setWindowIcon(icon)
        janela_principal.setUnifiedTitleAndToolBarOnMac(True)

        self.widget_central = QWidget(janela_principal)
        self.widget_central.setObjectName("widget_central")
        self.grid = QGridLayout(self.widget_central)
        self.grid.setObjectName("grid")
        self.fig = Figure(dpi = 120)
        self.widget_desenho = FigureWidget(self.fig)
        self.widget_desenho.setObjectName("widget_desenho")
        self.widget_desenho.setParent(self.widget_central)
        self.axes = self.fig.add_subplot(111, aspect = 'equal')

        self.navbar = Navbar(self.widget_desenho, self.widget_central)

        self.grid.addWidget(self.widget_desenho, 0, 0, 1, 1)
        self.grid.addWidget(self.navbar, 1, 0, 1, 1)

        janela_principal.setCentralWidget(self.widget_central)
        self.menubar = QMenuBar(janela_principal)
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_arquivo = QMenu(self.menubar)
        self.menu_arquivo.setObjectName("menu_arquivo")
        self.menu_sobre = QMenu(self.menubar)
        self.act_sobre_PyGPA = QAction(janela_principal)
        self.act_sobre_PyGPA.setObjectName("act_sobre_PyGPA")
        self.menu_sobre.addAction(self.act_sobre_PyGPA)
        self.menu_sobre.setObjectName("menu_sobre")
        self.menu_ferramentas = QMenu(self.menubar)
        self.menu_ferramentas.setObjectName("menu_ferramentas")
        janela_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(janela_principal)
        self.statusbar.setObjectName("statusbar")
        janela_principal.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(janela_principal)
        self.toolbar.setObjectName("toolbar")
        janela_principal.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
        janela_principal.addToolBar(self.toolbar)

        self.act_abrir_arquivo = QAction(janela_principal)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/document-open.png"),
                        QIcon.Mode.Normal, QIcon.State.Off)
        self.act_abrir_arquivo.setIcon(icon2)
        self.act_abrir_arquivo.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
        self.act_abrir_arquivo.setPriority(QAction.Priority.HighPriority)
        self.act_abrir_arquivo.setObjectName("act_abrir_arquivo")
        self.act_gerar_vetores = QAction(janela_principal)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("icons/vector.png"),
                        QIcon.Mode.Normal, QIcon.State.Off)
        self.act_gerar_vetores.setIcon(icon4)
        self.act_gerar_vetores.setObjectName("act_gerar_vetores")
        self.act_anular = QAction(janela_principal)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("icons/anula.png"),
                        QIcon.Mode.Normal, QIcon.State.Off)
        self.act_anular.setIcon(icon5)
        self.act_anular.setObjectName("act_anular")
        self.act_triangular = QAction(janela_principal)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap("icons/delauney.png"),
                        QIcon.Mode.Normal, QIcon.State.Off)
        self.act_triangular.setIcon(icon6)
        self.act_triangular.setObjectName("act_triangular")
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
        self.act_abrir_arquivo.triggered.connect(self.controle.abrir_arquivo)
        self.act_gerar_vetores.triggered.connect(self.controle.gerar_vetores)
        self.act_anular.triggered.connect(self.controle.anular)
        self.act_triangular.triggered.connect(self.controle.triangular)
        self.act_sobre_PyGPA.triggered.connect(self.mostrar_sobre)
        QMetaObject.connectSlotsByName(janela_principal)
        self.janela = janela_principal

    def retranslate_ui(self, JanelaPrincipal):
        '''
        retranslate_ui -> None
        
        Ajusta as Strings da interface gráfica.
        Método permite internacionalização de forma simples.
        '''
        JanelaPrincipal.setWindowTitle(QCoreApplication.translate(
                                        "JanelaPrincipal", "PyGPA"))
        self.menu_arquivo.setTitle(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Arquivo"))
        self.menu_ferramentas.setTitle(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Ferramentas"))
        self.menu_sobre.setTitle(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Sobre"))
        self.toolbar.setWindowTitle(QCoreApplication.translate(
                                        "JanelaPrincipal", "toolbar"))
        self.act_abrir_arquivo.setText(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Abrir"))
        self.act_sobre_PyGPA.setText(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Sobre o PyGPA"))
        self.act_abrir_arquivo.setStatusTip(QCoreApplication.translate(
                                "JanelaPrincipal", "Abre um arquivo de matriz"))
        self.act_abrir_arquivo.setShortcut(QCoreApplication.translate(
                                        "JanelaPrincipal", "Ctrl+O"))
        self.act_gerar_vetores.setText(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Gerar Vetores"))
        self.act_gerar_vetores.setShortcut(QCoreApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+V"))
        self.act_anular.setText(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Anular"))
        self.act_anular.setShortcut(QCoreApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+A"))
        self.act_triangular.setText(QCoreApplication.translate(
                                        "JanelaPrincipal", "&Triangular"))
        self.act_triangular.setShortcut(QCoreApplication.translate(
                                        "JanelaPrincipal", "Ctrl+Shift+T"))

    def mostrar_sobre(self):
        sobre = QDialog(self.janela)
        ui = ui_sobre()
        pix = QPixmap("icons/icon.png")
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
