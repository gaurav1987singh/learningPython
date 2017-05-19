__author__ = 'goldi'
name = ''
#while name != 'your name':
 #   print('Please type your name.')
  #  name = str(raw_input('Enter tour Name : '))
#print('Thank you!')


#while True:
 #   print('Please type your name.')
  #  name = str(raw_input('Enter tour Name : '))
   # if name == 'yourname':
    #    break
#print('Thank you!')

while True:
    print('Who are you?')
    name = str(raw_input('Enter tour Name : '))
    if name != 'Joe':
     continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = str(raw_input('Enter password : '))
    if password == 'swordfish':
        break
print('Access granted.')