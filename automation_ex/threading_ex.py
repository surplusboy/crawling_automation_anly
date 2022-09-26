import time
import requests
import json
from multiprocessing.dummy import Pool as ThreadPool
start_time = time.time()

headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

# a = 1608811200000
# b = 1608098400000
# c = 1606672800000
# d = 1605960000000

standard_time = int(time.time()*1000)

url = [f'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1d&last_time={str(standard_time-((17280000*1000) * i))}' for i in range(1, 11)]
print(url)

data = requests.get(url[0],headers=headers)
data_dict = json.loads(data.content)


# print(len(data_dict['data']))
def parsingClose(datas:list):
    print(datas)
    input()
    return [time.strftime(f"{time.strftime('%Y년%m월%d일',time.localtime(data['DT']/1000))} 종가 {data['Close']}") for data in datas]

test_list = [[1, 2, 3, 4], [2, 3, 4, 5]]

def testFunc(x:list) -> list:
    return [1+i for i in x]


print(list(map(testFunc, test_list)))
print(data_dict['data'])
# print(list(map(parsingClose, data_dict['data'])))


def nowPrice(url:list) -> list:

    data = requests.get(url, headers=headers)
    data_dict = json.loads(data.content)
    result_list = list()

    for i in data_dict['data']:
        # result_list.append()
        result_list.append(f"{time.strftime('%Y년%m월%d일',time.localtime(i['DT']/1000))} 종가 {i['Close']}")
    # result_list.append(map())
    return result_list
# for i in url:
#     for j in nowPrice(i):
#         print(j)

result = list()
pool = ThreadPool(int((len(url)/2)))
a = pool.map(nowPrice, url)
b = pool.map(print, a)
for i in a:
    for j in i:
        print(j)

# print('.'.join(j for i in a for j in i))
# print(c)

# pool.close()
# pool.join()

# for i in a:
#     print(i)

print('총 소요 시간 : {:.2f} 초'.format((time.time() - start_time)))
