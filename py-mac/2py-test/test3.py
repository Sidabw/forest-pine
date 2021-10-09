# -*- coding: UTF-8 -*-

msg = []
m2 = 1


def my_f():
    global msg
    global m2
    msg.append(1)
    m2 = 2


my_f()
print(msg)
print(m2)
