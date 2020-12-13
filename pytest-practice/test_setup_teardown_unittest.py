# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 20:09
# @Author  : longrong.lang
# @FileName: test_setup_teardown_unittest.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
unittest代码示例
'''
import unittest


class TestUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前执行")

    def setUp(self):
        print("每个用例开始前执行")

    def tearDown(self):
        print("每个用例结束后执行")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行后执行")

    def testA(self):
        '''用例A'''
        print("用例A执行了")
        self.assertEquals(1, 1)

    def testB(self):
        '''用例B'''
        print("用例B执行了")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
