#!/usr/bin/env python
# coding=utf-8

'''
基于一个简单文本，构造一个大文本（构造测试工具）
'''

import sys
#内容输入文件路径
input_file_path = sys.argv[1]
#输出文件路径
output_file_path = sys.argv[2]
#输出文件大小
output_size = int(sys.argv[3]) * 1024 * 1024
#输出文件大小
total_size = 0
#输入行号计数器
index = 0
#打开两个文件
input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

#提取内容 list[] 每个元素是每一行内容
input_data = input_file.readlines()

while True:
    #当输入文件大小大于预期时，跳出循环
    if total_size > output_size:
        break
    #写一行内容进输出文件
    output_file.write(input_data[index % len(input_data)])
    #输出文件大小增加输入长度
    total_size += len(input_data[index % len(input_data)])
    #行号加一
    index += 1
#循环结束 关闭文件
input_file.close()
output_file.close()
