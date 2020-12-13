# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 20:44
# @Author  : longrong.lang
# @FileName: test_fixtrueYield.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
fixture之yield示例
'''

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='module')
def open():
    print("打开浏览器！！！")
    yield
    print('关闭浏览器！！！')


def test01():
    print("\n我是第一个用例")
    # 如果第一个用例异常了，不影响其他的用例执行
    raise Exception #此处异常


def test02(open):
    print("\n我是第二个用例")


if __name__ == '__main__':
    pytest.main(["-q", "test_fixtrueYield.py"])

