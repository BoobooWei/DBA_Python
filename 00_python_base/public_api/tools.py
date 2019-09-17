# -*- coding: utf8 -*-

# Build-in Modules
import time
import datetime


# 把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# 把字符串转成datetime
def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


# 把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())


# 把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp))


# 把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTime):
    return time.mktime(dateTime.timetuple())