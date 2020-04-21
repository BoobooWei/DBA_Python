# -*- coding: utf8 -*-

# Build-in Modules
import time
import datetime


# 把datetime转成字符串
def datetime_toString(dt=datetime.datetime.now()):
    """
    # 本地时间
    dt = datetime.datetime.now()
    :param dt:
    :return:
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# 把字符串转成datetime
def string_toDatetime_8(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


def string_toDatetime_0(string):
    return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ")


# 把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())


# 把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stamp))


# 把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTime):
    return time.mktime(dateTime.timetuple())


# 将utc0字符串转为utf8字符串
def get_utc_0to8String(utc0String):
    """
    https://www.iso.org/iso-8601-date-and-time-format.html
    "T" appears literally in the string, to indicate the beginning of the time element.以指示时间元素的开始
    "Z" is the time zone offset specified as "Z" (for UTC) or either "+" or "-" followed by a time expression HH:mm
    :return:
    常用于获取到iso8601的时间字符串后，输出为东八区的时间字符串。
    """
    datatime_s = string_toDatetime_0(utc0String)
    stamp = datetime_toTimestamp(datatime_s)
    utc8String = timestamp_toString(stamp + 8 * 3600)
    return utc8String

# 将utc8字符串转为utf0字符串
def get_utc_8to0String(utc8String):
    """
    常用于获取到东八区的时间字符串输出为iso8601的时间字符串。
    """
    datatime_s = string_toDatetime_8(utc8String)
    stamp = datetime_toTimestamp(datatime_s)
    utc0String = timestamp_toString(stamp - 8 * 3600)
    return utc0String

if __name__ == "__main__":
    utc0String = '2020-04-21T17:31:45Z'
    print(get_utc_0to8String(utc0String))
    utc8String = '2020-04-22 01:31:45'
    print(get_utc_8to0String(utc0String))
