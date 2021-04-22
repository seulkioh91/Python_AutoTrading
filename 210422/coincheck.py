import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#assetRealBTC_KRW")

for tag in tags:
    print("비트코인 가격은", tag.text)

tags = soup.select("#assetRealETH_KRW")

for tag in tags:
    print("이더리움 가격은", tag.text)