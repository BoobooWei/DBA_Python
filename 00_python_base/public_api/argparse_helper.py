# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.19.03.09.0
Description: 参数
Help:
"""

# 3rd-part Modules
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--AccessKeyId", help="AccessKeyId 必要参数")
parser.add_argument("--AccessKeySecret", help="AccessKeySecret 必要参数")
parser.add_argument("--OutFile", help="输出文件名 必要参数")
parser.add_argument("--Region", help="指定地域 非必要参数，没有该参数则循环国内所有地域")

args = parser.parse_args()


common_region_ids = []

if args.Region:
    common_region_ids.append(args.Region)
else:
    common_region_ids.extend(["cn-qingdao",
                              "cn-beijing",
                              "cn-zhangjiakou",
                              "cn-huhehaote",
                              "cn-hangzhou",
                              "cn-shanghai",
                              "cn-shenzhen",
                              "cn-hongkong",
                              ])

if args.AccessKeyId and args.AccessKeySecret and args.OutFile:
    params = {
        'AccessKeyId': args.AccessKeyId,
        'AccessKeySecret': args.AccessKeySecret,
        'txt': args.OutFile,
    }
    print(params, indent=2)