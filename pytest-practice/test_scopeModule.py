# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 19:27
# @Author  : longrong.lang
# @FileName: test_scopeModule.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
fixture为module示例
'''
import pytest
@pytest.fixture(scope='module')
def data():
    return '\nscope为module'
def test1(data):
    print(data)
class TestClass(object):
    def test2(self, data):
        print('我在类中了哦，' + data)
if __name__ == '__main__':
    pytest.main(["-q", "test_scopeModule.py"])