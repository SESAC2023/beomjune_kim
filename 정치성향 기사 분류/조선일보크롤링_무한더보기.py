import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WebDriver 설정
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.chosun.com/politics/")
time.sleep(2)

cnt = 0
# "기사 더보기" 버튼이 있는지 확인하고 계속 클릭
while True:
    try:
        load_more_btn = browser.find_element(By.CLASS_NAME, "load-more-btn")
        load_more_btn.click()
        time.sleep(2)  # 로딩 대기 시간(필요에 따라 조절)
        cnt += 1
        print(cnt)
    except:
        break

print(cnt)

'''
# 추가 기사 파싱
articles = browser.find_elements(By.CSS_SELECTOR, ".news-item")
for article in articles:
    # 기사 파싱 및 처리
    # ...
'''