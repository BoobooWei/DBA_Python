# -*- coding:utf8 -*-

class Foo:
    def __init__(self, val):
        """将所有的数据属性都隐藏起来"""
        self.__NAME = val

    @property
    def name(self):
        """obj.name访问的是self.__NAME(这也是真实值的存放位置)"""
        return self.__NAME

    @name.setter
    def name(self, value):
        """在设定值之前进行类型检查"""
        if not isinstance(value, str):
            raise TypeError('%s must be str' % value)
        self.__NAME = value
        """通过类型检查后,将值value存放到真实的位置self.__NAME"""

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')


f = Foo('egon')
print(f.name)
f.name = 10
del f.name
