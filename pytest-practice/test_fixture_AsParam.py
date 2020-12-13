# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 18:23
# @Author  : longrong.lang
# @FileName: test_fixture_AsParam.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest
@pytest.fixture()
def param():
    return "fixture当做参数"
def test_Asparam(param):
    print('param : '+param)