###Criar toda a estrutura da rede


## Inicializar pesos da rede
## definir função de ativação
## definir taxa de aprendizado
## imprimir em um arquivo os pesos atuais
## criar rede
## variar camada intermediaria
## inserir comentarios iniciais pelo arquivo
## inserir comentarios como sentenças para teste real
## calcular e retornar acuracia da rede ou taxa de acerto
from Bag import* ## ta mt acoplado
import numpy as np
import random
from pybrain.structure.modules.tanhlayer import TanhLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer




class RedeNeural:
    def __init__(self):
        self.dataSetTotal = None
        self.dataTrain = None
        self.dataTest = None
        self.tamanhoBag = None
        self.network = None
        self.back = None
        self.bow = None


    def setBagOfWords(self, bag):
        print('BOOOOWWW' + str(bag))
        self.bow = bag
        print('BOOOOWWW' + str(self.bow))
        print(len(self.bow))

    def setDataTotal(self, datasetTotal, tamanhobag, bag): #talvez nem precise de tamanho bag
        #self.dataSetTotal = SupervisedDataSet(tamanhobag, 1)
        self.dataSetTotal = datasetTotal
        self.bow = bag
        print('BOOOOWWW' + str(self.bow))
        print(len(self.bow))

        print('datasetTotal' + str(self.dataSetTotal))

        #self.tamanhoBag = tamanhobag

        #print(len(self.dataSetTotal))
        #print('Tamanho na classe recebido bag' + str(self.tamanhoBag))
        print('Tamanho no array bow' + str(len(self.bow)))

    def divideTreinoTeste(self, proporcao):
        self.dataTrain, self.dataTest = self.dataSetTotal.splitWithProportion(proporcao)

        print(' Treino ' + str(self.dataTrain))
        print(' Teste ' + str(self.dataTest))

    def getTreino(self):
        return self.dataTrain

    def getTeste(self):
        return self.dataTest

    def constroiRede(self, qtdCamadInterm, funcAtivac):
        #self.network = buildNetwork(self.tamanhoBag, qtdCamadInterm, 1, bias=True, hiddenclass=funcAtivac)
        self.network = buildNetwork(len(self.bow), qtdCamadInterm, 1, bias=True, hiddenclass=funcAtivac)

    def adicionaPesosIniciais(self, faixaPesos): #faixa pesos vai dizer se é 1 ou 2 se for 1 vai ser entre 0 e 1, se for 2 vai ser o oiutro intervalo
        #print(self.network.params)

        new_weights = []

        for i in range(0, len(self.network.params)):  # gera pesos aleatorios entre 0 e 1 pode modificar depois pra outros intervalos pra ver a diferença, por exemplo intervalos com numeros grandes
            if faixaPesos == 1:
                new_weights.append(random.random())
            else:
                new_weights.append(random.uniform(1, 2)) #faixa de pesos 1 e 2
            # Testes -- Variar o random dos pesos
            #  o atual é entre zero e um mas para outros valores é so colocar uniform(a, b) no lugar do random()

        print(len(self.network.params))

        self.network._setParameters(new_weights)

        #print(self.network.params)

    def treinoRede(self, taxaAprend):
        self.back = BackpropTrainer(self.network, dataset=self.dataTrain, learningrate=taxaAprend, lrdecay=1.0, momentum=0.0, verbose=True, batchlearning=False, weightdecay=0.0)

    def treinaCTreinoTeste(self, nEpocas):
        for i in range(nEpocas):
            error = self.back.train() #quando é só treino e teste usa esse

            if error < 0.01:
                break
            #print('Epoch: ' + str(i) + 'Error: ' + str(error))

    def treinaCTreinoTesteValid(self):
        self.back.trainUntilConvergence(maxEpochs=None, verbose=True, continueEpochs=10, validationProportion=0.25)

    def predicaoCTeste(self):
        computed = self.network.activateOnDataset(self.dataTest)
        sentiment = None
        for i in range(0, self.dataTest.getLength()):
            if computed[i] >= 0.5:
                sentiment = 'positive'
            else:
                sentiment = 'negative'
            print(computed[i], sentiment)

    def predicaoTesteReal(self, sentencesTest): # retorna a predição de uma sentença
        for sent in sentencesTest:
            vector = self.bow.toarray(sent)
            computed = self.network.activate(list(vector)) #####ta dando erro aqui
            sentiment = None

            if computed[0] >= 0.5:
                sentiment = 'positivo'
            else:
                sentiment = 'negativo'
           # return sentiment
        print('Sentença: ' + str(sent) + 'Predicao : ' + str(sentiment))


#     def setPesosIni(self):
#
#     def getPesosIni(self):#inserir pesos em um arquivo
#
#     def setFuncAtiv(self):
#
#     def setTaxaAp(self):
#
#     def setCamInterm(self):
#
#     def getAcuracia(self): #ou taxa de acerto
#

#
#     def predicao(self):




