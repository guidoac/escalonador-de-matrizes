import math
import numpy as np

arq = open('in.txt','rt').read()

print (arq)

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

    def print_matriz(self):
        print(self.matriz_final)

    def getColuna(self, col):
        coluna = []
        for linha in self.matriz_final:
            try:
                coluna.append(linha[col])
            except:
                print('Numero da coluna fora do range')
        return coluna


matriz_e = Escalonador(arq)
matriz_e.print_matriz()
print(matriz_e.getColuna(2))
