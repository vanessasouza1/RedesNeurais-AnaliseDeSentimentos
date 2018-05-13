import json
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


print(outputs)


ds = SupervisedDataSet(bow.get_len(), 1)

for i, j in zip(inputs, outputs):
    print(i)
    print(j)
    ds.addSample(tuple(i), tuple(j))

# DIvide em treino e teste
dataTrain, dataTest = ds.splitWithProportion(0.8)

print("dataTrain " + str(dataTrain))
print("dataTest" + str(dataTest))

network = buildNetwork(bow.get_len(), 5, 1, bias=True, hiddenclass=TanhLayer)  #constroi a rede
#SigmoidLayer, LinearLayer, TanhLayer

#modificaparam = SVMTrainer(network)

lista = []

#for i in range(0, bow.get_len()):
 #   lista.append(random.random())

print(lista)

#modificaparam.__setattr__('weight', lista)

# tem taxa de aprendizado
back = BackpropTrainer(network, dataset=dataTrain, learningrate=0.01, lrdecay=1.0, momentum=0.0, verbose=False, batchlearning=False, weightdecay=0.0)

##################Treina com teste treino e validação#################
back.trainUntilConvergence(maxEpochs=None, verbose=True, continueEpochs=10, validationProportion=0.25)
########################################################


##########################   Treino só com conj de testes e treino#############################
# for i in range(3000):
#     error = back.train() #quando é só treino e teste usa esse
#
#     if error < 0.01:
#         break
#     print('Epoch: ' + str(i) + 'Error: ' + str(error))

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

# for i in range(0, dataTest.getLength()):
#     print(computed[i], sentiment)
# print(target)

