# 크롤링: html 파일에서 원하는 데이터를 얻는 방법(html 파싱)
from bs4 import BeautifulSoup

html_data = '''
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>크롤링실습</h1>
        <p id="a" class="x">홍길동 단락</p>
        <p id="b" class="x">이순신 단락</p>
    </body>
</html>
'''
bs = BeautifulSoup(html_data, "html.parser")
# 태그명으로 접근
print(bs.html)
print(bs.body)
print(bs.h1)
# 함수로 접근 -> find("태그")는 하나만, select("CSS 선택자")는 전부
print(bs.find("p"))
print(bs.find_all("p"))
print(bs.find_all({"p", "h1"}))
# 텍스트 얻기
print(bs.find("p").text)
for tag in bs.find_all("p"):
    print(tag.text)
# 속성으로 접근
print(bs.find(attrs={"id": "b"}).text)
