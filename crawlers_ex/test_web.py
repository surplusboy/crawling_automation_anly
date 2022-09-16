from bs4 import BeautifulSoup
import requests

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
# login_headers = {
#     "X-Requested-With": "XMLHttpRequest",
#     "Referer": "https://www.dcinside.com/",
#     'User-Agent': user_agent
# }
#
#
# def login(self, user_id: str, user_pw: str) -> bool:
#     self.user_id = user_id
#     self.session.headers.update(self.login_headers)
#     res = self.session.get('https://www.dcinside.com/')
#     soup = BeautifulSoup(res.text, 'html.parser')
#     input_elements = soup.select('#login_process > input')
#     login_data = self.serializeForm(input_elements)
#     login_data['user_id'] = user_id
#     login_data['pw'] = user_pw
#     self.session.post(
#         'https://sign.dcinside.com/login/member_check', data=login_data)
#     res = self.session.get('https://www.dcinside.com/')
#     if not BeautifulSoup(res.text, 'html.parser').select('.logout'):
#         return False
#     return True
#
# test = requestsd