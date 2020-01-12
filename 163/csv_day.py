# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import pymysql
import pandas as pd

def download_stock(i_stock_code):

    start_date = '20000101'  # 开始日期
    end_date = '20300101'  # 结束日期
    directory = 'D:\\stock\\StockData\\163\day\\'  # 下载存放目录

    HS = '2'                            # 沪深标识 沪0，深1
    if i_stock_code[0:1] == 6:
        HS = '0'
    else:
        HS = '1'
    stock_code = i_stock_code           # 股票代码'601857'
    new_stock_code = HS + stock_code    # 构造新的股票代码格式
    file = stock_code + '.csv'          # 文件名
    path = directory + file             # 文件存放路径

    # 163网易金融API
    json_url = 'http://quotes.money.163.com/service/chddata.html?code=' + new_stock_code + '&start=' + start_date + '&end=' \
               + end_date + '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    req = requests.get(json_url)

    with open(path, 'w', newline='') as f:
        f.write(req.text)
    # file_requests = req.json()

    print('ok')

csv_data =pd.read_csv('D:\\stock\\StockData\\StockList.csv', header=0, encoding="gbk", converters={u'代码': str})  # 读取训练数据

for i in range(0, 5):        # len(csv_data)
    print(csv_data.loc[i]['代码'])
    download_stock(csv_data.loc[i]['代码'])
