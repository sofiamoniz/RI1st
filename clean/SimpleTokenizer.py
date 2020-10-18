from string import digits

class SimpleTokenizer:
    def __init__(self, received_string):
        self.received_string=received_string

    def simple_tokenizer(self):
        tokens=[]
        count_tokens=0
        self.received_string=self.replace_non_alpha(self.received_string)
        self.received_string=self.received_string.lower().split()
        for word in self.received_string:
            if(len(word)>=3):
                for char in word: 
                    if(char.isnumeric()): char=' '
                tokens.append(word)
                count_tokens=1+count_tokens
        return tokens


    def replace_non_alpha(self,old_string):
        new_string = old_string.translate(str.maketrans('0123456789', '          '))
        return new_string