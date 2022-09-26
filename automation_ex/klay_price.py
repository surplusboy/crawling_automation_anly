import requests
import json
import time
headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneklay&type=1d', headers=headers) # get 요청 후 json 파싱 -> dict 형변환
# print(data.content)
print(data.content)

data_dict = json.loads(data.content)
print(data_dict)

price_dict = data_dict['data']
print(price_dict[-1].keys())
# b = price_dict[-1].items()
# c = [1,2,3,4]

# for i in enumerate(c):
#     print(i)
#
# for i, j in b:
#     print(i, j)

for i in range(len(price_dict)):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(price_dict[i]['DT']/1000)))
    print(price_dict[i]['Close'])