from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless') # 헤드리스 모드 설정
chrome_options.add_argument('--disable_gnu') # GNU 
chrome_options.add_argument("lang = ko_KR") # 한국어로 실행되도록 설정

#추가된 부분, UserAgent 값을 바꿔 headless 모드임을 숨김
chrome_options.add_argument("user-agent = Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")

driver = webdriver.Chrome(executable_path=r'C:/Chrome_Driver/chromedriver_win32/chromedriver.exe', chrome_options = chrome_options)

sleep(5)
driver.get("http://www.auction.co.kr/")
#sleep(5)
#driver.find_element_by_xpath('//*[@id="headerloginveiw"]/a').click() # 로그인 버튼 클릭