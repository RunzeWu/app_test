#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pages.page_locators.index_page_locator import IndexPageLocator as il

class IndexPage(BasePage):

    def switch_tiku(self):
        # 等待
        self.wait_eleVisible(locator=il.tk_locator,model_name="index_page").click()

    def switch_mylemon(self):
        self.wait_eleVisible(locator=il.mylemon_locator,model_name="index_page").click()

