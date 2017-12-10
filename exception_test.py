__author__= 'goldy'

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Dividing by zero Error: Invalid arguments')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
