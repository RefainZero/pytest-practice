# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 11:01
# @Author  : longrong.lang
# @FileName: test_pytestini.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
import pytest


@pytest.mark.xfail()
def test_case():
    assert 1 == 1
