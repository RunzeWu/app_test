#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
from appium.webdriver.common.mobileby import MobileBy

class IndexPageLocator:
    index_locator = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("主页")')
    tk_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("题库")')
    mylemon_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的柠檬")')
