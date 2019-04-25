#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
import random

from appium.webdriver.common.touch_action import TouchAction

from pages.page_locators.tiku_page_locator import TiKuPageLocator as tl
from pages.basepage import BasePage


class TikuPage(BasePage):

    # 随机选一个题库类型，然后点进去 == 随机、选第1个，选最后1个
    def select_tiku_type(self):
        # 获取所有的题库类型 - 翻页。需要获取每个页面的题库类型
        new = self.driver.page_source
        tiku_titles = []
        old = ''
        while old != new:
            for ele in self.get_elements(tl.titles_locator, model_name="tiku"):
                tiku_titles.append(ele.text)
            old = new
            self.swipe_up_down()
            new = self.driver.page_source
        # 放在一大的列表当中，去重。
        tiku_titles = list(set(tiku_titles))
        # 再随机选取题库类型名字，然后再去操作。
        random_tiku = tiku_titles[random.randint(0,len(tiku_titles)-1)]
        self.scroll_list_to_top()
        return self.scroll_find(random_tiku).click()


    # 选择题目等级：初中高
    def select_topic_level_by_name(self):
        random_number = random.randint(0,2)
        if random_number == 0:
            return self.get_element(tl.first_level_button_locator,model_name="tikuPage").click()
        elif random_number == 1:
            return self.get_element(tl.second_level_button_locator, model_name="tikuPage").click()
        else:
            return self.get_element(tl.third_level_button_locator,model_name="tikuPage").click()


    # 选择题目套题？如何选？随机、选第1个，选最后1个
    def select_topic_suite(self):
        '''
        准备改用 press方法执行
        :return:
        '''
        # return self.click_element(tl.timu_locator,model_name="tikuPage")
        lockview_size = self.driver.get_window_size()
        loc_height = lockview_size["height"]
        loc_width = lockview_size["width"]
        tc = TouchAction(self.driver)
        tc.press(x=loc_width*0.5, y=loc_height*0.15).wait(200).release().perform()


    # 收藏 开关
    def switch_favirate(self,aciton="False"):
        pass

    # 题目 开关
    def switch_answer(self,action="False"):
        pass

    def find_login_ele(self):
        source = self.driver.page_source
        if "去登录" in source:
            return True
        else:
            return False

    def go_login_page(self):
        return self.click_element(tl.go_login_locator)
