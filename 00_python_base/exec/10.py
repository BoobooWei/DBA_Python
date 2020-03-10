# -*- coding:utf8 -*-

import uuid
import pickle
import os

DB_PATH = './mysql_test'


class MySQL:
    def __init__(self, host, port):
        self.id = self.create_id()
        self.host = host
        self.port = port

    def save(self):
        if not self.is_exists:
            raise PermissionError('对象已存在')
        file_path = r'%s%s%s' % (DB_PATH, os.sep, self.id)
        pickle.dump(self, open(file_path, 'wb'))

    @property
    def is_exists(self):
        tag = True
        files = os.listdir(DB_PATH)
        for file in files:
            file_abspath = r'%s%s%s' % (DB_PATH, os.sep, file)
            try:
                obj = pickle.load(open(file_abspath, 'rb'))
            except Exception as e:
                break
            else:
                if self.host == obj.host and self.port == obj.port:
                    tag = False
                    break
        return tag

    @staticmethod
    def get_obj_by_id(id):
        file_abspath = r'%s%s%s' % (DB_PATH, os.sep, id)
        return pickle.load(open(file_abspath, 'rb'))

    @staticmethod
    def create_id():
        return str(uuid.uuid1())


conn1 = MySQL('127.0.0.1', 3306)
conn1.save()  # 抛出异常PermissionError: 对象已存在

obj = MySQL.get_obj_by_id('bc9f6576-d91c-11e9-b43e-acde48001122')
print(obj.host)
print(obj.port)
