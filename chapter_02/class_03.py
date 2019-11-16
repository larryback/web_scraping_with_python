from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")

allText = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in allText])