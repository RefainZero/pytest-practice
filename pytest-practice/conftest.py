# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 19:37
# @Author  : longrong.lang
# @FileName: conftest.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest
@pytest.fixture(scope='session')
def commonData():
    str = ' 通过conftest.py 共享fixture'
    print('获取到%s' % str)
    return str