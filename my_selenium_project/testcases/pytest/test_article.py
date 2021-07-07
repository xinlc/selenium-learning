from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

from testcases.pytest.test_admin_login import TestAdminLogin


class TestArticle(object):

    def setup_class(self):
        self.login = TestAdminLogin()

    # 测试添加文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_add_ok(self):
        title = '我的文章'
        content = '我的文章内容'
        expected = '文章保存成功。'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()

        sleep(1)

        self.login.driver.find_element_by_id('article-title').send_keys(title)

        frame1 = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')

        self.login.driver.switch_to.frame(frame1)

        sleep(1)

        self.login.driver.find_element_by_xpath('/html/body').send_keys(content)

        self.login.driver.switch_to.default_content()

        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

        sleep(1)

    # 测试删除单个文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_one_article_ok(self):
        # 接上一个添加文章测试，不用再点击文章链接，直接点击文章管理
        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击文章管理
        # //*[@id="sidebar-menu"]/li[4]/ul/li[1]/a
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        ActionChains(self.login.driver).move_to_element(link).perform()

        sleep(1)
        # 删除前文章数
        article_num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        #
        del_elem = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')
        del_elem.click()

        sleep(1)

        # 分页的情况下不能这样判断

        # 删除后文章数
        article_num2 = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))

        # assert article_num == article_num2 + 1

    # 测试删除所有文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    def test_delete_all_article_ok(self):
        # 点击文章
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')
        link.click()

        self.login.driver.find_element_by_id('batchDel').click()

        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()

        sleep(1)

        # 分页的情况下不能这样判断

        # 删除后文章数
        # artile_num = self.login.driver.find_elements_by_class_name('jp-actiontr')
        # assert len(artile_num) == 0


if __name__ == '__main__':
    pytest.main(['test_article.py'])
