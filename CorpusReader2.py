import csv
from string import digits


class CorpusReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def read_content(self):
        alreadyRead = [] #lista para guardar os ids dos documentos já lidos
        corpus=[]
        titleAbstract = ""
     
        with open('tokens.txt', 'w') as the_file:
            with open (self.fileName, mode='r') as csv_to_read:
                csv_reader=csv.DictReader(csv_to_read)
                for row in csv_reader:
                    
                    if row['pubmed_id'] != "" and row['abstract'] != "":
                        pub_id= row['pubmed_id']
                        if pub_id not in alreadyRead: #verificar se o documento já foi ou não lido
                            docContent = []
                            alreadyRead.append(pub_id) #adicionar à lista dos já lidos
                            #docContent[row['title']] = row['abstract'] #<title, abstract>  
                            titleAbstract = row['title'] + row['abstract']
                            docContent.append(titleAbstract)
                            docContent=self.simple_tokenizer(titleAbstract)
                            corpus.append(docContent)

        print(corpus)                               
        
        return corpus


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


corpusReader = CorpusReader("exemplo.csv");
corpusReader.read_content()







