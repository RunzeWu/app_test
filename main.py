#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/8 22:45
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :main.py
# Software  :PyCharm Community Edition
import pytest
from common.contants import allure
# from appium import webdriver
# from desired_caps.get_desired_caps import desired_caps
# from pages.page_objects.index_page import IndexPage
from pages.page_objects.my_lemon_page import MyLemonPage
from pages.page_objects.setting_page import SettingPage
from pages.page_objects.login_page import LoginPage
# from pages.page_objects.tiku_page import TikuPage
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# index_page = IndexPage(driver)

# index_page.switch_mylemon()
# my_lemon_page = MyLemonPage(driver)
# my_lemon_page.click_icon()
# setting_page = SettingPage(driver)
# setting_page.click_logout()
# setting_page.click_confirm_button()
# my_lemon_page.click_my_lemon_avatar()
# login_page = LoginPage(driver)
# login_page.input_mobile("17751810779")
# login_page.input_pwd("810779")
# login_page.click_login_button()
#
# index_page.switch_tiku()
# tiku_page = TikuPage(driver)
# tiku_page.select_tiku_type()
# tiku_page.select_topic_level_by_name()
# tiku_page.select_topic_suite()
if __name__ == '__main__':
    pytest.main(['-m run','--alluredir='+allure])