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

    #pip install nltk
    def improved_tokenizer(self):
        stop_words=self.list_stop_words()
        word_tokens=word_tokenize(self.received_string)
        filtered_sentence = [] 
        Stem_words = []
        ps =PorterStemmer()

        for w in word_tokens: 
            if w not in stop_words and len(w) >=3:
                filtered_sentence.append(re.sub('[^0-9a-zA-Z]+', '', w))
       
        for w in filtered_sentence:
            rootWord=ps.stem(w)
            Stem_words.append(rootWord)
        return Stem_words