#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, sys
import string
import json

import numpy as np

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer

class BagOfWords():

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
        comments = json.loads(open("Treinamento/" + str(name), "r").read())

        return comments

    def toUtf(self, unicode):
        text = ""

        for comment in unicode:

            sentence = comment.get('Text')
            coded = sentence.encode(sys.stdout.encoding)
            text = text + " " + coded

        print text
        text = text.split()
        print text
        return text



    def toarray(self, sentence):
        text = ""
        for comment in sentence:
            line = comment.get('Text')
            text = text + line

        words = text.split()
        #print words
        #print len(words)
        return words

    def clean_doc(self, tokens):
        # remove punctuation from each token
        #out = tokens.translate(tokens.maketrans("", ""), string.punctuation)
        #table = tokens.maketrans('', '', string.punctuation)
        #tokens = [w.translate(table) for w in tokens]
        ["".join(j for j in i if j not in string.punctuation) for i in tokens]
        # remove remaining tokens that are not alphabetic
        #tokens = [word for word in tokens if word.isalpha()]
        # filter out short tokens
        tokens = [word for word in tokens if len(word) > 1]
        return tokens

    def get_num_docs(self, arrayWords):
        return len(arrayWords)

    def term_num_docs(self, arrayWords, term):

        number = 0  
        for word in arrayWords:
            number = number+1

        return number

    def get_idf(self, term):
        """Retrieve the IDF for the specified term.

           This is computed by taking the logarithm of (
           (number of documents in corpus) divided by (number of documents
            containing this term) ).
         """

        return math.log(float(1 + self.get_num_docs()) /
                        (1 + self.term_num_docs[term]))

    def get_tf(self, arrayWords, word):
        return self.term_num_docs(arrayWords, word) / self.get_num_docs(arrayWords)

#bag = BagOfWords()

#comments = bag.readArchive()
#array = bag.toUtf(comments)
#array = bag.toarray(comments)

#tokens = bag.clean_doc(array)

bag = BagOfWords() # A classe que vai ter o bag of words

sentencesn = bag.readArchive("BaseComentariosNegativos.json")

print sentencesn

sentencesp = bag.readArchive("BaseComentariosPositivos.json")

print sentencesp


inputsn = []
inputsp = []


inputsn = bag.toarray(sentencesn)


inputsp = bag.toarray(sentencesp)

print inputsp


outputsn = []
outputsp = []

for cont in inputsn:
    outputsn.append(0.0)

for cont2 in inputsp:
   outputsp.append(1.0)



ds = SupervisedDataSet(len(inputsn)+len(inputsp), 1) #É um só eu acho

print ds

print inputsp

for l, m in zip(inputsp, outputsp):
    print l
    print m
    ds.addSample(tuple(l), tuple(m))


network = buildNetwork(len(inputsn)+len(inputsp), 5, 1, bias=True, hiddenclass=SigmoidLayer)  #hiddenclass ou outclass

back = BackpropTrainer(network, ds)

for i in range(3000):
    error = back.train()

    if error < 0.01:
        break
    print('Epoch: ' + str(i) + 'Error: ' + str(error))

    ######################### Teste, tem que pegar da base de teste





