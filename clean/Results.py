import json

class Results:

    def __init__(self,inverted_index,docIds,tokenizer_type,input_file):
        self.inverted_index=inverted_index
        self.docsIds=docIds
        self.tokenizer_type=tokenizer_type
        self.file_name=input_file
       



    def write_index_to_file(self):

        if(self.tokenizer_type=="s"):
            with open('results/simpleTokenizer/invertedIndex_'+self.file_name[:-4]+'.txt','w') as file_index:
                json.dump(self.inverted_index,file_index)
        else:
            with open('results/improvedTokenizer/invertedIndex_'+self.file_name[:-4]+'.txt','w') as file_index:
                json.dump(self.inverted_index,file_index)

        ## To quickly load the file from disk to a dictionary in memory do:
        #     
        # with open('results/invertedIndex.txt') as file_index:
        #   dic = json.load(file_index)            



    def write_document_ids_to_file(self):

        with open('results/documentIds.txt','w') as file_ids:
            json.dump(self.docsIds, file_ids)

        ## To quickly load the file from disk to a dictionary in memory do:
        #     
        # with open('results/documentIds.txt') as file_ids:
        #   dic = json.load(file_ids)






## OPTIONAL:
#  Prints in terminal a table with the inverted index

    def print_table_for_inverted_index(self):

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

            
