class Indexer:
    def __init__(self):
        self.invertedIndex={}
       

    def indexDocument(self,document,documentId):
        for term in document:
            newDocument=True
            if term not in self.invertedIndex:
                freqPosting=[]
                posting={}
                freqPosting.append(1)
                posting[documentId]=1
                freqPosting.append(posting)
                self.invertedIndex[term]=freqPosting
            else:
                freqPosting=self.invertedIndex[term]
                posting=freqPosting[1]
                for docId in posting.keys():
                    if docId==documentId: 
                        posting[docId]=posting[docId]+1
                        newDocument=False
                        break
                if(newDocument==True):
                    freqPosting[0]=freqPosting[0]+1
                    posting[documentId]=1
        
      
    def getInvertedIndex(self):
        return self.invertedIndex              
                
                   
    def sortInvertedIndex(self):    # no final
        self.invertedIndex={k: v for k, v in sorted(self.invertedIndex.items(), key=lambda item: item[0])}


    def showInvertedIndex(self):
        print(self.invertedIndex) 
   

