#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/26 14:47
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_tiku.py
# @Software : PyCharm
import pytest
from common.mylog import get_logger

logger = get_logger('test_tiku')


@pytest.mark.usefixtures('start_app')
@pytest.mark.usefixtures('tiku_env')
class TestTiku:

    def test_tiku(self, tiku_env):
        tiku_page = tiku_env

        try:
            tiku_page.select_tiku_type()
            tiku_page.select_topic_level_by_name()
            tiku_page.select_topic_suite()
        except:
            raise

