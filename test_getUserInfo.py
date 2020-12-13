# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 21:56
# @Author  : longrong.lang
# @FileName: test_getUserInfo.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang

def test_getUserInfo(login):
    username, token = login
    print(f"== 每个用例都调用的外层fixture：打印用户名\nusername：{username} 和token： {token} ==")
