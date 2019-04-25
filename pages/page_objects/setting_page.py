#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/23 22:32
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :setting_page.py
# Software  :PyCharm Community Edition
from pages.basepage import BasePage
from pages.page_locators.setting_page_locator import SettingPageLocator as cl

class SettingPage(BasePage):

    def click_logout(self):
        return self.click_element(locator=cl.logout_button_locator,model_name="SettingPage")

    def click_confirm_button(self):
        return self.click_element(locator=cl.confirm_locator,model_name="SettingPage")