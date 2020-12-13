# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 8:34
# @Author  : longrong.lang
# @FileName: test_allure.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import allure


@allure.step("打开网站首页")
def open():
    pass


@allure.step("输入账号、密码")
def input_UsernameAndPassWord():
    sendAndClickLogin("xiaoqiang", "1")


@allure.step("输入账号、密码{arg1}，{arg2}，并点击登录")
def sendAndClickLogin(arg1, arg2):
    pass


@allure.step("验证登录过程")
def test_login():
    open()
    input_UsernameAndPassWord()


# 添加附件
def test_attachments():
    # 在测试报告中画了一个html页面
    allure.attach('<head></head><body><strong>HTML页面，HelloWorld！</strong> </body>', 'Attach with HTML type',
                  allure.attachment_type.HTML)
    # 添加一个html附件
    allure.attach.file('./report.html', attachment_type=allure.attachment_type.HTML)
    # 添加一个图片附件
    allure.attach.file('./demo.jpg', attachment_type=allure.attachment_type.JPG)
