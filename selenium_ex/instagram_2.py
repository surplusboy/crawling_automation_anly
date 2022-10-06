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
profile_path = 'user-data-dir=C:/Users/babymon/AppData/Local/Google/Chrome/User/Default/'
options = webdriver.ChromeOptions()
options.add_argument(agent)
# options.add_argument(profile_path)
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.set_window_size(500, 1200)

driver.get('https://instagram.com/')

driver.implicitly_wait(5)

test_xpath = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div/img')
print(test_xpath.get_attribute('alt'))

user_id = driver.find_element(by=By.CSS_SELECTOR, value='input[name="username"]')
password = driver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')

user_id.send_keys(input('아이디 입력'))
password.send_keys(getpass('패스워드 입력'))

print(f'입력 아이디 : {driver.find_element(by=By.CSS_SELECTOR, value=".f0n8F input").get_attribute("value")}')
password.send_keys(Keys.ENTER)

time.sleep(3)

driver.implicitly_wait(5)
driver.get('https://www.instagram.com/hanpyeong_/')
driver.implicitly_wait(5)

time.sleep(3)

check_mount = driver.find_element(by=By.XPATH, value='/html/body/div[1]')
mount_value = check_mount.get_attribute('id')


print(mount_value)
print(type(mount_value))

input('next ?')

# 피드에 마우스 올리기

# first = driver.find_elements(by=By.CSS_SELECTOR, value='._aang')

# print(first)
# print(len(first))
# mount_value = input('input a mount_value') # 리다이렉트 시 마다 마운트 id 값이 달라짐
# first = driver.find_element(by=By.CSS_SELECTOR, value='._aang ._aanf')

# default_path = f'//*[@id="{mount_value}"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]'

# default_path = '//*[@id="{}"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[{}]'
default_path = '//*[@id="{}"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[{}]/div[{}]'
# /div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[2]/div[1]/a/div[1]/div[1]/img
# /div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[{}]/div[{}]

# '//*[@id="mount_0_0_ss"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]'
# '//*[@id="mount_0_0_ss"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]'

def likeCommnetCheck(mount_value : str, start : int, last : int) -> bool:
    check_list = list()

    for i in range(start, last + 1):
        for j in range(1, 4):
            check_list.append(default_path.format(mount_value, i, j))
    print(check_list)

    for i in check_list:

        driver.implicitly_wait(5)

        first = driver.find_element(by=By.XPATH, value=i)
        action = webdriver.ActionChains(driver)
        action.move_to_element(first).perform()
        time.sleep(0.8)  # 의도적으로 딜레이
        second = driver.find_elements(by=By.CSS_SELECTOR, value='._aang ._aanf ._ac2d')
        mbti = driver.find_element(by=By.CSS_SELECTOR, value=i+'/a/div[1]/div[1]/img/').get_attribute('alt')
        print(mbti.split(' ')[17])

        print(type(second))
        print(second[0].text)
        print(len(second[0].text))
        try:
            # print(second[0].text)
            new_text = ''.join(j for j in second[0].text)
            print(type(new_text))
            like_comment = new_text.split('\n')
            print(like_comment)

        except Exception as e:
            print(e)


        # for num, k in enumerate(second):
        #     print(num, k.text)
        time.sleep(0.6)



likeCommnetCheck(mount_value, 2, 8)

print(str(default_path))
print(type(default_path))
input('next line')

# first = driver.find_element(by=By.XPATH, value=default_path)
# action = webdriver.ActionChains(driver)
# action.move_to_element(first).perform()
# time.sleep(0.8) # 의도적으로 딜레이
# second = driver.find_elements(by=By.CSS_SELECTOR, value='._aang ._aanf ._ac2d')

# driver.find_element(by=By.XPATH)

# print(second)
# for i in second:
#     print(i.text)

driver.implicitly_wait(5)

input('press any key to quit')
driver.quit()
