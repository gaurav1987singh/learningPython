__author__ = 'goldi'

list1 = ['physics', 'chemistry', 'english','maths' ]
list2 = [56,66,77,88]
list3 = ["a", "b", "c", "d"]
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print list1
print  list2
print list3+list2+list1
print "list[2]",list1[2]
print "lenght", len(list1)
for x in list1:
    print x
print  list3
print list1
list4= list1 + list2 +list3
print list4
print spam[1][2]
print spam[1][4]
print spam[0][0]