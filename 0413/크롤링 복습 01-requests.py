# 일반 웹페이지 정보 가져오기.
# 실습에 사용할 웹페이지는 네이버의 메인 페이지이다.

import requests # requests 모듈 사용을 선언

url = 'https://www.naver.com' # 네이버 메인페이지 주소를 변수 url에 저장.
response = requests.get(url) # requests.get(url)은 해당 url의 응답 코드를 반환한다.
print('응답 코드: {}'.format(response.status_code)) # response.status_code : 응답 코드
print(response.text) # response.text : text 속성을 통해 UTF-8로 인코딩된 문자열을 받을 수 있다.
