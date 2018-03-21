__author__ = 'goldi'
words="the quick brown fox jumps over a lazy dog".split()
print(words)
info= [[ w.upper(),w.lower(), w.__len__()] for w in words]
for data in info:
 print(data)