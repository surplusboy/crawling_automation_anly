import time
import datetime


print(time.time())
print(time.ctime(time.time()))
print(time.localtime(time.time()).tm_year)
print(time.time())
print(time.strftime('%Y년%m월%d일', time.localtime(time.time())))
print(datetime.datetime(2022, 10, 1))


# 포매팅 문법
a = 'formatting'
#1.
print(f'{a} ㅋㅋ')
#2.
print('{} ㅋㅋ'.format(a))
#3.
print('%s ㅋㅋ' % a)
