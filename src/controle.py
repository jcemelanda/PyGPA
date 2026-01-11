# -*- coding: utf8 -*-
'''
Created on 31/08/2011

@author: julio
'''
from .GUI import ui_janela_principal
from PyQt6 import QtWidgets, QtGui
from matplotlib import tri
from os.path import expanduser
from PIL import Image
from time import time
import sys

HOME_PATH = expanduser('~')

class controle:
    '''
    class controle
    
    Controla o funcionamento do programa PyGPASim
    
    Métodos:
        abrir_arquivo -> None
        triangular-> None
        gerar_vetores -> None
        anular -> None
        get_dx -> list
        get_dy -> list
    
    '''

    def __init__(self):
        '''
        Inicializa a aplicação
        '''

        app = QtWidgets.QApplication(sys.argv)
        janela_principal = QtWidgets.QMainWindow()
        self.ui = ui_janela_principal(self)
        self.ui.setup_ui(janela_principal)
        janela_principal.showMaximized()
        self.matriz = []
        sys.exit(app.exec())

    def abrir_arquivo(self):
        '''
        abrir_arquivo -> None
        
        Abre um arquivo contendo uma matriz bidimensional de dados ou uma 
        imagem e gera a matriz de dados interna do programa.        
        
        '''
        self.normalizado = False
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent = None,
                                caption = 'Abrir arquivo',
        filter = 'Dados textuais (*.txt *.dat);;Imagens (*.png *.bmp *.jpg)')
        
        if not file_path:
            return

        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            try:
                im = Image.open(str(file_path), 'r')
                im = im.convert('L')
                #  im.show() # Optional: could be annoying if it pops up every time
                w, h = im.size
                mat = []
                dlg = QtWidgets.QProgressDialog('Lendo Imagem', 'Cancelar',
                                        0, h)
                dlg.setModal(True)
                dlg.setMinimumDuration(0)
                dlg.setAutoClose(True)
                dlg.setWindowTitle('Leitura de Imagem')
                dlg.show()
                for i in range(h):
                    line = []
                    for j in range(w):
                        line.append(im.getpixel((j, i)))
                    mat.append(line)
                    dlg.setValue(i)
                    if dlg.wasCanceled():
                        return
                mat.reverse()
                self.matriz = mat[:]
                self.gerar_vetores()
            except IOError as e:
                print('Abertura de imagem falhou ' + str(e))
                return
        else:
            try:
                f = open(str(file_path), 'r')
            except IOError as e:
                print('Abertura de arquivo de dados falhou ' + str(e))
                return
            
            matrix = []
            supermatrix = []
            mat_lines = f.readlines()
            self.matriz = []
            dlg = QtWidgets.QProgressDialog('Lendo Dados', 'Cancelar',
                                        0, len(mat_lines))
            dlg.setModal(True)
            dlg.setMinimumDuration(0)
            dlg.setAutoClose(True)
            dlg.setWindowTitle('Leitura de Dados')
            dlg.show()
            
            if mat_lines and mat_lines[-1].strip() == '':
                mat_lines.pop()
                
            for i, line in enumerate(mat_lines):
                if not line.strip():
                    matrix.reverse()
                    supermatrix.append(matrix[:])
                    matrix = []
                    continue
                row = line.strip().split()
                try:
                    matrix.append([float(e) for e in row])
                except ValueError:
                    continue # Skip non-numeric lines
                    
                dlg.setValue(i)
                if dlg.wasCanceled():
                    f.close()
                    return
            
            matrix.reverse()
            supermatrix.append(matrix[:])
            self.matriz = supermatrix[:]
            dlg.close()
            f.close()
            self.gerar_vetores()

    def triangular(self):
        '''
        triangular -> None
        
        Gera a triangulação de Delaunay para o conjunto de dados, 
        plota os triângulos e exibe o número de arestas encontradas.      
        
        '''
        vects = [list(zip(x, y)) for x, y in zip(self.dx, self.dy)]
        points = []
        for i in range(len(vects)):
            line = []
            for j in range(len(vects[0])):
                x, y = vects[i][j]
                if (abs(x) > 0.0) or (abs(y) > 0.0):
                    if [x + j, y + i] not in points:
                        line.append([x + j, y + i])
            points += line

        x, y = zip(*points)
        t = tri.Triangulation(x, y)
        self.ui.delaunay_axes.clear()
        minx = round(min(list(zip(*self.dx))[0])) - 1
        maxx = round(max(list(zip(*self.dx))[-1]))
        miny = round(min(self.dy[0])) - 1
        maxy = round(max(self.dy[-1]))
        if miny >= 0:
            miny = -1
        if minx >= 0:
            minx = -1
        self.ui.delaunay_axes.set_xlim(minx, len(self.dx[0]) + maxx)
        self.ui.delaunay_axes.set_ylim(miny, len(self.dx) + maxy)
        self.ui.delaunay_axes.triplot(t)
        self.ui.widget_delaunay.draw()

        dlg = QtWidgets.QMessageBox()
        dlg.setText('Ga = %.6f' % ((len(t.edges) - len(x)) / float(len(x))))
        dlg.setWindowTitle('Coeficiente de Assimetra')
        dlg.setModal(True)
        dlg.exec()
        self.ui.act_gerar_vetores.setEnabled(False)
        self.ui.act_anular.setEnabled(False)
        self.ui.act_triangular.setEnabled(True)
        self.ui.statusbar.showMessage('Delaunay completada.')

    def gerar_vetores(self, recalc = True):
        '''
        gerar_vetores -> None
        
        gera o campo de gradientes do conjunto de dados a partir das derivadas 
        parciais em x e y de cada elemento do conjunto.        
        
        '''
        if recalc:
            self.dx = self.get_dx()
            self.dy = self.get_dy()
            self.ui.act_gerar_vetores.setEnabled(False)
            self.ui.act_anular.setEnabled(True)
            self.ui.act_triangular.setEnabled(False)

        self.normaliza_derivadas()
        self.normalizado = True

        minx = -1
        maxx = round(max(list(zip(*self.dx))[-1]))
        miny = -1
        maxy = round(max(self.dy[-1]))

        self.ui.vector_axes.clear()
        q = self.ui.vector_axes.quiver(self.dx, self.dy, angles = 'xy', scale = 1.0,
                                scale_units = 'xy', minshaft = 2, minlength = 0.5)
        self.ui.vector_axes.quiverkey(q, 0, miny - 2, 1, '', coordinates = 'data')
        self.ui.vector_axes.set_xlim(minx, len(self.dx[0]) + maxx)
        self.ui.vector_axes.set_ylim(miny, len(self.dx) + maxy)
        self.ui.widget_vector.draw()

    def normaliza_derivadas(self):

        if self.normalizado:
            return

        maximo = 0.0

        for linha in self.dx:
            m = max([abs(l) for l in linha])
            if m > maximo:
                maximo = m
        for linha in self.dy:
            m = max([abs(l) for l in linha])
            if m > maximo:
                maximo = m
        self.dx = [[d / float(maximo) for d in linha] for linha in self.dx]
        self.dy = [[d / float(maximo) for d in linha] for linha in self.dy]

    def anular(self):
        '''
        anular -> None
        
        Coloca norma zero para os pares de vetores que se anulam.        
        
        '''
        vects = [list(zip(x, y)) for x, y in zip(self.dx, self.dy)]
        dlg = QtWidgets.QProgressDialog('Otimizando campo', 'Cancelar',
                                    0, len(vects))
        dlg.setModal(True)
        dlg.setMinimumDuration(0)
        dlg.setAutoClose(True)
        dlg.setWindowTitle('Eliminar vetores')
        dlg.show()
        for i in range(len(vects)):
            for j in range(len(vects[0])):
                for k in range(i, len(vects)):
                    for w in range(len(vects[0])):
                        a = vects[i][j]
                        b = vects[k][w]
                        if a == (0, 0):
                            break
                        if (a[0] == -b[0]) and (a[1] == -b[1]):
                                vects[i][j] = vects[k][w] = (0, 0)
                                break
            dlg.setValue(i)
            if dlg.wasCanceled():
                return
        dlg.close()
        del(dlg)
        v = [list(zip(*l)) for l in vects]
        self.dx, self.dy = zip(*v)
        self.gerar_vetores(False)
        self.ui.act_gerar_vetores.setEnabled(False)
        self.ui.act_anular.setEnabled(False)
        self.ui.act_triangular.setEnabled(True)

    def get_dx(self):
        '''
        get_dx -> list
        
        Gera uma matriz com as derivadas parciais em x para a matriz de dados
        lida
        
        
        '''
        dx = []
        dlg = QtWidgets.QProgressDialog('Calculando dx', 'Cancelar',
                                    0, len(self.matriz[:-1]))
        dlg.setModal(True)
        dlg.setMinimumDuration(0)
        dlg.setAutoClose(True)
        dlg.setWindowTitle('Cálculo da derivada')
        dlg.show()
        a = 0
        for linha in self.matriz[:]:
            linha_dx = []
            for i in range(len(linha)):
                if i == 0:
                    linha_dx.append(
                                (-3 * linha[0] + 4 * linha[1] - linha[2]) / 2.0)
                elif i == len(linha) - 1:
                    linha_dx.append(
                            (3 * linha[-1] - 4 * linha[-2] + linha[-3]) / 2.0)
                else:
                    linha_dx.append((linha[i + 1] - linha[i - 1]) / 2.0)
            dx.append(linha_dx)
            dlg.setValue(a)
            a += 1
            if dlg.wasCanceled():
                return
        dlg.close()
        return dx

    def get_dy(self):
        '''
        get_dy -> list
        
        Gera uma matriz com as derivadas parciais em y para a matriz de dados
        lida
        
        
        '''
        dy = []
        dlg = QtWidgets.QProgressDialog('Calculando dy', 'Cancelar',
                                    0, len(self.matriz[:-1]))
        dlg.setModal(True)
        dlg.setMinimumDuration(0)
        dlg.setAutoClose(True)
        dlg.setWindowTitle('Cálculo da derivada')
        dlg.show()
        a = 0
        for linha in zip(*self.matriz[:]):
            linha_dy = []
            for i in range(len(linha)):
                if i == 0:
                    linha_dy.append(
                                (-3 * linha[0] + 4 * linha[1] - linha[2]) / 2.0)
                elif i == len(linha) - 1:
                    linha_dy.append(
                            (3 * linha[-1] - 4 * linha[-2] + linha[-3]) / 2.0)
                else:
                    linha_dy.append((linha[i + 1] - linha[i - 1]) / 2.0)
            dy.append(linha_dy)
            dlg.setValue(a)
            a += 1
            if dlg.wasCanceled():
                return
        dlg.close()
        return list(zip(*dy))
