# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 13:42
# @Author  : longrong.lang
# @FileName: test_assertExp.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


def test_assertExp():
    assert 1 == 2
    print("我是硬断言assert,断言失败后，这段不会执行")
    assert 1 == 1


def test_assert():
    pytest.assume(1, 3)
    pytest.assume(1, 1)
    pytest.assume("test", 3)
    print("\n我是硬断言assume，断言失败，也会执行！")
