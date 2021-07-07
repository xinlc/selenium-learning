# from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, text, *loc):
        self.get_element(*loc).send_keys(text)

    def click(self, *loc):
        self.driver.find_element(*loc).click()

    def get_title(self):
        return self.driver.title


class BaiduPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        driver.get('http:/www.baidu.com')

    def test_search(self):
        loc = (By.ID, 'kw')
        loc2 = (By.ID, 'su')
        self.input_text('selenium', *loc)
        self.click(*loc2)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    baiduPage = BaiduPage(driver)
    baiduPage.test_search()
