# -*- coding: utf-8 -*-
"""
@time           : 2021/9/21 下午11:48
@author         : liuning
@file           : synchronized.py
@description    : ...
"""
import threading


def synchronized(func):
    """
    simple lock
    :param func:
    :return:
    """
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func
