# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 18:28
# @Author  : longrong.lang
# @FileName: test_fixtureParams.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
fixture的params示例
'''
import pytest

seq=[1,2]


@pytest.fixture(params=seq)
def params(request):
    # request用来接收param列表数据
    return request.param



def test_params(params):
    print(params)
    assert 1 == params