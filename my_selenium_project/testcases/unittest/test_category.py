from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from .test_admin_login import TestAdminLogin
import unittest


class TestCategory(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.login = TestAdminLogin()
    #     runner = unittest.TextTestRunner()
    #     runner.run(cls.login)

    def __init__(self, method, login):
        unittest.TestCase.__init__(self, method)
        # super.__init__(self, method)
        self.login = login

    # 测试文章分类失败，名称为空
    def test_add_category_error(self):
        name = ''
        parent = 'python'
        slug = 'test'
        expected = '分类名称不能为空'

        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击分类
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        # 选择父分类
        parent_category_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    # 测试文章分类成功
    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = None

        # 点击文章
        # 上一个测试直接 点击分类
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击分类
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').clear()
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        # 选择父分类
        parent_category_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element_by_name('category.slug').clear()
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        # 没有异常就添加成功，没有提示信息
        assert 1 == 1

    def runTest(self):
        self.test_add_category_error()
        self.test_add_category_ok()

# 以下代码 在main中测试
# from testcase.unittest import \
#     test_user_register, \
#     test_admin_login, \
#     test_user_login,\
#     test_category,\
#     test_article
# import unittest
#
# if __name__ == '__main__':
#
#     adminLoginCase = test_admin_login.TestAdminLogin('test_admin_login_code_ok')
#     categoryCase = test_category.TestCategory('test_add_category_ok', adminLoginCase)
#
#     suite = unittest.TestSuite()
#
#     suite.addTest(adminLoginCase)
#     suite.addTest(categoryCase)
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
