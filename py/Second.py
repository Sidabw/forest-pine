# coding=utf-8
from collections import Iterable
import os

# 函数相关
print(abs(-1))  # 绝对值
print(cmp(2, 1))  # 类似java的compareTo   大于返回1，小于返回-1，等于返回0
# 数据类型转换
print(int('123'))
print(int(12.34))  # 向下取整
print(float('12.34'))
print(str(12.34))
print(bool(1))  # true
print(bool(0))  # true
print(bool(''))  # false
print(bool('avc'))  # true
# 函数名只是一个函数对象的引用
a = abs
print(a(-1))
# 函数定义,函数定义上下空两行
print('--------------------------------------------------')


def my_abs(x):
    # 添加参数校验
    if not isinstance(x, (int, float)):
        raise TypeError('你还不给老子赶忙输入数字！！！')
    if x > 0:
        return  # 意思是return none
    else:
        return 'brew'


print(my_abs(10))
# print(my_abs('abc'))
if 5 > 6:
    pass  # pass意味着什么都不做，跟continue没关系


# 返回多值时实际上返回的是一个元组
# 参数默认值必须放在后面，通过默认参数值的设置，提高方法的调用简易型


def enroll(name, gender, age=10, address='北京'):
    print 'name:', name
    print 'gender', gender
    print 'age', age
    print 'address', address


enroll('aa', 'women')
enroll('abc', 'man', 12, '南京')
print('---')
enroll('aaaaaa', 1234, address='上海')  # 可以跳着来


def add_test(L=[]):
    L.append('END')
    return L


print(add_test())
print(add_test())  # 当传入可变参数时容易造成各种意外情况 ['END', 'END']，纵使第二次调用但获得的还是上一次的L，而且没有空指针

# 默认值方式，使得每次调用该方法L都会被指向None,当调用者两次调用都传入参数时也没关系，因为每次调用L都被重新指向了None
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end([1, 2, 3]))
print(add_end([1, 2, 3]))


def calc(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


print(calc(1, 2, 3))
lsittest = [1, 3, 4]
print(calc(*lsittest))


def person(name, age, **other):
    print('name', name, 'age', age, 'other', other)
    abc = other.get('address')
    print(abc)
    print(other.get('gender'))
    #print(abc.decode('utf-8'))

print('------')
person('zhangsan', 12)  #关键字参数，实际上是一个dict
person('lissi', 13, address='北京', gender='women')
dicttest = {'address': '北京', 'gender': 'women'}
person('wangwu', 14, **dicttest)    #同可变参数一样，调用时都需要额外加* 或 **
#参数定义顺序：必选参数，默认参数，可变参数，关键字参数


def func(a, b, c=0, *agrs, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', agrs, 'kw=', kw)


L = [1, 2, 3, 4]
LL = {'sid': 'bre'}
func(*L, **LL)  #任何函数都可以通过这种方式调用


def fact(n):
    if n == 1:
        return 1
    return n+fact(n-1)


print(fact(500))    #传入1000会导致栈溢出。每调用一次，加一层栈帧，函数每返回一次，就减一次栈帧；


# def fact_better(num, result): #尾递归，python未优化，故无效
#     if num == 1:
#         return result
#     return fact_better(num - 1, num+result)
#

r = [1, 2, 3, 4]
print(range(3))     #[0, 1, 2]
for i in range(3):
    print(r[i])

print(r[0:3])   #切片操作，同样是包头不包尾
print(r[-2:])   #倒叙切片，取倒数第1个、倒数第二个，两个元素
print('abc'[0:1])
print((1, 2, 3)[0:1])
print((1, 2, 3)[0:2])

dicttest2 = {'a': 1, 'b': 2}
for key in dicttest2:   #对dict进行迭代，因为dict实际是一个hashmap，所以key是无序的。
    print(key)
    print(dicttest2.get(key))

for value in dicttest2.itervalues():    #迭代dict的value
    print(value)

for item in dicttest2.iteritems():
    print(item)

for ch in 'abcdefg':
    print(ch)

print(isinstance(123, Iterable))    #需要 from collections import Iterable
print(isinstance('abc', Iterable))
#如果遍历list并且每次都想拿到下标，可以这么操作：
for i in enumerate([3, 4, 5]):
    print i
    print i[0]

LLL = []
for i in range(1, 11):
    LLL.append(i * i)
print(LLL)
print([num * num for num in range(1, 11)])  #列表生成器
print([m + n for m in 'ABC' for n in 'XYZ'])    #双重循环，生成全排列
LLLL = [d for d in os.listdir('.')]     #需要引入os模块
print(LLLL)

Ltest = ['abc', 12, 'dEF']
print([i.lower() for i in Ltest if isinstance(i, str)])     #加判断的列表生成器
#生成器学习
print([num for num in range(10)])
print((num for num in range(10)))   #直接打印得到的是generator的地址
LLtest = (num for num in range(10))
print(LLtest.next())
print(LLtest.next())
print(LLtest.next())
for num in LLtest:
    print(num)


def fib(max):       #斐波拉契数列 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b   #可以理解为a、b都是同时读入，等都计算完之后，再往回写
        print('verify:', a, b)
        n = n + 1


print('--------------')
#fib(10)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b         #使用yield关键字变成1个generator
        a, b = b, a+b
        n = n + 1


print(fib2(10))


def odd():      #这是1个generator 每次next会在执行到yield时退出，下次执行从上次退出的地方继续执行
    print('step 1')
    yield 1
    print('step 3')
    yield 3
    print ('step 5')
    yield 5


o = odd()
print(o.next())
print(o.next())
print(o.next())