import requests
from bs4 import BeautifulSoup
import re
from urllib import request as url_request

# 기본 흐름도
# 1. python 으로 특정 web에 request 요청 HTML 문서 받아냄
# 2. beautifulSoup 을 통해 HTML 문서 파싱
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = 'https://finance.naver.com/item/sise.naver?code=005930'
# url = 'https://www.dcinside.com/'

data = requests.get(url, headers=headers)
# data = requests.get(r'https://www.dcinside.com/')
#
print(data.status_code)
# print(data.content)

# print(data.content)
# print(data.status_code)

soup = BeautifulSoup(data.content.decode('euc-kr', 'replace'), features='html.parser')
# print(soup.findAll('strong', id='_nowVal')[0].text)
# print(soup.findAll('span', class_='tah')) # class는 파이썬 기본 문법이므로 _필요
# print(soup.findAll())

dump_list = soup.findAll()
d = list()

# for i in dump_list:
#     if '거래량' in i.text:
#         # print(type(i.text))
#         a = i.text
#         b = a.index('거래량')
#         c = a[b:b+20]
#         c = re.sub('[\n, ]', '', c)
#         f = re.sub(r'[^0-9]', '', c)
#         if f != '':
#             print(f)
#         d.append(c)
#
#         # print(c)
#         # input('break')
#
# print(d)

# print(soup.findAll('em', class_='no_down')[0].text) # class는 파이썬 기본 문법이므로 _필요



    # input('break')

soup.select('tag명')
soup.select('.class명')
soup.select('#id명')
# 그 외에 
# 여러 조건 : 붙여쓰기
# 내부 요소 : 띄어쓰기

img = soup.select('#img_chart_area')[0]
print(img['src'])
url_request.urlretrieve(img['src'], 'test.jpg')