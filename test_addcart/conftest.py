# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:50
# @Author  : longrong.lang
# @FileName: conftest.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


@pytest.fixture(scope='function')
def addcart(login):
    print("从详情页登录，将商品加入购物车")
    price="2099元"
    yield price
    print('添加购物车成功，累计计算中')