#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/2/20 20:50


import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"Outputs/Reports")

logs_dir =  os.path.join(base_dir,"Outputs/Logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/Screenshots")

#caps
caps_dir = os.path.join(base_dir,"Desired_Caps")

