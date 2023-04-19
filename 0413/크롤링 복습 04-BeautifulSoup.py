# BeautifulSoup 모듈 사용

import requests
from bs4 import BeautifulSoup

# BeautifulSoup 객체 만들기

url = 'https://www.naver.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


# BeautifulSoup의 메소드


# 1.find() 메소드

# 지정된 태그들 중 가장 첫 번째 태그만 가져오는 메소드이다. 일반적으로 하나의 태그만 존재하는 경우에 사용한다.
# 만약 여러 태그가 있으면 첫 번째 태그만 가져온다.

'''
ex)

<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.kakao.com">카카오</a>
</div>

태그)
    soup.find('a') : <a href="https://www.naver.com">네이버</a>
태그 내용)
    soup.find('a').text : 네이버
속성값)
    soup.find('a').get('href') : https://www.naver.com
''' 

# 2.find_all() 메소드

# 지정한 태그들을 모두 가져오는 메소드이다. 가져온 태그들은 모두 '리스트'에 보관된다.

'''
ex)

<ul>
    <li id="movie">영화</li>
    <li>여행</li>
    <li>독서</li>
</ul>

태그)
    soup.find_all('li')
        [
            <li id="movie">영화</li>,
            <li>여행</li>,
            <li>독서</li>
        ]
    
태그 내용)
    soup.find_all('li)[0].text : 영화
    soup.find_all('li)[1].text : 여행
    soup.find_all('li)[2].text : 독서
    
속성값)
    soup.find_all('li)[0].get("id") : movie
'''

# class 속성 활용하기

# 공통적인 특징을 갖는 태그들은 같은 class 속성값을 가지고 있다. 크롤링에서 자주 사용되는 속성이기 때문에 특정 class 속성값을 찾는 방법이 따로 있다.
# find() 메소드와 find_all() 메소드 모두 동일하게 지원한다.

'''
ex)
<div>
    <div class="gnb">뉴스</div>
    <div class="gnb">지도</div>
</div>

태그)
    soup.find_all('div', class_='gnb') : [<div class="gnb">뉴스</div>, <div class="gnb">지도</div>]
    soup.find_all('div', class_='gnb')[0].text : 뉴스
    soup.find_all('div', class_='gnb')[1].text : 지도

class 속성을 지정할 때는 class가 아니라 class_를 사용한다.
'''

# id속성 활용하기

# 같은 웹 페이지에서 같은 id 속성값을 가진 태그는 존재하지 않는다. 따라서 특정 id 속성값을 가진 태그는 오직 하나이다.
# find() 메소드와 함께 사용된다.

'''
ex)
<div id="container">
    <div id="left">왼쪽 영역</div>
    <div id="right">오른쪽 영역</div>
</div>

태그)
    soup.find(div, id='left') : <div id="ieft">왼쪽 영역</div>
태그 내용)
    soup.find(div, id='left').text : 왼쪽 영역
'''