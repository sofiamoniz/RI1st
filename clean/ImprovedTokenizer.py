import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from urllib.parse import urlparse

class ImprovedTokenizer:

    def __init__(self, received_string):
        self.received_string=received_string


    def list_stop_words(self): # Reads and saves the stop words from the file required

        with open ("snowball_stopwords_EN.txt", mode='r') as stop_words:
            stop_words_list = [word.strip() for word in stop_words]
            
        return stop_words_list



    def all_characs_same(self,s) : # Verifies if a string as all the same chars

        n = len(s)

        for i in range(1, n) :
            if s[i] != s[0] :
                return False    

        return True


    def improved_tokenizer(self):

        stop_words=self.list_stop_words() # Save the stop words to be used in a list
        word_tokens=word_tokenize(self.received_string) # Transform the received string in tokens, by using the function word_tokenize from library ntlk
        filtered_sentence = [] 
        ps =PorterStemmer()

        
        #check_general_conditions = [w for w in word_tokens if w not in stop_words if len(w) >= 3] #Save the words that are not stop_words and have len >=3
        websites = [w for w in word_tokens if w not in stop_words if len(w) >= 3 if ('www' in w or 'http' in w or 'https' in w) if w.count('.') > 1 ] #Save websites from words that follow the previous rules
        
        for w in websites:
            parse_object = urlparse(w)# These conditions are made to transfrom a website and give the user only the. 
                                    # Relevant part. Eg: www.google.com -> google
            if (parse_object.netloc != ''): filtered_sentence.append(parse_object.netloc.split('.')[1])
            else:
                # This refers to the websites objects that can't be treated by the library urlparse
                if w.startswith('www'): filtered_sentence.append(w.split('.')[1])        
       
        filtered_sentence += [re.sub('[^0-9a-zA-Z]+', '', w) for w in word_tokens if w not in stop_words if len(w) >= 3 if w not in websites  if not (any(char.isdigit() for char in w)) ]

        #Do the stem to the each word from filtered_sentence, using the PorterStemmer
        # Words with at least 3 chars (after the stem), and not having all the same chars (eg. zzz)
        return [ps.stem(w) for w in filtered_sentence if len(ps.stem(w)) >= 3 if not self.all_characs_same(ps.stem(w))]