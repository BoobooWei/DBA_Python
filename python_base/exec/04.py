# -*- coding:utf-8 -*-
import json

users_local = [
    {"username": "tom", "password": "123"},
    {"username": "jack", "password": "1234"}
]

current_user = {
    "username": None,
    "password": None,
    "login": False,
}


def auth(auth_type="filedb"):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            # 验证类型
            if auth_type == "filedb":
                print("认证类型为：{}".format(auth_type))
                users = json.loads(open('auth.json').read())
            else:
                print("认证类型为：{}".format("local"))
                users = users_local
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

    return auth_func


@auth(auth_type='filedb')
def index():
    print("欢迎来到京东主页")


@auth(auth_type='filedb')
def home(name):
    print("欢迎回家 {}".format(name))


@auth(auth_type="filedb")
def shopping_car(name):
    print("%s 的购物车中有[%s, %s, %s]" % (name, "奶茶", "妹妹", "牙刷"))


index()
home("booboo")
shopping_car("booboo")
