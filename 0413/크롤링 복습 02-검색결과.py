# 검색 결과 웹 페이지 정보 가져오기
# 네이버에 '파이썬'을 검색했을 때 나오는 결과 화면의 정보를 가져와보자.

# 서버 주소(URL) : https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파이썬
# 물음표 오른쪽부터 사용자가 서버에게 요청한 정보들이 전달되는 구역이다.
# '파라미터명=값'의 형식으로 전달되며 정보가 여러 개인 경우 '&'를 이용하여 '파라미터명=값&파라미터명=값'과 같은 형식으로 전달된다.
# 입력한 검색어 '파이썬'은 query라는 파라미터로 전달된다. 나머지 파라미터는 지금은 신경쓰지 않아도 되며, 실제로 다른 파라미터를 지우고 query=파이썬 만 남겨도 웹페이지의 결과는 같다.

# 요청 파라미터가 있는 웹페이지는 URL 자체와 요청 파라미터를 분리해서 정보를 요청할 수 있다.

import requests

url = 'https://search.naver.com/search.naver'
param = {'query' : '파이썬'} # 요청 파라미터. 딕셔너리 타입의 데이터를 변수 param에 저장
response = requests.get(url, params=param)
print(response.text)

# 만약 요청 파라미터를 둘 이상 보내고 싶다면 다음과 같이 작성하면 된다.
url = 'https://search.naver.com/search.naver'
params = {'query' : '파이썬', 'ie' : 'utf8'} # 요청 파라미터에 둘 이상의 데이터를 넣음
response = requests.get(url, params=params)
print(response.text)