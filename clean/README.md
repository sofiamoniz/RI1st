### To run the script:

    1. Run the command pip install nltk
    2. Run the command pip install psutil
    3. Execute one of the commands bellow: 
        1.python3 Main.py -s <fileToRead>
            (where -s means that SimpleTokenizer will be used) 
        2.python3 Main.py -i <fileToRead> 
            (where -i means that ImprovedTokenizer will be used)

### Answers to the last exercise:

    1.What was the total indexing time and how much memory (roughly) is required to index
    this collection?
        A:
            -With simple tokenizer:
                -Indexing time: 1.989 seconds
                -Memory used by python process: 443.535 megabytes
                -Memory used by the dictionary structure: 2.5 megabytes
            -With improved tokenizer:
                -Indexing time: 1.533 seconds
                -Memory used by python process: 355.996 megabytes
                -Memory used by the dictionary structure: 2.5 megabytes

    2.What is your vocabulary size?
        A: 
            -With simple tokenizer: 4159309
            -With improved tokenizer: 3097377

    3.List the ten first terms (in alphabetic order) that appear in only one document (document
    frequency = 1).
        A:

    4.List the ten terms with highest document frequency.
        A:
