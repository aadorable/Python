#!/usr/bin/env python
# coding=utf-8

'''
遍历一个目录
'''

import os,sys

path = sys.argv[1]

#os.walk() 递归遍历一个目录，返回的是一个三元组
#(当前遍历目录，当前目录下的子目录，当前目录下的文件)
for root,dirnames,filenames in os.walk(path):
    for filename in filenames:
        print filename
