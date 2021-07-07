from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from testcases.ddt.test_admin_login import TestAdminLogin
import pytest


class TestCategory(object):

    def setup_class(self):
        self.login = TestAdminLogin()

    category_data = [
        ('', 'python', 'test', '分类名称不能为空'),
        ('test', 'python', 'test', ''),
    ]

    # 测试文章分类
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    @pytest.mark.parametrize('name,parent,slug,expected', category_data)
    def test_add_category(self, name, parent, slug, expected):

        if name == '':
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
        if name == '':
            loc = (By.CLASS_NAME, 'toast-message')
            WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
            msg = self.login.driver.find_element(*loc).text
            assert msg == expected
        else:
            assert 1 == 1
        sleep(2)


if __name__ == '__main__':
    # 这里可以跳过登录错误
    pytest.main(['test_category.py'])
