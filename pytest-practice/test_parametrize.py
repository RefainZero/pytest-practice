# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 15:00
# @Author  : longrong.lang
# @FileName: test_parametrize.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


# 一个参数一个值
@pytest.mark.parametrize("input", ["输入值"])
def test_case1(input):
    print("\n" + input)
    assert input == "输入值"


@pytest.mark.parametrize("input", ["输入值1", "输入值2", "输入值3", "输入值4", "输入值5"])
def test_case2(input):
    print("\n" + input)
    assert '输入值' in input


@pytest.mark.parametrize("user,pwd",
                         [("xiaoqiang", "123456"), ("rose", "123456"),
                          pytest.param("jone", "123456", marks=pytest.mark.xfail),
                          pytest.param("Alex", "123456", marks=pytest.mark.skip)])
def test_login(user, pwd):
    print(user + " : " + pwd)
    assert user == "rose"


data1 = [1, 2]
data2 = ["python", "java"]
data3 = ["软", "件", "测", "试", "君"]


@pytest.mark.parametrize("a", data1)
@pytest.mark.parametrize("b", data2)
@pytest.mark.parametrize("c", data3)
def test_case3(a, b, c):
    print(f"生成新的数据组合为:[{a} {b} {c}]")


json = ({"username": "alex", "password": "123456"}, {"username": "rongrong", "password": "123456"})


@pytest.mark.parametrize('json', json)
def test_parametrize_1(json):
    print(f'字典为\n{json}')
    print(f'username : {json["username"]}, password : {json["password"]}')
