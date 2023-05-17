from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
import time
import requests
import re



def reservation(court_num):
    # 크롬 드라이버 실행
    driver = webdriver.Chrome()
    
    # 축구장 예약 웹 사이트의 URL
    url = 'http://www.futsalbase.com/login'
    
    # 대관예약 페이지로 이동
    res = requests.get(url)
    
    time.sleep(1)

    # 로그인 처리
    driver.find_element(By.ID, "id").send_keys("somoon0422")
    driver.find_element(By.ID, "pwd").send_keys("gooddata001!@#")
    click_button = driver.find_element(By.XPATH, '/html/body/div/div/div/section/div/div[2]/div[1]/div[2]/button')
    click_button.click()
    
    time.sleep(2)

    #팝업창 닫기
    try:
        for window in driver.window_handles[1:]:
            driver.switch_to.window(window) # 창으로 전환
            driver.close() # 창 닫기
        driver.switch_to.window(driver.window_handles[0]) # 메인 창으로 전환
    except:
        pass

    # 대관예약 페이지로 이동
    reserve_button = driver.find_element(By.XPATH, '/html/body/div/div/div/section/div/ul/li[3]/a')
    reserve_button.click()
    
    # 축구장 목록 찾기
    html = driver.page_source
    courts = re.findall(r'<li class="ballpark-list">(.*?)</li>', html)
    
    # 선택한 구장 번호에 해당하는 구장 찾기
    for court in courts:
        if court.find("a").text == "{}구장".format(count_num):
            court_url = court.find("a")["href"]
            break
    
    # 해당하는 구장의 링크 클릭
    res = requests.get(court_url)


if __name__ == '__main__':
    count_num = int(input("예약하실 축구장 번호를 입력하세요: ")) # ex) 4
    reservation(count_num)
