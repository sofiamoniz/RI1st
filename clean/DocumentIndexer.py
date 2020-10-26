from CorpusReader import CorpusReader
from Indexer import Indexer
from Results import Results
import time
import sys, getopt
import os
import psutil

class DocumentIndexer:

    def __init__(self,input_file,tokenizer_type):
        self.input_file=input_file
        self.tokenizer_type=tokenizer_type

    def document_indexer(self):
        doc_ids={}
        total_docs=0
        total_terms=0
        indexing_time=0

        corpusReader = CorpusReader(self.input_file,self.tokenizer_type) ## Corpus Reader with Tokenization
        corpus,real_doc_ids=corpusReader.read_content() # corpus: [[doc1_terms_after_tokenization],[doc2_terms_after_tokenization]...]
                                                        # real_doc_ids: [real_doc1_id,real_doc2_id,...]
                                                        # in python, the order of an array is mantained, so no problem!
        total_docs=len(corpus)
        
        for j in range(total_docs):
            total_terms=total_terms+len(corpus[j])
 
        indexer = Indexer() ## Indexer
        start_time = time.time()
        for i in range(total_docs):   # Index one document at a time. The id's are auto generated by incrementation, starting at id=1 
            generated_id=i+1 
            indexer.index_document(corpus[i],generated_id)
            doc_ids[generated_id]=real_doc_ids[i]
        indexer.sort_inverted_index() ## All documents have been indexed and the final Inverted Indexer created!
        indexing_time=time.time()-start_time
        inverted_index=indexer.get_inverted_index()
        
        results = Results(inverted_index,doc_ids,self.tokenizer_type,self.input_file) ## Results ( writes informations to files )
        results.write_document_ids_to_file()
        results.write_index_to_file()
        #results.print_table_for_inverted_index()
        
        process = psutil.Process(os.getpid())
        
        memory_used= self.format_bytes(process.memory_info().rss) # Memory used by the program
        memory_dic = self.format_bytes(indexer.get_size_in_mem()) # Memory of the structure used

        
        # Print results:
        if(self.tokenizer_type=="s"):
            print("\n    Tokenizer used: Simple \n"
                    +"\n--- Number of documents:  %s documents." % (total_docs) 
                    +"\n--- Total number of terms: %d terms." % (total_terms)
                    +"\n--- Indexation time:  %s seconds." % (round(indexing_time,3))
                    +"\n--- Size in memory used by the dictionary structure:  %s %s." % (round(memory_dic[0],3), memory_dic[1])
                    +"\n--- Memory required by the program:  %s %s." % (round(memory_used[0],3), memory_used[1])
                    + "\n--- Directory with the Inverted Index: results/simpleTokenizer"
                    + "\n--- Directory that contains the real document Id's and auto generated ones: results\n")
        else:
            print("\n    Tokenizer used: Improved \n"
                    +"\n--- Number of documents:  %s documents." % (total_docs) 
                    +"\n--- Total number of terms: %d terms." % (total_terms)
                    +"\n--- Indexation time:  %s seconds." % (round(indexing_time,3))
                    +"\n--- Size in memory used by the dictionary structure:  %s %s." % (round(memory_dic[0],3), memory_dic[1])
                    +"\n--- Memory required by the program:  %s %s." % (round(memory_used[0],3), memory_used[1])
                    + "\n--- Directory with the Inverted Index: results/improvedTokenizer"
                    + "\n--- Directory that contains the real document Id's and auto generated ones: results\n")
        

    def format_bytes(self,size): # Conversion 
        # 2**10 = 1024
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
        while size > power:
            size /= power
            n += 1
        return size, power_labels[n]+'bytes'

