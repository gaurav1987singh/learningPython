__author__='goldy'
def loadFile(fileName):
    fh=open(fileName)
    count=0
    text=fh.readlines()
    print(text)
    for word in text:
        if 'gaurav' in word:
         print('word value:',word)
         count+=1
    return count
print('count of word gaurav from file:',loadFile('file1.txt'))