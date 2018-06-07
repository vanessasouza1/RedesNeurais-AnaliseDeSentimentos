##Criar o Bag of word
import json
##pegar as frases do arquivo e colocar em uma estrutura
## transformar essas frases em uma estrutura com todas as palavras
## eliminar acentuação
## eliminar repetição
## metodo que retorna o vocabulario

class BagOfWords:
    def __init__(self):
        self.vocab = [] #lista de palavras
       # print(type(coments))

    def getArquivo(self):

    def criaVocab(self, sentences): ##tem que receber sentenças em algum lugar
        for sentence in sentences:
            for word in sentence.split(' '):
                if word not in self.vocab:
                    self.vocab.append(word)
                    print(word)
        self.vocab.sort()
        print(len(self.vocab), 'words')

    def retiraAcentuacao(self):

    def retiraRepeticao(self):

    def getVocab(self):




