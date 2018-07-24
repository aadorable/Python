#!/usr/bin/env python
# coding=utf-8
import math

#dict1 = {
#        "IP":"127.0.0.1",
#        "Host":"www.baidu.com"
#        }
#list1 = [1, 2, 3, 4, 
#        5, 6, 7]
#tuple1 = (1,2,3,4,
#        5,6,7)
#
#a = b = 2
#if a == \
#        b:
#            print "success"
#
#str1 ="""My name
#is wu"""
#
#print str1[7]
#
#x, y = 1, 2
#x, y = y, x
#print x, y
#
#for count in range(10):
#    x = 1
#print x

#x = 1
#def Test():
#    '''
#    Test函数毫无作用
#    '''
#    a = b = c = 2
#    print "函数内"
#    print "全局变量"
#    print globals()
#    print "局部变量"
#    print locals()
#    return "success"
#print Test.__doc__
#Test()
##print help(Test)
#
#import add
#print add.__doc__
#
#print type(None)
#if not None:
#    print "Haha"

#print [1, 2, 3] < "123"
#
#a = 1
#b = 1
#if a is b:
#    print "success"
#b = 2
#if a is not b:
#    print "success"

#类型比较
#a = 1
#b = 0.5
#if type(a) != type(b):
#    print "success"
#
##isinstance()两个参数，第一个参数是变量名，第二个参数是类型
##判断变量类型和指定类型是否相同
#if isinstance(a, int):
#    print "success agin"
#print isinstance(a, float)
#print isinstance(a, bool)
#print isinstance(a, str)

#def Test():
#    '''
#    这个函数什么都不做
#    '''
#    return True
#
#print Test.__doc__
#print help(Test)

#a = 5 + 2j
#print type(a)
#print type(None)
#
#a = 100
#b = 10
#print id(a) == id(b)

##求绝对值函数
#print abs(-5)
#print abs(-(3 + 4j))
##求商和余数(返回一个元组)
#a, b = divmod(20, 3)
#print a, b
##对浮点数四舍五入
#print round(3.1415926, 2)
#for count in range(10):
#    print round(math.pi, count)
#print type(oct(1234))
#print type(hex(1234))

#x = 1
#y = -2
#if x > 0:
#    if y > 0:
#        print 'x and y > 0'
#else:
#    print 'x <= 0'
#
#if x > 0:
#    if y > 0:
#        print 'x and y > 0'
#    else:
#        print 'y <= 0'

#x = 4
#y = 2
#smaller = x if x < y else y
#print smaller

#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#def Find(x, List):
#    for item in List:
#        if item == x:
#            return item
#    else:
#        return "No Search"
#
#result = Find(8, list1)
#print result
##
##def Test():
##    pass
##print Test()
#
#def Hello(x = 0, y = 0, z = 0):
#    print type(x)
#    print type(Find)
#    print x, y, z
##print Hello()
##print Hello(1, 2)
##print Hello(3, 4, 5)
##print Hello(100, z = 200)
##print Hello(1, Find(8, list1))
#Hello(x = 1, z = 200)

##sorted 排序函数 四个参数 Cmp比较函数 key比较函数只接收一个参数，返回一个数
##比较绝对值
#list1 = [2, 6, 1, 3, 9, 4, 5]
#def Cmp(x, y):
#    if abs(x) > abs(y):                    #a > b返回正数
#        return 1
#    elif abs(x) < abs(y):                  #a < b返回负数
#        return -1
#    else:
#        return 0
##Result = sorted(list1, cmp = Cmp)
##print Result
#
#list2 = ["123", "12345", "1", "345678"]
#Result = sorted(list2, key = len)
##Result = sorted(list1, reverse = True)   #默认False，返回增序，True返回降序
#print Result
#
##可变长参数组 *变量名代表list
##_.join(list2) 以_的方式将字符串拼接起来
#def Log(prefix, *data):
#    print type(data)
#    print prefix + '\t'.join(data)
#Log("[Error]:", "Test", "Error", "Info")
#
#def Log2(prefix, **data):
#    print type(data)
#    print data.keys()
#    print prefix + '\t'.join(data.values())   #values()和keys()是字典的内建方法
#Log2("[Warning]:", Ip = "127.0.0.1", Host = "www.baidu.com", Name = "wu")
#print dir(Log2)

#def Hello(x = 0, y = 0, z = 0):
#    return x, y, z
#print Hello(y = 100, z = 200)
#
#def Log(prefix, *data):
#    print prefix + '\t'.join(data)
#    print type(data)
#Log("[Error]:", "1", "2", "3")
#
#list1 = ["my", "name", "is", "wu"]
##print " ".join(list1)
#str1 = " ".join(list1)
#print type(str1)



