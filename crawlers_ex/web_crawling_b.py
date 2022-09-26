import requests
from bs4 import BeautifulSoup
import re
import lxml

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

# a = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=서울 성형외과&nso=&nqx_theme={"theme":{"main":{"name":"location","score":"0.601790"}}}&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=33&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09650101&fgn_region=&fgn_city=&lgl_lat=37.4941452&lgl_long=126.988785&abt=&_callback=viewMoreContents')
b = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=61&query=서울 성형외과&nso=&nqx_theme={"theme":{"main":{"name":"location","score":"0.601790"}}}&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=63&sm=tab_jum&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09650101&fgn_region=&fgn_city=&lgl_lat=37.4941452&lgl_long=126.988785&abt=&_callback=viewMoreContents')
c = requests.get('https://blog.naver.com/NVisitorgp4Ajax.naver?blogId=')
# payload = {
#     'rev': '44',
#     'where': 'blog',
#     'query': '',
#     'start': '1',
#     # 'sm': 'tab_pge',
#     # 'api_type': '1',
#     #
#     # 'dup_remove': '1'
# }

# payload = {
#     'where': 'blog',
#     'sm': 'tab_pge',
#     'api_type': '1',
#     'query': str(),
#     'rev': '44',
#     'start': '31',
#     'dup_remove': '1',
#     'post_blogurl': None,
#     'post_blogurl_without': None,
#     'nso': None,
#     'nlu_query': None,
#     'dkey': '0',
#     'source_query': None,
#     'nx_search_query': str(),
#     'spq': '0',
#     '_callback': 'view'
# }

payload = {
    'query': str(),
    # 'nso': None,
    'where': 'blog',
    'sm': 'tab_opt',
    'start': '1'
}

query_kwr = input('검색어 : ')
page_loop = map(int,input('긁어올 갯수'))

payload['query'] = query_kwr
# payload['nx_search_query'] =query_kwr
print(payload)

# a = requests.get('https://s.search.naver.com/p/review/search.naver', headers=headers, params=payload)
a = requests.get(f'https://search.naver.com/search.naver?', headers=headers, params=payload)
# print(a.text)



soup = BeautifulSoup(a.text, 'html.parser')
print(len(soup.text))
input('break')

# print(c.text)

soup = BeautifulSoup(a.text.replace('\\',''), 'html.parser')
post_list = soup.select('a.api_txt_lines')
print(len(post_list))

# input('break')
for i in range(30):
    try:
        if 'blog.naver.com' not in post_list[i]['href']:
            pass
        else:
            print('글 제목 :', post_list[i].text)
            print('url :', post_list[i]['href'])
            print('blog id :', post_list[i]["href"].split("/")[3])
            visit_data = requests.get(f'https://blog.naver.com/NVisitorgp4Ajax.naver?blogId={post_list[i]["href"].split("/")[3]}')
            # print(visit_data)
            visit_soup = BeautifulSoup(visit_data.text, features='xml')
            print('날짜:', visit_soup.select('visitorcnt')[-1]['id'], '/', '방문자 수 :', visit_soup.select('visitorcnt')[-1]['cnt'], '\n')
    except Exception as e:
        print(e)
