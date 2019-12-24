# forest-py

* python简介
    * python是一门解释型语言，即没有编译环节。python也是面向对象的。
    * python数据类型(只是说创建变量是不需要什么变量类型)，Number、String、List、Tuple(元组)、Dictionary(dict 字典)
        * Number支持int、long、float、complex(复数)   [long已被废弃，用int替代，数据溢出时会自动转型为long]
        * string的下标可以使用负号表示。-1角标对应( length - 1)角标。
        * list除了与string相同的用法外，还拥有pop/insert/append等方法。list中的元素可以是list。
        * tuple元组与list类似，不同之处在于不可以二次赋值。
        * dic就是k-v的map
        * set就是元素不会重复的集合。
    * python中的参数传递
        * 不可变对象，如果string、tuples、number类型，不严谨的说是“值传递”
        * 可变对象，如list等，不严谨的说是“引用传递”
    * python中的包是多个模块的集合，但必须包含一个__init__.py的文件。
    * open函数
        * file object = open(file_name [, access_mode] [, buffering])
            * access_mode详细见下图 
            * buffering
                * 负数 表示寄存区大小为系统默认
                * 0 表示不寄存
                * 1 表示寄存行
                * 其他为具体的寄存区的缓冲大小
    * pip 包管理
        * 保证pycharm中的pip版本与系统的pip版本一致。
        * sudo -H pip install MySQL-python
    * gc(垃圾回收garbage collection)
        * py通过引用计数进行跟踪和回收垃圾。引用计数器变为0时，该对象所占用内存空间等待被回收，不会立即回收。
    * make a script boot importable and executable. 当前模块即可导入使用，亦可直接运行。
        * 当前模块运行 __name__为__main__
        * 其他模块导入此模块，运行，__name__为module
        * 故而目的就是不会使得当前代码导入运行的时候，运行两次。
if __name__ == '__main__':

![image](/Users/feiyi/Desktop/Screen Shot 2019-12-24 at 5.29.09 PM.png)



