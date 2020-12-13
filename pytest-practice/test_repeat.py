# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 8:52
# @Author  : longrong.lang
# @FileName: test_repeat.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


def test_repeat():
    import random
    num = random.randint(1, 9)
    print(f"\n输出随机数：{num}")
    assert num == 2


@pytest.mark.repeat(3)
def test_repeat2():
    print("\n 测试脚本")
