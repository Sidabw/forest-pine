# -*- coding: UTF-8 -*-


def bubble_sort():
    # "每一次循环，大的到最后边"
    print
    '冒泡'
    ori_list = [1, 2, 3, 5, 2, 9, 4, 7, 1, 0]
    print
    ori_list
    list_len = len(ori_list)
    for each in range(list_len - 1):
        for eachIn in range(list_len - each - 1):
            if ori_list[eachIn + 1] < ori_list[eachIn]:
                each_in1 = ori_list[eachIn + 1]
                each_in2 = ori_list[eachIn]
                ori_list[eachIn + 1] = each_in2
                ori_list[eachIn] = each_in1
                # 上边四行代码可以用一行代替 a[j], a[j+1] = a[j+1], a[j]
    print
    ori_list
    print
    '冒泡'


def selection_sort():
    # "每一次循环，最小的放左边"
    print
    '选择'
    ori_list = [1, 2, 3, 5, 2, 9, 4, 7, 1, 0]
    print
    ori_list
    list_len = len(ori_list)
    for i in range(list_len - 1):
        for j in range(list_len):
            if j + i + 1 > list_len - 1:
                break
            if ori_list[j + i + 1] < ori_list[i]:
                ori_list[i], ori_list[j + i + 1] = ori_list[j + i + 1], ori_list[i]
    print
    ori_list
    print
    '选择'


def selection_sort2():
    # "每一次循环，最小的放左边, 不使用if，使用sub list"
    print
    '选择'
    ori_list = [1, 2, 3, 5, 2, 9, 4, 7, 1, 0]
    print
    ori_list
    list_len = len(ori_list)
    for i in range(list_len - 1):
        for j in range(list_len)[i + 1:]:
            if ori_list[j] < ori_list[i]:
                ori_list[i], ori_list[j] = ori_list[j], ori_list[i]
    print
    ori_list
    print
    '选择'


def insertion_sort():
    # "从右侧未排序区域选择一个数，插入到左侧已排序的数组中的合适位置上"
    print
    "插入"
    ori_list = [1, 2, 3, 5, 2, 9, 4, 7, 1, 0]
    print
    ori_list
    list_len = len(ori_list)
    sorted_list = [ori_list[0]]  # 初始化sorted_list
    for i in range(list_len)[1:]:
        # 插入一共三种情况：1.插到最前面2.插到最后面3.插到中间
        if sorted_list[0] >= ori_list[i]:
            sorted_list.insert(0, ori_list[i])
            continue
        if sorted_list[len(sorted_list) - 1] <= ori_list[i]:
            sorted_list.append(ori_list[i])
            continue
        for j in range(len(sorted_list)):
            boolean1 = sorted_list[j] < ori_list[i]
            boolean2 = sorted_list[j + 1] >= ori_list[i]
            if boolean1 & boolean2:
                sorted_list.insert(j + 1, ori_list[i])
                break
    print
    sorted_list
    print
    "插入"


# bubble_sort()
# selection_sort()
# selection_sort2()
insertion_sort()
