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

# Function to scrape article details using BeautifulSoup
def scrape_article_details(url):
    driver.get(url)
    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.select_one(".article-header__headline > span").text.strip()
    content = soup.select_one("section.article-body").text.strip()
    date = soup.select_one("span.dateBox").text.strip()
    return title, date.split(" ")[1], content, url

article_url_list = []
data = []
cnt = 0

for i in range(1, 50):
    try:
        driver.get(f"https://www.chosun.com/politics/politics_general/?page={i}")
        driver.implicitly_wait(20)
        article_links = driver.find_elements(By.CSS_SELECTOR, ".story-card__headline")

        for link in article_links:
            article_url_list.append(link.get_attribute("href"))

        for link in article_url_list:
            title, date, content, article_url = scrape_article_details(link)
            data.append([title, date, content, article_url])
            print(title)
            print(date)
            print(content)
            print(article_url)
            cnt += 1
            print(cnt)

    except Exception as e:
        print(f"Error: {e}")
        break

# Close the Selenium driver
driver.quit()

df = pd.DataFrame(data, columns=["title", "date", "content", "article_url"])

# Export to CSV
df.to_csv("articles03.csv", encoding="cp949")
