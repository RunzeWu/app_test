#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/20 12:47
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :myLemon_page_locator.py
# Software  :PyCharm Community Edition
from appium.webdriver.common.mobileby import MobileBy

class MyLemonLocator:
    my_lemon_avatar_locator = (MobileBy.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")
    image_button_locator = (MobileBy.CLASS_NAME, "android.widget.ImageButton")