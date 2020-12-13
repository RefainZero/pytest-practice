# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 20:27
# @Author  : longrong.lang
# @FileName: test_dynamic.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest, allure


@allure.epic("演示动态生成的注解使用")
@allure.story("讲述一个测试用例包含很多动态注解的事")
class TestDynamict(object):
    @allure.title("默认的用例标题")
    @allure.description("默认的用例描述")
    def test_case(self):
        print("测试用例")
        allure.dynamic.title("动态标题")
        allure.dynamic.description("动态描述")
        # 其他属性
        allure.dynamic.feature('动态feature')
        allure.dynamic.story('动态story')
        allure.dynamic.link("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Link')
        allure.dynamic.issue("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Issue')
        allure.dynamic.testcase("https://www.cnblogs.com/longronglang/category/1859053.html", '动态testcase')


data = [("jojo", "1", "登录成功的用例"),
        ("rongrong", "1", "登录成功的用例"),
        ("lilei", "1", "登录失败的用例")
        ]


@allure.story("讲述登录成功，返回成功的故事！")
@allure.title("测试登录接口 {title}")
@pytest.mark.parametrize("userName,password,title", data)
def test_loginTo(userName, password, title):
    print(userName + "\t" + password + "\t" + title)
    allure.dynamic.title(title)
