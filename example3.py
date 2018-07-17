#!/usr/bin/env python
# coding=utf-8

'''
介绍文件操作路径方法
'''

import os.path

#从路径截取文件名
print os.path.basename("/home/wu/code/test/python/example.py")

#从路径截取文件所在目录
print os.path.dirname("/home/wu/code/test/python/example.py")

#切割路径，返回文件所在目录和文件名，返回的是元组
print os.path.split("/home/wu/code/test/python/example.py")

#返回值中包含文件后缀名
print os.path.splitext("/home/wu/code/test/python/example.py")
