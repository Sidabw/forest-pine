# -*- coding: UTF-8 -*-
class Employee:
    "这是Employee的文档字符串....  这是一个员工基类"
    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name  # 类实例，实例变量。不是固定的。甚至都不需要声明：25line
        self.salary = salary
        Employee.employeeCount += 1  # 基类，类变量
        print("I'm ", name, "my salary is ", salary, "----method __init__")


    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


employee1 = Employee('brew', "50000")
print("employee1.get_name()", employee1.get_name())
print("employee1.name", employee1.name)

employee2 = Employee('brew2', '600000')
print(employee2.get_name())
print(Employee.employeeCount)

employee1.age = 7
print("employee1.age", employee1.age)

# del employee1.age
# print employee1.age   # 报错：Employee instance has no attribute 'age'

print('-----')
# 调用函数访问类实例变量
print("hasattr(employee1, 'age')", hasattr(employee1, 'age'))
print("hasattr(employee1, 'name')", hasattr(employee1, 'name'))
print(getattr(employee1, 'age'))
print(setattr(employee1, 'age', 10))
print(delattr(employee1, "age"))


# py内置属性
print("employee1.__class__ ", employee1.__class__)
print("employee1.__doc__ ", employee1.__doc__)
print("employee1.__module__ ", employee1.__module__)

# py-gc(垃圾回收)->笔记见Evernote
a = 40  # 创建对象
b = a  # 增加引用
c = [b]  # 增加引用

del a  # 减少引用
b = 2  # 减少引用
c = -1  # 减少引用
