from requests_toolbelt import MultipartEncoder
import requests
from bs4 import BeautifulSoup
import re
import json
import time

# 폼 데이터 담아서 post 요청 후 response 받기 예시
common_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'


def post(url:str, field_data:dict) -> tuple:
    # multi = MultipartEncoder(fields=field_data)
    data = {'drwNo' : field_data['drwNo']}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent' : common_agent}
    res = requests.post(url, headers=headers, data=data)
    return res.status_code, res.content


def request_winning(round:int) -> post:
    field = {'drwNo': round, 'dwrNoList': round}
    return post('https://dhlottery.co.kr/gameResult.do?method=byWin', field)


def total_winnings(result:object) -> tuple:
    soup = BeautifulSoup(result, 'html.parser')
    round_num = soup.select_one('.win_result>h4>strong')
    ratio_1 = soup.select_one('.list_text_common>li>strong')
    ratio_2 = int(re.sub(r'[^0-9]', '', ratio_1.text))

    result = soup.select('tbody>tr')
    total = int()

    print(round_num.text)
    for i in range(len(result)):
        a = int(re.sub(r'[^0-9]', '', result[i].select('td')[1].text))
        total += a
    return total, total/ratio_2


def search(start_num:int):
    flag = False
    if start_num - 200 <= 0:
        last_num = start_num - 200 - (start_num - 200)
        flag = True
    else:
        last_num = start_num - 200

    # for i in range(start_num, last_num if flag else start_num-200, -1): # 삼항 연산자가 꼭 필요한지 ?
    for i in range(start_num, last_num, -1):
        result_1, result_2 = request_winning(i)
        sales, ratio = total_winnings(result_2)
        print('총 당첨 금액 : {}\n비율 : {}'.format(sales, ratio))
        time.sleep(0.1)


index_num = int(input('기준 회차 부터 200회 차까지 조회'))
if not index_num > 0:
    raise TypeError('index_num must be positive integer')
search(index_num)


# search(int(input('기준 회차 부터 200회 차까지 조회')))


