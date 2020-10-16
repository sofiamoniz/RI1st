import csv
import nltk
nltk.download('punkt')
from string import digits
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

class CorpusReader:
    def __init__(self, fileName):
        self.fileName = fileName


    def read_content(self):
        alreadyRead = [] #lista para guardar os ids dos documentos já lidos
  
        titleAbstract = ""
        contador=0
        with open('tokens.txt', 'w') as the_file:
            with open (self.fileName, mode='r') as csv_to_read:
                csv_reader=csv.DictReader(csv_to_read)
                for row in csv_reader:
                    
                    if row['pubmed_id'] != "" and row['abstract'] != "":
                        pub_id= row['pubmed_id']
                        if pub_id not in alreadyRead: #verificar se o documento já foi ou não lido
                            contador=contador+1
                            docContent = {}
                            alreadyRead.append(pub_id) #adicionar à lista dos já lidos
                            #docContent[row['title']] = row['abstract'] #<title, abstract>  
                            titleAbstract = row['title'] + row['abstract']
                            lista_tokens=self.simple_tokenizer(titleAbstract)
                            docContent[contador]=lista_tokens
                            the_file.write(str(docContent)+"\n") 
        return titleAbstract

    def simple_tokenizer(self,string):
        tokens=[]
        count_tokens=0
        string=self.replace_non_alpha(string)
        string=string.lower().split()
        for word in string:
            if(len(word)>=3):
                for char in word: 
                    if(char.isnumeric()): char=' '
                tokens.append(word)
                count_tokens=1+count_tokens
        return tokens


    def replace_non_alpha(self,old_string):
        new_string = old_string.translate(str.maketrans('0123456789', '          '))
        return new_string

    '''
    An improved tokenizer that incorporates your own tokenization decisions (e.g. how to
    deal with digits and characters such as ’, -, @, etc).
    Integrate the Porter stemmer (http://snowball.tartarus.org/download.html) and a stopword
    filter. Use this list as default: https://bit.ly/2kKBCqt
    '''

    def list_stop_words(self):
        stop_words_list=[]
        with open ("snowball_stopwords_EN.txt", mode='r') as stop_words:
            for word in stop_words:
                stop_words_list.append(word.strip())
        return stop_words_list



    #pip install nltk
    def improved_tokenizer(self):
        example="Ola above"
        stop_words=self.list_stop_words()
        word_tokens=word_tokenize(example)
        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
        filtered_sentence = [] 

        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w) 
        
        Stem_words = []
        ps =PorterStemmer()
        for w in filtered_sentence:
            rootWord=ps.stem(w)
            Stem_words.append(rootWord)
        print(filtered_sentence)
        print(Stem_words) 

      




corpusReader = CorpusReader("exemplo.csv");
corpusReader.read_content()
corpusReader.improved_tokenizer()
#print(corpusReader.list_stop_words())







