"""
pytest参数化处理：使用参数化装饰器、解析列表、元组、字典等数据
"""

import pytest

# 列表
data = ['123', '456']


@pytest.mark.parametrize('pwd', data)
def test1(pwd):
    print(pwd)


# 元组

data2 = [
    (1, 2, 3),  # 或者[1, 2,3]
    (4, 5, 6)  # 或者[4, 5,6]
]


@pytest.mark.parametrize('a, b, c', data2)
def test2(a, b, c):
    print(a, b, c)


# 字典

data3 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'user': 3,
        'pwd': 4
    }
)


@pytest.mark.parametrize('dic', data3)
def test3(dic):
    print(dic)


data_1 = [
    pytest.param(1, 2, 3, id="(a+b):pass"),  # id的值可以自定义， 只要方便理解每个用例是干什么的即可
    pytest.param(4, 5, 10, id="(a+b):fail")
]


def add(a, b):
    return a + b


class TestParametrize(object):

    @pytest.mark.parametrize('a, b, expect', data_1)
    def test_parametrize_1(self, a, b, expect):
        assert add(a, b) == expect


if __name__ == '__main__':
    pytest.main(['-sv', 'test3.py'])
