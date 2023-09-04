from newspaper import Article
#크롤링할 url 주소
url = 'https://www.chosun.com/politics/politics_general/2023/07/20/WAXAP6PRPBGBFLGYXEP6QIC6SM/'

#한국어이므로 language='ko'
article = Article(url, language='ko')
article.download()
article.parse()
#기사 제목 가져오기
print(article.title)
print(article.text)