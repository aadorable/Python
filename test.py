#!/usr/bin/env python
# coding=utf-8

import urllib2
import re
import json
from bs4 import BeautifulSoup
#import MySQLdb
#yum install python-devel
#pip install mysql-python

def OpenPage(url):
    Myheaders = {}
    req = urllib2.Request(url,headers=Myheaders)
    f = urllib2.urlopen(req)
    data = f.read()
    return data

def Test1():
    print OpenPage("http://jy.51uns.com:8022/Pro_StudentEmploy/StudentJobFair/Zhaoping.aspx?WorkType=0")

def Test2():
    print OpenPage("http://jy.51uns.com:8022/Frame/Data/jdp.ashx?rnd=1528794488557&fn=GetZhaopinList&StartDate=2000-01-01&SearchKey=&InfoType=-1&CompanyAttr=&CompanyType=&Area=&City=&CompanyProvice=&Post=&Zhuanye=&XLkey=&Age=&start=0&limit=15&DateType=999&InfoState=1&WorkType=0&CompanyKey=")

#解析主页内容，获取招聘信息的url
def ParseMainPage(page):
    #json.dumps() 转化数据成json格式
    #json.loads() 转化json格式成python数据类型
    data = json.loads(page)
    #解析后的Data是一个大的字典,rows是招聘信息数据的key
    #rows里面保存了一个包含多个招聘信息的list
    #list里面的每个元素都是一条招聘信息，保存为字典类型
    rows = data["rows"]
    prefix = "http://jy.51uns.com:8022/Frame/Data/jdp.ashx?rnd=1533005391497&fn=GetOneZhaopin&StartDate=2000-01-01&JobId="
    IdList = []
    for item in rows:
        IdList.append(prefix + item['Id'])
    #return [prefix + item["Id"] for item in rows]
    return IdList

def Test3():
    page = OpenPage("http://jy.51uns.com:8022/Frame/Data/jdp.ashx?rnd=1533001139862&fn=GetZhaopinList&StartDate=2000-01-01&SearchKey=&InfoType=-1&CompanyAttr=&CompanyType=&Area=&City=&CompanyProvice=&Post=&Zhuanye=&XLkey=&Age=&start=0&limit=15&DateType=999&InfoState=1&WorkType=0&CompanyKey=")
 
    print ParseMainPage(page)

#mysql -u root -p < table.sql
if __name__ == "__main__":
    url = "http://jy.51uns.com:8022/Frame/Data/jdp.ashx?rnd=1533001139862&fn=GetZhaopinList&StartDate=2000-01-01&SearchKey=&InfoType=-1&CompanyAttr=&CompanyType=&Area=&City=&CompanyProvice=&Post=&Zhuanye=&XLkey=&Age=&start=0&limit=15&DateType=999&InfoState=1&WorkType=0&CompanyKey="
    #根据主页ajax获取数据的url，获取服务器端相应的招聘信息
    mainPage = OpenPage(url)
    #分析服务器端响应，得到招聘信息详情页的数据获取url
    urlList = ParseMainPage(mainPage)
    for item in urlList:
        print "crawler url=" + item
        #获取招聘信息详情
        detailPage = OpenPage(item)
        #解析数据
        data = ParseDetailPage(detailPage)
        #id,公司名,招聘岗位,招聘详情
        WriteDataToFile("\n".join(data))
        print "crawler done"
