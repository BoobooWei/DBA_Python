# -*- coding:utf8 -*-

settings = {
    "HOST": 'localhost',
    "PORT": 3306,
}


class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @staticmethod
    def from_conf():
        return MySQL(settings["HOST"], settings["PORT"])

    def __str__(self):
        return '就不告诉你'


class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' % (self.host, self.port)


m = Mariadb.from_conf()
print(m)


# -*- coding:utf8 -*-

settings = {
    "HOST": 'localhost',
    "PORT": 3306,
}


class MySQL:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def from_conf(cls):
        return cls(settings["HOST"], settings["PORT"])

    def __str__(self):
        return '就不告诉你'


class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' % (self.host, self.port)


m = Mariadb.from_conf()
print(m)

