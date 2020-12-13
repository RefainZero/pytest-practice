# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 17:27
# @Author  : longrong.lang
# @FileName: test_param_title.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import allure
import pytest

data = [("jojo", "1", "登录成功的用例"),
        ("rongrong", "1", "登录成功的用例"),
        ("lilei", "1", "登录失败的用例")
        ]


@allure.story("讲述登录成功，返回成功的故事！")
@allure.title("测试登录接口 {title}")
@pytest.mark.parametrize("userName,password,title", data)
def test_loginTo(userName, password, title):
    print(userName + "\t" + password + "\t" + title)
