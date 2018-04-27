__author__='goldy'
'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''
num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))
print('You inputs:',num,check)
print(type(num))

if num==0 & check==0:
    print('Give value greater than 0')
elif num%2==0:
    print('Number is even')
else:
    print('Number is odd')


if num%check==0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divides evenly by", check)