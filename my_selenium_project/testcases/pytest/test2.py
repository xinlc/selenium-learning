"""
pytest标记：查找测试策略、标记测试函数
"""

import pytest


@pytest.mark.do
def test1():
    print('test1')


@pytest.mark.do
def test2():
    print('test2')


@pytest.mark.undo
def test3():
    print('test3')


@pytest.mark.undo
def test4():
    print('test4')


if __name__ == '__main__':
    pytest.main(['-s', '-m', 'undo', 'test2.py'])
