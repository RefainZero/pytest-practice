# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 20:36
# @Author  : longrong.lang
# @FileName: test_retry.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
from collections import Counter
import random
import pytest


@pytest.mark.flaky(reruns=5,reruns_delay=2)
def test_retry1():
    n = random.randint(0, 9)
    print(f"\n 输出随机数： {n} ")
    assert n == 2


@pytest.mark.flaky(reruns=5)
def test_retry2():
    assert random.choice([True, False, False])

