# -*- coding: utf-8 -*-

"""
author: BooBooWei
info: Oracle python3
"""

# https://oracle.github.io/odpi/doc/installation.html#macos
# https://github.com/oracle/python-cx_Oracle

# Build-in Modules
import os
import json

# 3rd-part Modules
import cx_Oracle

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class OracleHelper:
    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.port = kwargs['port']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.service_name = kwargs.get('service_name')
        self.oracle_sid = kwargs.get('oracle_sid')

        if self.service_name:
            try:
                dsn = cx_Oracle.makedsn(self.url, self.port, service_name=self.service_name)
                self.conn = cx_Oracle.connect(self.username, self.password, dsn)
                self.cur = self.conn.cursor()
            except Exception as e:
                print(str(e))
                self.error = 1
            else:
                self.error = 0

        elif self.oracle_sid:
            try:
                dsn = cx_Oracle.makedsn(self.url, self.port, self.oracle_sid)
                self.conn = cx_Oracle.connect(self.username, self.password, dsn)
                self.cur = self.conn.cursor()
            except Exception as e:
                print(str(e))
                self.error = 1
            else:
                self.error = 0

    def col_query(self, sql):
        result = []
        # sql = "select 'booboo' as name, 1 as num from dual union all select 'jack' as name, 2 as num from dual"
        res = self.cur.execute(sql)
        rows = res.fetchall()
        # print(self.cur.description)
        cols = [d[0].lower() for d in self.cur.description]
        for row in rows:
            result.append(dict(zip(cols, row)))
        return result

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
