import requests
from bs4 import BeautifulSoup 
# bs4 : beautifulsoup4의 패키지명
# bs4의 클래스명 BeautifulSoup를 사용

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent' : 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

list_title_list = soup.find_all('a', class_='list_title')

print(len(list_title_list))

for list_title in list_title_list:
    print(list_title.text.strip())
    
# ctrl + K + C 한꺼번에 주석처리
# ctrl + K + U 한꺼번에 주석처리한거 없애기

