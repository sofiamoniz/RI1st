import csv
from SimpleTokenizer import *
from ImprovedTokenizer import *

class CorpusReader:

    def __init__(self, fileName, chosen_arg):
        self.fileName = fileName
        self.chosen_arg=chosen_arg

    def read_content(self):
        alreadyRead = [] #lista para guardar os ids dos documentos já lidos
        corpus=[]
        titleAbstract = ""
        with open (self.fileName, mode='r') as csv_to_read:
            csv_reader=csv.DictReader(csv_to_read)
            for row in csv_reader:
                if row['pubmed_id'] != "" and row['abstract'] != "":
                    pub_id= row['pubmed_id']
                    if pub_id not in alreadyRead: #verificar se o documento já foi ou não lido
                        docContent = []
                        alreadyRead.append(pub_id) #adicionar à lista dos já lidos
                        titleAbstract = row['title'] + row['abstract']
                        docContent.append(titleAbstract)
                        if self.chosen_arg == 's':
                            simp = SimpleTokenizer(titleAbstract)
                            docContent=simp.simple_tokenizer()
                        elif self.chosen_arg == 'i':
                            improv = ImprovedTokenizer(titleAbstract)
                            docContent=improv.improved_tokenizer()
                        corpus.append(docContent)                               
        return corpus