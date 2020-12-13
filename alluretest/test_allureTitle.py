# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 14:24
# @Author  : longrong.lang
# @FileName: test_allureTitle.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import allure, pytest


@allure.title("前置操作：获取用户名")
@pytest.fixture()
def users(request):
    user = request.param
    print(f" 用户名：{user}")
    return user


@allure.title("前置操作：获取密码")
@pytest.fixture()
def pwds(request):
    pwd = request.param
    print(f" 密码：{pwd}")
    return pwd


data1 = ["lilei", "hameimei", "jojo"]
data2 = ["1", "2", "3"]


@allure.title("组合操作：获取用户名: {users}  密码: {pwds}")
@pytest.mark.parametrize("users", data1, indirect=True)
@pytest.mark.parametrize("pwds", data2, indirect=True)
def test_getuserinfo(users, pwds):
    print(f"用户名为：{users} 密码为：{pwds}")
