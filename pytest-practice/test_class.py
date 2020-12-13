"""
将多个测试用例放到一个类中执行
"""


class TestClass(object):
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 'h' in "hello"