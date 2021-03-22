#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author = LuoDongMei
# Date = 2021/3/22
# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

#输出第10个斐波纳列数列
print(fib(10))