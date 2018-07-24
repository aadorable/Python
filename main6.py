#!/usr/bin/env python
# coding=utf-8

'''
类和实例
'''

#class Animal(object):
#    #静态变量
#    x = 1
#    #非静态成员函数, 第一个参数必须是本身(self)
#    def Print(self, x, y = 9):
#        print "非静态方法调用"
#        print x + y
#    #静态成员函数
#    @staticmethod    #装饰器
#    def Print1():
#        print "静态方法调用"
#    ##静态方法转化
#    #Print1 = staticmethod(Print1)
#    #构造器
#    def __init__(self, x, y):
#        self.Name = x
#        self.Age = y
#
#C = Animal("Cat", 10)
##C.Print(1, 2)
##C.Print(3)
#C.Sex = "male"
#print C.Name
#print C.Age
#print C.Sex
#C.Print1()

##组合 多个类，尤其是几个比较小的类，组合起来来共同解决一个问题
##通讯录 两个类来进行组合，解决问题
##联系人类 姓名和电话
#class Contact(object):
#    def __init__(self, name, phone):
#        self.Name = name
#        self.Phone = phone
#
##通讯录类
#class CBook(object):
#    def __init__(self):
#        #data 属性保存么一个通讯录对象
#        self.data = []
#        self.Number = 0
#    def AddContact(self, Contact):
#        self.data.append(Contact)
#        self.Number += 1
#    def PrintContact(self):
#        print "当前通讯录保存 %d 条信息" % self.Number
#        for item in self.data:
#            print "姓名：%s, 联系电话：%s" % (item.Name, item.Phone)
#
#C = CBook()
#Person1 = Contact("wu", "1234")
#C.AddContact(Person1)
#Person2 = Contact("haha", "10086")
#C.AddContact(Person2)
#
#C.PrintContact()

#继承和多态，发展出开闭原则


#类的私有化
class Animal(object):
    def __init__(self):
        self.__Name = "Dog"
        self.__Age = 10
        self.Sex = "male"
    #str构造器，给类添加
    def __str__(self):
        return "这是一个动物类"
    def GetAge(self):
        return self.__Age
    def SetAge(self, x):
        if x < 0:
            raise Exception("年龄不能是负数")
        else:
            self.__Age = x

C = Animal()
print C.GetAge()
try:
    C.SetAge(20)
    C.SetAge(-1)
except Exception,e:
    print e
print C.GetAge()

#hasattr() 接受两个参数，第一个参数是类的实例化对象，第二个参数是属性名，根据类中有无这个属性，返回True或False
print hasattr(C, "Name")
#getattr() 接受两个参数，第一个参数是类的实例化对象，第二个参数是属性名，返回属性值
print getattr(C, "Sex")
#setattr() 接受三个参数，第一个参数是类的实例化对象，第二个参数是属性名，第三个参数是要赋给的属性值
setattr(C, "Sex", "famale")
print C.Sex
#delattr 接受两个参数，第一个参数是类的实例化对象，第二个参数是属性名
delattr(C, "Sex")
print hasattr(C, "Sex")
