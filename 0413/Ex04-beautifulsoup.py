'''
pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.nate.com/rank/' 
# https://news.nate.com/rank/?mid=m1000 여기에 접속
param = {"mid" : "n1000"}
response = requests.get(url, params=param)
html = response.text


soup = BeautifulSoup(html, 'html.parser') # .parser : 읽어서 패턴 분석, 파악
tit_list = soup.find_all('strong', class_='tit') # <div></div>태그
for tit in tit_list:
    print(tit.text.strip())