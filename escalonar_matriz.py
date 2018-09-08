import math
import numpy as np

arq = open('in.txt','rt').read()

class Escalonador():
    def __init__(self, matriz_orig):
        self.matriz_orig = matriz_orig
        matriz_f = []
        matriz = self.matriz_orig.splitlines()
        for l in matriz:
            linha_int = []
            linha_aux = l.split()
            for elem in linha_aux:
                linha_int.append(int(elem))
            matriz_f.append(linha_int)
        self.matriz_final = np.array(matriz_f)

    def getColuna(self, col):
        return np.array(self.matriz_final[:,col])

    def getPivo(self, linha):
        try:
            return self.matriz_final[linha,linha]
        except:
            print('Numero da linha fora do range')

    def escalonar(self):
        i = 0
        for linha in self.matriz_final:
            pivo = self.getPivo(i)
            coluna = self.getColuna(i)
            coef = self.escolher_coef(coluna, i)
            print ('Linha {0}: {1}, pivo: {2}, coluna: {3}, coef: {4}'.format(i, linha, pivo, coluna, coef))
            if i != 0:
                self.matriz_final[i] = 
            i+=1

    def escolher_coef(self, col, index):
        for i in col[index:]:
            if i != 0:
                break
        return i

matriz_e = Escalonador(arq)
print(matriz_e.matriz_final)
matriz_e.escalonar()
