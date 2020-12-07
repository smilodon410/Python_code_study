import time
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
from geopy.geocoders import Nominatim
from pprint import pprint

param = '강남'
url = 'https://www.diningcode.com/list.php?query=' + param
###################################################################################################
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
url = driver.get(url)
for i in range(2):
    driver.find_element_by_xpath('//*[@id="div_list_more"]').click()
    time.sleep(1)
html = driver.page_source
###################################################################################################
soup = BeautifulSoup(html, 'html.parser')  # 가져온 html 파일을 html parser를 통해서 정리
# notices = soup.select('span')
# for n in notices:
#     print(n.text.strip())
restaurants = soup.find_all("span", attrs={"class": "btxt"})
food_kinds = soup.find_all("span", attrs={"class": "stxt"})
score = soup.find_all("span", attrs={"class": "point"})
###################################################################################################
res = []
food = []
sco = []
loc = []
lat = []
lon = []
location_elements = soup.select('span.ctxt')
location = [i.text for i in location_elements]

###################################################################################################
for i in range(len(location)):
    loc = location[3::2]
for i in range(len(loc)):
    locsp = loc[i].split(' ')
    loc[i] = ' '.join(locsp[1:4])

print(loc)
###################################################################################################
for line1, line2 in zip(restaurants[1:], food_kinds[1:]):
    res.append(line1.get_text())
    food.append(line2.get_text())
for line3 in score:
    sco.append(line3.get_text())
for i in food[::-1]:
    if i.find('광고') > -1:
        a = food.index(i)
        food.remove(i)
        del res[a]
        del loc[a]
###################################################################################################
for i, j, k, l in zip(res, food, sco, loc):
    print(i, end=': ')
    print(j, end=' - ')
    print(k, end=' __ ')
    print(l)
print('-' * 50)

# locator = Nominatim(user_agent='myGeocoder')

for i in range(len(res)):
    # print(i)
    print(loc[i])
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(loc[0])
    print(location)
    if i == 0:
        break
#     print(location)
#     print(location.latitude)
#     print(location.longitude)
# print(lat)
# print(lon)
# for i in zip(lat, lon):
#     print(i)
