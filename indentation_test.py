__author__ = 'goldi'
print('Enter your subjects marks:')
print('Enter first subject marks:')
_subject1=raw_input()
print('Enter second subject marks:')
_subject2=raw_input()
print('Enter third subject marks:')
_subject3=raw_input()
print('Enter fourth subject marks:')
_subject4=raw_input()
print('Enter fifth subject marks:')
_subject5=raw_input()
print('you entered subjects are'+'subject1='+_subject1+'subject2='+_subject2+'subject3='+_subject3+'subject4='+'subject5='+_subject5)

total_marks=int(_subject1)+int(_subject2)+int(_subject3)+int(_subject4)+int(_subject5)
_percentage=(total_marks)/5
print('total_marks:'+str(total_marks))
print('percentage='+str(_percentage))








