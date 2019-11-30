from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:/Chrome_Driver/chromedriver_win32/chromedriver.exe')
driver.maximize_window() #For maximizing window
sleep(5)
driver.get('http://www.auction.co.kr/')
sleep(5)
#selected = driver.find_element_by_css_selector('#overview > p:nth-child(4) > a:nth-child(6)')
#print(selected.text)

driver.find_element_by_xpath('//*[@id="headerloginveiw"]/a').click() #로그인 버튼 클릭
sleep(2)

driver.find_element_by_name('id').send_keys('larryback72')

act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()


driver.find_element_by_name('password').send_keys('slick1972')
driver.find_element_by_xpath('//*[@id="Image1"]').click()

sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()