# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:19
# @Author  : longrong.lang
# @FileName: conftest.py.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


@pytest.fixture(scope='module')
def query(login):
    print("====调用查询接口")
    shopName="AJ男鞋"
    size=44
    colour="红色"
    yield shopName, size,colour
    print(f"调用查询接口成功，返回查询商品信息")