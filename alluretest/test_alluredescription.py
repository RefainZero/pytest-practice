# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 11:15
# @Author  : longrong.lang
# @FileName: test_alluredescription.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang

import allure


# @allure.description(str）
@allure.description("验证1=1")
def test_description1():
    assert 1 == 1


# 在测试用例函数声明下方添加 """ """
def test_description2():
    """
    验证1=1
    """
    assert 1 == 1


# @allure.description_html(str）
@allure.description_html("""
<h1>这是一段html描述</h1>
<img src="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1993234373,1554417853&fm=26&gp=0.jpg">
""")
def test_description3():
    assert 'h' in 'html'
