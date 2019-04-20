#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/4/14 22:54
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :__init__.py
# Software  :PyCharm Community Edition
import os
import time

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"testdatas")

testcases_dir =  os.path.join(base_dir,"testcases")

htmlreport_dir =  os.path.join(base_dir,"outputs/reports")

logs_dir =  os.path.join(base_dir,"outputs/logs")

allure = os.path.join(base_dir, "allure")

screenshot_dir = os.path.join(base_dir,"outputs/screenshots")
file_name = time.strftime('%Y%m%d%H%M%S')
screenshot_img = os.path.join(screenshot_dir, file_name + ".png'")

#caps
caps_dir = os.path.join(base_dir,"desired_caps")

log = os.path.join(logs_dir,time.strftime('%Y-%m-%d')+".log")

conf_dir = os.path.join(base_dir,"conf")

global_conf = os.path.join(conf_dir,"global.conf")

test_env_conf = os.path.join(conf_dir,"test_env.conf")

prod_env_conf = os.path.join(conf_dir,"prod_env.conf")
