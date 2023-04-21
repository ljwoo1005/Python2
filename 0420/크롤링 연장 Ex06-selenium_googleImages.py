'''
selenium 패키지
    어플리케이션을 테스트하기 위한 프레임워크이다.
    웹 어플리케이션의 다양한 브라우저 동작 테스트용
    보통 웹 크롤링으로 많이 사용된다.
    java, python, c#, ruby 등 다양한 언어 지원
    ex) 브라우저 컨트롤로 사용
    
https://chromedriver.chromium.org/downloads

C:\Program Files\Google\Chrome\Application\chromedriver.exe

구글에서 단어를 검색해 이미지 10장을 저장하는 자동화 프로그램을 만들었다. 

'''

import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import traceback

def download_images(keyword, num_images=10, output_dir='images'):
    # Chrome 드라이버 경로
    chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    
    service = Service(executable_path=chrome_driver_path)
    
    # Chrome 드라이버 인스턴스 생성
    driver = webdriver.Chrome(service=service)
    
    # Google 이미지 검색 페이지 접속
    driver.get('https://google.co.kr/imghp')
    
    # 검색어 입력 find_element
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(keyword) # 키워드 입력
    search_bar.send_keys(Keys.RETURN) # 엔터 입력
    
    # 페이지 로딩 대기
    time.sleep(2)
    
    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 썸네일 요소 선택
    thumbnails = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    
    # 썸네일 클릭 및 이미지 다운로드
    for index, thumbnali in enumerate(thumbnails[:num_images]):
        try:
            thumbnali.click()
            time.sleep(2) # 이미지 뜰 때까지 기다리는 시간
            
            # 이미지 요소 대기 및 선택
            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb") # 큰따옴표 안은 클래스를 작성한다. 띄어쓰기 대신 "."으로 채움
                )
            )
            
            '''
            <img src="https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=1.00xw:0.753xh;0,0.153xh&amp;resize=1200:*" jsaction="VQAsE" class="r48jcc pT0Scc iPVvYb" style="max-width: 1200px; height: 280px; margin: 0px; width: 557px;" alt="30 Cute Cat Photos — Best Photos of Cats" jsname="kn3ccd" aria-hidden="false">
            '''
            
            # 이미지 URL 가져오기
            image_url = image.get_attribute("src") # .get_attribute() : ()안에 속성값들을 가져올 수 있다. src=값은 이미지의 링크를 나타내고 있다.
            
            # 이미지 URL이 데이터 형식인 경우 건너뛰기
            if image_url.startswith("data:"): # 가끔 이미지 url이 아니라 실제 이미지 데이터일 경우가 있다. 아래 코드에서 url을 이용하기 때문에 실제 데이터의 경우 건너뛴다.
                continue
            
            # HTTP 요청 헤더에 User-Agent 값을 추가하여 이미지 다운로드
            headers = {"User-Agent" : "Mozilla/5.0"}
            request = urllib.request.Request(image_url, headers = headers)
            with urllib.request.urlopen(request) as response:
                with open(f"{output_dir}/{keyword}_{index}.jpg", "wb") as out_file:
                    out_file.write(response.read())
            
            
        except Exception as e:
            print(f'Error downlaodings image {index}: {e}')
            traceback.print_exc()
            
    
    
    # 드라이버 종료
    driver.quit()
    
# 실행코드
keyword = 'cute cat'
num_images = 10
output_dir = 'images'

# 이미지 다운로드 함수 호출
download_images(keyword, num_images, output_dir)