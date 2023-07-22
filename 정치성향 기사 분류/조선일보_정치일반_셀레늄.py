from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import TimeoutException

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼두기
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())

driver = webdriver.Chrome(options=chrome_options)

article_url_list = []
data = []
cnt = 0
for i in range(1, 2):
    try:
        driver.get(f"https://www.chosun.com/politics/politics_general/?page={i}")
        #driver.refresh()
        driver.implicitly_wait(20)
        article_links = driver.find_elements(By.CSS_SELECTOR, ".story-card__headline")

        for link in article_links:
            article_url_list.append(link.get_attribute("href"))
        for link in article_url_list:
            driver.get(link)
            driver.implicitly_wait(10)
            title = driver.find_element(By.CSS_SELECTOR, ".article-header__headline > span").text
            content = driver.find_element(By.CSS_SELECTOR, "section.article-body").text
            date = driver.find_element(By.CSS_SELECTOR, "span.dateBox").text
            article_url = link
            data.append([title, date.split(" ")[1], content, article_url])
            cnt += 1
            print(cnt)
            print(title)
            print(content)
            print(article_url)

    except TimeoutException:
        print("종료!")
        break


df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])

# 엑셀 파일로 내보내기
df.to_csv("articles01.csv", encoding="cp949")

