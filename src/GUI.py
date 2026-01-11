# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Jul 19 09:36:32 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureWidget
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as Navbar
from matplotlib.figure import Figure
from PyQt6 import QtCore, QtGui, QtWidgets
from .about import ui_sobre

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
        janela_principal.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        janela_principal.resize(1024, 768)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/icons/icon.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        janela_principal.setWindowIcon(icon)
        
        self.widget_central = QtWidgets.QWidget(janela_principal)
        self.widget_central.setObjectName("widget_central")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_central)
        self.gridLayout.setObjectName("gridLayout")
        self.Tabs = QtWidgets.QTabWidget(self.widget_central)
        self.Tabs.setObjectName("Tabs")
        
        self.graphicPage1 = QtWidgets.QWidget()
        self.graphicPage1.setObjectName("graphicPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graphicPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GPAGrid = QtWidgets.QGridLayout()
        self.GPAGrid.setObjectName("GPAGrid")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.GPAGrid.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.GPAGrid.addItem(spacerItem1, 0, 0, 1, 1)
        self.GPAGroup = QtWidgets.QGroupBox(self.graphicPage1)
        self.GPAGroup.setObjectName("GPAGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.GPAGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.GPALabel = QtWidgets.QLabel(self.GPAGroup)
        self.GPALabel.setObjectName("GPALabel")
        self.gridLayout_5.addWidget(self.GPALabel, 0, 0, 1, 1)
        self.GPAGrid.addWidget(self.GPAGroup, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.GPAGrid, 1, 2, 1, 1)
        
        self.delaunayGroup = QtWidgets.QGroupBox(self.graphicPage1)
        self.delaunayGroup.setObjectName("delaunayGroup")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.delaunayGroup)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.delaunay_figure = Figure(dpi = 120)
        self.widget_delaunay = FigureWidget(self.delaunay_figure)
        self.widget_delaunay.setObjectName("widget_delaunay")
        self.widget_delaunay.setParent(self.delaunayGroup)
        self.delaunay_axes = self.delaunay_figure.add_subplot(111, aspect = 'equal')
        self.gridLayout_4.addWidget(self.widget_delaunay, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.delaunayGroup, 1, 1, 1, 1)
        self.vetfieldGroup = QtWidgets.QGroupBox(self.graphicPage1)
        self.vetfieldGroup.setObjectName("vetfieldGroup")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.vetfieldGroup)
        self.gridLayout_9.setObjectName("gridLayout_9")
        
        self.vector_figure = Figure(dpi = 120)
        self.widget_vector = FigureWidget(self.vector_figure)
        self.widget_vector.setObjectName("widget_vector")
        self.widget_vector.setParent(self.vetfieldGroup)
        self.vector_axes = self.vector_figure.add_subplot(111, aspect = 'equal')
        self.gridLayout_9.addWidget(self.widget_vector, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.vetfieldGroup, 1, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.gridLayout_3.setColumnStretch(1, 8)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.Tabs.addTab(self.graphicPage1, "")
        self.vectorTab = QtWidgets.QWidget()
        self.vectorTab.setObjectName("vectorTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.vectorTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.vetGroupTab = QtWidgets.QGroupBox(self.vectorTab)
        self.vetGroupTab.setObjectName("vetGroupTab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.vetGroupTab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        
        self.vector_figure_tab = Figure(dpi = 120)
        self.widget_vector_tab = FigureWidget(self.vector_figure_tab)
        self.widget_vector_tab.setObjectName("widget_vector_tab")
        self.widget_vector_tab.setParent(self.vetGroupTab)
        self.vector_tab_axes = self.vector_figure_tab.add_subplot(111, aspect = 'equal')
        self.gridLayout_12.addWidget(self.widget_vector_tab, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.vetGroupTab, 0, 0, 1, 1)
        self.toolGroupVet = QtWidgets.QGroupBox(self.vectorTab)
        self.toolGroupVet.setObjectName("toolGroupVet")
        self.gridLayout_6.addWidget(self.toolGroupVet, 1, 0, 1, 1)
        self.gridLayout_6.setRowStretch(0, 5)
        self.gridLayout_6.setRowStretch(1, 1)
        self.Tabs.addTab(self.vectorTab, "")
        self.delaunayTab = QtWidgets.QWidget()
        self.delaunayTab.setObjectName("delaunayTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.delaunayTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.delaunayGroupTab = QtWidgets.QGroupBox(self.delaunayTab)
        self.delaunayGroupTab.setObjectName("delaunayGroupTab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.delaunayGroupTab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        
        self.delaunay_figure_tab = Figure(dpi = 120)
        self.widget_delaunay_tab = FigureWidget(self.delaunay_figure_tab)
        self.widget_delaunay_tab.setObjectName("widget_delaunay_tab")
        self.widget_delaunay_tab.setParent(self.delaunayGroupTab)
        self.delaunay_tab_axes = self.delaunay_figure_tab.add_subplot(111, aspect = 'equal')
        self.gridLayout_11.addWidget(self.widget_delaunay_tab, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.delaunayGroupTab, 0, 0, 1, 1)
        self.toolGroupDelaunay = QtWidgets.QGroupBox(self.delaunayTab)
        self.toolGroupDelaunay.setObjectName("toolGroupDelaunay")
        self.gridLayout_7.addWidget(self.toolGroupDelaunay, 1, 0, 1, 1)
        self.gridLayout_7.setRowStretch(0, 5)
        self.gridLayout_7.setRowStretch(1, 1)
        self.Tabs.addTab(self.delaunayTab, "")
        self.gpaTab = QtWidgets.QWidget()
        self.gpaTab.setObjectName("gpaTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gpaTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.GPAGraphGroup = QtWidgets.QGroupBox(self.gpaTab)
        self.GPAGraphGroup.setObjectName("GPAGraphGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.GPAGraphGroup)
        self.gridLayout_10.setObjectName("gridLayout_10")
        
        self.GPA_figure = Figure(dpi = 120)
        self.widget_gpa_ev = FigureWidget(self.GPA_figure)
        self.widget_gpa_ev.setObjectName("widget_gpa_ev")
        self.widget_gpa_ev.setParent(self.GPAGraphGroup)
        self.GPA_axes = self.GPA_figure.add_subplot(111, aspect = 'equal')
        self.gridLayout_10.addWidget(self.widget_gpa_ev, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.GPAGraphGroup, 0, 0, 1, 1)
        self.Tabs.addTab(self.gpaTab, "")
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        self.controGroup = QtWidgets.QGroupBox(self.widget_central)
        self.controGroup.setFlat(False)
        self.controGroup.setObjectName("controGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.controGroup)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.controGroup, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 1)
        janela_principal.setCentralWidget(self.widget_central)
        self.menubar = QtWidgets.QMenuBar(janela_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        janela_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(janela_principal)
        self.statusbar.setObjectName("statusbar")
        janela_principal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(janela_principal)
        self.toolBar.setObjectName("toolBar")
        janela_principal.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionAbrir_Matriz = QtGui.QAction(janela_principal)
        self.actionAbrir_Matriz.setObjectName("actionAbrir_Matriz")
        self.actionAbrir_Matriz.setIcon(QtGui.QIcon("src/icons/document-open.png"))
        self.actionAbrir_Matriz.triggered.connect(self.controle.abrir_arquivo)

        self.actionAbrir_Conjunto_de_Matrizes = QtGui.QAction(janela_principal)
        self.actionAbrir_Conjunto_de_Matrizes.setObjectName("actionAbrir_Conjunto_de_Matrizes")
        self.actionAbrir_Conjunto_de_Matrizes.triggered.connect(self.controle.abrir_arquivo)
        
        self.actionAbrir_Imagem = QtGui.QAction(janela_principal)
        self.actionAbrir_Imagem.setObjectName("actionAbrir_Imagem")
        self.actionAbrir_Imagem.setIcon(QtGui.QIcon("src/icons/document-open-recent.png"))
        self.actionAbrir_Imagem.triggered.connect(self.controle.abrir_arquivo)

        self.act_gerar_vetores = QtGui.QAction(janela_principal)
        self.act_gerar_vetores.setObjectName("act_gerar_vetores")
        self.act_gerar_vetores.setIcon(QtGui.QIcon("src/icons/vector.png"))
        self.act_gerar_vetores.triggered.connect(self.controle.gerar_vetores)

        self.act_anular = QtGui.QAction(janela_principal)
        self.act_anular.setObjectName("act_anular")
        self.act_anular.setIcon(QtGui.QIcon("src/icons/anula.png"))
        self.act_anular.setEnabled(False)
        self.act_anular.triggered.connect(self.controle.anular)

        self.act_triangular = QtGui.QAction(janela_principal)
        self.act_triangular.setObjectName("act_triangular")
        self.act_triangular.setIcon(QtGui.QIcon("src/icons/delauney.png"))
        self.act_triangular.setEnabled(False)
        self.act_triangular.triggered.connect(self.controle.triangular)

        self.menu_Arquivo.addAction(self.actionAbrir_Matriz)
        self.menu_Arquivo.addAction(self.actionAbrir_Conjunto_de_Matrizes)
        self.menu_Arquivo.addAction(self.actionAbrir_Imagem)
        self.menubar.addAction(self.menu_Arquivo.menuAction())

        self.toolBar.addAction(self.actionAbrir_Matriz)
        self.toolBar.addAction(self.actionAbrir_Imagem)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_gerar_vetores)
        self.toolBar.addAction(self.act_anular)
        self.toolBar.addAction(self.act_triangular)

        self.retranslateUi(janela_principal)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(janela_principal)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None))
        self.GPAGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "GPA", None))
        self.GPALabel.setText(QtWidgets.QApplication.translate("MainWindow", "0,778", None))
        self.delaunayGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Triangulação de Delaunay", None))
        self.vetfieldGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Campo Vetorial", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.graphicPage1), QtWidgets.QApplication.translate("MainWindow", "Gráficos", None))
        self.vetGroupTab.setTitle(QtWidgets.QApplication.translate("MainWindow", "Gráfico", None))
        self.toolGroupVet.setTitle(QtWidgets.QApplication.translate("MainWindow", "Toolbox", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.vectorTab), QtWidgets.QApplication.translate("MainWindow", "Campo Vetorial", None))
        self.delaunayGroupTab.setTitle(QtWidgets.QApplication.translate("MainWindow", "Gráfico", None))
        self.toolGroupDelaunay.setTitle(QtWidgets.QApplication.translate("MainWindow", "Toolbox", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.delaunayTab), QtWidgets.QApplication.translate("MainWindow", "Triangulação de Delaunay", None))
        self.GPAGraphGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Gráfico", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.gpaTab), QtWidgets.QApplication.translate("MainWindow", "Evolução do GPA", None))
        self.controGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Controle", None))
        self.menu_Arquivo.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Arquivo", None))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None))
        self.actionAbrir_Matriz.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir Matriz", None))
        self.actionAbrir_Conjunto_de_Matrizes.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir Conjunto de Matrizes", None))
        self.actionAbrir_Imagem.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir Imagem", None))

    def mostrar_sobre(self):
        sobre = QtWidgets.QDialog(self.janela)
        ui = ui_sobre()
        pix = QtGui.QPixmap("icons/icon.png")
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
