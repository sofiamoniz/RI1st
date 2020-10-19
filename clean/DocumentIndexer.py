from CorpusReader import CorpusReader
from Indexer import Indexer
from Table import Table
import time
import sys, getopt

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hs:i:",["sfile=","ifile="])
    except getopt.GetoptError:
        print ('DocumentIndexer.py -s <fileToRead>')
        print ('DocumentIndexer.py -i <fileToRead>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('DocumentIndexer.py -s <fileToRead>')
            print('or')
            print ('DocumentIndexer.py -i <fileToRead>')
            sys.exit()
        elif opt == '':
            print ('DocumentIndexer.py -s <fileToRead>')
            print('or')
            print ('DocumentIndexer.py -i <fileToRead>')
            sys.exit()
        elif opt in ("-s", "--sfile"):
            inputfile = arg
            corpusReader = CorpusReader(inputfile,'s')
            corpus=corpusReader.read_content()
            results(corpus)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            corpusReader = CorpusReader(inputfile,'i')
            corpus=corpusReader.read_content()
            results(corpus)

def results(corpus):
    start_time = time.time()
    indexer = Indexer()
    for i in range(len(corpus)):
        indexer.indexDocument(corpus[i],i+1)
    indexer.sortInvertedIndex()
    invertedIndex=indexer.getInvertedIndex()
    #indexer.showInvertedIndex()
    table = Table(invertedIndex)
    print("\n--- Tempo de execução:  %s segundos." % (time.time() - start_time))
    table.createTable()



if __name__ == '__main__':
    main(sys.argv[1:])