__author__='goldy'
"""Given an array containing N words, you need to find the most frequent word in the array. 
If multiple words have same frequency then print the word that comes first in 
lexicographical order.
Input:
3
geeks for geeks
2
hello world
3
world wide fund
Output:
geeks
hello
fund

hey holla namastae gracias sashriyakaal vankam namsakara
"""

enterWords=input("Enter your word to check frequncy:")
print("Sentence:",enterWords)
splitted_word=enterWords.split()
print("Splitted list:",splitted_word)
numOfWords=len(splitted_word)
counter={}
i=0
print('type of count',type(counter))
for eachWord in splitted_word:
    count=splitted_word.count(eachWord)
    counter[eachWord]=count
print('finalDicat:',counter)
print('sorted list:',sorted(counter))
maxKey=max(counter, key=lambda key: counter[key])
print('maxKeyValue:',maxKey)
