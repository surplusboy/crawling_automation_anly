from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import time
import getpass

# 간단한 켑챠 우회

user_agent = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
profile_path = 'user-data-dir=C:/Users/babymon/AppData/Local/Google/Chrome/User/Default/'
# profile_path = 'user-data-dir=C:/Users/babymon/AppData/Local/Microsoft/Edge/User Data/'

options = webdriver.ChromeOptions()
options.add_argument(user_agent)
options.add_argument(profile_path)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('chromedriver.exe', options=options)

input('break')

driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')
driver.implicitly_wait(5)

pyperclip.copy('id입력') # 클립보드에 넣어두기

e = driver.find_element(by=By.CSS_SELECTOR, value='#id')
e.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

pw = getpass.getpass('패스워드 입력')
pyperclip.copy(pw)

e = driver.find_element(by=By.CSS_SELECTOR, value='#pw')
e.send_keys(Keys.CONTROL, 'v')

e.send_keys(Keys.ENTER)

input('quit is enter')
driver.quit()

# 업로드 관련은 주로 <input type="file"> 요소를 찾아보면 됨.