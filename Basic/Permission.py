permissions='rw'
print('w' in permissions)
print('r' in permissions)
print('x' in permissions)
database=[['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
username=input('User name: ')
pin=input('PIN code: ')
if[username,pin] in database:
    print('Access granted')
    