#!/usr/bin/env python
# coding=utf-8

'''
批量修改文件名
'''

import os,sys,time

#os.chdir("./") 切换工作路径到指定目录
os.chdir("./data")
#time.strftime 转换时间戳为字符串
#time.localtime() 获取当前时间
data = time.strftime("%Y%m%d", time.localtime())

for filename in os.listdir("./"):
    if filename.startswith("dict"):
        #os.rename(oldname, newname) 重命名文件，两个参数
        os.rename(filename, filename + '.' + data)
