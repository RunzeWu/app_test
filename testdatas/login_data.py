#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/4/26 13:57
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : login_data.py
# @Software : PyCharm

wrong_login = [{'mobile': '17751810778', 'pwd': '810778', 'expected': '错误的账号信息'},
               {'mobile': '17751810779', 'pwd': '', 'expected': '手机号码或密码不能为空'},
               {'mobile': 'adassadd', 'pwd': 'dasdas', 'expected': '手机号码格式不正确'},
               {'mobile': '17751810779', 'pwd': '156', 'expected': '密码格式不正确'}]

correct_login = {'mobile': '17751810779', 'pwd': '810779', 'expected': '夜雨身烦'}
