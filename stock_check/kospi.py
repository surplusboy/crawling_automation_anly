from bs4 import BeautifulSoup
import requests
import os
import datetime
import re


class KOSPI:
    print('KOSPI')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    url = 'https://finance.naver.com/item/sise.naver?code='
    now_time = datetime.datetime.now()

    def nowPrice(self, code_list: list) -> str:
        # data = requests.get(self.url, headers=self.headers)
        # soup = BeautifulSoup(data.content, 'html.parser')
        # if not isinstance(code, str):
        #     str(code)
        print(code_list)
        for i in code_list:
            data = requests.get(f'{self.url}{i}', headers=self.headers)
            # print(data)
            soup = BeautifulSoup(data.content.decode('euc-kr', 'replace'), 'html.parser')
            print(soup.select('h2 a')[0].text, soup.find_all('strong', id='_nowVal')[0].text)


    # def check_data(self):
    # def read_stock_code(self):
    #     if 'stock_code.txt' in os.listdir('./data'):
    #         with open

class Console:
    print('console')
    stock_list = list()

    def __init__(self):
        self.kospi = KOSPI()
        self.getCommand()

    def parseAndExecute(self, cmd : str) -> None:
        cmd = cmd.split()

        if cmd[0] == 'help':
            print('run - 저장된 종목코드의 당일 종가를 불러와 저장합니다.') # 추가 로직 필요
            print('help - 도움말을 봅니다.')
            print('exit - 종료합니다.')
            return

        elif cmd[0] == 'run':
            if len(self.stock_list) == 0:
                with open(f'{os.getcwd()}/data/stock_code.txt') as code:
                    for i in code.readlines():
                        code = re.sub(r'\n', '', i)
                        self.stock_list.append(code)
                self.stock_list.sort()

            self.kospi.nowPrice(self.stock_list)
    # def parseStockCode(self):
    #     print('hello')

    def getCommand(self):
        print('KOSPI 종목 종가 체크')
        print('사용법은 help를 입력하세요.')
        flag = True
        while True:
            if flag and 'stock_code.txt' not in os.listdir(os.getcwd()+'/data/'):
                print(f'{os.getcwd()}/data')
                print('현재 관심 종목코드가 없습니다.\n코스피 상위 10종목을 불러올까요? Y, N') # 추가 로직 필요
                flag = False

            cmd = input('>> ')
            if cmd == 'exit':
                exit()
            try:
                self.parseAndExecute(cmd)

            except Exception as e:
                print(e)
                print('문제가 발생하였습니다.')


cli = Console()
cli.getCommand()


# run = KOSPI()

# run.getCommand()

# print(os.listdir('./data'))
# print(datetime.datetime.now().strftime('%Y_%m_%d'))
