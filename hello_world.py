__author__ = 'goldi'
import sys
print(sys.platform )
x = 'spam'
print(x * 3)
print "Hello World"
print "a"
print "b"
print x
print('I have eaten ' + str(99) + ' burritos.')
rain = str(raw_input('Enter if its raining : '))
umbrella = str(raw_input('Do u have Umbrella : '))
#print("Is it raining?" + rain)
#print("Do u have Umbrella?" + umbrella)
#print 43==43
#print 2!=0
if rain == 'True':
    print("Do u have umbrella " + umbrella)
    if umbrella == 'True':
        print('you can go out.Enjoy the rain!')
    else:
        print('Wait For rain to stop.')
else:
    print('U can go out. Enjoy the day!')