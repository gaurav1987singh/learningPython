__author__ = 'goldi'

list1 = ['physics', 'chemistry', 'english','maths' ]
list2 = [56,66,77,88]
list3 = ["a", "b", "c", "d"]
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(list1)
print(list2)
print(list3+list2+list1)
print("list[2]",list1[2])
print("lenght", len(list1))
for x in list1:
    print (x)
print (list3)
print (list1)
list4= list1 + list2 +list3
print (list4)
print (spam[1][2])
print (spam[1][4])
print (spam[0][0])

s=[[-1,1]]
print ('s:values',s)
s=[[-1,1]]*5
print ('s:values after *5:',s)
s[3].append(6)
print ('s:values after appending 6:',s)
s[1].append(9)
print ('s:values after appending 9:',s)
s.append(19)
print ('s:values after appending 19:',s)
