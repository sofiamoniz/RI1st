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

        stop_words_list=[]

        with open ("snowball_stopwords_EN.txt", mode='r') as stop_words:
            for word in stop_words:
                stop_words_list.append(word.strip())

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
        Stem_words = []
        ps =PorterStemmer()

         for w in word_tokens: 
            if w not in stop_words and len(w) >=3:
                if ('www' in w or 'http' in w or 'https' in w) and w.count('.') > 1: # This condition is made to transfrom a website and give the user only the. 
                                                                                     # Relevant part. Eg: www.google.com -> google
                    parse_object = urlparse(w)
                    if (parse_object.netloc != ''):
                        filtered_sentence.append(parse_object.netloc.split('.')[1])
                    else:
                        if w.startswith('www'): # This refers to the objects that can't be treated by the library urlparse
                            filtered_sentence.append(w.split('.')[1])
                else:   
                    word = re.sub('[^0-9a-zA-Z]+', '', w) # Replaces special characters by nothing -> example anti-virus to antivirus
                    if not any(char.isdigit() for char in word):
                        filtered_sentence.append(word)
                    #if not word.isdigit(): # If the string is a number, it will only save the ones with > 4 digits (meaning years)
                    #    filtered_sentence.append(word)
                    #elif not any(char.isdigit() for char in word): # These conditions are made to avoid words like xy3 and x3y that are not perceptible
                    #    if len(word) > 3 and re.match('^[a-zA-Z]+', word) and not word[-1].isalpha() :
                    #        filtered_sentence.append(word)
       
        for w in filtered_sentence:            
            rootWord=ps.stem(w) # Do the stem to the each word from filtered_sentence, using the PorterStemmer
            if len(rootWord) >= 3 and not self.all_characs_same(rootWord): # Words with at least 3 chars (after the stem), and not having all the same chars (eg. zzz)
                Stem_words.append(rootWord)

        '''
        w="https://www.gov.uk/government/publications/novel-coronavirus-2019-ncov-guidance-for-healthcare-providers-with-staff-who-have-travelled-to-china/guidance-for-healthcare-providers-healthcare-workers-who-have-travelled-to-chinaFind"
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
        
        #w="https://www.gov.uk/government/publications/novel-coronavirus-2019-ncov-guidance-for-healthcare-providers-with-staff-who-have-travelled-to-china/guidance-for-healthcare-providers-healthcare-workers-who-have-travelled-to-chinaFind"

        #parse_object = urlparse("www.proteomicsresource.org")
        #print("ola",parse_object.netloc == '')

        #w="www.proteomicsresource.org"
        #parse_object = urlparse(w)
        #print("parse ", parse_object.netloc == '')
       

        return Stem_words