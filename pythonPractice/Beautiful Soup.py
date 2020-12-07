from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import re   # 정규 표현식

# def get_element(element, url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bs = BeautifulSoup(html.read(), 'html.parser')
#         result = getattr(bs, element).string
#     except AttributeError as e:
#         return None
#     return result
#
#
# result = get_element('h1', 'http://www.pythonscraping.com/pages/page1.html')
# if result is None:
#     print('Title could not be found')
# else:
#     print(result)



# 다른 예시( 당근 마켓 )
webpage = requests.get("https://www.daangn.com/hot_articles")
# print(webpage.text)
#
soup = BeautifulSoup(webpage.content, 'html.parser')
# print(soup)
# print(soup.p)
# print(soup.p.string)

# print(soup.find_all('h2'))  # find_all : html tag 중심
# print(soup.find_all(re.compile('h[1-9]')))  # 정규식 사용
# print(soup.find_all(['h1', 'p']))   # 리스트 활용
print(soup.find_all(attrs={'class':'card-title'}))  # html 속성 활용 : 다중 선택 가능
print('-' * 50)
# 함수 사용( 이해 필요 )
# def search_funtion(tag):
#     return tag.attr('class') == 'card-title' and tag.string == 'Hello World'


# select 활용 : css 선택자 사용 가능
# print(soup.select('.card-region-name'))    # class 이름 앞에 . 을 찍어준다
# print(soup.select('#hot-articles-go-download'))    # id 앞에는 # 을 찍어준다

# .get_text() 활용 : tag 제외 텍스트만 확인하고 싶을 때
for x in range(0, 10):
    print(soup.select('.card-title')[x].get_text())


