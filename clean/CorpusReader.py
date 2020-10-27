# Alina Yanchuk, nmec 89093
# Ana Sofia Fernandes, nmec 88739

import csv
from SimpleTokenizer import *
from ImprovedTokenizer import *


## Class that reads the documents of the .csv file, calls the tokenizer class and returns the corpus tokenized

class CorpusReader:

    def __init__(self, file_name, chosen_arg):
        self.file_name = file_name
        self.chosen_arg=chosen_arg



    def read_content(self):

        """
        Reads each row (document) of the .csv file, checks if the "abstract" column is not empty and if the 
        document wasn't already read (by the "title" field) and passes the text (title+abstract) to the choosen
        tokenizer (that returns an array of terms).

        Returns an array of arrays, where each array stores the terms, from tokenization, for respective document.
        Because in python the order of an array is always the same, we know that the first array has the terms of
        the first readed document, the second has the terms of the second readed document and so on...
        Also, returns an array with the real document IDs, that were stored in the same order as mentioned above, so we know that
        the first ID corresponds to the first reader document, and so on...
        """

        already_read = [] # Will store the title of documents already read
        corpus_tokenized=[] # Will store, at each position, an array, for each document, with the terms after tokenization
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
                        corpus_tokenized.append(doc_content) # Save the content of the document after passing through the tokenizer


        return corpus_tokenized,real_doc_ids