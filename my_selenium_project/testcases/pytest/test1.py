import pytest


# 不会执行，不符合命名规则
def add():
    assert (1 + 2) == 3


def test_sub():
    assert 2 - 1 == 1


class TestRegister(object):
    def test_register(self):
        assert len('admin') == 5


if __name__ == '__main__':
    # 默认会递归寻找当前目录所有已 test开头或结尾的文件内的所有已 test开头或结尾的方法执行
    # pytest.main(['-s', '-v', '01-pytest简介.py::test_sub'])
    # :: 标记显示执行函数名词，经过我测试用命令行是好用的，pytest -vs test1.py::test_sub
    pytest.main(['-s', '-v', 'test1.py::TestRegister::test_register'])
