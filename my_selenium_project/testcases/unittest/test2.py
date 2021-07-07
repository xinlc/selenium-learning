import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('每次都运行：setUp')

    # 类共享的fixture，在整个测试类执行过程中仅仅执行一次，需加装饰器@classmethod
    @classmethod
    def setUpClass(cls) -> None:
        print('运行一次：setUpClass')

    def test1(self):
        print('test1')
        self.assertEqual(1, 1)
        self.assertIn(1, [1, 2, 3])

    def test2(self):
        print('test2')
        self.assertLess(1, 2)
        self.assertGreater(2, 1)

    def tearDown(self) -> None:
        print('每次都运行：tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('运行一次：tearDownClass')


if __name__ == '__main__':
    unittest.main()
