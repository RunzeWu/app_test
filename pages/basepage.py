#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/8 22:46
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :basepage.py
# Software  :PyCharm Community Edition
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.dir_config import screenshot_dir
import logging
import time
from appium.webdriver.common.mobileby import MobileBy

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,model_name="model"):
        logging.info("等待元素可见：{}".format(locator))
        try:
            #获取开始等待的时间
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            #获取结束等待的时间
            #获取等待的总时长 - 以秒为单位
            logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        except:
            #写进日志
            logging.exception("等待元素可见超时。")
            #截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise


    #查找元素
    def get_element(self,locator,model_name="model"):
        logging.info("查找模块：{}下的元素：{}".format(model_name,locator))
        try:
            ele =  self.driver.find_element(*locator)
            logging.info("查元素成功。")
            return ele
        except:
            # 写进日志
            logging.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise


    #点击元素
    def click_element(self,locator,model_name="model"):
        #元素查找
        ele = self.get_element(locator,model_name)
        #元素操作
        logging.info("点击操作：模块 {} 下的元素 {}".format(model_name,locator))
        try:
            ele.click()
        except:
            # 写进日志
            logging.exception("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #输入内容
    def input_text(self,locator,value,model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("输入操作：模块 {} 下的元素 {}输入文本 {}".format(model_name, locator,value))
        try:
            ele.send_keys(value)
        except:
            # 写进日志
            logging.exception("元素输入操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            logging.exception("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #获取元素的文本内容
    def get_element_text(self,locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素文本值：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写进日志
            logging.exception("获取元素文本值失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise


    def save_webImg(self,model_name):
        #文件名称=模块名称_当前时间.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截图成功，文件路径为：{}".format(filePath))
        except:
            logging.exception("截图失败！！")

    # 获取设备大小
    def get_device_size(self):
        try:
            return self.driver.get_window_size()
        except:
            pass

    # 滑屏操作 - 左右、上下
    # 左右
    def swipe_left_right(self,start_per=0.9,end_per=0.1):
        size = self.get_device_size()
        self.driver.swipe(size["widht"]*start_per,size["height"]*0.5,size["widht"]*end_per,size["height"]*0.5,200)
        time.sleep(0.5)

    # 上下滑动
    def swipe_up_down(self,start_per=0.9,end_per=0.1):
        size = self.get_device_size()
        self.driver.swipe(size["widht"] * 0.5, size["height"] * start_per, size["widht"] *0.5 ,size["height"] * end_per, 200)
        time.sleep(0.5)

    # 列表滑动 === 页面内容太多，需要翻页才能看到其它的内容。  找其它页面的内容
    def scroll_list(self,str_obj=None):
        if str_obj is not None:
            # 查找。
            pass
        pass

    # toast获取
    def get_toast_msg(self,text):
        # xpath表达式 -- 文本匹配去获取
        ele_loc = '//*[contains(@text,"{}")]'.format(text)
        # uiautomator2
        # 等待元素存在，而不是元素可见。
        WebDriverWait(self.driver,10,0.01).until(EC.presence_of_element_located((MobileBy.XPATH,ele_loc)))
        return self.get_element((MobileBy.XPATH,ele_loc))


    # h5切换

    def hide_keyboard(self):
        pass




