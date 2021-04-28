import pybithumb
import time

con_key = "02f897188c6c87b61e52999293750908"
sec_key = "b4788d9bf03adee3344f61ffe46dac95"

bithumb = pybithumb.Bithumb(con_key, sec_key)

krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/sell_price
print(unit)