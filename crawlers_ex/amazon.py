import requests
from bs4 import BeautifulSoup

# 크롤링을 막기위해 여러 기법이 들어가있을 경우 크롤링
def createCookies(data:str) -> dict:
    cookie_dict = dict()
    cookie_list = data.split(';')
    for cookie in cookie_list:
        key_value = cookie.split('=')
        if key_value[0][0] == ' ': # 간단한 구현 예제이므로 여러 상황을 고려하진 않았지만 정규표현식이나 문자열 치환등을 통해 처리하여도 되는 부분
            cookie_dict[key_value[0][1:]] = key_value[1]
        else:
            cookie_dict[key_value[0]] = key_value[1]
    return cookie_dict
cookies = createCookies(input('please input a cookies'))

print(cookies) # 모든 쿠키 정보를 담을 필요는 없다. 쿠키의 밸류값 중 dict 형태가 있다면 지워도 무방

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

req = requests.get('https://www.amazon.com/s?k=macbook', headers=headers, cookies=cookies)
#
# print(req.text)
print(req.status_code)
soup = BeautifulSoup(req.content, 'lxml')


try:
    if req.status_code == 200: # 함수화 하여 지속적으로 시도하게 만들 수 있음
        tags = soup.select('a.a-link-normal>span.a-size-medium') # list로 담아온 특정 태그 내 데이터들을 재가공
        for tag in tags:
            print(tag.getText())
except Exception as e:
    print(e)
    