from selenium import webdriver                         # 기존의 기본 selenium 모듈
from selenium.webdriver.chrome.options import Options  # 크롬의 옵션 설정 모듈
import os                              # chromebrowser의 경로를 설정해줄 os모듈

# 크롬의 헤드리스 모드 브라우저 인스턴스를 생성하기 전 크롬 브라우져의 옵션을 정해 주어야 합니다.
chrome_options = Options()
chrome_options.add_argument("--headless")    # 브라우저를 헤드리스로 사용할거임
chrome_options.add_argument("--window-size=1920x1080")     # 브라우저 크기
chrome_options.add_argument("disable-gpu")                 # gpu

# 크롬의 바이너리 위치를 옵션에 넣어주고 크롬브라우저 프로그램의 위치를 지정해줍니다
chrome_options.binary_location = "/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(executable_path=os.path.abspath("/Users/Administrator/Desktop/chromedriver_win32"), chrome_options= chrome_options)

