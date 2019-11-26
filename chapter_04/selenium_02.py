from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:/Chrome_Driver/chromedriver_win32/chromedriver.exe')
sleep(5)
driver.get('https://www.wikiwand.com/ko/%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC')
sleep(5)
selected = driver.find_element_by_css_selector('#overview > p:nth-child(4) > a:nth-child(6)')
print(selected.text)