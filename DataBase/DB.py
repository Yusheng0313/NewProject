# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

class DB():
    def __init__(self, host='192.168.0.110', port=3306, db='mysql-test', user='root', passwd='123456', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

if __name__ == '__main__':
    with DB(host='192.168.0.110', user='root', passwd='123456', db='mysql-test') as db:
        db.execute('select * from department')
        print('db类型：', db)
        for i in db:
            print(i)


