__author__='goldi'
student={'name':'danish','age':'12','grade':'fifth','address':'dehradun'}
print('name',student['name'],'address',student['address'])
print(type(student))
for k,v in student.items():
    print(k,v)
print(student.get('age'))
student.pop('address')
print(student)
student['age']=10
student['name']='gaurav'
print(student)
del student['grade']
print(student)