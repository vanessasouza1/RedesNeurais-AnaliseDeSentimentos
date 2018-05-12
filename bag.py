# -*- coding: utf-8 -*-

import json
import numpy as np

import os, sys
import string



from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer
from pybrain.structure import SoftmaxLayer


class BagOfWords:
    def __init__(self):
        self.vocab = [] #lista de palavras

    def readArchive(self, name):
        # arq = open('/Treinamento/BaseComentariosNegativos.txt', 'r')
        # texto = arq.readlines()
        #
        # arrayWords = []
        # for linha in texto :
        #     print(linha)
        #     arrayWords = arrayWords.union(linha)
        #
        # arq.close()
        comments = json.loads(open(str(name), "r").read())

        return comments

    def toUtf(self, unicode):
        text = []
        sentence = str(unicode)
        text = sentence.encode('utf-8')
        print text
        #for comment in unicode:

         #   sentence = comment.get('Text')
          #  coded = sentence.encode(sys.stdout.encoding)
           # text.append(coded)


        return text

    def build_vocab(self, sentences):
        for sentence in sentences:
            for word in sentence.split(' '):
                if word not in self.vocab:
                    self.vocab.append(word)
        self.vocab.sort()
        print(len(self.vocab), 'words')

    def toarray(self,sentence):
        words = sentence.split(' ')

        vector = np.zeros(len(self.vocab))

        for word in words:
            for i, _word in enumerate(self.vocab):
                #print(i, _word)
                if _word == word:
                        vector[i] = 1.0
        return vector

    def get_len(self):
        return len(self.vocab)


bow = BagOfWords() # A classe que vai ter o bag of words

sentencesn = bow.readArchive("BaseComentariosNegativos.json")

print sentencesn

sentencesp = bow.readArchive("BaseComentariosPositivos.json")

print sentencesp

negative = bow.toUtf(sentencesn)
positive = bow.toUtf(sentencesp)
sentences = ""

sentences = sentences + " " + str(negative) + " " + str(positive)

print sentences

bow.build_vocab(sentences)

print sentences
#sentences = ['eu gosto de você', 'eu te odeio', 'eu gosto de ir ao shopping', 'eu detesto ir a praia', 'amo ir ao shopping']
#sentences = json.loads(open("BaseComentariosNegativos.json", "r").read())
test = ['gosto de você', 'amo comprar roupas', 'odeio ir a escola', 'garoto malvado']

#bow = BagOfWords()
#bow.build_vocab(sentences)

inputs = []
#outputs = []
outputs = [[0.99], [0.01], [0.99], [0.01], [0.99]]

#for cont in sentences:
#    outputs[cont] = [0.0]

for sentenc in sentences:
    vectors = bow.toarray(sentenc)

    sample = []
    for num in vectors:
        sample.append(num)
    inputs.append(sample)

print()
ds = SupervisedDataSet(bow.get_len(), 1)
print("input " + str(inputs))
print(outputs)

for i, j in zip(inputs, outputs):
    print(i)
    print(j)
    ds.addSample(tuple(i), tuple(j))

network = buildNetwork(bow.get_len(), 5, 1, bias=True, hiddenclass=SigmoidLayer)  #hiddenclass

back = BackpropTrainer(network, ds)

#back.trainEpochs(3000)
for i in range(3000):
    error = back.train()

    if error < 0.01:
        break
    print('Epoch: ' + str(i) + 'Error: ' + str(error))

for sent in test:  #Pega cada sentença do teste e faz bag of words com cada uma
    vector = bow.toarray(sent)

    computed = network.activate(list(vector)) # valor computado final entre 0 e 1

    sentiment = None

    if computed[0] >= 0.5:
        sentiment = 'positive'
    else:
        sentiment = 'negative'

    print(sent, sentiment)