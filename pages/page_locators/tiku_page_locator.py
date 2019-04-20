#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/20 14:09
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :tiku_page_locator.py
# Software  :PyCharm Community Edition
from appium.webdriver.common.mobileby import MobileBy

class TiKuPageLocator:

    go_login_locator = (MobileBy.ID, "com.lemon.lemonban:id/button_go_login")

    titles_locator = (MobileBy.ID, "com.lemon.lemonban:id/fragment_category_type")

    first_level_button_locator = (MobileBy.ID, "com.lemon.lemonban:id/first_level")

    second_level_button_locator = (MobileBy.ID, "com.lemon.lemonban:id/second_level")

    third_level_button_locator = (MobileBy.ID, "com.lemon.lemonban:id/third_level")

    timu_locator = (MobileBy.ID,'android.widget.RelativeLayout')