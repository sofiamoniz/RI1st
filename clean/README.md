### To run the script:

    1. Run the command pip install nltk
    2. Run the command pip install psutil
    3. Execute one of the commands bellow: 
        1.python3 Main.py -s <fileToRead>
            (where -s means that SimpleTokenizer will be used) 
        2.python3 Main.py -i <fileToRead> 
            (where -i means that ImprovedTokenizer will be used)

### All the results ( Inverted Index and ID's mapping files are stored in the "results" folder )            

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
            -With simple tokenizer: ['aaaaaag', 'aaaauga', 'aaac', 'aaag', 'aaap', 'aaars', 'aabb', 'aacaaaaaaggg', 'aacetaminophen', 'aacgaa']
            - With improved tokenizer: ['ababa', 'abadoglu', 'abaecin', 'abagiu', 'abarhead', 'abas', 'abatacept', 'abcabc', 'abcd', 'abctyp']

    4.List the ten terms with highest document frequency.
        A:
            -With simple tokenizer: {'the': 22515, 'and': 22420, 'for': 18066, 'with': 18026, 'that': 16887, 'this': 13889, 'from': 12826, 'was': 12392, 'are': 11677, 'were': 11586}       (terms and doc frequency)
            - With improved tokenizer: {'the': 15671, 'infect': 11563, 'use': 11229, 'viru': 10535, 'studi': 10526, 'result': 10199, 'diseas': 8055, 'cell': 7942, 'viral': 7714, 'human': 6930}
