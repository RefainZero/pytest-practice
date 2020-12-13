# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 9:51
# @Author  : longrong.lang
# @FileName: test_mark.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest

@pytest.mark.mylogin
def test_login():
    print('登录成功！')


@pytest.mark.query
def test_query():
    print('检索商品成功！')


@pytest.mark.addcart
def test_addcart():
    print('加入购物车')


if __name__ == '__main__':
    # pytest -s -m query test_mark.py
    pytest.main(['-s', '-m query', 'test_mark.py'])
