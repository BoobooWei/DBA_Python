# -*- coding:utf8 -*-
"""
__Author__ = 'BoobooWei'
__CreateTime__ = '2019/5/24'
"""


# Build-in Modules
import urllib3

# 3rd-part Modules
from influxdb import InfluxDBClient

urllib3.disable_warnings()


class InfluxHelper:
    """
    https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdbclient
    """

    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.port = kwargs['port']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.dbname = kwargs['dbname']
        self.ssl = kwargs['ssl']

        try:
            self.client = InfluxDBClient(host=self.url, port=self.port, username=self.username,
                                         password=self.password, database=self.dbname, ssl=self.ssl)
        except Exception:
            print('connection err')

    def create_database(self, database):
        self.client.create_database(database)

    def insert(self, json_body):
        try:
            self.client.write_points(json_body)
        except Exception as e:
            print('write err : {0}'.format(str(e)))

    def select(self, sql):
        try:
            result = self.client.query(sql)
            return result
        except Exception as e:
            print('select err : {0}'.format(str(e)))

    def close(self):
        self.client.close()


if __name__ == "__main__":
    print("This is influxdb api.")

    # 连接InfluxDB数据库
    influx_dict = {  # InfluxDB连接方式
        'url': 'url',
        'port': '3242',
        'username': 'xx',
        'password': 'xxx',
        'dbname': 'telegraf',
        'ssl': True
    }
    influx_cli = InfluxHelper(**influx_dict)
    influx_cli.insert([
        {
            "measurement": "rds_for_mysql_slow_query_top10",
            "tags": {
                "group": "\u9a7b\u4e91\u8fd0\u7ef4\u9879\u76ee",
                "db_server": "rr-bp1d96998y68h5439.mysql.rds.aliyuncs.com:3306",
                "db_instance_id": "rr-bp1d96998y68h5439",
                "db_region": "cn-hangzhou",
                "db_name": "cloudcare_crm",
                "db_tag": "Readonly"
            },
            "fields": {
                "ParseMaxRowCount": 6699,
                "MySQLTotalExecutionCounts": 2,
                "SQLText": "select id , create_time , update_time , update_account_id , service_type , customer_id , content from crm_customer_service_record where ( :1 <= id and id < :2 )",
                "MaxLockTime": 0,
                "ReturnTotalRowCounts": 13293,
                "SQLIdStr": "0",
                "TotalLockTimes": 0,
                "MaxExecutionTime": 4,
                "CreateTime": "2019-05-25Z",
                "SlowLogId": 1069072718013427713,
                "ParseTotalRowCounts": 13293,
                "MySQLTotalExecutionTimes": 5,
                "SQLHASH": "5628307f99b4e3c6f2a81f3224d0363a",
                "DBName": "cloudcare_crm",
                "ReturnMaxRowCount": 6699
            }
        }
    ])
    influx_cli.close()
