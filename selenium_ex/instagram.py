from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import time

from getpass import getpass
import time

# Service.

agent = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

options = webdriver.ChromeOptions()
options.add_argument(agent)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('chromedriver.exe', options=options)

driver.get('https://instagram.com/')

driver.implicitly_wait(5)
# time.sleep(2)

# a = driver.find_element(by=By.CSS_SELECTOR, value='input[name="username"]').text
# b = driver.find_element(by=By.NAME, value='username')
user_id = driver.find_element(by=By.CSS_SELECTOR, value='input[name="username"]')
password = driver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')

user_id.send_keys(input('아이디 입력'))
password.send_keys(getpass('패스워드 입력'))

# 요소 강제 클릭 하기
# e = driver.find_element_by_css_selector('클릭하고싶은요소')
# driver.execute_script('arguments[0].click();', e)

print(f'입력 아이디 : {driver.find_element(by=By.CSS_SELECTOR, value=".f0n8F input").get_attribute("value")}')
password.send_keys(Keys.ENTER)

# find_element : 맨 위의 요소만
# find_elements : 모든 요소들을 찾아 list 자료형에 담음

driver.implicitly_wait(5)
driver.get(f'https://www.instagram.com/explore/tags/{input("태그명 설정 : ")}/')
driver.implicitly_wait(5)
e = driver.find_element(by=By.CSS_SELECTOR, value='._aagu').click()
driver.implicitly_wait(5)
count = 0

try:
    for i in range(50):
        next_button = driver.find_element(by=By.CSS_SELECTOR, value='._aaqg ._abl-')
        driver.implicitly_wait(5)
        img = driver.find_element(by=By.CSS_SELECTOR, value='._aatb ._aagt') # 중복된 클래스일 확률이 높으므로 유니크한 클래스를 찾아 연결하는 것이 좋음
        if 'person' not in img.get_attribute('alt'):
            driver.execute_script('arguments[0].click();', next_button)
            time.sleep(0.4)
            continue
        urllib.request.urlretrieve(img.get_attribute('src'), f'./data/{str(count)}.jpg')
        count += 1
        driver.execute_script('arguments[0].click();', next_button)
        time.sleep(0.4)
except Exception as e:
    print(e)



# urllib.request.urlretrieve(img, '파일명')

input('press any key to quit')
driver.quit()

'''
고려 사항

id, pw 요청시 status_code 200 인지 확인
메인 사진 포함 모든 사진 저장
동영상은 데이터 수집 제외
'''