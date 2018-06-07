##integrar as outras classes
from Bag import*
from RedeNeural import*
import numpy as np
import random
from pybrain.structure.modules.tanhlayer import TanhLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# class Main:
#     def lerArquivo(self): # ler dados do arquivo e coloca em um array de sentencas ou esse msm retorna o arra
#
#     def divideTreinTest(self):
#
#     def divideTreinTestValid(self): #procurar tbm o crossvalidator
#         #passa como parametro o dataset de treino e teste
#     #def getArraySentec(self): #retorna array de sentencas

#BasePositivos = []
#BaseNegativos = []
#BaseComum = []
inputsPos = []
outputsPos = []

inputsNeg = []
outputsNeg = []

sentencesPos = ['Gostei da estadia do hotel. A comida é boa e o atendimento é ótimo', 'Adoreeeeeii!!!!!', 'melhor hotel que ja visitei, recomendo',
                'Perfeito, não tenho do que reclamar, atendimento excelente!!!', 'vou vir sempre, nunca fui tão bem atendida']

sentencesNeg = ['O atendimento é muito ruim, não tenho pretenção de voltar', 'odiei tudo, a cama é ruim, o banheiro é sujo e cheio de baratas.',
                'péssimo, localização ruim, não tem um bom atendimento e os funcionarios são mau humorados',
                'não pretendo voltar', 'odiei, nunca recomendarei, achei pésssimoo...']

bow = Bag()

BasePositivos = bow.constroiSubVocab(sentencesPos) #palavras
BaseNegativos = bow.constroiSubVocab(sentencesNeg) #palavras
bow.setVocabTotal(BasePositivos, BaseNegativos)

print('Positivos : ' + str(BasePositivos))


####################################verificar se estão funcionado da maneira correta

for sentenc in sentencesPos:
    vectors = bow.toarray(sentenc)#constroi um vetor para cada sentença apontando sua ocorrencia nas palavras de entrada
    #print('Tamanho Vec: ' + str(len(vectors)))
   # print('vectors : ' + str(vectors))
    sample = []
    for num in vectors:
        sample.append(num)
       # print('input : ' + str(num))
    for i in range(0, len(vectors)):
        outputsPos.append([0.99])
    inputsPos.append(sample)

print('Negativos : ' + str(BaseNegativos))

for sentenc in sentencesNeg:
    vectors = bow.toarray(sentenc)  # constroi um vetor para cada sentença apontando sua ocorrencia nas palavras de entrada
    #print('Tamanho Vec: ' + str(len(vectors)))
    #print('vectors : ' + str(vectors))
    sample = []
    for num in vectors:
        #print('num: ' + str(num))
        sample.append(num)
   # print('sample : ' + str(sample))
    for i in range(0, len(vectors)):
        outputsNeg.append([0.01])
    inputsNeg.append(sample)
   # print('inputs : ' + str(inputsNeg))



ds = SupervisedDataSet(bow.getSizeVocabTotal(), 1) #inputs e target
for i, j in zip(inputsPos, outputsPos):
    #print('i posit : ' + str(i))
    #print('j posit : ' + str(j))
    ds.addSample(tuple(i), tuple(j))

for i, j in zip(inputsNeg, outputsNeg):
    #print('i neg : ' + str(i))
    #print('j neg : ' + str(j))
    ds.addSample(tuple(i), tuple(j))

#print(ds)
#print('bow getsizevocab' + str(bow.getSizeVocabTotal()))
rede = RedeNeural()
print('VOOOCCCAABBBTTTT : ' + str(bow.getVocabTotal()))
#rede.setBagOfWords(bow.getVocabTotal()) #envia o bag pra rede
rede.setDataTotal(ds, bow.getSizeVocabTotal(),bow.getVocabTotal())

rede.divideTreinoTeste(0.8) # divide dados em treino e teste
#print(' ds print' + str(ds))
rede.constroiRede(5, TanhLayer) #qtd neuronios na camada intermediaria e função de ativação
rede.adicionaPesosIniciais(1) #coloca 1 para numeros de 0 a 1 e outro numero pra outra faixa
rede.treinoRede(0.01) #taxa de aprendizado
#rede.treinaCTreinoTeste(3000) #n de épocas
rede.treinaCTreinoTesteValid() # p usar validação
rede.predicaoCTeste()


#############################Predição do teste manual
sentenceTest1 = ['Gostei do hotel, muito bom a estadia é perfeita', 'o hotel é tenebroso, odiei tudo nunca mais eu volto',
                 'achei meio ruim, cheio de baratas e sujeira, n gostei', 'perfeitooooo, amei']
rede.predicaoTesteReal(sentenceTest1)

# print(str(sentenceTest1) +' -- '+ str(predic))
#
# sentenceTest2 = []
# predic2 = rede.predicaoTesteReal(sentenceTest2)
#
# print(str(sentenceTest2) +' -- '+ str(predic2))











