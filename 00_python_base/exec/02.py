# -*- coding:utf-8 -*-

users = {
    "username": "tom",
    "password": "123",
    "login": False,
}


def auth_func(func):
    def wrapper(*args, **kwargs):
        # 验证功能
        if users["login"]:
            res = func(*args, **kwargs)
            return res
        else:
            username = input("username:").strip()
            password = input("password:").strip()

            if username == users["username"] and password == users["password"]:
                res = func(*args, **kwargs)
                users["login"] = True
                return res
            else:
                print("认证失败")

    return wrapper


@auth_func
def index():
    print("欢迎来到京东主页")


@auth_func
def home(name):
    print("欢迎回家 {}".format(name))


@auth_func
def shopping_car(name):
    print("%s 的购物车中有[%s, %s, %s]" % (name, "奶茶", "妹妹", "牙刷"))


index()
home("booboo")
shopping_car("booboo")
