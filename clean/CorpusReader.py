import csv
from SimpleTokenizer import *
from ImprovedTokenizer import *

class CorpusReader:

    def __init__(self, file_name, chosen_arg):
        self.file_name = file_name
        self.chosen_arg=chosen_arg


    def read_content(self):

        already_read = [] # Will store the title of documents already read
        corpus=[] # Will store, at each position, an array, for each document, with the terms after tokenization
        title_abstract = ""
        real_doc_ids=[]

        with open (self.file_name, mode='r') as csv_to_read:
            csv_reader=csv.DictReader(csv_to_read)
            for row in csv_reader: # Reads and Tokenizes one document at time
                if row['abstract'] != "":
                    title=row['title'] 
                    if title not in already_read: # Verifies if the document was already read
                        if row['doi'] == "": real_id=row['pmcid']
                        else: real_id=row['doi']   
                        doc_content = []
                        already_read.append(title) # Add to the list that has the documents that were already read
                        real_doc_ids.append(real_id)
                        title_abstract = row['title'] + " " + row['abstract'] # Save the title and the abstract of the document and save it to the doc_content list
                        doc_content.append(title_abstract)
                        if self.chosen_arg == 's': # The user chose to use the simpleTokenizer
                            simp = SimpleTokenizer(title_abstract)
                            doc_content=simp.simple_tokenizer()
                        elif self.chosen_arg == 'i': # The user chose to use the improvedTokenizer
                            improv = ImprovedTokenizer(title_abstract)
                            doc_content=improv.improved_tokenizer()
                        corpus.append(doc_content) # Save the content of the document after passing through the tokenizer


        

        return corpus,real_doc_ids