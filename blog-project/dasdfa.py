import time


res = time.time()
# print(res)
res2 = time.localtime()
# print(res2)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=10, tm_hour=20, tm_min=21, tm_sec=41, tm_wday=6, tm_yday=314, tm_isdst=0)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=10, tm_hour=20, tm_min=22, tm_sec=15, tm_wday=6, tm_yday=314, tm_isdst=0)
res3 = time.strftime('%Y-%m-%d %H:%M:%S %A')
print(res3)