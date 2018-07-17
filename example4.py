#!/usr/bin/env python
# coding=utf-8

'''
生成一个py文件并执行，打印Hello World!
'''

import os,stat

#python里面os库也给大家提供了文件操作方法
#os.path.exists方法根据路径判断文件是否存在，返回bool值

if os.path.exists("Hello.py"):
    #remove方法，根据路径删除指定文件
    os.remove("Hello.py")
#生成指定文件
os.mknod("Hello.py")

#f = open("Hello.py", "w")
#f = os.open("Hello.py", 2)
f = os.open("Hello.py", os.O_RDWR)
os.write(f, "#!/usr/bin/env python\nprint 'Hello World!'")
os.close(f)
#os.chmod("Hello.py", 320)
os.chmod("Hello.py", stat.S_IRUSR | stat.S_IXUSR)
os.system("./Hello.py")

