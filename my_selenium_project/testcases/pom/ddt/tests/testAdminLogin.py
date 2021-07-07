import pytest
from selenium.webdriver.support.wait import WebDriverWait

from testcases.pom.ddt.pages.adminLoginPage import AdminLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from util import util


class TestAdminLogin(object):
    admin_login_data = [
        # ('admin', '123456', '666', '验证码不正确，请重新输入'),
        ('admin', '123456', '111', 'JPress后台'),
    ]

    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.adminLoginPage = AdminLoginPage(self.driver)
        self.adminLoginPage.goto_admin_login_page()

    # 测试管理员登录验证码错误
    # @pytest.mark.skip()
    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('username,pwd,captcha,expected', admin_login_data)
    def test_admin_login(self, username, pwd, captcha, expected):

        self.adminLoginPage.input_username(username)
        self.adminLoginPage.input_pwd(pwd)
        if captcha != '666':
            captcha = util.get_code(self.driver, 'captchaImg')
        self.adminLoginPage.input_captcha(captcha)
        self.adminLoginPage.click_admin_login_btn()

        if captcha != '666':
            WebDriverWait(self.driver, 5).until(EC.title_is(expected))
            assert expected == self.driver.title
        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            assert alert.text == expected
            alert.accept()

            sleep(5)


if __name__ == '__main__':
    pytest.main(['testAdminLogin.py'])
