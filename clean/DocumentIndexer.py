from CorpusReader import CorpusReader
from Indexer import Indexer
from Table import Table
import time
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--simple', action='store_true', 
                        help="uses simple tokenizer")
    parser.add_argument('-i', '--improved', action='store_true', 
                        help="uses improved tokenizer")
    parser.add_argument('f', '--file', type=str, help='file name')
    args = parser.parse_args()

    if args.file:
        if args.simple:
            corpus_reader= CorpusReader(args.f, 's')
        elif args.improved:
            corpus_reader= CorpusReader(args.f, 'i')

    else:
        print("Please indicate one file to read!")   



if __name__ == '__main__':
    main()