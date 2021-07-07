from testcases import testcase1, testcase2
from util import util
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister
# from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_category import TestCategory
from testcases.basic.test_article import TestArticle
import unittest
import os
from libs.HTMLTestRunner import HTMLTestRunner
from testcases.unittest.test import *

if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    path = os.path.dirname(os.path.dirname(__file__)) + '/reports/ExampleReport.html'
    print(path)

    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTest))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
