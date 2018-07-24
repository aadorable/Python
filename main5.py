#!/usr/bin/env python
# coding=utf-8

##导入整个模块
#import sys
##from module import method
##import datetime
##从模块中导入具体内容
#from datetime import datetime
##print sys.path
##print datetime.now()
##print type(sys)
##print id(sys)
#sys.path.append('/home/wu/code/test')
#print sys.path
#import add
#print add.Add(1,2)

#def test():
#    import sys
#    print sys.path
#test()
#print sys.psth

#import sys as p
#print p.path
#
##主函数
#if __name__ == "__main__":
#    print "作为执行文件"
#    print __name__

#print globals()

from package.add import Add
print Add(1,2)

import sys
print sys.argv
print sys.byteorder
print sys.builtin_module_names

