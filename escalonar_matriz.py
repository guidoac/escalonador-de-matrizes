import math
import numpy as np

#ler arquivo e transforma em str
arq = open('in.txt','rt').read()

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

    def getColuna(self, col):
        return np.array(self.matriz_final[:,col])

    def getPivo(self, linha):
        try:
            return self.matriz_final[linha,linha]
        except:
            print('Numero da linha fora do range')

    def escalonar(self):
        #inicio as variaveis contadoras. i = linha (começa com 1 pois quero escalonar apenas as linhas 1 em diante). j= elemento que precisa ser zerado
        i = 1
        #percorre cada linha da matriz_final a partir da linha 1, pois não escalonamos a linha 1
        for linha in self.matriz_final[1:]:
            #percorre cada elemento da linha a ser escalonada a procura de um elemento diferente de 0 e que vem antes do pivo daquela linha
            j = 0
            for elem in linha:
                if elem !=0 and j < i:
                    coluna = self.getColuna(j)
                    print(coluna)
                    #mais detalhes da func escolher_coef no codigo dela.
                    coefi, linha_esc = self.escolher_coef(coluna[:i])
                    print('formula: {0} * {1} - {2} * {3}'.format(coefi, self.matriz_final[i], elem, self.matriz_final[linha_esc]))
                    pivo_ant = self.getPivo(i-1)
                    #linha_res é a linha que vai substituir na matriz. com as devidas operações feitas para zerar seus elementos que precisam ser zerados
                    linha_res = coefi * self.matriz_final[i] - elem * self.matriz_final[linha_esc]
                    self.matriz_final = np.delete(self.matriz_final, i,0)
                    self.matriz_final = np.insert(self.matriz_final, i, linha_res, axis=0)
                    #troco a linha_res pela linha a ser substituida na matriz_final. E executo a função da forma recursiva para finalizar a matriz.
                    print (self.matriz_final)
                    self.escalonar()
                elif elem == 0 and j==i-1:
                    break
                else:
                    pass
                j+=1

            i+=1
    #função escolher_coef recebe como parametro a coluna do elemento que precisa ser zerado até o elemento imediatamento acima deste.
    #função que possi um retorno duplo, que é o coef que vai ser usado na equação e a linha deste coef.
    #percorro a coluna de forma reversa pois é necessário que o coef seja o ultimo elemento não zero da coluna
    def escolher_coef(self, col):
        if len(list(col)) == 0:
            return col
        else:
            linha_esc = len(col)
            for coef in reversed(col):
                if coef == 0:
                    pass
                else:
                    linha_esc-=1
                    break
                linha_esc-=1
            return coef, linha_esc

matriz_e = Escalonador(arq)
print(matriz_e.matriz_final)
matriz_e.escalonar()
