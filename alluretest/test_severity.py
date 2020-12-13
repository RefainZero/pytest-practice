# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 13:48
# @Author  : longrong.lang
# @FileName: test_severity.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import allure


@allure.severity(allure.severity_level.BLOCKER)
def test_case1():
    print("case1")


@allure.severity(allure.severity_level.CRITICAL)
def test_case2():
    print("case2")


@allure.severity(allure.severity_level.NORMAL)
def test_case3():
    print("case3")


@allure.severity(allure.severity_level.MINOR)
def test_case4():
    print("case4")


@allure.severity(allure.severity_level.TRIVIAL)
def test_case5():
    print("case5")

def test_case6():
    """ 没标记 severity 的用例默认为 normal"""
    print("case6")