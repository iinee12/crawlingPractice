from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver



chrome_options = Options()
chrome_options.add_argument("--disable-extenstions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login

driver.get('https://minumsa.com/wp-login.php?redirect_to=%2F') # 네이버 로그인 URL로 이동하기
driver.find_element_by_id('user_login').send_keys('iinee12') # 값 입력
driver.find_element_by_id('user_pass').send_keys('Eogksdml1@')
driver.find_element_by_xpath(
    '//*[@id="wp-submit"]'
    ).click() # 버튼클릭하기

driver.close

driver.implicitly_wait(3)
# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://minumsa.com/wp-login.php?redirect_to=%2F') # 네이버 로그인 URL로 이동하기
driver.find_element_by_id('user_login').send_keys('dddd') # 값 입력
driver.find_element_by_id('user_pass').send_keys('sfdf@')
driver.find_element_by_xpath(
    '//*[@id="wp-submit"]'
    ).click() # 버튼클릭하기
driver.close