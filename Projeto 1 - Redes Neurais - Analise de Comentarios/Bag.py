import unicodedata
from unicodedata import normalize
import re
import numpy as np

# depois tentar fazer com que as palavras que estejam nos dois conjuntos pos e neg sejam excluidas, pq elas n vao ter valor
import json
##pegar as frases do arquivo e colocar em uma estrutura
## transformar essas frases em uma estrutura com todas as palavras
## eliminar acentuação
## eliminar repetição
## metodo que retorna o vocabulario
#import numpy as np
# tem q fazer uma base de positivos com as qualificações, outra com os negativos e outra pra juntar os dois
#s.split(" ") para separar o texto
#colocar todoo o texto em minusculo  "ALFA".lower()
# coloca as palavras em um vetor eliminando o que for pontuaçao e o q tiver menos 1 ou 2 letras e iterar pra ve se tem alguma pontuação grudada (pesquisando a string)
# ou que retorna false se não for letras "abc".isalpha()
#remove duplicações     words = set(words)
#depois faz o bagof words do array
class Bag:
    def __init__(self):
       # self.vocabPos = [] #lista de palavras
       # self.vocabNeg = []
        self.vocabTotal = []
    ## Cria array com todas as palavras

    # def constroiVocab(self, sentencesPos, sentencesNeg): #passa array de parametros com sentences e retorna o array de palavras
    #     for sentence in sentencesPos:
    #         for word in sentence.split(' '):
    #             if len(word) > 2:  # verifica se a palavra tem mais de duas letras
    #                 print(word)
    #                 word1 = word.lower()
    #                 print(word1)
    #                 self.vocabPos.append(word1) #coloca em caixa baixa
    #     self.vocabPos = set(self.vocabPos)
    #     print(len(self.vocabPos), 'words')
    #     print(self.vocabPos)
    #
    #     for sentence in sentencesNeg:
    #         for word in sentence.split(' '):
    #             if len(word) > 2:  # verifica se a palavra tem mais de duas letras
    #                 print(word)
    #                 word1 = word.lower()
    #                 print(word1)
    #                 self.vocabNeg.append(word1)  # coloca em caixa baixa
    #     self.vocabNeg = set(self.vocabNeg)
    #     print(len(self.vocabNeg), 'words')
    #     print(self.vocabNeg)
    def setVocabTotal(self, vocabPos, vocabNeg):
        print('Vocab1 : ' + str(len(self.vocabTotal)))
        self.vocabTotal.extend(vocabPos)
        print('Vocab2 :' + str(len(self.vocabTotal)))
        self.vocabTotal.extend(vocabNeg)
        print('Vocab3 :' + str(len(self.vocabTotal)))
        print(self.vocabTotal)

    def getVocabTotal(self):
        return self.vocabTotal

    def getSizeVocabTotal(self):
        return len(self.vocabTotal)


    def removerAcentosECaracteresEspeciais(self,palavra):

        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

    def constroiSubVocab(self, sentences):  # passa array de parametros com sentences e retorna o array de palavras
        subVocab = []
        for sentence in sentences:
                for word in sentence.split(' '):
                    if len(word) > 2:  # verifica se a palavra tem mais de duas letras
                        word1 = self.removerAcentosECaracteresEspeciais(word).lower() #remove acentos e pontuacao e coloca em caixa baixa
                        subVocab.append(word1)
        subVocab = set(subVocab) #retira repeticoes
        print(len(subVocab), 'sub words')
       # print(subVocab)
        return subVocab

    def toarray(self, sentence): # o size vai ser passado como a soma dos arrays pos e neg
        words = sentence.split(' ')

        vector = np.zeros(len(self.vocabTotal))

        for word in words:
            word1 = self.removerAcentosECaracteresEspeciais(word).lower()
            for i, _word in enumerate(self.vocabTotal):
                if _word == word1:
                    vector[i] = 1.0
                    #print(i, word1, _word)
       # print(vector)
        return vector

    # def retiraPalavPeq(self):  ## colocar pra retirar palavras com 1 ou 2 letras

    # def retiraAcentuacao(self):
    #
    # def retiraRepeticao(self):
    #
    # def getVocab(self):







