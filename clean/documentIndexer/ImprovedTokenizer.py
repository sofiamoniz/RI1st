"""
IR, October 2020
Assignment 1: Indexing documents
Autors: Alina Yanchuk, 89093
        Ana Sofia Fernandes, 88739
"""

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

        with open ("documentIndexer/snowball_stopwords_EN.txt", mode='r') as stop_words:
            stop_words_list = [word.strip() for word in stop_words]
            
        return stop_words_list



    def characs_same(self,s) :

        """
        Verifies if a string has all the same chars (Eg. "aaaaa" )
        or 3 same sequential chars (Eg. "aaab")
        or 2 same sequential and len equal to 3 (Eg. "aab")
        

        After a research, we found that
        "In English the most common repeated letters are ss, ee, tt, ff, ll, mm and oo" from https://www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html
        
        So, we also exclude all ther terms with repeated chars not from this list.
        """

        n = len(s)
        sameChars=0
        repeatedChars=""

        if(len(s)>=3):
            for i in range(0, n-1) :
                j=i+1
                if s[i] == s[j] :
                    sameChars=sameChars+1
                    repeatedChars=s[i]+s[j]   

        if (sameChars>=2) or (sameChars==1 and len(s)==3) or (sameChars==1 and repeatedChars not in ["ss","tt","ff","ll","mm","oo","ee"]): return True
        else: return False



    def contains_digit(self, w): 

        """
        Check if a given string contains digits
        """

        if any(char.isdigit() for char in w): return True



    def is_website(self, w):

        """
        Check if a given string is a website
        """

        if ('www' in w or 'http' in w or 'https' in w) and w.count('.') > 1: return True




    def improved_tokenizer(self):

        """
        Returns an array with treated and tokenized terms (without numbers,repeated sequences of chars, treated URLs, len bigger than 3, after PorterStemmer, and so on...)
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
        # Words with at least 3 chars (after the stem), and not having all the same chars or more than 3 sequentially (eg. zzz)
        final_tokenized=[]
        for w in filtered_sentence:
            w=ps.stem(w)
            if (len(w)>=3) and (not self.characs_same(w)):
                final_tokenized.append(w)
        return final_tokenized