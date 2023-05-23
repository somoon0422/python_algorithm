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
        for day in range(2,7): # 1~7일
            xpath_month = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div' #달력전체화면
            xpath_day = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[{}]/div[1]/table/tbody/tr/td[{}]'.format(i, day))#1일단위박스
            time.sleep(2)
            xpath_day.click()
            # actions = ActionChains(driver)
            # actions.move_to_element(xpath_day)
            # actions.perform()
            # driver.execute_script("arguments[0].click();", xpath_day)
            
            print("클릭성공")
            time.sleep(2)
            #import pdb; pdb.set_trace()
            try:
                #체크 박스 클릭
                check_box = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/table/tbody/tr[8]/td[1]/label/span')
                check_box.click()
                print("체크박스를 클릭했습니다.")
                next_level = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/button[2]')
                next_level.click()
                print("다음단계로 넘어갑니다.")
                time.sleep(2)
                break
            except:
                print("예약이 어렵습니다. 다음날을 확인합니다.")
                continue
        break
    
    agree_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/label/span')
    agree_button.click()
    reserve_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/button[2]')
    reserve_button.click()
    time.sleep(2)
    done_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/button')
    done_button.click()
    print("예약이 완료되었습니다.")
    
    driver.close()
    
    
    
                
            


if __name__ == '__main__':
    count_num = int(input("예약하실 축구장 번호를 입력하세요: ")) # ex) 4  
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    reservation(count_num)
    
    
    
            # 오늘날짜 이후 기준으로 찾고 싶을 때 
            # date = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[{}]/div[2]/table/thead/tr/td[{}]'.format(i, day)
            # date_text = date.get_property("data-date") if date else ""
            # print(date_text)
            # today = datetime.date.today() #datetime.date(2023, 5, 23)
            # today_str = today.strftime("%Y-%m-%d") #오늘날짜
            # choice_date = date_text #선택한날짜
            # # date = xpath_day.find("span" , class_ = "fc-day-number").get_text()
            
            # if choice_date <= today_str: # 오늘날짜 이전일 경우
            #     print("이전날짜입니다. 다음날짜로 넘어갑니다.")
            #     continue
