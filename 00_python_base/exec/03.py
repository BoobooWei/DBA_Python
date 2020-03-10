# -*- coding:utf-8 -*-

users = [
    {"username": "tom", "password": "123"},
    {"username": "jack", "password": "123"},
]

current_user = {
    "username": None,
    "password": None,
    "login": False,
}


def auth_func(func):
    def wrapper(*args, **kwargs):
        # 验证功能
        if current_user["login"]:
            res = func(*args, **kwargs)
            return res
        else:
            username = input("username:").strip()
            password = input("password:").strip()
            for user in users:
                if username == user["username"] and password == user["password"]:
                    res = func(*args, **kwargs)
                    current_user["username"] = username
                    current_user["password"] = password
                    current_user["login"] = True
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
