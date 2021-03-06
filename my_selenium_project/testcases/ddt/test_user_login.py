from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import pytest


class TestUserLogin(object):
    login_data = [
        ('', '123456', '账号不能为空'),
        ('admin', '123456', '用户中心'),
    ]

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    # 测试用户登录
    @pytest.mark.parametrize('username, pwd, expected', login_data)
    def test_user_login(self, username, pwd, expected):

        # 输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_class_name('btn').click()

        # 等待提示框
        if username == '':
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            sleep(3)
            # 验证
            assert alert.text == expected
            alert.accept()
        else:
            # 等待提示框
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            sleep(3)
            # 验证
            assert self.driver.title == expected
            self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_user_login.py'])
