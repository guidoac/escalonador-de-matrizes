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
        i = 1
        j = 0
        for linha in self.matriz_final[1:]:
            for elem in linha:
                if elem !=0 and j < i:
                    pivo_ant = self.getPivo(i-1)
                    linha_res = pivo_ant * self.matriz_final[i] - elem * self.matriz_final[i-1]
                    self.matriz_final = np.delete(self.matriz_final, i,0)
                    self.matriz_final = np.insert(self.matriz_final, i, linha_res, axis=0)
                    print (self.matriz_final)
                    self.escalonar()
                elif elem == 0 and j==i-1:
                    break
                elif elem ==0 and j<i:
                    pass
                j+=1

            #print ('Linha {0}: {1}, pivo ant: {2}'.format(i, linha, coluna, coef))
            i+=1

    def escolher_coef(self, col, index):
        for coef in col[index:]:
            if coef!= 0:
                break
        return coef

matriz_e = Escalonador(arq)
print(matriz_e.matriz_final)
matriz_e.escalonar()
