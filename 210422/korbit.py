import requests
r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=xrp_krw")

print(type(r.text))
print(r.text)