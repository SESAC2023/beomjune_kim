import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = "https://www.chosun.com/politics/politics_general/?page=1"

# User-Agent 설정 (선택사항)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
print(1)
# 요청이 성공적으로 이루어졌는지 확인
if response.status_code == 200:
    print(response.status_code)
    # 페이지의 HTML 소스 가져오기
    html = response.text

    # BeautifulSoup으로 파싱
    soup = BeautifulSoup(html, "html.parser")

    # 원하는 정보 추출
    articles = soup.select("div.story-card-component > a")
    print(2)
    print(articles)
    for article in articles:
        print(article.text)
else:
    print("페이지를 가져오는데 실패하였습니다.")

print(3)
