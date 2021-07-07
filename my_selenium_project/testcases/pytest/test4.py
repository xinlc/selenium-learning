
"""
pytestFixture：使用fixture实现用例之间的调用
"""
import pytest


# 不能已test开头
@pytest.fixture()
def init():
    print('init...')
    return 1


def test1(init):
    print('test1')


def test2(init):
    print('test2')


if __name__ == '__main__':
    pytest.main(['-s', '04 pytest Fixture.py'])
