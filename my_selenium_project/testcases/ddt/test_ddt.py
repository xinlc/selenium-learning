import os

# 有了 pytest parametrize 后，ddt模块用的并不多了
from ddt import ddt, data, unpack, file_data
import unittest


def get_data():
    testdata = [{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}]
    return testdata


@ddt
class MyTestCase(unittest.TestCase):
    # 读取元组数据-单组元素
    @data(1, 2, 3)
    def test1(self, value):
        print(value)

    # 读取元组数据-多组元素
    @data((1, 2, 3), (4, 5, 6))
    def test2(self, value):
        print(value)

    # 读取元组数据-拆分数据
    @data((1, 2, 3), (4, 5, 6))
    @unpack  # 拆分数据
    def test3(self, value1, value2, value3):
        print(value1, value2, value3)

    # 列表
    @data([{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}])
    def test4(self, value):
        print(value)

    # 字典
    @data({'name': 'tom', 'age': '20'}, {'name': 'kite', 'age': '30'})
    def test5(self, value):
        print(value)

    # 字典-拆分
    @data({'name': 'tom', 'age': '20'}, {'name': 'kite', 'age': '30'})
    @unpack
    def test6(self, name, age):
        print(name, age)

    # 变量或者方法调用

    testdata = [{'name': 'tom', 'age': 20}, {'name': 'kite', 'age': 30}]

    # @data(*testdata)
    @data(get_data())
    def test7(self, value):
        print(value)

    # 读文件
    @file_data(os.getcwd() + '/test.json')
    def test8(self, value2):
        print(value2)


if __name__ == '__main__':
    unittest.main()
