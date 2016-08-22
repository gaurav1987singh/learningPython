__author__ = 'goldi'

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # New block starts here
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'
    # New block ends here
elif guess < number:
    # Another block
    num_higher=number-guess
    print 'No, it is :'+str(int(num_higher)) +' little higher than that'

    # You can do whatever you want in a block ...
else:
    num_lower=guess-number
    print 'No, it is a little lower: '+str(int(num_lower))+ ' than that'
    # you must have guessed > number to reach here

print 'Done'
# This last statement is always executed,
# after the if statement is executed.
