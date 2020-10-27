# Alina Yanchuk, nmec 89093
# Ana Sofia Fernandes, nmec 88739

import sys, getopt
from DocumentIndexer import DocumentIndexer

def main(argv):

    # Get the parameters and start the process:
    input_file = ''

    try:
        opts,args = getopt.getopt(argv,"hs:i:",["sfile=","ifile="])
    except getopt.GetoptError: # If there's an argument error, the instructions are shown
        print ('\nUsage:\nMain.py -s <fileToRead>\nor Main.py -i <fileToRead>')
        sys.exit(2)
    if opts==[]: # If the user didn't pass any arguments
        print ('\nUsage:\nMain.py -s <fileToRead>\nor Main.py -i <fileToRead>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h': # If the user looks for help, the instructions are shown
            print ('\nUsage:\nMain.py -s <fileToRead>\nor Main.py -i <fileToRead>')
            sys.exit()            
        elif opt in ("-s", "--sfile"): # The user choses to use the simple tokenizer
            input_file = arg
            doc_indexer= DocumentIndexer(input_file,'s')
            doc_indexer.document_indexer()
        elif opt in ("-i", "--ifile"): # The user choses to use the improved tokenizer
            input_file = arg
            doc_indexer=DocumentIndexer(input_file,'i')
            doc_indexer.document_indexer()

if __name__ == '__main__':
    main(sys.argv[1:])