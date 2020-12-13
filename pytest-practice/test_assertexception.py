"""
使用pytest断言异常
"""
import pytest


def myfunction():
    # 使用raise在测试方法中指定异常的类型
    raise IOError("指定异常类型")
def test_myfuntion():
    # 使用 with pytest.raises（异常类型）
    with pytest.raises(SyntaxError):
        myfunction()
if __name__ == '__main__':
    pytest.main()