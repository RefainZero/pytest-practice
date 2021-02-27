# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 17:48
# @Author  : longrong.lang
# @FileName: test_pytestWithAllure.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang

import json

import allure
import pytest
import requests


# 数据源
@pytest.fixture()
def getParams(request):
    param = request.param
    return param


data = [{"url": "http://api.qingyunke.com/api.php?key=free&appid=0&msg=", "keyWord": "鹅鹅鹅", "expected": "曲项向天歌"}]


@allure.feature('机器人聊天功能')  # 用feature说明产品需求，可以理解为JIRA中的Epic
class TestClass(object):
    @allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
    @allure.feature("测试模块_聊天")  # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
    @allure.story("测试模块_回复")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    @allure.issue("https://www.cnblogs.com/longronglang/p/14056500.html", "BUG号：123")  # 问题表识，关联标识已有的问题，可为一个url链接地址
    @allure.testcase("用例名：测试机器人回复功能")  # 用例标识，关联标识用例，可为一个url链接地址
    @allure.story('机器人回复功能')  # 用story说明用户场景，可以理解为JIRA中的Story
    @pytest.mark.parametrize("getParams", data, indirect=True)
    def test_requests(self, getParams):
        """
        用例描述：测试机器人回复功能
        """

        print(f"获取参数成功，输出：\n Url：{getParams['url']} \n 输入关键字：{getParams['keyWord']} \n 预期断言：{getParams['expected']}")
        # 模拟客户端请求
        content = getResult(getParams)
        # 获取预期结果
        expected = getParams['expected']
        with allure.step("获取输入参数"):  # 步骤1，step的参数将会打印到测试报告中
            allure.attach('请求路径', 'url')  # attach可以打印一些附加信息
            allure.attach('输入关键字', 'keyWord')
            allure.attach('预期结果', 'expected')
        with allure.step("模拟客户端输入，返回结果"):  # 步骤2
            pass
        with allure.step("校验结果"):  # 步骤3
            allure.attach('机器人回复', '期望结果')
            allure.attach('机器人回复', '实际结果')
            assert content == expected

    @allure.story('机器人会话中')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('机器人没电了')
    def test_delete_shopping_trolley(self):
        pass


@allure.step('模拟客户端请求')
def getResult(getParams):
    # 请求url和参数
    url = getParams['url'] + getParams['keyWord']
    # 模拟客户端请求
    req = requests.get(url)
    json.loads(req.text)
    map = req.json()
    content = map['content']
    return content
