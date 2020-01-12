# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import pymysql

# 方法4：http://img1.money.126.net/data/[沪深拼音]/[是否复权]/[周期]/times/[股票代码].json
#
# 返回结果：获取日线所有时间节点和收盘价。
# 其中，[是否复权]，不复权为kline，复权为klinederc。
# 其中，[周期]，day为日数据，week周数据，month月数据。
#
# 例如，http://img1.money.126.net/data/hs/kline/day/times/1399001.json，获取深证成指所有时间节点数据。

json_url = 'http://img1.money.126.net/data/hs/kline/day/times/0601318.json'
req = requests.get(json_url)

with open('sh601318', 'w') as f:
    f.write(req.text)
file_requests = req.json()

print(file_requests)

