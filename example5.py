#!/usr/bin/env python
# coding=utf-8

'''
实现ls命令 显示当前路径下的内容
'''

import os,sys

path = sys.argv[1]

for filenames in os.listdir(path):
    print filenames
