import unittest


class LoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('准备工作')

    def test_login(self):
        username = 'tom'
        pwd = '123'
        expected = 'welcome'
        self.assertEqual(expected, 'welcome')

    def tearDown(self) -> None:
        print('还原工作')


class RegisterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('准备工作')

    def test_register(self):
        username = 'tom'
        pwd = '123'
        email = 'tom@qq.com'
        expected = 'login'
        self.assertEqual(expected, 'login')

    def tearDown(self) -> None:
        print('还原工作')


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(LoginTestCase())
    suite.addTest(RegisterTestCase())

    runner = unittest.TextTestRunner()
    runner.run(suite)
