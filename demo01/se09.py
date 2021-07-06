"""
Selenium三种等待方式：剖析原理、用法和应用场景，ajax 异步
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # sleep(2)

    # 仅适用于调试
    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2) # 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()

    # 全局隐士等待,不是很灵活
    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2) # 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()

    # 动态显示等待，等待到能拿到指定数据就结束等待，最常用
    def test_wait(self):
        wait = WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2) # 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()
