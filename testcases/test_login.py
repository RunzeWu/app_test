#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 10:12
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_login.py
# @Software : PyCharm
import pytest
from pages.page_objects.login_page import LoginPage
# from pages.page_objects.index_page import IndexPage
from testdatas.login_data import correct_login,wrong_login
from common.mylog import get_logger
from testcases.conftest import is_login

logger = get_logger('test_login')


@pytest.mark.usefixtures("start_app")
@pytest.mark.usefixtures("login_env")
@pytest.mark.run
class TestLogin:

    @pytest.mark.login
    @pytest.mark.parametrize("value", wrong_login)
    def test_wrong_login(self, value, login_env):

        '''
        前提条件：打开App，保证未登录
        后置条件：退出登录
        :return:
        '''
        mobile = value['mobile']
        pwd = value['pwd']
        msg = value['expected']
        driver = login_env
        login_page = LoginPage(driver)
        login_page.login(mobile, pwd)

        try:
            actual = login_page.get_toast_msg(msg)
            logger.info('获取toast:{}成功'.format(actual))
        except:
            logger.error('Failed, 没有获取到toast')
            raise

    @pytest.mark.login
    def test_correct_login(self, login_env):
        mobile = correct_login['mobile']
        pwd = correct_login['pwd']
        # msg = correct_login['expected']
        driver = login_env
        login_page = LoginPage(driver)
        # index_page = IndexPage(driver)
        login_page.login(mobile, pwd)
        try:
            flag = is_login(driver)
            if flag:
                logger.info('登录成功')
            else:
                logger.error('FAILED! 登录失败')
        except:
            logger.error('FAILED! 登录失败')
            raise

if __name__ == '__main__':
    pytest.main('-m login')