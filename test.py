from getpass import getpass
import os

# a = getpass('Enter your Password: ')
# print(a)

b = 'Photo shared by onde 온드 on September 21, 2022 tagging @eider.official. May be an image of 1 person and standing.'

if 'person' in b:
    print('true')

a = 'test.jpg'

if a.endswith('.jpg'):
    print('true')

print(os.getcwd())

c = os.path.join(os.getcwd(), 'test', 'test')
print(c)