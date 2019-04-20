#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/20 12:59
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :setting_page_locator.py
# Software  :PyCharm Community Edition
from appium.webdriver.common.mobileby import MobileBy

class SettingPageLocator:

    logout_button_locator = (MobileBy.ID,"com.lemon.lemonban:id/logout_button")

    confirm_locator = (MobileBy.ID, "com.lemon.lemonban:id/tv_sure")

    cancle_locator = (MobileBy.ID, "com.lemon.lemonban:id/tv_cancel")