import time
time_now = time.time()

day = time_now/(60*60*24)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(day)