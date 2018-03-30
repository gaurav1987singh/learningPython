__author__='goldy'
list = ["1", "4", "0", "6", "9"]
print('before converting to int:',list)
list = [int(i) for i in list]
print('after converting to int:',list)
list.sort()
print (list)