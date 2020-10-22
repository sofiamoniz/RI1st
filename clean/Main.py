import sys, getopt
from DocumentIndexer import DocumentIndexer

def main(argv):

    # Get the parameters and start the process:
    input_file = ''

    try:
        opts,args = getopt.getopt(argv,"hs:i:",["sfile=","ifile="])
    except getopt.GetoptError: #if there's an argument error, the instructions are shown
        print ('Usage:\nDocumentIndexer.py -s <fileToRead>\nor DocumentIndexer.py -i <fileToRead>')
        sys.exit(2)
    if opts==[]: #if the user didn't pass any arguments
        print ('Usage:\nDocumentIndexer.py -s <fileToRead>\nor DocumentIndexer.py -i <fileToRead>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h': #if the user looks for help, the instructions are shown
            print ('Usage:\nDocumentIndexer.py -s <fileToRead>\nor DocumentIndexer.py -i <fileToRead>')
            sys.exit()            
        elif opt in ("-s", "--sfile"): #the user choses to use the simple tokenizer
            input_file = arg
            doc_indexer= DocumentIndexer(input_file,'s')
            doc_indexer.document_indexer()
        elif opt in ("-i", "--ifile"): #the user choses to use the improved tokenizer
            input_file = arg
            doc_indexer=DocumentIndexer(input_file,'i')
            doc_indexer.document_indexer()

if __name__ == '__main__':
    main(sys.argv[1:])