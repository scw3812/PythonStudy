import requests
from bs4 import BeautifulSoup

# 검색차트
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B9%80%EC%A0%95%EC%9D%80&oquery" \
      "=%ED%81%B4%EB%A6%B0%ED%84%B4&tqi=UAaPCwprvN8ss7kW79Zssssst4C-198155 "
raw = requests.get(url, headers={"User-Agent": "Mozilla5.0"})
bs = BeautifulSoup(raw.text, "html.parser")
container = bs.find("ol", attrs={"class": "lst_realtime_srch _tab_area"})
keywords = container.find_all("span", attrs={"class": "tit"})
i = 1
for k in keywords:
    print(i, k.text)
    i += 1
print()

# 미세먼지
url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"
raw = requests.get(url, headers={"User-Agent": "Mozilla5.0"})
bs = BeautifulSoup(raw.text, "html.parser")
container = bs.find("dl", attrs={"class": "indicator"})
data1 = container.find_all("dt")
data2 = container.find_all("dd")

for i in range(3):
    print(data1[i].text+" "+data2[i].text)
