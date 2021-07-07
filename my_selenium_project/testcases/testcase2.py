"""
解决验证码问题-方案一：使用pytesseract和Pillow实现验证码识别
"""

import time

from selenium import webdriver
from PIL import Image
import pytesseract


def test1():
    # 打开谷歌浏览器
    browser = webdriver.Chrome()
    # 打开首页
    browser.get("http://localhost:8080/jpress/user/register")
    browser.maximize_window()

    # 获取验证码图片
    t = time.time()
    picture_name1 = str(t) + '.png'
    browser.save_screenshot(picture_name1)

    ce = browser.find_element_by_id("captchaimg")
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    # 抠图
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = str(t) + '.png'

    img.save(picture_name2)  # 这里就是截取到的验证码图片
    browser.close()


def test2():
    image1 = Image.open('test.jpg')
    str = pytesseract.image_to_string(image1)
    print(str)
