#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
from pages.basepage import BasePage

class IndexPage(BasePage):

    def switch_nav(self,nav_name):
        ele_loc = 'new UiSelector().text("{}")'.format(nav_name)
        # 等待
        # self.click_element()
        pass

