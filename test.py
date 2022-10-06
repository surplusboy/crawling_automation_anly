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
default_path = '//*[@id="{}"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[{}]/div[{}]'

'/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[2]/div[1]'
'/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[2]/div[1]'

def likeCommnetCheck(mount_value : str, start : int, last : int):
    check_list = list()
    for i in range(start, last + 1):
        for j in range(1, 4):
            print(default_path.format(mount_value, i, j))
            check_list.append(default_path.format(mount_value, i, j))

    return check_list

print(likeCommnetCheck('123', 2, 8))

