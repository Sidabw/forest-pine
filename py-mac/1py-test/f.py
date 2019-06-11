#!/usr/bin/python
# -*-coding:utf-8 -*-
import math

print "hello world"
print "你好"
# 初识python代码格式
a = 32
if a > 50:
    print('a')
elif a > 40:
    print('b')
else:
    print('c')
'''
这里是多行注释
'''
# 变量，动态语言，不需要声明类型，直接赋值
a = 1
a = 1.0
a = 'sida'
a = b = c = 1
a, b, c = 1, 2, 'sida'  # 多个变量同时赋值

# 动态语言、静态语言区分
dyvar = 1
print(dyvar)
dyvar = 'sida'
print(dyvar)

print('--------------- "String - start"----------------')
# 字符串截取中的[s:e] start or end 任意一方为空则表示取到头或尾
print (dyvar[0:2])  # 字符串截取，同样包头不包尾
print (dyvar[1])    # 输出角标为1
print (dyvar[:1])   # 输出
print (dyvar[1:])   # 输出角标为1一直到最后
print dyvar * 2     # 表示该字符串输出两次
print dyvar + " and brew"    # 字符串append
# 字符串转int
inttest = '123'
print(inttest > 124)    # true   dont know why
print(int(inttest) > 124)   # false
print('--------------- "String - end"----------------')
print

print('--------------- "list - start"----------------')
# 列表截取用法同字符串截取相同
listtest = [1, 2, 3]
print(listtest[0:1])    # 切片操作
print(len(listtest))
print(listtest[-2])   # 打印倒数第二个
listtestt = ['a', 'b', 'c']
listtest = listtest + listtestt     # 同append用法相同
listtest.append('avc')
print(listtest[3])     # list中可以同时有整形、字符串、布尔、list等。即数据类型可以不一致
listtest.insert(1, 2)   # 同ArrayList中的add(index,element);
listtest.pop(1)    # 删除指定索引的元素
listtest.pop()     # 删除最后1个元素
listtest[2] = ['abc', 1, True]  # 二维数组
print('--------------- "list - end"----------------')
print


print('--------------- "tuple - start"----------------')
tupletest = (1, 2, 3)     # 定义1个元组，其内容不可以改变
tupletest2 = (1,)       # 定义1个大小为1的元组
print(tupletest)
print(tupletest2)
# 报错：tupletest[1] = 0
tupletest3 = (1, 2, [1, 2, 3])
tupletest3[2][1] = 5
print(tupletest3)   # 元组内容不可变，实质上说的是引用不可变
# 初识for循环
for num in tupletest3:
    print(num)
print('--------------- "tuple - end"----------------')
print

print('--------------- "dict - start"----------------')
# 上边是基础语法和list、元组，下边是map和set，在py里map叫做字典dict
dicttest = {'sida': '老大','brew': '老小','test': 12}   # 同样支持不同类型
print(dicttest['sida'])
print(dicttest['test'])
print('sida' in dicttest)   # 判断key是否存在
print(dicttest.get('sidaa', 1))  # 如果key不存在，返回指定值
print(dicttest.get('test'))
dicttest.pop('test')    # 删除指定的key-value
print(dicttest.get('test'))  # 会打印 None
print('--------------- "dict - end"----------------')
print

print('--------------- "set - start"----------------')
settest = set([1, 5, 2, 3])
print(settest)
settest.add(3)  # set 不可重复，添加重复元素无作用
settest.remove(5)
print(settest)
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)  # 取两个set的并集
print(s1 | s2)  # 取两个set的交集
fset = frozenset(s1 | s2)   # 创建一个不可变集合。
# s1.add([34,5])    # 会报错，同dic一样，key只能是string这一类不可变元素，而不能是list这一类可变元素
print('--------------- "set - end"----------------')
print

# 运算符
print('--------------- "运算符 - start"----------------')
list = [11, 22, 33, 44]
a = 11
b = 12
print (a in list)
print (b not in list)
c = 11
print (a is c)
print (a == c)
print('--------------- "运算符 - end"----------------')
print

print('--------------- "条件语句 - start"----------------')
# python指定任何非null值和非0 为true。 null 或 0 为 false
b = 0
if b or a:
    print "hahah"
elif a:
    print "heheh"
print "python 不支持 switch case"
print
print('--------------- "条件语句 - end"----------------')
print

print('--------------- "循环语句 - start"----------------')
print
# 这个循环我也看不懂....什么玩意...  自己写的
a = 1
while a == 1:
# b = raw_input("请输入一个数字")
    a = int(b)
    if a == 3:
        continue
    elif a == 2:
        break
    else:
        print "......"
else:
    print "while 循环执行完了。。。"
# 是的，没看错，python可以写 while/for...else...   这里的else表示正常执行完后执行的语句，break跳出循环时不执行...  好鸡肋啊...

for letter in 'sida':
    print letter;print

for index in range(5):
    print index
    print   # 结果是 0 1 2 3 4

# pass 只有占位的作用。比如定义了一个空函数，此时就需要一个pass占位 不然报错
print('--------------- "循环语句 - end"----------------')
print
print('--------------- "math - start"----------------')
print dir(math)
a = 'aaa'
