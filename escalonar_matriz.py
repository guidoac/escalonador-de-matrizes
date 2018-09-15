import math
import numpy as np

#ler arquivo e transforma em str
arq = open('in.txt','rt').read()
arq_s = open('out.txt', 'w')

'''
classe Escalonador possi como entrada no construtor a str formatada no in.txt.

::attr:: matriz_orig - É a matriz lida no arquivo original in.txt, o atribudo é apenas a str lida
::attr:: matriz_final - É a matriz que vai ser mostrada a cada ciclo do escalonamento. Com as devidas formatações e em lista.
::func:: getPivo - Função que recebe como parametro a linha da matriz_final que deseja obter o pivo. Retorna um int.
::func:: escalonar - Função que faz todo o processo de escalonamento da matriz_final junto com a função escolher_coef. Detalhes no código.
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
        self.dim = self.matriz_final.shape
        print(self.matriz_final)
        arq_s.write('{}\n'.format(self.matriz_final))
        print('Dimensões da Matriz: {}'.format(self.dim))
        arq_s.write('Dimensões da Matriz: {}'.format(self.dim))
        print()
        arq_s.write('\n')

    def getPivo(self, linha):
        try:
            pivo = self.matriz_final[linha,linha]
            return pivo
        except:
            print('Numero da linha fora do range')
            arq_s.write('Numero da linha fora do range')

    def escalonar(self):
        #inicio as variaveis contadoras. i = linha j = coluna
        #percorre cada linha da matriz para escalonar e zerar os elementos anteriores ao pivo desta linha
        for i in range(len(self.matriz_final)):
            #percorre cada elemento da linha a ser escalonada a procura de um elemento diferente de 0 e que vem antes do pivo daquela linha para fazer os cálculos, gravar na matriz e zerar o elemento
            for j in range(self.matriz_final.shape[0]):
                if self.matriz_final[i,j] !=0 and j < i:
                    print('elemento para zerar: {0} | linha: {1} coluna: {2}|'.format(self.matriz_final[i][j], i+1,j+1))
                    arq_s.write('\nelemento para zerar: {0} | linha: {1} coluna: {2}|'.format(self.matriz_final[i][j], i+1,j+1))
                    pivo = self.getPivo(j)
                    print('formula: {0} * {1} - {2} * {3}'.format(pivo, self.matriz_final[i], self.matriz_final[i][j], self.matriz_final[j]))
                    arq_s.write('\nformula: {0} * {1} - {2} * {3}'.format(pivo, self.matriz_final[i], self.matriz_final[i][j], self.matriz_final[j]))
                    print()
                    arq_s.write('\n')
                    #linha_res é a linha que vai substituir na matriz. com as devidas operações feitas para zerar seus elementos que precisam ser zerados
                    linha_res = pivo * self.matriz_final[i] - self.matriz_final[i,j] * self.matriz_final[j]
                    self.matriz_final = np.delete(self.matriz_final, i,0)
                    self.matriz_final = np.insert(self.matriz_final, i, linha_res, axis=0)
                    #troco a linha_res pela linha a ser substituida na matriz_final. E executo a função da forma recursiva para finalizar a matriz.
                    print (self.matriz_final)
                    arq_s.write('{0}\n'.format(self.matriz_final))
                else:
                    if j == i:
                        #se cair aqui, quer dizer que o elemento j-1 da linha i é zero e ele é o ultimo elemento antes do pivo, muda de linha
                        break
                    if j < i:
                        #se cair aqui, quer dizer que o elemento j-1 da linha i é zero porém este não e o ultimo elemento antes do pivo, continua na mesma linha
                        pass
        print('---------------------------- ESCALONAMENTO FINALIZADO! ----------------------------')
        arq_s.write('\n---------------------------- ESCALONAMENTO FINALIZADO! ----------------------------')

matriz = Escalonador(arq)
matriz.escalonar()
arq_s.close()
