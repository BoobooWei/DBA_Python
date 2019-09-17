# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.19.03.09.0
Description: regexp help
Help:
"""

# Build-in Modules
import re

# 设定正则表达式
r = re.compile('INSERT|DELETE|UPDATE')
n = re.compile('#')
insert = re.compile('INSERT')
delete = re.compile('DELETE')
update = re.compile('UPDATE')
e = re.compile('@.*=')
w = re.compile('WHERE')
s = re.compile('SET')

a_str = "insert into t1 values (1,2,3);"

# 正则匹配
if r.match(a_str):
    if insert.match(a_str):
        sql_type_str = 'insert'
    if delete.match(a_str):
        sql_type_str = 'delete'
    if update.match(a_str):
        sql_type_str = 'update'

# group匹配
host_str = 'host=192.168.1.1port=3306user=accountpassword=123456'

match_obj = re.match(r'host=(.*)port=(.*)user=(.*)password=(.*)', host_str)
if match_obj:
    host = match_obj.group(1).strip()
    port = match_obj.group(2).strip()
    user = match_obj.group(3).strip()
    password = match_obj.group(4).strip()

# 这个案例只是为了理解group的用法，不是好的带参数方法，推荐用第三方模块argparse
