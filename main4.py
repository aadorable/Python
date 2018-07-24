#!/usr/bin/env python
# coding=utf-8

#异常处理 try except
#str1 = "123"
#try:
#    print str1 + 10
#    print str1 + "12"
##except:           #捕获全部类型的异常，但是无法获取异常对象
##    print "非法错误"
##except IOError, e:
##    print e
#except TypeError, e:    #捕获指定类型的异常
#    print e
##except Exception, e:   #捕获全部类型的异常，把异常对象用变量e引用
##    print e

#抛出异常 raise
def Division(x, y):
    if y == 0:
        raise Exception("除数不能为0")
    else:
        return x / y

try:
    Division(1, 0)

except Exception, e:  
    print e

finally:
    print "Finish"
    print "必须执行的代码块"
