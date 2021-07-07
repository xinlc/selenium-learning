from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util
import unittest
import pytest


class TestAdminLogin(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    admin_login_data = [
        # ('admin', '123456', '666', '验证码不正确，请重新输入'),
        ('admin', '123456', '111', 'JPress后台'),
    ]

    # 测试管理员登录
    # @pytest.mark.skip()
    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', admin_login_data)
    def test_admin_login(self, username, pwd, captcha, expected):
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('captcha').clear()
        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        if captcha != '666':
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            assert expected == self.driver.title
        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            assert alert.text == expected
            alert.accept()

            sleep(5)

        # self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_admin_login.py'])
