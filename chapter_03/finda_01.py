import requests 
from urllib.request import urlopen
from bs4 import BeautifulSoup 

 
res = urlopen('https://www.finda.co.kr/loans/mortgage-loans?p=1')
 
soup = BeautifulSoup(res, 'html.parser')
 
# a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장됨
links = soup.select('div  h2 > a')
   
for link in links:
    print (link.get_text()) # 스포츠
    # print (link['href']) # http://sports.media.daum.net/sports
    #if res.search('http://\w+', link['href']):  # http:// 문자열 이후에 숫자 또는 문자[a-zA-Z0-9_]가 한 개 이상 있는 데이터와 매치됨 
        #print (link['href'])