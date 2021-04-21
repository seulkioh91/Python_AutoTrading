import pyupbit

price = pyupbit.get_current_price("KRW-DOGE")
print("현재 도지코인의 가격은", price, "입니다.")

price = pyupbit.get_current_price("KRW-BTC")
print("현재 비트코인의 가격은", price, "입니다.")