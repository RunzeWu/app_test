#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 10:12
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_login.py
# @Software : PyCharm
import pytest
from pages.page_objects.login_page import LoginPage
from pages.page_objects.index_page import IndexPage


class TestLogin:

    def test_login(self):
        '''
        前提条件：打开App，保证未登录
        后置条件：退出登录
        :return:
        '''
        pass
