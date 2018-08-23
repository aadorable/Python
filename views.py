#!/usr/bin/env python
# coding=utf-8

'''
从小说网站抓取一本小说的内容
'''

#Python库，提供一系列针对url的操作方法
import urllib2
#Re正则表达式库，提供一系列针对正则表达式的方法
import re
#BeautifulSoup库
from bs4 import BeautifulSoup

import sys

#获取网页内容
def OpenPage(url):
    MyHeaders = {}
    #urllib2.Request 填写两个参数，第一个参数是url，第二个参数是我们的请求头headers
    request = urllib2.Request(url, headers = MyHeaders)
    #类文件对象
    #urlopen发送指定请求
    f = urllib2.urlopen(request)
    #f.read()读取响应对象的内容
    data = f.read()
    #编码解码方法 decode解码 encode编码
    #ignore replace
    return data.decode("GBK", errors="ignore").encode("utf-8")
#测试访问页面内容
def Test1():
    print OpenPage("http://www.shengxu6.com/book/2967.html")

def ParseMainPage(page):
    #调用BeautifulSoup库解析页面
    soup = BeautifulSoup(page, "html.parser")
    #find_all方法查询所有的指定内容
    #包含read字符串的href链接 通过正则表达式
    list_charts = soup.find_all(href=re.compile("read"))
    #url_list = ["http://www.shengxu6.com" + item['href'] for item in list_charts]
    url_list = []
    for item in list_charts:
        #print type(item)
        #每一个item是一个tag标签类的实例化对象
        #通过item['href'] 可以获取到href的值
        #print item["href"]
        url_list.append("http://www.shengxu6.com" + item['href'])
    return url_list

def Test2():
    page = OpenPage("http://www.shengxu6.com/book/2967.html")
    print ParseMainPage(page)

if __name__ == "__main__":
    #构建完整的爬虫应用
    #小说主页
    url = raw_input("请输入要爬取的小说地址：")
    #获取主页内容
    main_page = OpenPage(url)
    #获取主页内的各个章节的url list
    url_list = ParseMainPage(main_page)
    for url in url_list:
        print "Clone url=" + url
        detail_page = OpenPage(url)
        title,content = ParseDetailPage(detail_page)
        data = "\n\n\n" + title + "\n\n\n" + content
        data = data.encode("utf-8")
        WriteDataToFile("mqnth.txt", data)
        #WriteDataToFile("mqnth.txt", content)
    print "爬取完成"



