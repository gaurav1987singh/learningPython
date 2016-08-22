__author__ = 'goldi'
name=raw_input('Enter Name:')
age=int(raw_input('Enter age:'))
if name == 'Alice':
 print('Hi, Alice.')
elif age < 12:
 print('You are not Alice, kiddo.')
elif age > 2000:
 print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
 print('You are not Alice, grannie.')
