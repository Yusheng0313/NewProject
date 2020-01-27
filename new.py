import psutil
import time

# 获取cpu个数
print(psutil.cpu_count())  # 获取cpu 逻辑个数
print(psutil.cpu_count(logical=False)) # 获取cpu 物理个数

# 获取cpu利用率
print(psutil.cpu_percent()) # 返回cpu利用率，如2.1
print(psutil.cpu_percent(percpu=True)) #返回每个cpu的利用率[3.4, 1.9, 1.7, 1.1, 1.3, 2.1, 1.2, 2.0]
print(psutil.cpu_percent(interval=2,percpu=True)) #阻塞interval秒，返回这段时间的利用率

for _ in range(1000):
  time.sleep(0.01)
# 以元组的形式，返回cpu的时间花费
print(psutil.cpu_times())
"""
也可以指定 percpu=True
scputimes(user=16687.609375, system=11913.625000000233, idle=1412197.8906249998, interrupt=1263.90625, dpc=456.09375)
"""

# 返回耗时时间比例
psutil.cpu_times_percent()

# 返回cpu统计信息，包括上下文切换，中断，软中断和系统调用的次数
psutil.cpu_stats()



