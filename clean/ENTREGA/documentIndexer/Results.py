"""
IR, October 2020
Assignment 1: Indexing documents
Autors: Alina Yanchuk, 89093
        Ana Sofia Fernandes, 88739
"""

import json
import operator

## Class that writes the results files and answers the questions in the assignment guide

class Results:

    def __init__(self,inverted_index,docIds,tokenizer_type,input_file):
        self.inverted_index=inverted_index
        self.docsIds=docIds
        self.tokenizer_type=tokenizer_type
        self.file_name=input_file



    def write_index_to_file(self):

        """
        Writes the Inverted Index to a file.

        Example: file used- > example.csv     tokenizer used -> Improved

        File generated:


        documentIndexer
        results
            ├── improvedTokenizer
            │           └── invertedIndex_example.txt        <----- file generated
            │   
            └── simpleTokenizer                  


        """

        if(self.tokenizer_type=="s"):
            with open('results/simpleTokenizer/invertedIndex_'+self.file_name[:-4]+'.txt','w') as file_index:
                json.dump(self.inverted_index,file_index)
        else:
            with open('results/improvedTokenizer/invertedIndex_'+self.file_name[:-4]+'.txt','w') as file_index:
                json.dump(self.inverted_index,file_index)

        ## To quickly load the file from disk to a dictionary in memory do:
        #     
        # with open('results/improvedTokenizer/invertedIndex.txt') as file_index:
        #   dic = json.load(file_index)            



    def write_document_ids_to_file(self):

        """
        Writes the mapping between real doc IDs and the generated ones to a file.

        File generated:


        documentIndexer
        results
            ├── improvedTokenizer
            │   
            └── simpleTokenizer    
            │   
            └── documentIDs.txt            <---- file generated


        """

        with open('results/documentIDs.txt','w') as file_ids:
            json.dump(self.docsIds, file_ids)

        ## To quickly load the file from disk to a dictionary in memory do:
        #     
        # with open('results/documentIDs.txt') as file_ids:
        #   dic = json.load(file_ids)






## OPTIONAL:

    

    def print_table_for_inverted_index(self):

        """
        Prints in terminal a table with the Inverted Index
        """

        inverted_list=[]
        entry_list=[]

        print("\nTable for Inverted Index: \n")
        for term,freq_posting in self.inverted_index.items():            
            entry_list.append(term)
            entry_list.append(str(freq_posting[0]))
            entry_list.append(str(freq_posting[1]))
            inverted_list.append(entry_list)
        print ("{:<20} {:<9} {:<10}".format('Term','DocFreq','Docs and Occurrance'))
        for item in inverted_list:
            print ("{:<20} {:<9} {:<10}".format(item[0],str(item[1]),str(item[2])))        




    ## TO ANSWER THE QUESTIONS FROM ASSIGNMENT GUIDE:
           

    def terms_doc_frequency_1(self):

        """
        Return and array with the ten first terms (in alphabetic order) that appear in only one document
        """

        top_10=[]
        for term in self.inverted_index:
            if(len(top_10)!=10):
                if(self.inverted_index[term][0]==1): # doc frequency for this term == 1
                    top_10.append(term)
            else: break

        return top_10
                



    

    def terms_highest_doc_frequency(self):

        """
        Return an dictionary with the ten terms with highest document frequency and their frequency
        """

        top_10={}
        top=dict(sorted(self.inverted_index.items(), key=lambda i: i[1][0], reverse=True)[:10])  # Sorts by the doc frequency
        for key in top:
            top_10[key]=top[key][0]  
       
        return top_10