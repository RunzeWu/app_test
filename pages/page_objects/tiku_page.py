#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: tiku_page
# Author: 简
# Time: 2019/4/3

from pages.basepage import BasePage
class TikuPage(BasePage):

    # 随机选一个题库类型，然后点进去 == 随机、选第1个，选最后1个
    def select_tiku_type(self):
        # 获取所有的题库类型 - 翻页。需要获取每个页面的题库类型
        # 放在一大的列表当中，去重。
        # 再随机选取题库类型名字，然后再去操作。
        pass

    # 选择题目等级：初中高
    def select_topic_level_by_name(self,level_name):
        pass

    # 选择题目套题？如何选？随机、选第1个，选最后1个
    def select_topic_suite(self):
        pass

    # 收藏 开关
    def switch_favirate(self,aciton="False"):
        pass

    # 题目 开关
    def switch_answer(self,action="False"):
        pass

    # 拉动题目