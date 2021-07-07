from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from libs.HTMLTestRunner import HTMLTestRunner
from util import util

import unittest


class TestUserRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/user/register')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://localhost:8080/jpress/user/register')
    #     self.driver.maximize_window()

    # 测试登录验证码错误
    def test1_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # assert alert.text == expected
        self.assertEqual(alert.text, expected)
        alert.accept()
        sleep(5)

    # 测试成功
    def test2_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        username_elem = self.driver.find_element_by_name('username')
        username_elem.clear()
        username_elem.send_keys(username)

        # email
        email_elem = self.driver.find_element_by_name('email')
        email_elem.clear()
        email_elem.send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证
        # assert alert.text == expected
        self.assertEqual(alert.text, expected)
        alert.accept()

    def runTest(self):
        self.test1_register_code_error()
        self.test2_register_ok()


if __name__ == '__main__':
    suite = unittest.TestSuite()

    # 方法一： 通过测试用例类进行加载
    suite.addTest(TestUserRegister("test2_register_ok"))

    fp = open(r"./result.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="test register", description="用例执行情况")
    runner.run(suite)
    runner.generateReport()
    fp.close()
    # unittest.main()
