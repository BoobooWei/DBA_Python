# -*- coding:utf8 -*-

# 非 oss 产品
# 3rd-part Modules
from aliyun_sdk import client
ak = {
    "AccessKeyId":"example",
    "AccessKeySecret": "example"
}
aliyun_client = client.AliyunClient(ak)
status_code, response = aliyun_client.common('ecs', Action='DescribeRegions')

# response ==> (status_code, result)
print(status_code, response)

# example result
# (404, {'Recommend': 'https://error-center.aliyun.com/status/search?Keyword=InvalidAccessKeyId.NotFound&source=PopGw', 'Message': 'Specified access key is not found.', 'RequestId': 'AEA6AEB8-6F44-445B-Bd0E-9E5F706B5665', 'HostId': 'ecs.aliyuncs.com', 'Code': 'InvalidAccessKeyId.NotFound'})

# oss 产品
status_code, oss_response = aliyun_client.oss('GET', **{"max-keys": 1000})
print(status_code, oss_response)
status_code, oss_response = aliyun_client.oss('GET', BucketName='cxp-test', Query={'acl': None})
print(status_code, oss_response)
