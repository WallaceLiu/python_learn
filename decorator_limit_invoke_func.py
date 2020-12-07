# coding=UTF-8
# !/usr/bin/env python
# filename decorator.py
import time
from functools import wraps


def decorator(func):
    "cache for function result, which is immutable with fixed arguments"
    print
    "initial cache for %s" % func.__name__
    cache = {}

    @wraps(func)
    def decorated_func(*args, **kwargs):
        # 函数的名称作为key
        key = func.__name__
        result = None
        # 判断是否存在缓存
        if key in cache.keys():
            (result, updateTime) = cache[key]
            # 过期时间固定为10秒
            if time.time() - updateTime < 10:
                print
                "limit call 10s", key
                result = updateTime
            else:
                print
                "cache expired !!! can call "
                result = None
        else:
            print
            "no cache for ", key
        # 如果过期，或则没有缓存调用方法
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
        return result

    return decorated_func


@decorator
def func(x):
    print('call func')


import time

func(1)
time.sleep(10)
func(1)
