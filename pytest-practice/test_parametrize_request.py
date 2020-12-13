# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 20:30
# @Author  : longrong.lang
# @FileName: test_parametrize_request.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


# # 传单个参数
# @pytest.fixture()
# def getuser(request):
#     user = request.param
#     print(f" 获取用户: {user}")
#     return user
#
#
# data = ["lilei", "jojo", "hanmeimei"]
# # 用英文哈,中文会被加密
# ids = [f" mark input ：{user} " for user in data]
#
#
# @pytest.mark.parametrize("getuser", data, ids=ids, indirect=True)
# class TestClass(object):
#     def test_getuser(self, getuser):
#         print(f"输出用户信息：{getuser}")

# # 传多个参数
# @pytest.fixture()
# def getlogins(request):
#     param = request.param
#     print(f" 获取用户名: {param['username']} 获取密码：{param['password']}")
#     return param
#
#
# data = [{"username": "jojo", "password": "123456"},
#         {"username": "hanmeimei", "password": "123456"},
#         {"username": "lilei", "password": "123456"}]
#
#
# @pytest.mark.parametrize("getlogins", data, indirect=True)
# def test_getlogin(getlogins):
#     print(f"用户名：{getlogins['username']} 密码：{getlogins['password']}")


# # 一个装饰器+多个fixture
# @pytest.fixture(scope="module")
# def getusername(request):
#     username = request.param
#     print(f" username is {username}")
#     return username
#
#
# @pytest.fixture(scope="module")
# def getpassword(request):
#     password = request.param
#     print(f" password is {password}")
#     return password
#
#
# data = [("jojo", "1"), ("lilei", "123654")]
#
#
# @pytest.mark.parametrize("getusername,getpassword", data, indirect=True)
# def test_getUserinfo(getusername, getpassword):
#     print(f"用户名：{getusername} 密码：{getpassword}")

# 多个装饰器+多个fixture
@pytest.fixture()
def users(request):
    user = request.param
    print(f" 用户名：{user}")
    return user


@pytest.fixture()
def pwds(request):
    pwd = request.param
    print(f" 密码：{pwd}")
    return pwd


data1 = ["lilei", "hameimei", "jojo"]
data2 = ["1", "2", "3"]


@pytest.mark.parametrize("users", data1, indirect=True)
@pytest.mark.parametrize("pwds", data2, indirect=True)
def test_getuserinfo(users, pwds):
    print(f"用户名为：{users} 密码为：{pwds}")
