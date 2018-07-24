#!/usr/bin/env python
# coding=utf-8

##in / not in 关键字在字符串中使用
#list1 = [1, 2, 3, 4, 5]   #无法判断是否是子集
#print 1 in list1
#list2 = [1, 2, 3, 4, [1, 2, 3]]
#print [1, 2, 3] in list2
#str1 = "abcdefg"      #可以判断子集
#print "a" in str1
#print "bcd" in str1
#
##+拼接  *重复
#print (list1 + ["hello", "world"]) * 4

#切片传送做进阶 list1[::]
#list1[:][:) 前闭后开区间
#list1[起始区间:区间结束:步长]
#[1, 5)区间 隔2取值
#print list2[1:5:2]
#当步长 >0 时，从前到后按步长取值，区间默认值是[0, len - 1)
#当步长 <0 时，变成逆推过程，区间默认值是[0, len)
#print list2[::-1]
#print list2[5:1:-1]

#max最大值 min最小值
#print max(list2)
#print min(list2)
#print [1, 2, 3] > 5

#sum序列求和
#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list2 = ["1", 2, 3, 4]
#print sum(list1)
#print sum(list2)

##enumerate 枚举序列的下标和对应的值，每组构成一个元组
#list1 = ["a", "b", "c", "d"]
#for item in enumerate(list1):
#    print item
#def Find(x, List):
#    for index, value in enumerate(List):
#        if x == value:
#            return index
#    return -1
#print Find("c", list1)
#
##zip 行列转换函数(以最短的作为约束)  用途：构建字典
#list1 = [1, 2, 3]
#list2 = [4, 5, 6, 10]
#list3 = [7, 8, 9]
#print zip(list1, list2, list3)
#
#keys = ["IP", "Host", "Name"]
#values = ["127.0.0.1", "www.baidu.com", "wu"]
#print zip(keys, values)

##字符串不可修改
#str1 = "abcdsfhjvgfigy"
#print id(str1)
#str1 = "1" + str1[1:]
#print id(str1)
#
##原始字符串 字符串中的转义字符串不再被翻译 raw string
#str1 = r"My name is \n wu"
#print str1
#
##str() 和 repr() 字符串转换
#print str(3.1415926129035893432436768)
#print repr(3.1415897489275729454254252)
#print type(str(3.1415926129035893432436768))
#print type(repr(3.1415897489275729454254252))
#print str("hello")
#print repr("hello")

##"拼接工具".join(元素为字符串的可迭代对象)
##splist()切割函数
#str1 = "My name is wu"
#print str1.split(" ")
#
##startswith 判断是否是起始子串
#print str1.startswith("name")
##endswith 判断是否是结束子串
#print str1.endswith("wu")
#
##find() 返回字符串首字符所在位置
#print str1.find("name")
#print str1.find("is")
#
##strip() 去除开头结尾的空格和制表符
#str2 = "            Test strip          "
#print str2.strip()
#
##replace() 替换函数
#str1 = "ABCD Test EFGH"
##print str1.replace("Test", "HHHH")

##list 常用函数
##append() 用于在列表最后追加元素(每次只能追加一个元素)
#list1 = [1, 2, 3]
#list1.append(4)
#print list1
#print id(list1)
##extend() 用于列表扩展
#list1.extend([5, 6, 7, 8])
#print list1
#print id(list1)
#list1 = list1 + [9, 10, 11]
#print list1
#print id(list1)
##remove() 用于删除 list 内指定值的元素
#list1 = [1, 2, 3, 4]
#list1.remove(3)
#print list1
##del 删除关键字， 用于删除 list 指定下标的元素
#del list1[1]
#print list1
##pop() 删除最后一个元素
#list1 = [1, 2, 3, 4, 5, 6]
#Get = list1.pop()
#GetAgain = list1.pop()
#print Get, GetAgain
##sort 排序函数，接收三个参数，和sorted排序函数只有一个参数不同，就是没有可迭代对象
#print id(list1)
#list2 = list1.sort()
#print id(list2)
#sorted(list1)
#print id(list1)

#深/浅拷贝
a = [1, [2, 3]]
b = a     #直接复制
c = a[:]  #浅拷贝 简单元素生成新的，复杂元素拿来用 
d = list(a)
a[0] = "A"
a[1][0] = "Change"
print a, b, c, d
#深拷贝copy.deepcopy()
#e = copy.deepcopy(a)
#a[1][0] = "ChangeAgain"
#print e
#直接赋值 = 完全引用
#浅拷贝 = 简单元素（不包含子元素)进行拷贝生成新对象，复杂元素(包含子元素)拿来引用，不生成新对象
#深拷贝 通过copy.deepcopy()函数，对所有元素进行拷贝，全部生成新对象

#元组的不可变是指元组id不变
tuple1 = (1, 2, 3, [1, 'A', 4])
print id(tuple1)
tuple1[3][1] = "B"
print id(tuple1)
print tuple1

dict1 = {}.fromkeys(("x", "y", "z"), 0)
print dict1

dict2 = dict([[1, 2], [3, 4]])
print dict2

