# coding=utf-8
# function

def add(*args):
    sum = 0
    for item in args:
        sum += item
    print sum


def add2(**args):
    sum = 0
    for value in args.values():
        sum += value
    print sum


add(1, 2, 3, 4)
add2(p=1, t=2)

"""
所谓的“内置作用域”就是Python内置的那些标识符，我们之前用过的input、print、int等都属于内置作用域。

什么是闭包
"""
