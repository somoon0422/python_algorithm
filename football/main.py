from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime
import time


seleted_time = '2023-07-##'
seleted_time = '20:00 ~ 22:00'

# 예약 사이트 URL
url = 'http://www.futsalbase.com/login'

# Chrome WebDriver 객체 생성
driver = webdriver.Chrome('C:\Users\MarkAny-N220\Downloads\chromedriver_win32')

# 예약 사이트 접속
driver.get(url)

# 로그인 정보 입력
username = driver.find_element_by_name('id')
password = driver.find_element_by_name('pwd')
username.send_keys('kunose')
password.send_keys('wjdehdtjr1!')
password.send_keys(Keys.ENTER)

#팝업창 닫기
try:
    for window in driver.window_handles[1:]:
        driver.switch_to.window(window) # 창으로 전환
        driver.close() # 창 닫기
    driver.switch_to.window(driver.window_handles[0]) # 메인 창으로 전환
except:
    pass



#대관예약 페이지로 이동
driver.get('http://www.futsalbase.com/home#')

# XPath 표현식으로 a 요소 찾기
a_elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/ul/li[5]/a')
# a 요소 클릭하기
a_elem.click()


# 현재 시간과 7월 1일 시간 계산
now = datetime.datetime.now()
target_time = datetime.datetime(now.year, 5, 31, 0, 0, 0)

# 5월 31일까지 대기
while now < target_time:
    # 페이지 새로고침
    driver.refresh()
    time.sleep(10)  # 10초간 대기

    # 예약 가능한 구장이 있는지 확인
    if now == target_time:
        try:
            # '예약하기' 버튼이 나오면 클릭하여 예약
            reserve_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='예약하기']"))
            )
            reserve_button.click()
            break  # 예약 성공 시 반복문 종료

        except:
            # 예약 가능한 구장이 없으면 다시 대기
            print("예약 가능한 구장이 없습니다. 다시 대기합니다.")
            pass
        
        # 현재 시간 다시 계산
        now = datetime.datetime.now()
    
# 7월 1일 이후 코드 작성
if now >= target_time:
    # 7월 달력이 열린 후에 예약 가능한 구장을 찾아 예약하는 코드 작성
    # ...
    
    
# WebDriver 종료
driver.quit()
