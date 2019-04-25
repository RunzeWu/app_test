#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/23 22:26
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :my_lemon_page.py
# Software  :PyCharm Community Edition
from pages.basepage import BasePage
from pages.page_locators.myLemon_page_locator import MyLemonLocator as ml

class MyLemonPage(BasePage):


    def click_my_lemon_avatar(self):
        return self.click_element(locator=ml.my_lemon_avatar_locator,model_name="MyLemonPage")

    def click_icon(self):
        return self.click_element(locator=ml.image_button_locator, model_name="MyLemonPage")
