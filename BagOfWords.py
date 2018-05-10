
import string
import json
import numpy as np

class BagOfWords():

    def readArchive(self):
        # arq = open('/Treinamento/BaseComentariosNegativos.txt', 'r')
        # texto = arq.readlines()
        #
        # arrayWords = []
        # for linha in texto :
        #     print(linha)
        #     arrayWords = arrayWords.union(linha)
        #
        # arq.close()
        comments = json.loads(open("Treinamento/BaseComentariosNegativos.json", "r").read())

        #for comment in comments:

            #print comment.get('Text')
            #print "separa"

        return comments

    def toarray(self, sentence):

        #for comment in sentence:

        words = sentence.split()
        #print words
        #print len(words)
        return words

    def clean_doc(self, tokens):
        # remove punctuation from each token
        table = bytearray.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
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

bag = BagOfWords()

comments = bag.readArchive()

array = bag.toarray(str(comments))
print "aaaaaaaaaaaaaaaaa"
tokens = bag.clean_doc(array)
print comments



