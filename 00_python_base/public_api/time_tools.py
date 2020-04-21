# -*- coding: utf8 -*-

# Build-in Modules
import time
import datetime

"""
# 时间戳《--》字符串《--》时间组
常用格式：
 f = '%Y-%m-%d %H:%M:%S'
 f = "%Y-%m-%dT%H:%M:%SZ"
 f = "%Y/%m/%d %H:%M:%S"
"""


# 把时间戳转成字符串形式
def timestamp_toString(stamp, f=None):
    if not f:
        f = '%Y-%m-%d %H:%M:%S'
    return time.strftime(f, time.localtime(stamp))


# 把字符串转成时间戳形式
def string_toTimestamp(strTime, f=None):
    if not f:
        f = '%Y-%m-%d %H:%M:%S'
    return time.mktime(string_toDatetime(strTime, f).timetuple())


# 把datetime类型转时间戳形式
def datetime_toTimestamp(dateTime):
    return time.mktime(dateTime.timetuple())


# 把datetime转成字符串
def datetime_toString(dt=None, f=None):
    if not dt:
        dt = datetime.datetime.now()
    if not f:
        f = '%Y-%m-%d %H:%M:%S'
    return dt.strftime(f)


# 把字符串转成datetime
def string_toDatetime(string, f=None):
    if not f:
        f = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.strptime(string, f)


# 将utc0字符串转为utf8字符串
def get_utc_0to8String(utc0String):
    """
    https://www.iso.org/iso-8601-date-and-time-format.html
    "T" appears literally in the string, to indicate the beginning of the time element.以指示时间元素的开始
    "Z" is the time zone offset specified as "Z" (for UTC) or either "+" or "-" followed by a time expression HH:mm
    :return:
    常用于获取到iso8601的时间字符串后，输出为东八区的时间字符串。
    """
    datatime_s = string_toDatetime(utc0String, "%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime_toTimestamp(datatime_s)
    utc8String = timestamp_toString(stamp + 8 * 3600)
    return utc8String


# 将utc8字符串转为utf0字符串
def get_utc_8to0String(utc8String):
    """
    常用于获取到东八区的时间字符串输出为iso8601的时间字符串。
    """
    datatime_s = string_toDatetime(utc8String, "%Y-%m-%d %H:%M:%S")
    stamp = datetime_toTimestamp(datatime_s)
    utc0String = timestamp_toString(stamp - 8 * 3600)
    return utc0String


# 将utc0字符串转为DataV的utf0字符串格式
def get_datav_time(utc0String):
    datatime_s = string_toDatetime(utc0String, "%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime_toTimestamp(datatime_s)
    utc8String_datav = timestamp_toString(stamp + 8 * 3600, "%Y/%m/%d %H:%M:%S")
    return utc8String_datav


if __name__ == "__main__":
    utc0String = '2020-04-21T17:31:45Z'
    print(get_utc_0to8String(utc0String))
    print(get_datav_time(utc0String))
    utc8String = '2020-04-22 01:31:45'
    print(get_utc_8to0String(utc8String))
