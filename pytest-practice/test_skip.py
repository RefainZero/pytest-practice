# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 20:30
# @Author  : longrong.lang
# @FileName: test_skip.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import sys

import pytest

if sys.platform.startswith("win"):
    pytest.skip("当 allow_module_level=True 时，可以设置在模块级别跳过整个模块",allow_module_level=True)


@pytest.fixture(autouse=True)
def dataTable():
    print("数据初始化成功")


def test_case1():
    print("我是用例1")



# 标记在函数上
@pytest.mark.skip(reason="标记在函数上，被标记函数不会被执行！！")
def test_case2():
    print("我是测试用例2，但我不会执行")


class TestClass1(object):

    def test_case3(self):
        print("我是用例3")

    # 标记在类中的函数上
    @pytest.mark.skip(reason="标记在类中的函数上，同样也不会执行哦！")
    def test_case4(self):
        print("我是测试用例4，但我不会执行")


@pytest.mark.skip(reason="标记在类上，整个类及类中的方法都不会执行！")
class TestClass2(object):
    def test_case5(self):
        print("我是用例5")


def test_case6():
    for i in range(50):
        print(f"输出第 【{i}】个数")
        if i == 3:
            pytest.skip("我跑不动了，不输出了")
希望有条件地跳过某些测试用例
@pytest.mark.skip(sys.platform.startswith("win"),reason="windows系统不执行哦")
def test_case7():
    print("我是用例7")
skip = pytest.mark.skip("skip的标记变量，标记的函数或类不执行")
skipif = pytest.mark.skipif("skipif的标记变量，标记的函数或类不执行")


@skip
def test_case8():
    print("测试用例8")


class TestClass(object):
    @skipif
    def test_case9(self):
        print("测试用例9")
importskip = pytest.importorskip("importskip", minversion="0.3",reason="此处是导入失败，跳过的测试")


@importskip
def test_10():
    print('测试用例10')
