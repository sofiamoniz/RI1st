# Alina Yanchuk, nmec 89093
# Ana Sofia Fernandes, nmec 88739

from sys import getsizeof

## Class that creates the Inverted Index for the document Corpus

class Indexer:

    def __init__(self):
        self.inverted_index=dict()
       
    def index_document(self,document_terms,document_id):

        """

        """

        for term in document_terms:
            if term not in self.inverted_index:
                freq_posting=[] # [doc_freq,posting]  where doc_freq is the number total of documents where the term occurs
                                # In python, the order of an array is mantained, so no problem!
                posting={} # {"doc1":occurrences_of_term_in_doc1,"doc2":occurences_of_term_in_doc2,...}  only with documents where the term occurs
                freq_posting.append(1)
                posting[document_id]=1
                freq_posting.append(posting)
                self.inverted_index[term]=freq_posting # {"term1":freq_posting1,"term2":freq_posting2,...}
            else:
                freq_posting=self.inverted_index[term]
                posting=freq_posting[1] # The second position of this arrays are always the posting dictionary!
                if document_id in posting:
                    posting[document_id]=posting[document_id]+1 # The document already exists in the posting dictionary, so we only need to increment the occurance of the term in it
                else: # The document for this term don't exists in the posting dictionary
                    posting[document_id]=1
                    freq_posting[0]=freq_posting[0]+1
                    
        
      

    def get_inverted_index(self):

        """
        Returns the dictionary with the Inverted Index
        """

        return self.inverted_index              
                
                   

    def sort_inverted_index(self):    # Used after indexing all documents

        """
        Returns the dictionary with Inverted Index sorted in alphabetical order of the terms (keys)
        """
        self.inverted_index={k: v for k, v in sorted(self.inverted_index.items(), key=lambda item: item[0])}



    def show_inverted_index(self):

        """
        Prints the Inverted Index
        """

        print(self.inverted_index) 
   


    def get_size_in_mem(self):
<<<<<<< HEAD

        """
        Returns the size of the dictionary with the Inverted Index
        """

        return getsizeof(self.inverted_index)
=======
        return getsizeof(self.get_inverted_index())
>>>>>>> 8f9ecd9fad8390a662d3cd072783b2256cdaf1f9

