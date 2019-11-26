from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:/Chrome_Driver/chromedriver_win32/chromedriver.exe')
sleep(5)
driver.get('http://www.auction.co.kr/')
sleep(5)
#selected = driver.find_element_by_css_selector('#overview > p:nth-child(4) > a:nth-child(6)')
#print(selected.text)

driver.find_element_by_xpath('//*[@id="headerloginveiw"]/a').click() #로그인 버튼 클릭