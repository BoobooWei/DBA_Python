def human_time(times):
    """
    时间自适应
    :param times: 时间，单位为 毫秒， example: 1000
    :return: <string> example: 1s
    """
    if isinstance(times, (int, float)):
        times = float(times)
    else:
        return times

    if times >= 86400000:
        sec_times = times / 86400000
        human_times = '%.0fd' % sec_times
    elif times >= 3600000:
        min_times = times / 3600000
        human_times = '%.0fh' % min_times
    elif times >= 60000:
        hour_times = times / 60000
        human_times = '%.0fm' % hour_times
    elif times >= 1000:
        day_times = times / 1000
        human_times = '%.0fs' % day_times
    else:
        human_times = '%.0fms' % times

    return human_times


def human_byte(bytes):
    """
    文件大小自适应
    :param bytes: 文件大小, 单位为 bytes，example: 1024
    :return: <string> example：1KB
    """
    if isinstance(bytes, (int, float)):
        bytes = float(bytes)
    else:
        print(bytes)
        return bytes
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.0fTB' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.0fGB' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.0fMB' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.0fKB' % kilobytes
    else:
        size = '%.0fB' % bytes
    return size
