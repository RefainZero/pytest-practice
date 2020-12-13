# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 20:10
# @Author  : longrong.lang
# @FileName: test_fixtureCall.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
fixture调用示例
'''
import pytest
# 调用方式一
@pytest.fixture
def login1():
    print('第一种调用')
# 传login
def test_case1(login1):
    print("\n测试用例1")
# 不传login
def test_case2():
    print("\n测试用例2")
# 调用方式二
@pytest.fixture
def login2():
    print("第二种调用")
@pytest.mark.usefixtures("login2", "login1")
def test_case3():
    print("\n测试用例3")
# 调用方式三
@pytest.fixture(autouse=True)
def login3():
    print("\n第三种调用")
# 不是test开头，加了装饰器也不会执行fixture
@pytest.mark.usefixtures("login2")
def loginss():
    print(123)
if __name__ == '__main__':
    pytest.main(["-q", "test_fixtureCall.py"])
