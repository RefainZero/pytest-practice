# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 21:26
# @Author  : longrong.lang
# @FileName: conftest.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


@pytest.fixture(scope='session')
def login():
    print(u'调用登录接口')
    username = "zhangsan"
    token = "ZXF3ZTEyMTIzMTIxYWUxcWUxYGAyYDJgYDIx"
    yield username, token
    print("====登录成功，返回用户名，token！")


@pytest.fixture(autouse=True)
def get_userinfo(login):
    username, token = login
    print(f"== 每个用例都调用的外层fixture：打印用户名username：{username} 和token： {token} ==")
