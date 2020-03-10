# import sys, os
#
# print(sys.path)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# print(os.path.dirname(BASE_DIR))
# print(sys.path)

# import time
#
#
# a1 = time.time()
#
# a2 = time.localtime()
#
# a3 = time.gmtime()
#
# a4 = time.mktime(a2)
#
# a5 = time.asctime(a2)
#
# a6 = time.ctime(a1)
#
# a7 = time.strftime('%Y-%m-%d %X', a2)
#
# a8 = time.strptime(a7, '%Y-%m-%d %X')
#
# for i in [a1, a2, a3, a4, a5, a6, a7, a8]:
#     print(i)


#

# import random
#
#
# def v_code():
#     code = ''
#     for i in range(5):
#         num = random.randint(0, 9)
#         alf = chr(random.randint(65, 90))
#         add = random.choice([num, alf])
#         code += str(add)
#     return code
#
#
# print(v_code())


# import sys, time
#
# for i in range(10):
#     sys.stdout.write('#')
#     time.sleep(1)
#     sys.stdout.flush()


# import json
#
# a = {
#     'name': 'booboo',
#     'goods': ['机票', '酒店']
# }
#
# a_json = json.dumps(a, indent=2, ensure_ascii=False)
#
# b_json = """
# {
#   "name": "booboo",
#   "goods": [
#     "机票",
#     "酒店"
#   ]
# }
# """
#
# b_dict = json.loads(b_json)
#
# print(type(a_json), a_json)
# print(type(b_dict), b_json)


# import hashlib
#
# m = hashlib.md5()
#
# m.update('hello'.encode('utf8'))
# print(m.hexdigest())
#
# m.update('alvin'.encode('utf8'))
#
# print(m.hexdigest())
#
# m2 = hashlib.md5()
# m2.update('hello word'.encode('utf8'))
# print(m2.hexdigest())
#
# m3 = hashlib.sha256()
# print(m3.hexdigest())


# import hashlib
#
# a = hashlib.sha256('hello'.encode('utf8'))
# a.update('booboo'.encode('utf8'))
# print(a.hexdigest())


# import hmac
#
# h = hmac.new('booboo'.encode('utf8'))
# h.update('hello'.encode('utf8'))
# print(h.hexdigest())


import re

some_str = "this is a string with {{words}} embedded in {{curly brackets}} to show an {{example}} of {{regular expressions}}"
re_str = '{{.*}}'
for match in re.findall(re_str, some_str):
    print("match-->", match)
