# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 8:32
# @Author  : longrong.lang
# @FileName: test_mark.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang

import allure
import pytest


@pytest.fixture(scope="session")
def login_fixture():
    print("=== 前置登录 ===")


@allure.step("步骤1")
def step_1():
    print("操作步骤 查找商品---------------1")


@allure.step("步骤2")
def step_2():
    print("操作步骤 将商品加入购物车---------------2")


@allure.epic("epic 此处为总体描述")
@allure.feature("测试模块，如加入购物车")
class TestAllure:

    @allure.testcase("https://www.cnblogs.com/longronglang/", '测试用例使用链接')
    @allure.issue("https://www.cnblogs.com/longronglang/", 'Bug使用链接')
    @allure.title("用例的标题（将商品加入购物车）")
    @allure.story("story one")
    # 严重级别
    @allure.severity("critical")
    @allure.story("检索商品并加入购物车")
    @allure.title("久曲健博客：https://www.cnblogs.com/longronglang/")
    def test_case_1(self, login_fixture):
        print("测试用例1")
        step_1()
        step_2()
