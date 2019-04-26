#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
from pages.basepage import BasePage
from pages.page_locators.login_page_locator import LoginPageLocator as ll

class LoginPage(BasePage):

    # 点击用户输入框
    def click_mobile_element(self):
        return self.click_element(locator=ll.login_input_locator,model_name="LoginPage")

    # 点击密码输入框
    def click_pwd_ele(self):
        return self.click_element(locator=ll.pwd_input_locator, model_name="LoginPage")

    # 输入用户名
    def input_mobile(self,value):
        self.clear_input(locator=ll.login_input_locator, model_name="LoginPage")
        return self.input_text(locator=ll.login_input_locator,value=value,model_name="LoginPage")

    # 输入密码
    def input_pwd(self,value):
        self.clear_input(locator=ll.pwd_input_locator, model_name="LoginPage")
        return self.input_text(locator=ll.pwd_input_locator,value=value,model_name="LoginPage")

    # 点击登录按钮
    def click_login_button(self):
        return self.click_element(ll.login_button_locator,model_name="LoginPage")

    def get_empty_toast_msg(self):
        return self.get_toast_msg("手机号码或密码不能为空")

    def get_wrong_mobile_toast_msg(self):
        return self.get_toast_msg("手机号码格式不正确")

    def get_wrong_pwd_toast_msg(self):
        return self.get_toast_msg("密码格式不正确")

    def get_wrong_login_toast_msg(self):
        return self.get_toast_msg("错误的账号信息")

    def login(self, mobile, pwd):
        self.click_mobile_element()
        self.input_mobile(mobile)
        self.click_pwd_ele()
        self.input_pwd(pwd)
        self.click_login_button()



