

class Table:
    def __init__(self,invertedIndex):
        self.invertedIndex=invertedIndex
       

    def createTable(self):
        print("\n")
        invertedList=[]
        for term,freqPosting in self.invertedIndex.items():
            entryList=[]
            entryList.append(term)
            entryList.append(str(freqPosting[0]))
            entryList.append(str(freqPosting[1]))
            invertedList.append(entryList)
        print ("{:<20} {:<9} {:<10}".format('Term','DocFreq','Docs'))
        for item in invertedList:
            print ("{:<20} {:<9} {:<10}".format(item[0],str(item[1]),str(item[2])))