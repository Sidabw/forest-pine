# -*- coding: UTF-8 -*-
import os
print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "input 函数 - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
# raw_input函数
#str = raw_input("请输入：")
#print "你输入的内容是：", str

# str = input("请输入：") #可以输入py表达式。例如[x*5 for x in range(2,10,2)] 一个列表生成器
# print "你输入的内容是：", str
print

print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "文件open/close/read/write - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
#open 函数的三个参数以及常用的mode见Evernote
fo = open("/Users/feiyi/Documents/feiyiGitProject/forest-py/py-mac/1py-test/test/practice.txt", "r+")
# 读取所有
print fo.read()     # 类中函数的第一个参数self代表当前类对象，不需要作为参数传递。
print fo.name
# fo.write("ha")  #默认向后追加
print fo.read()
print fo.close()

print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "文件seek/tell - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
# fo = open("/Users/feiyi/Documents/feiyiGitProject/forest-py/py-mac/1py-test/test/practice.txt", "r+")
# print fo.read()
# print fo.tell() #当前指针位置
# fo.seek(0, 0)  #重定位
# print fo.tell()
# print fo.read()
"""
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
from设为0，使用文件的开头作为移动字节的参考位置。
from设为1，使用当前的位置作为参考位置。
from设为2，使用文件的末尾将作为参考位置
"""
print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "文件seek/tell - end"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
print

print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "文件mkdir/mkfifo/rename/remove - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
#os.mkfifo("/Users/feiyi/Desktop/py-test/file-test2.txt")
# os.rename("/Users/feiyi/Desktop/py-test/file-test2.txt","/Users/feiyi/Desktop/py-test/file-test3.txt")
# os.remove("/Users/feiyi/Desktop/py-test/file-test3.txt")
# os.chdir("/Users/feiyi/Desktop/py-test")
# os.mkdir("py-t")
# os.removedirs("py-t")   #目录下的文件应当先被删除。
print os.getcwd()
# os.mkfifo("py-t/111.txt")
print '⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "文件mkdir/mkfifo/rename/remove - end"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇-'
print





