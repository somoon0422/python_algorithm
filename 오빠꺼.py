from bs4 import BeautifulSoup # HTML을 파싱하는 라이브러리
import urllib.request as req # url을 열고 html을 읽어오는 라이브러리
from selenium import webdriver # 웹드라이버를 사용하기 위한 라이브러리
from time import sleep # sleep을 사용하기 위한 라이브러리
from selenium.webdriver.common.by import By # 웹드라이버에서 By를 사용하기 위한 라이브러리
import pandas as pd # 데이터프레임을 사용하기 위한 라이브러리

def crawler(search_key): # 크롤링 함수
    # 크롬드라이버 사용 지정
    driver = webdriver.Chrome('./chromedriver')​
    # HTML 가져오기
    url = "https://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoProduct.do?menu_grp=MENU_NEW04&menu_no=2815#page1"

    # 크롬드라이버로 url 열기
    driver.get(url)​
    # 검색어 입력    
    search_box = driver.find_element(By.XPATH, r'//*[@id="prd_nm"]').send_keys(search_key) # search_box에 search_key(검색어) 넣어줌

    # 페이지 로딩 기다리기
    sleep(1)
​
    # 검색 버튼 클릭
    search_btn = driver.find_element(By.CSS_SELECTOR, '#mode1 > div > span') # 버튼 지정
    search_btn.click() # 지정한 버튼 클릭
​
    # 전체 제품의 성분 및 원료 저장할 리스트
    product = []
​
    # html에서 원하는 데이터를 뽑아내는 과정
    for page in range(0, search_pages): # 페이지 수 만큼 반복
        # 페이지 로딩 기다리기
        sleep(30)
​
        try: # 페이지가 1페이지일 경우 예외처리
            for i in range(1, 11): # 페이지당 10개의 항목이 있으므로 10번 반복
                # 한 소스의 정보를 저장할 리스트
                product_tmp = []
​
                try: # 마지막 페이지에는 10개 항목 이하가 있을 수 있으므로 예외처리
                    # 현재 페이지 소스 가져오기
                    req = driver.page_source # 지금 브라우저 화면의 페이지 소스를 가져옴
                    soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup로 파싱
                    
                    # 제품명 클릭
                    elements = '#tbody > tr:nth-child({0}) > td:nth-child(6) > span.table_txt'.format(i)
                    elements_text = driver.find_element(By.CSS_SELECTOR, elements).text.strip() # 제품명 가져오기
                    search_btn = driver.find_element(By.CSS_SELECTOR, elements) # 버튼 지정
                    search_btn.click() # 지정한 버튼 클릭
                    sleep(2)
​
                    # 현재 페이지 소스 가져오기
                    req = driver.page_source # 지금 브라우저 화면의 페이지 소스를 가져옴
                    soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup로 파싱
                    
                    # 제품명의 성분 및 원료 따오기
                    for idx in range(1, 1000):
                        # 성분 및 원료 항목 가져오기
                        element = 'body > div.fancybox-wrap.fancybox-desktop.fancybox-type-ajax.fancybox-opened > div > div > div > div.page-container > div.fcs_ddt > table.col.table-sm > tbody > tr:nth-child({0}) > td:nth-child(2)'.format(idx)
​
                        # 가져온 항목이 비어있지 않으면 리스트에 추가
                        if str(soup.select(element)) != '[]':
                            # 가져온 항목을 리스트에 추가
                            product_tmp.append(str(soup.select(element)))
                            
                            # 리스트에 저장된 항목의 불필요한 부분 제거
                            product_tmp = [i.strip('[<td>') for i in product_tmp]
                            product_tmp = [i.strip('</td>]') for i in product_tmp]
                            
                            #한번에 작성 예시
                            #product_tmp.append(str(soup.select(element)).strip('[<td>').strip('</td>]'))
​
​
                        else: # 가져온 항목이 비어있으면 반복문 종료
                            break
                    
                   
                    
                    # 한 제품의 성분 및 원료를 전체 제품의 성분 및 원료 리스트에 추가
                    product.extend([elements_text,product_tmp])
​
                    # 뒤로가기 (X버튼 클릭)
                    search_btn = driver.find_element(By.CSS_SELECTOR, r'#close') # 버튼 지정
                    search_btn.click() # 지정한 버튼 클릭
                    sleep(1)
​
                    print(f'{page+1}번째 페이지 {i}번째 항목 완료')
​
                except: # 마지막 페이지에는 10개 항목 이하가 있을 수 있으므로 예외처리
                    break
​
            # 현재 페이지 소스 가져오기
            req = driver.page_source # 지금 브라우저 화면의 페이지 소스를 가져옴
            soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup로 파싱  
            
            # 다음 페이지로 넘어가기
            element = '#contents > main > section > div.list-container > div.board-footer > div > ul > li:nth-child({0})'.format(page+3) # 다음 페이지 버튼의 XPath 지정
            search_btn = driver.find_element(By.CSS_SELECTOR, element) # 버튼 지정
            search_btn.click() # 지정한 버튼 클릭
​
            print(f'{page+1}번째 페이지 완료')
​
        except:
            print('Paging Error!!!')
            break
​
    print('\n<<product >>')
    print(product)
    print('-- Parshing Complete --')
    driver.close() #드라이버를 닫아준다.
​
    # 크롤링 내역 csv로 저장
    df = pd.DataFrame(data = product) 
    df.to_csv('./product.csv', encoding='utf-8-sig') # csv로 저장
    print('-- CSV Save Complete --')
    
    return product
​
if __name__ == '__main__':
    search_key = input('검색어를 입력하세요 : ')
    search_pages = int(input('탐색할 페이지를 입력하세요 : '))
    crawler(search_key)
    print('-- Crawling Complete --')