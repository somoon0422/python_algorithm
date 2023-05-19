from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import re
import datetime

def reservation(court_num):
    # 크롬 드라이버 실행
    driver = webdriver.Chrome()
    
    # 축구장 예약 웹 사이트의 URL
    driver.get("http://www.futsalbase.com/login")
    time.sleep(1)

    #로그인하기
    xpath_username = '//*[@id="id"]' 
    xpath_password = '//*[@id="pwd"]'
    xpath_login = '/html/body/div/div/div/section/div/div[2]/div[1]/div[2]/button'
    
    driver.find_element(By.XPATH, xpath_username).send_keys(username) # 아이디 입력
    driver.find_element(By.XPATH, xpath_password).send_keys(password) # 비밀번호 입력
    driver.find_element(By.XPATH, xpath_login).click() # 로그인 버튼 클릭
    print("로그인 성공")
    time.sleep(2)

    #팝업창 닫기
    for i in range(3):
        try:
            xpath_popup = '/html/body/div/div/div/div[3]/div/div/div/div[2]/button'
            driver.find_element(By.XPATH, xpath_popup).click()
        except:
            pass
    

    # 대관예약 페이지로 이동
    
    reserve_button = driver.find_element(By.XPATH, '/html/body/div/div/div/section/div/ul/li[3]')
    reserve_button.click()
    print("대관예약 페이지로 이동합니다.")
    time.sleep(2)
    
    #대관예약 페이지 클릭
    for i in range(8):
        xpath_court_link= '/html/body/div/div/div/div[2]/div[2]/ul/li[{}]/a'.format(i) # 축구장 링크 xpath
        if i == court_num+1 :
            driver.find_element(By.XPATH, xpath_court_link).click()
            break
    
    next_month = "/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/a[2]"
    driver.find_element(By.XPATH, next_month).click()
    
    
    #여기서부터 잘 안됨.....
    
    # 오늘 날짜를 가져옵니다.
    # 예약 가능한 날짜 확인
    for i in range(2,7): # 2~6주차
        for day in range(1,8): # 1~7일
            xpath_month = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div' #전체화면
            xpath_week = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[{}]'.format(i))#1주일단위 
            #날짜가 오늘날짜 이후일 경우 진행, 아닐 경우 pass
            xpath_date ='/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[{}]/div[2]/table/thead/tr/td[{}]/span'.format(i,day)
            today = datetime.today()
            today_str = today.strftime("%Y-%m-%d")
        
        for day in range(1,8):
            xpath_day1 = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[3]/table/tbody/tr/td[{}]'.format(day)
            xpath_day2 = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr/td[{}]/a/div[1]/span'.format(day)
            check_box = '//*[@id="pushYn"]'
            #action
            #날짜를 하나씩 클릭
            driver.find_element(By.XPATH, xpath_day1).click()
            driver.find_element(By.XPATH, xpath_day2).click()
            print("{}일을 조회합니다.".formaty(day))
            time.sleep(1)
            
            try:
                target_xpath = '/html/body/div/div/div/div[2]/div[2]/table/tbody/tr[8]/td[1]/label'
                if target_xpath in 'label':
                    driver.find_element(By.XPATH, check_box).click()
                    print("예약 가능한 날짜입니다.")
            except:
                print("예약 불가능한 날짜입니다.")
                pass


            path = /html/body/div/div/div/div[2]/div[2]/table/tbody/tr[10]/td[1]/label에 접근해봐서 성공하면 클릭하기. 실패하면 pass
        


if __name__ == '__main__':
    count_num = int(input("예약하실 축구장 번호를 입력하세요: ")) # ex) 4  
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    reservation(count_num)
