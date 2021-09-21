# -*- coding: utf-8 -*-
"""
@time           : 2021/9/13 下午10:47
@author         : liuning
@file           : memprofile_int.py
@description    : ...
"""
from memory_profiler import *

from datetime import datetime


@profile
def my_func():
    beg = datetime.now()
    a = {}
    for i in range(1000000):
        a[str(i)] = i
    print("+++++++++")
    del a
    print("+++++++++")
    end = datetime.now()
    print("time:", end - beg)


if __name__ == '__main__':
    my_func()
