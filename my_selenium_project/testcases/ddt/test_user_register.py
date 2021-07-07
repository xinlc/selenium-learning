from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util

import pytest


class TestUserRegister(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    login_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确'),
        ('test200', 'test009@qq.com', '123456', '123456', '111', '注册成功，点击确定进行登录。'),
    ]

    @pytest.mark.parametrize('username,email,pwd,confirmPwd,captcha,expected', login_data)
    def test1_register(self, username, email, pwd, confirmPwd, captcha, expected):

        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        # 自动识别验证码
        if captcha != '666':
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
            assert alert.text == expected

            alert.accept()
        else:
            self.driver.find_element_by_name('captcha').clear()
            self.driver.find_element_by_name('captcha').send_keys(captcha)
            self.driver.find_element_by_class_name('btn').click()

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            assert alert.text == expected
            alert.accept()
            sleep(5)


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])
