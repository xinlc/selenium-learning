from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util
import unittest


class TestAdminLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/admin/login')
        cls.driver.maximize_window()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://localhost:8080/jpress/admin/login')
    #     self.driver.maximize_window()

    # 测试管理员登录验证码错误
    @unittest.skip
    def test_admin_login_code_error(self):
        username = 'admin'
        pwd = '123456'
        captcha = '666'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()

        sleep(5)

        # self.driver.quit()

    # 测试登录成功
    def test_admin_login_code_ok(self):
        username = 'admin'
        pwd = '123456'

        expected = 'JPress后台'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        captcha = util.get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert expected == self.driver.title


if __name__ == '__main__':
    unittest.main()
