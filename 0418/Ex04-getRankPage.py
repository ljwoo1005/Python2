import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list = soup.find_all('p', class_='artist')

# I AM - IVE

'''def music(a,b):
    global music_list
    global artist_list
    for title in music_list:
        return title.text.strip()
    for artist in artist_list:
        return artist.text.strip()

    
print(music(music_list, artist_list))
'''
for idx, chart in enumerate(music_list): # enumerate : 인덱스까지 같이 받을 수 있다.
    print(chart.text.strip(), end=' - ')
    print(artist_list[idx].find_all('a')[0].text.strip())