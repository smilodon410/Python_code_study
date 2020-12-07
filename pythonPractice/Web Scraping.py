import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# 네이버에서 Crawling 해보기
if __name__ == "__main__":
    soup = BeautifulSoup(urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20201119').read(),'html.parser')
    res = soup.find_all('div', 'tit5')
    point = soup.find_all('td' , 'point')
    # print(res + point)
    for n, j in zip(res, point):
        print(n.get_text(), end='')
        print(j.get_text())
