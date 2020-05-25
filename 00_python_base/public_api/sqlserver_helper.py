import pymssql

class DatabaseSQLServerConnDriver:
    """MySQL驱动连接驱动"""

    def __init__(self, connection):

        try:
            self.connection = pymssql.connect(**{
                'host': connection.get('host'),
                'port': connection.get('port'),
                'user': connection.get('user'),
                'password': connection.get('password'),
                'charset': 'utf8',
                'autocommit': True
            })
        except Exception as e:
            print(e)
            print('账号无效, 请检查权限或密码!')

        # print(self.connection)

    def query(self, sql):
        """数据查询操作"""

        # 使用cursor()方法获取操作游标，返回字典
        cursor = self.conn.cursor(as_dict=True)

        # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            self.connection.commit()
            return 0, '执行成功', results
        except Exception as e:
            print("Error: unable to fecth data %s " % e)
            return 1, '执行失败, %s' % str(e), False

        finally:
            print('query cursor closed')
            cursor.close()

    def update(self, sql):
        """数据更新操作"""

        # 使用cursor()方法获取操作游标
        cursor = self.connection.cursor()

        # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            self.connection.commit()
            return 0, '执行成功', True
        except Exception as e:
            print("Error: unable to fecth data %s " % e)
            return 1, '执行失败, %s' % str(e), False

        finally:
            print('update cursor closed')
            cursor.close()


"""
# 3rd-part Modules
import urllib3
from influxdb import InfluxDBClient
import pymssql


# pymssql.org/en/stable/intro.html#getting-started


class MssqlHelper():
    def __init__(self, **kwargs):
        try:
            conn = pymssql.connect(kwargs["server"], kwargs["user"], kwargs["password"], "master")
        except Exception as e:
            print(str(e))
            exit()
        self.cursor = conn.cursor()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            response = self.cursor.fetchone()
        except Exception as e:
            print(str(e))
            response = []
        return response

    def close(self):
        self.conn.close()


urllib3.disable_warnings()
"""
