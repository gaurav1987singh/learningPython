__author__='goldy'

print('Please enter string to reverse:')
inputString=input('input your string:')
lenthOfInputString=len(inputString)
print('stringlenght:',lenthOfInputString)
reversed=''
i=lenthOfInputString -1
while i >= 0:
    reversed=reversed+inputString[i]
    i-=1
print('reversed:',reversed)