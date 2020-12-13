# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 20:23
# @Author  : longrong.lang
# @FileName: test_fixtureRelyCall.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang

'''
fixture依赖其他fixture的调用示例
'''
import pytest


@pytest.fixture(scope='session')
# 打开浏览器
def openBrowser():
    print('\n打开Chrome浏览器')


# @pytest.mark.usefixtures('openBrowser')这么写是不行的哦，肯定不好使
@pytest.fixture()
# 输入账号密码
def loginAction(openBrowser):
    print('\n输入账号密码')


#  登录过程
def test_login(loginAction):
    print('\n点击登录进入系统')


if __name__ == '__main__':
    pytest.main(["-q", "test_fixtureRelyCall.py"])

