# -*- coding: UTF-8 -*-
# py 继承机制
# 以下内容包括方法覆写/构造方法覆写/多继承


class Parent:
    parentAttr = 100

    def __init__(self):
        print "调用了父类的init"

    def parent_method(self):
        print "调用了父类的method"

    def parent_method_override(self):
        print "你可能要override该方法"

    def set_attr(self, attr):
        Parent.parentAttr = attr

    def get_attr(self):
        return Parent.parentAttr


class Mother:

    def __init__(self):
        print "调用了母类的init"

    def mother_method(self):
        print "调用了母类的方法"


class Child(Parent, Mother):

    __private_att = 0   # 私有变量，不可再外部直接访问。方有方法亦同。开头加双下划线。

    def __init__(self):
        print "调用了子类的init"

    def child_method(self):
        print "调用了子类的method"

    def parent_method_override(self):
        print "override..."


child = Child()
child.child_method()
child.parent_method()
print child.get_attr()
child.set_attr(101)
print child.get_attr()
child.parent_method_override()
child.mother_method()
print isinstance(child, Mother)
print issubclass(Child, Parent) # 参数为Class1, Class2
print child._Child__private_att # 不推荐。访问类私有变量

