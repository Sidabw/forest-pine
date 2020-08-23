# coding=utf-8
# python is fun
print
"hello world"
a = 32
if a > 50:
    print('a')
elif a > 40:
    print('b')
else:
    print('c')

# 动态语言、静态语言区分
dyvar = 1
print(dyvar)
dyvar = 'sida'
print(dyvar)

print('中文')
listtest = [1, 2, 3]
print(listtest)
print(len(listtest))
print(listtest[-2])  # 打印倒数第二个

listtest.append('avc')
print(listtest[3])  # list中可以同时有整形、字符串、布尔、list等。即数据类型可以不一致

listtest.insert(1, 2)  # 同ArrayList中的add(index,element);
listtest.pop(1)  # 删除指定索引的元素
listtest.pop()  # 删除最后1个元素
listtest[2] = ['abc', 1, True]

tupletest = (1, 2, 3)  # 定义1个元组，其内容不可以改变
tupletest2 = (1,)  # 定义1个大小为1的元组
print(tupletest)
print(tupletest2)
# 报错：tupletest[1] = 0

tupletest3 = (1, 2, [1, 2, 3])
tupletest3[2][1] = 5
print(tupletest3)  # 元组内容不可变，实质上说的是引用不可变
print('-------------------------------')
for num in tupletest3:
    print(num)
sum = 0
for num in tupletest:
    sum = sum + num
print(sum)

inttest = '123'
print(inttest > 124)  # true
print(int(inttest) > 124)  # false
# 上边是基础语法和list、元组，下边是map和set，在py里map叫做字典dict
dicttest = {'sida': '老大', 'brew': '老小', 'test': 12}  # 同样支持不同类型
print(dicttest['sida'])
print(dicttest['test'])
print('sida' in dicttest)  # 判断key是否存在
print(dicttest.get('sidaa', 1))  # 如果key不存在，返回指定值
print(dicttest.get('test'))
dicttest.pop('test')  # 删除指定的key-value
print(dicttest.get('test'))

settest = set([1, 5, 2, 3])
print(settest)
settest.add(3)  # set 不可重复，添加重复元素无作用
settest.remove(5)
print(settest)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # 取两个set的并集
print(s1 | s2)  # 取两个set的交集
# s1.add([34,5])    #会报错，同dic一样，key只能是string这一类不可变元素，而不能是list这一类可变元素
