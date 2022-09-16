import re
import random
import psutil
import sys
import numpy as np

# 기초적인 내용 다시 리마인드 하기


# 메모리 체크
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")




print(isinstance('test', int))

a = list()
with open('a.txt', 'w') as txt:
    txt.write('test')

with open('a.txt', 'a') as txt:
    txt.write('\ntest')

with open('a.txt', 'r') as txt:
    # print(txt.read())
    b = random.randint(0, 1)
    print(b)
    print(bool(b))
    if b:
        for i in txt.readlines():
            a.append(i.strip())
    else:
        for i in txt.readlines():
            a.append(re.sub(r'\n', '', i))
print(a)



with open('data.csv', 'w') as csv:
    csv.write('first, second, third')


new_list = list()
new_list2 = list()
# print(dump_list)

memory_usage('#1')
dump_list = [i for i in range(1, 10)]
new_words = [f'{str(i)}x{str(j)}={i*j}' for i in dump_list[1:] for j in dump_list[0:]]
print(new_words)

memory_usage('#2')
new_words2 = [i*j for i in range(1, 10) for j in range(1, 10) if i > 1]
print(new_words2)
memory_usage('#3')

tesT_list = [1,2,3,4]

print(sys.getsizeof(dump_list))
print(sys.getsizeof(new_words))
print(sys.getsizeof(new_words2))
del dump_list

v = np.array([1,2,3,4])
print(f'v : {v}')

with open('test.txt', 'w') as txt:
    # for i in range(2, 10):
    #     for j in range(1, 10):
    #         txt.write(f'{str(i * j)}\n')
    for i in new_words:
        txt.write(f'{str(i)}\n')


print([i * j for i in [k for k in range(1,10)][1:] for j in [k for k in range(1,10)][0:]])
print([i * j for i in list(range(1,10))[1:] for j in list(range(1,10))[0:]])