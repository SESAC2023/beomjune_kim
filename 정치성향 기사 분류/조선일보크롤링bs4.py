import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())

driver = webdriver.Chrome(options=chrome_options)

data = []

# 기사 목록 URL
for i in range(1, 2):
    url = f"https://www.chosun.com/politics/politics_general/?page={i}"
    driver.get("https://www.chosun.com/politics/politics_general/2023/07/20/WAXAP6PRPBGBFLGYXEP6QIC6SM/")
    driver.implicitly_wait(10)

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(driver.page_source, "html.parser")
    content = soup.select_one("section.article-body").text.strip()

    # 기사 링크 추출
    print(content)

"""    for article in articles:
        link = article["href"]  # The "a" element is already the anchor tag, so no need for article.a
        article_links.append(link)
    print(article_links)"""

"""    # 각 기사의 내용 크롤링
    for link in article_links:
        # 기사 URL
        article_url = "https://www.chosun.com/" + link

        # 페이지 요청
        article_response = requests.get(article_url)
        article_content = article_response.content

        # BeautifulSoup 객체 생성
        article_soup = BeautifulSoup(article_content, "html.parser")

        # 기사 제목
        title = article_soup.find("span").text

        # 등록날짜
        date = article_soup.find("span", class_="upDate").text.strip()

        # 기사 내용
        content = article_soup.find("section", class_="article-body").text.strip()

        # 데이터 리스트에 추가하여 엑셀로 내보내기
        data.append([title, date, content, article_url])

        # 결과 출력
        print("제목:", title)
        print("등록날짜:", date)
        print("내용:", content)
        print("url:", article_url)
        print("---------------")

df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])

# 엑셀 파일로 내보내기
df.to_csv("articles01.csv", index=False)
"""