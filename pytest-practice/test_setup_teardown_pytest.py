# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 20:27
# @Author  : longrong.lang
# @FileName: test_setup_teardown_pytest.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
pyetest示例
'''

import pytest


def setup_module():
    print("setup_module():在模块最之前执行，且只执行一次")


def teardown_module():
    print("teardown_module()：在模块之后执行，且只执行一次")


def setup_function():
    print("setup_function():每个方法之前执行")


def teardown_function():
    print("teardown_function():每个方法之后执行")


def test_1():
    print("正在执行用例1")
    x = "this"
    assert 'h' in x


def test_2():
    print("正在执行用例2")
    assert 1 == 1


class TestClass(object):

    def setup_class(self):
        print("setup_class(self)：每个类之前执行一次,只执行一次")

    def teardown_class(self):
        print("teardown_class(self)：每个类之后执行一次,只执行一次")

    def test_A(self):
        print("正在执行用例A")
        x = "this"
        assert 'h' in x

    def test_B(self):
        print("正在执行B")
        assert 1 == 1


if __name__ == "__main__":
    pytest.main(["-q", "test_setup_teardown_pytest.py"])
