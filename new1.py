# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd

csv_data = pd.read_csv('D:\\stock\\StockData\\StockList.csv', header=0, encoding="gbk", converters={u'代码': str})  # 读取训练数据
print(csv_data)
print(csv_data.shape)               # (3890行, 2列)
#print(csv_data.loc[:, ['代码']].head(5))    # 输出前5行 只含有代码列

# List = [csv_data.loc[0:4, ['代码']]]
# print(List)
for i in range(0, len(csv_data)):
    print(csv_data.loc[i]['代码'])

# N = 10
# csv_batch_data = csv_data.head(N)  # 取后5条数据
# print(csv_batch_data)  # (5, 9)

