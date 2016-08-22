__author__ = 'goldi'
number=24
running=True


while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        # this causes the while loop to stop
        running = False
    elif guess < number:
        num_higher=number-guess
        print 'No, it is '+''+str(int(num_higher))+' '+ 'little higher than that.'
    else:
        num_lower=guess-number
        print 'No, it is a little lower'+' '+str(int(num_lower))+' '+ 'than that'
else:
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'

while True:
 print('Who are you?')
 name = raw_input()
 if name != 'a':
  continue
 print('Hello, Joe. What is the password? (It is a fish.)')
 password = name = raw_input()
 if password == 'swordfish':
   break
print('Access granted.')


