#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/20 13:42
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page_locator.py
# Software  :PyCharm Community Edition
from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocator:

    login_input_locator = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")

    pwd_input_locator = (MobileBy.ID, "com.lemon.lemonban:id/et_password")

    login_button_locator = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")

    empty_toast_locator = (MobileBy.XPATH, '//*[@text,"手机号码或密码不能为空")]')

    pwd_wrong_format_toast_locator = (MobileBy.XPATH, '//*[@text,"密码格式不正确")]')

    mobile_wrong_format_toast_locator = (MobileBy.XPATH, '//*[@text, "手机号码格式不正确"]')

    wrong_login_toast_locator = (MobileBy.XPATH, '//*[@text, "错误的账号信息"]')