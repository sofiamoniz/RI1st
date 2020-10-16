class Indexer:
    def __init__(self):
        self.invertedIndex={}

    def indexDocument(self,document,documentId):
        for token in document:
            new=True
            if token not in self.invertedIndex:
                freqPosting={}
                postingList=[]
                postingEntry= {}
                postingEntry["docId"]=documentId
                postingEntry["freq"]=1
                postingList.append(postingEntry)
                freqPosting["docFreq"]=1
                freqPosting["docs"]=postingList
                self.invertedIndex[token]=freqPosting
            else:
                freqPosting=self.invertedIndex.get(token)
                freqPosting["docFreq"]=freqPosting["docFreq"]+1
                postingList=freqPosting["docs"]
                for entry in postingList:
                    if entry["docId"]==documentId:
                        
                        entry["freq"]=entry["freq"]+1
                        new=False
                        break
                if(new==True):
                    print("hi")
                    newEntry={}
                    newEntry["docId"]=documentId
                    newEntry["freq"]=1
                    self.invertedIndex[token]["docs"].append(newEntry) 


    def showInvertedIndex(self):
        print(self.invertedIndex)                   


