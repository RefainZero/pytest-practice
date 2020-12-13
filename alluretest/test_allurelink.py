# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 15:49
# @Author  : longrong.lang
# @FileName: test_allurelink.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import allure
from allure_commons.types import LinkType


@allure.issue("https://v.youku.com/v_show/id_XNDk5MDQyODI1Ng==.html", "youku 三个金币")
def test_issue():
    pass


@allure.link("https://www.baidu.com/", link_type=LinkType.LINK, name="baidu")
def test_link():
    pass


@allure.testcase("https://www.cnblogs.com/longronglang/", "久曲健博客园")
def test_testCase():
    pass
