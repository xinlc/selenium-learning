import unittest


class MyTest1(unittest.TestCase):
    def test1(self):
        print('test1')

    # 跳过
    @unittest.skip
    def test2(self):
        print('test2')


class MyTest2(unittest.TestCase):
    def test2(self):
        print('test2')


if __name__ == '__main__':
    # 实例化
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # 方法一： 通过测试用例类进行加载
    suite.addTest(loader.loadTestsFromTestCase(MyTest1))
    suite.addTest(loader.loadTestsFromTestCase(MyTest2))

    # 方法二： 通过测试用例模板去加载
    # suite.addTest(loader.loadTestsFromModule(MyTest1))
    # suite.addTest(loader.loadTestsFromModule(MyTest2))

    # 方法三：通过路径加载
    # import os
    # path = os.path.dirname(os.path.abspath(__file__))
    # suite.addTest(loader.discover(path))

    # 方法四：逐条加载测试用例 low

    # case1 = MyTest1("test1")
    # case2 = MyTest1("test2")
    #
    # suite.addTest(case1)
    # suite.addTest(case2)

    # 运行
    runner = unittest.TextTestRunner()
    runner.run(suite)
