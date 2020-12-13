# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 16:03
# @Author  : longrong.lang
# @FileName: test_tempdir.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''生成唯一临时文件夹'''


class TestTempDir:
    def test_tempdir(self, tmpdir):
        print('\n', tmpdir)
