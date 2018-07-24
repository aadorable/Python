#!/usr/bin/env python
# coding=utf-8

#读文件时的方法介绍
#f = open("test.py", "r")
#print f.read(10)
#f.close()

#f = open("python.txt", "r")
#readline 没有参数 读取一行内容
#print f.readline()
#f.close()

#readlines 没有参数 读取全部内容 返回一个列表，列表里的元素就是每一行内容
#print f.readlines()

#写文件时的方法介绍
#write() 写一段内容，参数就是要写入文件的内容
#f = open("python.txt", "w")
#f.write("#!/usr/bin/env python")
#f.close()

#writeslines() 接收一个列表，输入列表里的每个y7uansu
list1 = ["123\n", "123456\n", "haha\n", "hehe\n"]
#f.writelines(list1)
#f.close()

f = open("python.txt", "r")
#seek 偏移文件指针的位置，默认情况下从文件开始出计算
#默认情况下不需要第二个参数，第二个参数设置了偏移模式
#mode = 0 从头开始 mode = 1 从当前位置开始 mode = 2 从尾开始
#f.seek(-10, 2)
#f.seek(10)
print f.readlines()
#tell() 查询文件指针当前位置
f.seek(10)
print "当前文件指针位置" + str(f.tell())
f.close()

#上下文管理器
with open("python.txt", "r")
print f.readlines()
