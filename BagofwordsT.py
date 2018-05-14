import json

import numpy
import numpy as np
import random
from pybrain.datasets.classification import ClassificationDataSet
#from pybrain.supervised.trainers.svmtrainer import SVMTrainer
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.tanhlayer import TanhLayer

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer
from pybrain.structure import SoftmaxLayer


class BagOfWords:
    def __init__(self):
        self.vocab = [] #lista de palavras

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


sentences = ['eu gosto de você', 'eu te odeio', 'eu gosto de ir ao shopping', 'eu detesto ir a praia', 'detesto ir ao shopping', 'estou satisfeita com o serviço',
             'não voltarei', 'com certeza voltarei', 'gostei muito daqui', 'estão de parabéns', 'que lugar terrível', 'nunca mais volto aqui', 'muito bom, voltarei sempre']

bow = BagOfWords()
bow.build_vocab(sentences) #constroi vocabulario de palavras

inputs = []
outputs = [[0.99], [0.01], [0.99], [0.01], [0.01], [0.99], [0.01], [0.99], [0.99], [0.99], [0.01], [0.01], [0.99]]


for sentenc in sentences:
    vectors = bow.toarray(sentenc) #constroi um vetor para cada sentença apontando sua ocorrencia nas palavras de entrada

    sample = []
    for num in vectors:
        sample.append(num)
    inputs.append(sample)


#print(outputs)


ds = SupervisedDataSet(bow.get_len(), 1)

for i, j in zip(inputs, outputs):
   # print(i)
    #print(j)
    ds.addSample(tuple(i), tuple(j))

# Divide em treino e teste
dataTrain, dataTest = ds.splitWithProportion(0.8)

#print("dataTrain " + str(dataTrain))
#print("dataTest" + str(dataTest))

network = buildNetwork(bow.get_len(), 5, 1, bias=True, hiddenclass=TanhLayer)  #constroi a rede
#Funções de ativação para variar no teste  - SigmoidLayer, LinearLayer, TanhLayer



########################################## Adicionar pesos iniciais ################
print(network.params)

new_weights = []

for i in range(0, len(network.params)):  # gera pesos aleatorios entre 0 e 1 pode modificar depois pra outros intervalos pra ver a diferença, por exemplo intervalos com numeros grandes
    new_weights.append(random.random())
    #Testes -- Variar o random dos pesos
    #  o atual é entre zero e um mas para outros valores é so colocar uniform(a, b) no lugar do random()

print(len(network.params))

network._setParameters(new_weights)

print(network.params)

###############################################################################################################

#taxa se aprendizado
back = BackpropTrainer(network, dataset=dataTrain, learningrate=0.01, lrdecay=1.0, momentum=0.0, verbose=False, batchlearning=False, weightdecay=0.0)
# variar learningrate  - 0.1 , 1.0, 0.001


##################Treina com teste treino e validação#################
#back.trainUntilConvergence(maxEpochs=None, verbose=True, continueEpochs=10, validationProportion=0.25)
########################################################


##########################   Treino só com conj de testes e treino#############################
for i in range(3000):
     error = back.train() #quando é só treino e teste usa esse

     if error < 0.01:
         break
     print('Epoch: ' + str(i) + 'Error: ' + str(error))

    ##############################################################################


computed = network.activateOnDataset(dataTest)
target = dataTest['target']
sentiment = None

for i in range(0, dataTest.getLength()):
    if computed[i] >= 0.5:
        sentiment = 'positive'
    else:
        sentiment = 'negative'
    print(computed[i], sentiment)
print(target)


