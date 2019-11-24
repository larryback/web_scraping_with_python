from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=11&searchCtgId=&welInfSno=&searchWelInfNm=&pageGb=&domainName=&searchSidoCode=&searchCggCode=&cardListTypeCd=list&welSrvTypeCd=03&pageUnit=10&pageIndex={}'

for n in range (8) :
    url = base_url.format(n+1)
    webpage = urlopen(url)
    bs = BeautifulSoup(webpage, 'html5lib')
    reviews = bs.find_all('dt', {'class':'tit'})
    for review in reviews :
        print(review.get_text().strip())

