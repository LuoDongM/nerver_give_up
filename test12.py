#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author = LuoDongMei
# Date = 2021/3/22
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
from math import sqrt
leap = 1
count = 0
for num in range(101,200):
    k = int(sqrt(num+1))
    for i in range(2, k+1):
        if num % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%4ld' % num, end = ' ')
        count += 1
        if count % 10 == 0:
            print()
    leap = 1
print("\n101-200共有素数：%d" % count)
