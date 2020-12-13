# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 19:45
# @Author  : longrong.lang
# @FileName: test_scope1.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


def testScope1(commonData):
    print(commonData)
    assert commonData == ' 通过conftest.py 共享fixture'


if __name__ == '__main__':
    pytest.main(["-q", "test_scope1.py"])
