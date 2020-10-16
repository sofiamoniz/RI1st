import csv

class CorpusReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def read_content(self):
        alreadyRead = [] #lista para guardar os ids dos documentos já lidos
        docContent = {} #dicionário para guardar o conteúdo de cada documento
        titleAbstract = ""
        with open (self.fileName, mode='r') as csv_to_read:
            csv_reader=csv.DictReader(csv_to_read)
            for row in csv_reader:
                if row['pubmed_id'] != "" and row['abstract'] != "":
                    pub_id= row['pubmed_id']
                    if pub_id not in alreadyRead: #verificar se o documento já foi ou não lido
                        alreadyRead.append(pub_id) #adicionar à lista dos já lidos
                        #docContent[row['title']] = row['abstract'] #<title, abstract>  
                        titleAbstract += row['title'] + row['abstract']                      
        #print(docContent)
        return titleAbstract

corpusReader = CorpusReader("all_sources_metadata_2020-03-13.csv");
print(corpusReader.read_content())