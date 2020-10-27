# Alina Yanchuk, nmec 89093
# Ana Sofia Fernandes, nmec 88739

import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from urllib.parse import urlparse

## Class that acts as the Improved Tokenizer

class ImprovedTokenizer:

    def __init__(self, received_string):
        self.received_string=received_string



    def list_stop_words(self): 

        """
        Reads and saves the stop words from the file required
        """

        with open ("snowball_stopwords_EN.txt", mode='r') as stop_words:
            stop_words_list = [word.strip() for word in stop_words]
            
        return stop_words_list

<<<<<<< HEAD


    def all_characs_same(self,s) :

        """
        Verifies if a string has all the same chars
        """
=======
    def all_characs_same(self,s) : # Verifies if a string has all the same chars
>>>>>>> 8f9ecd9fad8390a662d3cd072783b2256cdaf1f9

        n = len(s)

        for i in range(1, n) :
            if s[i] != s[0] :
                return False    

        return True

    def contains_digit(self, w): #Check if a given string contains digits

        if any(char.isdigit() for char in w): return True

    def is_website(self, w): #Check if a given string is a website

        if ('www' in w or 'http' in w or 'https' in w) and w.count('.') > 1: return True

    def improved_tokenizer(self):

        """
        Returns an array 
        """

        stop_words=self.list_stop_words() # Save the stop words to be used in a list
        word_tokens=word_tokenize(self.received_string) # Transform the received string in tokens, by using the function word_tokenize from library ntlk
        filtered_sentence = [] 
        ps =PorterStemmer()

        for w in word_tokens:
            if w not in stop_words and len(w)>=3:
                if self.is_website(w):
                    parse_object = urlparse(w)
                    if (parse_object.netloc != ''): filtered_sentence.append(parse_object.netloc.split('.')[1]) # This condition is made to transfrom a website and give the user only the. 
                                                                                                                # Relevant part. Eg: www.google.com -> google
                    else:
                        if w.startswith('www'): filtered_sentence.append(w.split('.')[1])   # This refers to the objects that can't be treated by the library urlparse     
                else:
                    w = re.sub('[^0-9a-zA-Z]+', '', w)
                    if not self.contains_digit(w): filtered_sentence.append(w)  #If the treated string doesn't contain numbers, it will be appended.
                                                                                #This is made in order to avoid strange words like a23df or xcxft3, for example

        #Do the stem to the each word from filtered_sentence, using the PorterStemmer
        # Words with at least 3 chars (after the stem), and not having all the same chars (eg. zzz)
        return [ps.stem(w) for w in filtered_sentence if len(ps.stem(w)) >= 3 if not self.all_characs_same(ps.stem(w))]