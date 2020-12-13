# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:40
# @Author  : longrong.lang
# @FileName: test_nofixture.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
def test_no_fixture(login):
    print("==\n没有__init__测试用例，登录后，我就想退出登录了==", login)
