import math
import numpy as np

#ler arquivo e transforma em str
arq = open('in.txt','rt').read()
arq_s = open('out.txt', 'wt')

'''
classe Escalonador possi como entrada no construtor a str formatada no in.txt.

::attr:: matriz_orig - É a matriz lida no arquivo original in.txt, o atribudo é apenas a str lida
::attr:: matriz_final - É a matriz que vai ser mostrada a cada ciclo do escalonamento. Com as devidas formatações e em lista.
::func:: getColuna - Função que retorna uma instancia de um array numPy da coluna col da matriz_final
::func:: getPivo - Função que recebe como parametro a linha da matriz_final que deseja obter o pivo. Retorna um int.
::func:: escalonar - Função que faz todo o processo de escalonamento da matriz_final junto com a função escolher_coef. Detalhes no código.
::func:: escolher_coef - Auxilia no escalonamento da matriz_final
'''
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
        print('shape: {}'.format(self.matriz_final.shape))

    def getPivo(self, linha):
        try:
            return self.matriz_final[linha][linha]
        except:
            return self.matriz_final[1][linha]

    def escalonar(self):
        #inicio as variaveis contadoras. i = linha (começa com 1 pois quero escalonar apenas as linhas 1 em diante). j= elemento que precisa ser zerado
        #percorre cada linha da matriz_final a partir da linha 1, pois não escalonamos a linha 1
        i = 1
        for i in range(len(self.matriz_final)):
            #percorre cada elemento da linha a ser escalonada a procura de um elemento diferente de 0 e que vem antes do pivo daquela linha
            print('linha: {}'.format(self.matriz_final[i]))
            for j in range(self.matriz_final.shape[0]):
                if self.matriz_final[i][j] !=0 and j < i:
                    print('self.matriz_final[i,j]: {0}, i: {1}, j: {2}'.format(self.matriz_final[i][j], i,j))
                    pivo = self.getPivo(j)
                    print('formula: {0} * {1} - {2} * {3}'.format(pivo, self.matriz_final[i], self.matriz_final[i][j], self.matriz_final[j]))
                    #linha_res é a linha que vai substituir na matriz. com as devidas operações feitas para zerar seus elementos que precisam ser zerados
                    linha_res = pivo * self.matriz_final[i] - self.matriz_final[i][j] * self.matriz_final[j]
                    self.matriz_final = np.delete(self.matriz_final, i,0)
                    self.matriz_final = np.insert(self.matriz_final, i, linha_res, axis=0)
                    #troco a linha_res pela linha a ser substituida na matriz_final. E executo a função da forma recursiva para finalizar a matriz.
                    print (self.matriz_final)
                else:
                    if j == i:
                        print ('i: {0}, j: {1} '.format(i, j))
                        break
                    if j < i:
                        pass
        print('------- finalizado ---------')


matriz_e = Escalonador(arq)
print(matriz_e.matriz_final)
matriz_e.escalonar()
for i in range(matriz_e.matriz_final.shape[0]):
    for j in range(matriz_e.matriz_final[i].shape[0]):
        arq_s.writelines(str(matriz_e.matriz_final[i][j]))
for linha in matriz_e.matriz_final:
    arq_s.write(str(linha))
arq_s.close()
