'''
requests 라이브러리를 사용
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리.
    이를 사용하면 웹페이지를 가져오거나 API와 상호작용할 수 있다.
    
라이브러리 설치 requests
pip install requests
라이브러리 설치 에러발생 시 
pip install charadet
pip install brotli

pip - 라이브러리를 모아놓은 저장 공간
pip install - 그 공간에서 다운받아 사용하는 것
'''
import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code' : 161967}
response = requests.get(url, params = param)
print(response.text)