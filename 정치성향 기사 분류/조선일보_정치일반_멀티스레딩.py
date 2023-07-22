from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import TimeoutException
import requests
import threading

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼두기
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 멀티스레드 작업용 세션 생성
service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())

def crawl_page(url, data, lock):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            driver = webdriver.Chrome(options=chrome_options, service=service)
            driver.get(url)
            driver.implicitly_wait(10)
            title = driver.find_element(By.CSS_SELECTOR, ".article-header__headline > span").text
            date = driver.find_element(By.CSS_SELECTOR, "span.dateBox").text
            print(title)
            print(date)
            print(url)
            with lock:
                data.append([title, date.split(" ")[1], content, url])
            driver.quit()

    except TimeoutException:
        print("종료!")

article_url_list = []
data = []
cnt = 0
lock = threading.Lock()

for i in range(1, 500):
    driver = webdriver.Chrome(options=chrome_options, service=service)
    try:
        driver.get(f"https://www.chosun.com/politics/politics_general/?page={i}")
        # driver.refresh()
        driver.implicitly_wait(20)
        article_links = driver.find_elements(By.CSS_SELECTOR, ".story-card__headline")

        for link in article_links:
            article_url_list.append(link.get_attribute("href"))

    except TimeoutException:
        print("종료!")

    driver.quit()

# 멀티스레드로 기사 크롤링
threads = []
for url in article_url_list:
    thread = threading.Thread(target=crawl_page, args=(url, data, lock))
    thread.start()
    threads.append(thread)

# 모든 스레드 작업이 끝날 때까지 기다림
for thread in threads:
    thread.join()

df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])

# 엑셀 파일로 내보내기
df.to_csv("articles02.csv", encoding="cp949")
