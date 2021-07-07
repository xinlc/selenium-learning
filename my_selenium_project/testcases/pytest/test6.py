"""
pytestallure生成测试报告

pip install allure-pytest
"""
import allure
import pytest


@pytest.fixture(scope="session")
def login():
    print("用例先登录")


@allure.step("步骤1:点xxx")
def step_1():
    print("111")


@allure.step("步骤2:点xxx")
def step_2():
    print("222")


@allure.feature("编辑页面")
class TestEditPage():
    '''编辑页面'''

    @allure.story("这是一个xxx的用例")
    def test_1(self, login):
        '''用例描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")

    @allure.story("打开a页面")
    def test_2(self, login):
        '''用例描述：先登录，再去执行yyy'''
        print("yyy")


if __name__ == '__main__':
    # 注意生成测试报告 必须在命令行执行

    # pytest --alluredir reports testcase/pytest/test6.py
    # allure serve reports
    pytest.main(['--alluredir', './report', '05 pytest allure生成测试报告.py'])
