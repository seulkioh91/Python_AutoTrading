import pyupbit
access_key= "N3yAPoxbxcdRN9VFNiC1TWqEvxqKxCKQkDUH9V4c"
secret_key= "0aeEAqNlAindbYHxT9C5enejWIFU0fz0B2JttoM3"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())