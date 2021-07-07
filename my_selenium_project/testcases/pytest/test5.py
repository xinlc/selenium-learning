"""
pytestsetup和teardown


模块级（setup_module/teardown_module）开始与模块始末，全局的
函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
类级（setup_class/teardown_class）只在类中前后运行一次
方法级（setup_method/teardown_method）开始于方法始末（在类中）
类厘米的（setup/teardown)运行在调用方法的前后

"""
import pytest


class TestCase1(object):

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    @classmethod
    def setup_class(self):
        print('setup_class')

    @classmethod
    def teardown_class(self):
        print('teardown_class')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')


if __name__ == '__main__':
    pytest.main(['-s'])
