# -*- coding: utf-8 -*-
"""
@time           : 2021/9/13 下午10:59
@author         : liuning
@file           : memusage.py
@description    : ...
"""

from memory_profiler import memory_usage

#
# def f(a, n=100):
#     import time
#     time.sleep(2)
#     b = [a] * n
#     time.sleep(1)
#     return b
#
#
# print(memory_usage((f, (2,), {'n': int(1e6)})))

mem_usage = memory_usage(-1, interval=.2, timeout=1)
print(mem_usage)
