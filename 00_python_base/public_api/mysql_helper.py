# -*- coding:utf8 -*-

"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.19.03.09.0
Description:
Help:
"""

# Build-in Modules
import json
import datetime
import decimal

# 3rd-part Modules
import pymysql


class MysqlHelper:
    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.port = kwargs['port']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.dbname = kwargs['dbname']
        self.charset = "utf8"
        self.conn = pymysql.connect(host=self.url, user=self.username, passwd=self.password, port=self.port,
                                    charset=self.charset, db=self.dbname)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def col_query(self, sql):
        """
        打印表的列名
        :return list
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    params = {
        "url": "url",
        "port": 3306,
        "username": "xx",
        "password": "xxx",
        "dbname": "xxx",
    }
    sql = """
    select * from t1 limit 10; 
    """

    api = MysqlHelper(**params)
    response = api.col_query(sql)
    print(json.dumps(response, cls=CJsonEncoder, ensure_ascii=False, indent=2))
