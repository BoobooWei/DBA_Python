# Build-in Modules
import json
import time
import datetime

# 3rd-part Modules
import isodate


# 时间转换为时间戳
def iso8601_to_unix_timestamp(s):
    d_time = isodate.parse_datetime(s)
    utc_naive = d_time.replace(tzinfo=None) - d_time.utcoffset()
    timestamp = (utc_naive - datetime.datetime(1970, 1, 1)).total_seconds()
    return timestamp


def utc0_8(utc):
    timeStamp = iso8601_to_unix_timestamp(utc)
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

def utc_plus_8(s):
    utc = d_time = isodate.parse_datetime(s)
    utc_reduce_8 = utc - datetime.timedelta(hours=8)
    utc_plus_16 = utc + datetime.timedelta(hours=16)
    return utc_reduce_8.strftime("%Y-%m-%dT%H:%M:%SZ"), utc_plus_16.strftime("%Y-%m-%dT%H:%M:%SZ")

if __name__ != "main":
    iso8601_string = "2020-10-10T22:44:06Z"
    # 转为时间戳
    iso8601_number = iso8601_to_unix_timestamp(iso8601_string)
    utf_8_string = utc0_8(iso8601_string)
    print(iso8601_number)
    print('国际标准时间: {}'.format(iso8601_string))
    print('东八区: {}'.format(utf_8_string))


    _iso8601_string = datetime.datetime.combine(datetime.datetime.now(), datetime.time.min).strftime(
        '%Y-%m-%dT%H:%M:00Z')
    print(_iso8601_string)
    StartTime, EndTime = utc_plus_8(_iso8601_string)
    print(StartTime, EndTime)   
