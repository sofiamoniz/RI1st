import re

class SimpleTokenizer:

    def __init__(self, received_string):
        self.received_string=received_string


    def simple_tokenizer(self):

        tokens=[]

        self.received_string=self.replace_non_alpha(self.received_string) # Replace non-alpha chars
        self.received_string=self.received_string.lower().split() # Put all chars to lower

        for word in self.received_string:
            if(len(word)>=3): # Only admit strings with len >=3
                tokens.append(word)
                
        return tokens


    def replace_non_alpha(self,old_string): # Used to replace non-alpha chars

        new_string = re.sub('[^a-zA-Z]+', ' ', old_string) 

        return new_string