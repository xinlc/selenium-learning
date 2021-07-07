import unittest
from testcases.pom.ddt.pages.searchPage import SearchPage
from selenium import webdriver
from time import sleep


class TestSearchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.searchPage = SearchPage(cls.driver)

    def testSearch(self):
        self.searchPage.goto_baidu_home()
        self.searchPage.input_kw()
        self.searchPage.click_search_btn()
        sleep(2)
        title = self.searchPage.get_title()
        assert_title = 'selenium_百度搜索'
        self.assertEqual(title, assert_title)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
