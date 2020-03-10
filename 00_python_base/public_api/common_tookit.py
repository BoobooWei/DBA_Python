# -*- coding: utf-8 -*-

# Build-in Modules
import re
import uuid
import json
import time
import datetime
import hashlib
import random
from collections import OrderedDict

# 3rd-part Modules
import arrow
from dateutil import parser as dateutil_parser
import shortuuid

UNIX_TIMESTAMP_OFFSET        = 1503982020
MAX_UNIX_TIMESTAMP_IN_SECOND = 9999999999

def print_var(v, name=None):
    print('[VAR] `{}` type=`{}`, value=`{}`'.format(name or '<NO NAME>', type(v), str(v)))

def get_attr(obj, attr, default=None):
    if hasattr(obj, attr):
        return obj.__getattribute__(attr)

    return default

def gen_uuid():
    return str(uuid.uuid4())

def gen_data_id(prefix=None):
    prefix = prefix or 'data'
    return prefix + '-' + str(uuid.uuid4())

def gen_short_data_id(prefix=None):
    prefix = prefix or 'data'
    return prefix + '-' + shortuuid.uuid()

def gen_time_serial_seq(d=None, rand_length=4):
    if not d:
        d = time.time()
    elif isinstance(d, datetime.datetime):
        d = time.mktime(d.timetuple())

    if not rand_length:
        rand_length = 4

    rand_pow_base = pow(10, rand_length)

    offsetted_timestamp = int(d * 1000 - UNIX_TIMESTAMP_OFFSET * 1000) * rand_pow_base
    rand_int = int(random.random() * rand_pow_base)

    return offsetted_timestamp + rand_int

def get_first_part(s, sep='-', count=2):
    return sep.join(s.split(sep)[0:count])

def json_find(j, path, safe=False):
    if j is None:
        if safe:
            return None
        else:
            raise Exception('json_find() - hit `None`')

    if not isinstance(path, (str, unicode)):
        if safe:
            return None
        else:
            raise Exception('json_find() - Path must be a string or unicode')

    curr_path = '<TOP>'
    sub_j = j
    steps = path.split('.')
    for step in steps:
        curr_path = '.'.join([curr_path, step])

        if not isinstance(sub_j, (dict, OrderedDict)):
            if safe:
                return None
            else:
                raise Exception('json_find() - hit non-dict at `{}`'.format(curr_path))

            break

        sub_j = sub_j.get(step)

    return sub_j

def json_smart_find(j, key, safe=False):
    if j is None:
        if safe:
            return None
        else:
            raise Exception('json_smart_find() - hit `None`')

    if not isinstance(key, (str, unicode)):
        if safe:
            return None
        else:
            raise Exception('json_smart_find() - Key must be a string or unicode')

    ret = None
    if key in j:
        return j[key]

    for k, v in j.items():
        if isinstance(v, (dict, OrderedDict)):
            ret = json_smart_find(v, key, safe)
            if ret is not None:
                break

    return ret

def json_override(s, d):
    if not s:
        return

    for k in s.keys():
        if k not in d:
            d[k] = s[k]
        elif isinstance(s[k], (tuple, list)):
            d[k] = s[k]
        elif s[k] is None:
            d[k] = s[k]
        elif isinstance(s[k], dict):
            json_override(s[k], d[k])
        else:
            d[k] = s[k]

def json_copy(o):
    return json.loads(json.dumps(o))

def json_dump_default(v):
    if isinstance(v, datetime.datetime):
        return to_iso_datetime(v)

    return v

def no_duplication(arr):
    return list(set(arr))

def is_none_or_empty(o):
    if o is None:
        return True

    if isinstance(o, (str, unicode)) and len(o) == 0:
        return True

    return False

def is_none_or_white_space(o):
    if is_none_or_empty(o):
        return True

    if isinstance(o, (str, unicode)) and len(o.strip()) == 0:
        return True

    return False

def no_none_or_white_space(o):
    return dict([(k,v) for k, v in o.items() if not is_none_or_white_space(v)])

def get_date_string(d=None, f=None):
    if not d:
        d = time.time()
    elif isinstance(d, (str, unicode)):
        d = to_unix_timestamp(d)
    elif isinstance(d, datetime.datetime):
        d = time.mktime(d.timetuple())

    if not f:
        f = '%Y-%m-%d'
    return time.strftime(f, time.localtime(d))

def get_time_string(d=None, f=None):
    if not d:
        d = time.time()
    elif isinstance(d, (str, unicode)):
        d = to_unix_timestamp(d)
    elif isinstance(d, datetime.datetime):
        d = time.mktime(d.timetuple())

    if not f:
        f = '%H:%M:%S'
    return time.strftime(f, time.localtime(d))

def get_datetime_string(d=None, f=None):
    if not d:
        d = time.time()
    elif isinstance(d, (str, unicode)):
        d = to_unix_timestamp(d)
    elif isinstance(d, datetime.datetime):
        d = time.mktime(d.timetuple())

    if not f:
        f = '%Y-%m-%d %H:%M:%S'
    return time.strftime(f, time.localtime(d))

def to_arrow(d):
    d_arrow = None
    if isinstance(d, (int, long, float)):
        # UNIX Timstamp in number type
        if d > MAX_UNIX_TIMESTAMP_IN_SECOND:
            d = int(d / 1000)

        d_arrow = arrow.get(d)

    elif isinstance(d, (str, unicode)) and d.isdigit():
        # UNIX Timstamp in string type
        if len(d) > len(str(MAX_UNIX_TIMESTAMP_IN_SECOND)):
            d = d[0:-3]

        d_arrow = arrow.get(d)

    else:
        # Normal
        try:
            d_arrow = arrow.get(d)
        except Exception as e:
            d_arrow = arrow.get(dateutil_parser.parse(d))

    return d_arrow

def to_datetime(d):
    d_arrow = to_arrow(d)
    return d_arrow.datetime

def to_unix_timestamp(d):
    d_arrow = to_arrow(d)
    return d_arrow.timestamp

def to_unix_timestamp_ms(d):
    timestamp = to_unix_timestamp(d)
    return timestamp * 1000

def to_iso_datetime(d):
    d_arrow = to_arrow(d)
    return d_arrow.isoformat()

def is_past_datetime(d):
    ts = to_unix_timestamp(d)
    return ts > time.time()

def get_days_from_now(d):
    ts = to_unix_timestamp(d)
    days = (ts - time.time()) / 3600 / 24
    return days

def get_md5(s):
    h = hashlib.md5()
    h.update(s.encode('utf8'))

    return h.hexdigest()

def get_sha1(s):
    h = hashlib.sha1()
    h.update(s.encode('utf8'))

    return h.hexdigest()

def _get_cache_key(topic, name, tags=None):
    if not topic:
        raise Exception('WAT: Can not use a topic with `{}`'.format(topic))

    if not name:
        raise Exception('WAT: Can not use a name with `{}`'.format(name))

    if not tags:
        cache_key = '{}@{}'.format(topic, name)
        return cache_key

    else:
        parts = [str(tag) for tag in tags]
        cache_key = '{}@{}:{}:'.format(topic, name, ':'.join(parts))
        return cache_key

def as_array(o):
    if o is None:
        return o

    elif isinstance(o, (list, tuple)):
        return list(o)

    else:
        return [o]

def as_array_str(o):
    if isinstance(o, (str, unicode)):
        return o

    arr = as_array(o)
    if arr is None:
        return arr
    else:
        return ','.join(arr)

def gen_reg_exp_by_wildcard(pattern):
    reg_exp = ''

    reg_exp_parts = []
    pattern_parts = pattern.split('.')
    for step in pattern_parts:
        if step == '**':
            reg_exp_parts.append('')

        elif step == '*':
            reg_exp_parts.append('[A-Za-z0-9_]+')

        else:
            reg_exp_parts.append(step)

    reg_exp = '\\.'.join(reg_exp_parts)

    if pattern_parts[len(pattern_parts) - 1] == '**':
        reg_exp = '^{}'.format(reg_exp)
    else:
        reg_exp = '^{}$'.format(reg_exp)

    return reg_exp

def match_wildcard(value, pattern):
    reg_exp = gen_reg_exp_by_wildcard(pattern)

    if re.match(reg_exp, value):
        return True
    else:
        return False

def match_wildcards(value, patterns):
    if not value or not patterns:
        return False

    patterns = as_array(patterns)

    for p in patterns:
        if match_wildcard(value, p):
            return True

    return False
