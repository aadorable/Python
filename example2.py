#!/usr/bin/env python
# coding=utf-8

'''
从大文件中读取一个屏幕的内容，按任意键翻页，按q退出
'''

import sys,os

#内容显示函数
def PrintScreen(f):
    #行数计数器
    line_num = 0
    #循环遍历文件对象，按行输出
    for line in f:
        #输出25行结束，跳出循环
        if line_num > 25:
            break
        print line
        line_num += 1

#读取文件路径
path = sys.argv[1]
#打开文件
f = open(path, "r")
while True:
    #执行Linux系统命令，清屏
    os.system("clear")
    #输出内容
    PrintScreen(f)
    #获取用户输入
    commond = raw_input(":")
    #q键退出，其他键翻页
    if commond == 'q':
        break
f.close()
