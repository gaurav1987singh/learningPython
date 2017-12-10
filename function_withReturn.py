__author__ = 'goldy'

def returnAnswer(name):
    if name == 'Gaurav':
        print('Hey you are welcome My Knight ' + name + '!' )
        eggss = 'meLocalvariable'
        return name
    else:
        print ('Hey you are not welcome, you are a Hound ' + name + '!' )
        global eggs
        eggs = 'MeGlobalvariable'
        eggs= 'ichangedValueofEgg'
        return eggs

returnedName = returnAnswer('abc')
eggs= 'initialValue'
print ('eggs value initially:' + eggs)
print('You entered name is: ' + returnAnswer('dededed'))
print ('eggs value after:' + eggs)