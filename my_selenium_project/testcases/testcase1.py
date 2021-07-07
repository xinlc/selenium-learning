"""
PyAutoGUI 是一个图形用户界面自动化工具，通过屏幕XY坐标系统确定目标位置，控制鼠标和键盘发送虚拟点击和鼠标点击，完成点击按钮、填写表单等操作。

如遇到 selenium 无法点击操作可以考虑用 PyAutoGUI 实现，或找到元素后用JS代码实现。
"""
from selenium import webdriver
from time import sleep
import pyautogui


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    driver.maximize_window()
    sleep(1)
    elem = driver.find_element_by_id('agree')
    rect = elem.rect
    pyautogui.click(rect['x'] + 10, rect['y'] + 130)
    # pyautogui.click()

    sleep(3)

    # elem.click()
