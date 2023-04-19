import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code' : 10016}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div', class_='score_reple')

for review in review_list:
    print(review.find('p').text.strip())

# 교재에 있던 예제 내용인데 네이버가 영화쪽 홈페이지를 철수했다고 들었다. 결과물로 아무것도 표시되지 않았다.

