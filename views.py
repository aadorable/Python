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



