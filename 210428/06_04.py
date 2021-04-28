import pybithumb
import time

con_key = "02f897188c6c87b61e52999293750908"
sec_key = "b4788d9bf03adee3344f61ffe46dac95"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_limit_order("BTC", 59000000, 0.001)
print(order)