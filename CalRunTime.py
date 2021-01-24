# DrawStar.py
import time
limit=10*1000*1000
start=time.perf_counter()
while True:
    limit -= 1 # 注意自减号“-=”，行等同于“limit = limit - 1”
    if limit <= 0:
        break
delta=time.perf_counter() - start  # 结束时间-开始时间=运行时间
print("程序运行时间是：{}秒".format(delta))
