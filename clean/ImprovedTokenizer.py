import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re

class ImprovedTokenizer:

    def __init__(self, received_string):
        self.received_string=received_string


    def list_stop_words(self):

        stop_words_list=[]

        with open ("snowball_stopwords_EN.txt", mode='r') as stop_words:
            for word in stop_words:
                stop_words_list.append(word.strip())

        return stop_words_list



    def all_characs_same(self,s) :

        n = len(s)

        for i in range(1, n) :
            if s[i] != s[0] :
                return False    

        return True



    def improved_tokenizer(self):

        stop_words=self.list_stop_words()
        word_tokens=word_tokenize(self.received_string)
        filtered_sentence = [] 
        Stem_words = []
        ps =PorterStemmer()

        for w in word_tokens: 
            if w not in stop_words and len(w) >=3:
                if ('www' in w or 'http' in w or 'https' in w) and w.count('.') > 1:
                    if len(w) > 5:
                            filtered_sentence.append(w.split('.')[1])
                        #else: #caso contrário, como em https://clinicaltrials. gov, fazer split por //
                         #   if (w.split('//')[1].count('.') > 0):
                          #      filtered_sentence.append(w.split('//')[1].split(".")[0])
                #isto assim está a descartar muitos sites
                else:   
                    word = re.sub('[^0-9a-zA-Z]+', '', w)
                    if word.isdigit(): #se a string for apenas um numero, vai apenas guardar aqueles com  4 digitos - equivalente a anos
                        if len(word) == 4:
                            filtered_sentence.append(word)
                    else:
                        filtered_sentence.append(word)
       
        for w in filtered_sentence:            
            rootWord=ps.stem(w)
            if len(rootWord) >= 3 and not self.all_characs_same(rootWord): #palavras com pelo menos 3 cars, depois do stem, e sem letras todas iguais (como zzz)
                Stem_words.append(rootWord)

        '''
        #w="https://www.gov.uk/government/publications/novel-coronavirus-2019-ncov-guidance-for-healthcare-providers-with-staff-who-have-travelled-to-china/guidance-for-healthcare-providers-healthcare-workers-who-have-travelled-to-chinaFind"
        #w="https://www.cdc.gov/coronavirus/index.html."
        #w="http://www.ncbi.nlm.nih.gov/geo/"
        w="www.proteomicsresource.org"
        #w= "https://clinicaltrials. gov"
        if 'www' in w or 'http' in w or 'https' in w:
                    if len(w) > 5:
                        if w.count('.') > 1: ##verificar que existem pelo menos dois pontos para fazer split
                            print(ps.stem(w.split('.')[1]))
                        else:
                            if (w.split('//')[1].count('.') > 0):
                                print(w.split('//')[1].split(".")[0])
        '''

        return Stem_words