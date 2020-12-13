# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 19:05
# @Author  : longrong.lang
# @FileName: test_fixture_scopeFunction.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
scope="function"示例
'''
import pytest
# 默认不填写
@pytest.fixture()
def test1():
    print('\n默认不填写参数')
# 写入默认参数
@pytest.fixture(scope='function')
def test2():
    print('\n写入默认参数function')
def test_defaultScope1(test1):
    print('test1被调用')
def test_defaultScope2(test2):
    print('test2被调用')
class Testclass(object):
    def test_defaultScope2(self, test2):
        print('\ntest2,被调用，无返回值时，默认为None')
        assert test2 == None
if __name__ == '__main__':
    pytest.main(["-q", "test_fixture_scopeFunction.py"])