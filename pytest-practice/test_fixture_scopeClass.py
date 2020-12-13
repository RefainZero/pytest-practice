# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 19:15
# @Author  : longrong.lang
# @FileName: test_fixture_scopeClass.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
scope="class"示例
'''
import pytest
@pytest.fixture(scope='class')
def data():
    # 这是测试数据
    print('这是我的数据源,优先准备着哈')
    return [1, 2, 3, 4, 5]
class TestClass(object):
    def test1(self, data):
        # self可以理解为它自己的，英译汉我就是这么学的哈哈
        print('\n输出我的数据源：' + str(data))
if __name__ == '__main__':
    pytest.main(["-q", "test_fixture_scopeClass.py"])