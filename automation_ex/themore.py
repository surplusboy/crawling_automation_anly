import requests
import time
import getpass
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

url = 'https://themorehelp.com/qoo10_rate.json?'

a = int(time.time() * 1000)

# print(a)

# time_str = time.strftime('%Y-%m-%d %H %M', time.localtime(int(time.time())))
# time_str = time.strftime('%Y년%m월%d일', time.localtime(time.time()))
print(url + str(a))

# url = 'https://themorehelp.com/'


# req = requests.get(url, headers=headers).json()
# print(req)

# print(req.status_code)

# print(req.content)

# soup = BeautifulSoup(req.content, parser='html.parser', features='lxml')

# table = soup.select('#qoo10_rate_table')

# print(soup)
# print(table)

