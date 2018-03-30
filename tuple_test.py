__author__ = 'goldi'
myList=['gsgs',1,33,'fgfggf']
mytuple=('abc','def','fgh',1,3,5)
mydict={'India':'Delhi','Pakisthan':'Islamabad','Bangaladesh':'Dhaka','Srilanka':'Colombo'
    ,'Bhutan':'Thimhpu'}
print ("type of datatype:",type(mytuple))
print('type of datatype:',type(myList))
print('type of datatype:',type(mydict))
print ('tuple:',mytuple)
print('list:',myList)
print('list:',mydict)
print (mytuple.__add__(mytuple))
print('new tuple value:',mytuple)
print('dict values',mydict.keys())
mytuple[2]='akaka'