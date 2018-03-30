__author__ = 'goldy'


# Write a function named collatz() that has one parameter named number . If
# number is even, then collatz() should print number // 2 and return this value.
# f number is odd, then collatz() should print and return 3 * number + 1 .
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1 .
# Amazingly enough, this sequence actually works for any integer sooner


def collatz(number):
    if number % 2 == 0:
        print ("Number is even number")
        abc = ( number // 2)
        return int(abc)
    elif number % 2 == 1:
        print("Number is odd number")
        number = 3 * number + 1
        return (print (int (number)))

print("Enter a number")
try:
    enterNumber = (int(input()))
except ValueError:
          print("Please enter a valid INTEGER.")
result = collatz(enterNumber)
while result != 1:
    collatz(enterNumber)

print('Collaz sequence:' + str(result))
