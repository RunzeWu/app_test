#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: demo
# Author: 简
# Time: 2019/4/8

# 读取yaml文件的数据，并转换成python对象
# 1、打开yaml文件
# 2、使用yaml的load()函数
from ommon.dir_config import caps_dir
import os

import yaml
fs = open(os.path.join(caps_dir,"demo.yaml"))
res = yaml.load(fs)
print(res)c