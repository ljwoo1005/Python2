# 네이버 영화에서 2019년에 개봉한 봉준호 감독의 영화 '기생충'의 소개 페이지를 가져와보자.

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code' : 161967}
response = requests.get(url, params=param)
print(response.text)

'''
03 : requests 모듈 사용을 선언

05~07 : 네이버 영화에서 '기생충'을 검색하고 해당 페이지의 주소를 복사해서 사용했다. 
전체 주소에서 물음표 뒷부분은 요청 파라미터이므로 별도의 딕셔너리에 저장하고(param에 저장), requests 모듈의 get()메소드에 params인자값으로 저장했던 딕셔너리를 넣는다.
'''