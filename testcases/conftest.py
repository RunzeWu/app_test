#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 10:12
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : conftest.py
# @Software : PyCharm
import pytest
from appium import webdriver
from desired_caps.get_desired_caps import desired_caps
from pages.page_objects.index_page import IndexPage
from pages.page_objects.login_page import LoginPage
from pages.page_objects.tiku_page import TikuPage


# 根据测试用例需求，动态配置启动参数。
def basedriver(noReset=None, port=4723, **kwargs):
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if kwargs:
        # 修改从配置文件当中读取出来的desired_caps.
        for key, value in kwargs:
            desired_caps[key] = value
    # 启动appium会话 - 连接appium server  端口号
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_caps)
    return driver

# 确认用户是否已登陆。进入题库，判断是否有【去登陆】的提示。
# 如果没有，pass。如果有，就先登陆。
def is_login():
    driver = basedriver()
    index_page = IndexPage(driver)
    tiku_page = TikuPage(driver)
    index_page.switch_tiku()

    if tiku_page.find_login_ele():
        flag = False  # 未登录
    else:
        flag = True  # 已登录
    return flag

@pytest.fixture(scope="session")
def start_app_withReset():
    driver = basedriver(False)
    yield driver
    driver.close_app()
    driver.quit()

@pytest.fixture(scope="class")
def login_env():
    # 启动App后检查登录，已登录退出登录
    pass
    # 保持登录状态






