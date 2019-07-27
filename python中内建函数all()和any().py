#!/usr/bin/env python
# coding:utf-8
"""
@Name   : python中内建函数all()和any().py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/27
"""

# any()
# 其实any函数非常简单：判断一个tuple或者list是否全为空，0，False。如果全为空，0，False，则返回False；如果不全为空，则返回True。
math, physics, computer = 70, 40, 80
if any([math < 60, physics < 60, computer < 60]):
    print("not pass!")

# all()
# all函数正好和any相反：判断一个tuple或者list是否全为不为空，0，False。如果全不为空，则返回True；否则返回False。
print(all(['a', 'b', 'c', 'd']))
