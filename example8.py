#!/usr/bin/env python
# coding=utf-8

'''
按照文件后缀的时间戳，删除3天之前的文件
'''

import os
from datetime import datetime

#删除函数
def CheckRemove(file_name):
    #获取当前时间 = time.localtime()
    current_date = datetime.datetime.now()
    #splitext 分隔文件后缀 .20170717
    _, file_date_str = os.path.splitext(file_name)
    #datetime.strftime 把时间戳转化为指定格式字符串
    #datetime.strptime 把字符串转化为时间戳
    file_date = datetime.datetime.strptime(file_date_str[1:], '%Y%m%d')
    #时间戳.days() 按转化
    if (current_date - file_date).days >= 3:
        print 'remove file:' + file_name
        #删除文件
        os.remove(file_name)

path = './data/'
os.chdir(path)
[CheckRemove(file_name) for file_name in os.listdir('./') if file_name.startswith('dict')]

