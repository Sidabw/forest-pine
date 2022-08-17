#!/usr/bin/python
# -*-coding:utf-8 -*-
import math

# 当前first.py 只有Python基础部分，包含：
# 数据类型和变量、字符串和编码、使用list和tuple、条件判断、循环、使用dict和set



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
print("dyvar：" + dyvar)

print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "String - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
# 字符串截取中的[s:e] start or end 任意一方为空则表示取到头或尾
print("dyvar[0:2]：" + dyvar[0:2])  # 字符串截取，同样包头不包尾
print("dyvar[1]：" + dyvar[1])  # 输出角标为1的元素
print("dyvar[0]：" + dyvar[0])
print("dyvar[-1]：" + dyvar[-1])  # -1角标对应( length - 1)角标。
print("dyvar[:1]：" + dyvar[:1])  # 输出,同样包头不包尾
print("dyvar[1:]：" + dyvar[1:])  # 输出角标为1一直到最后

print("dyvar * 2: " + (dyvar * 2))  # 表示该字符串输出两次
# 字符串转int
inttest = '123'
print(int(inttest) > 124)  # false


print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇"list - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
# 列表截取用法同字符串截取相同
lsit1 = [1, 2, 3]
print(lsit1[0:1])  # 切片操作
print(len(lsit1))
print(lsit1[-2])  # 打印倒数第二个
list2 = ['a', 'b', 'c']
list2 = lsit1 + list2  # 同append用法相同
list2.append('avc')
print(list2)

print(list2[4])  # list中可以同时有整形、字符串、布尔、list等。即数据类型可以不一致
list2.insert(1, 2)  # 同ArrayList中的add(index,element);
list2.pop(1)  # 删除指定索引的元素
list2.pop()  # 删除最后1个元素
list2[2] = ['abc', 1, True]  # 二维数组
print(list2)

print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "tuple - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
tupletest = (1, 2, 3)  # 定义1个元组，其内容不可以改变
tupletest2 = (2,)
print(tupletest)
print(tupletest2)
# 报错：tupletest[1] = 0
tupletest3 = (1, 2, [1, 2, 3])
tupletest3[2][1] = 5
print(tupletest3)  # 元组内容不可变，实质上说的是引用不可变
# 初识for循环
for num in tupletest3:
    print(num)

print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "set - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
settest = {1, 5, 2, 3}
#settest = set([1, 5, 2, 3])  #第二种写法
print(settest)
settest.add(3)  # set 不可重复，添加重复元素无作用
settest.remove(5)
print(settest)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2   # 取两个set的并集
print(s3)
s4 = s1 | s2  # 取两个set的交集
print(s4)
fset = frozenset(s1 | s2)  # 创建一个不可变集合。
print(fset)
# s1.add([34,5])    # 会报错，同dic一样，key只能是string这一类不可变元素，而不能是list这一类可变元素

print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "dict - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
# 上边是基础语法和list、元组，下边是map和set，在py里map叫做字典dict
dicttest = {'sida': '老大', 'brew': '老小', 'test': 12}  # 同样支持不同类型
print("dicttest['sida']：" + dicttest['sida'])
dicttest['sida2'] = "老大2"  # add/push操作
print("dicttest['sida2']：" + dicttest['sida2'])
print('sida' in dicttest)  # 判断key是否存在
print(dicttest.get('sidaa', 1))  # 如果key不存在，返回指定值
print(dicttest.get('test'))
dicttest.pop('test')  # 删除指定的key-value
print(dicttest.get('test'))  # 会打印 None


print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "运算符 - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ ')
# 算数运算符
"""
+：　　加法运算
-：　　减法运算
*：　　乘法运算
**：    幂运算
/:  　　除法运算（如果有小数则返回结果为小数，如果都为整数则返回结果为整数）
//：     整除，取整数部分
%：　 取余
"""
# '逻辑运算符
list = [11, 22, 33, 44]
a = 11
b = 12
print(a in list)
print(b not in list)
c = 11
ac = a is c
print("数值比较：a is c：" + str(ac))  #字符串直接拼接bool会报错
print("数值比较：a == c：" + str(a == c))


print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "条件语句 - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ ')
# python指定 null 或 0 为 false
b = 0
if b or a:
    print("hahah")
elif a:
    print("heheh")

print("python 不支持 switch case")

print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ "循环语句 - start" ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ ')
a = 1
while a == 1:
    # b = raw_input("请输入一个数字")
    a = int(b)
    if a == 3:
        continue
    elif a == 2:
        break
    else:
        print("......")

else:
    print("while 循环执行完了。。。")

# 是的，没看错，python可以写 while/for...else...   这里的else表示正常执行完后执行的语句，break跳出循环时不执行...  好鸡肋啊...

for letter in 'sida':
    print(letter, end='')
print()

for index in range(5):  # 结果是 0 1 2 3 4
    print('sidaa'[index], end='')
print()

# pass 只有占位的作用。比如定义了一个空函数，此时就需要一个pass占位 不然报错
print('⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇"math - start"⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇')
dir(math)
a = 'aaa'
