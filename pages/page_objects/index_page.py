#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: index_page
# Author: 简
# Time: 2019/4/3
from pages.basepage import BasePage

class IndexPage(BasePage):

    def switch_nav(self,nav_name):
        ele_loc = 'new UiSelector().text("{}")'.format(nav_name)
        # 等待
        # self.click_element()
        pass

