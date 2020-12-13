# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 19:37
# @Author  : longrong.lang
# @FileName: test_assert.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


def f():
    return 5;


def test_f():
    n = f()
    assert n % 3 == 0, "判断n 是否能被3整除，当前 n 的值为：%s" % n


# 异常断言
def test_zero_division():
    with pytest.raises(ZeroDivisionError) as exceptionInfo:
        100 / 0
    # 断言异常类型
    assert exceptionInfo.type == ZeroDivisionError
    # 断言异常的值
    assert "division by zero" in str(exceptionInfo.value)


# match的使用
def test_zero_division_match():
    with pytest.raises(ZeroDivisionError, match=".*zero.*") as exceptionInfo:
        100 / 0
    # 也可以这样
    with pytest.raises(ZeroDivisionError, match="zero") as exceptionInfo:
        100 / 0


# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0
