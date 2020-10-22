import csv
from SimpleTokenizer import *
from ImprovedTokenizer import *

class CorpusReader:

    def __init__(self, file_name, chosen_arg):
        self.file_name = file_name
        self.chosen_arg=chosen_arg


    def read_content(self):

        already_read = [] # Will store the id's of documents already read
        corpus=[] # Will store, at each position, an array, for each document, with the terms after tokenization
        title_abstract = ""

        with open (self.file_name, mode='r') as csv_to_read:
            csv_reader=csv.DictReader(csv_to_read)
            for row in csv_reader: # Reads and Tokenizes one document at time
                if row['pubmed_id'] != "" and row['abstract'] != "":
                    pub_id= row['pubmed_id']
                    if pub_id not in already_read: #verifies if the document was already read
                        doc_content = []
                        already_read.append(pub_id) #add to the list that has the documents that were already read
                        title_abstract = row['title'] + " " + row['abstract'] #save the title and the abstract of the document and save it to the doc_content list
                        doc_content.append(title_abstract)
                        if self.chosen_arg == 's': #the user chose to use the simpleTokenizer
                            simp = SimpleTokenizer(title_abstract)
                            doc_content=simp.simple_tokenizer()
                        elif self.chosen_arg == 'i': #the user chose to use the improvedTokenizer
                            improv = ImprovedTokenizer(title_abstract)
                            doc_content=improv.improved_tokenizer()
                        corpus.append(doc_content) #save the content of the document after passing through the tokenizer

        real_doc_ids=already_read    

        return corpus,real_doc_ids