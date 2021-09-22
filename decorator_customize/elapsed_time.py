# -*- coding: utf-8 -*-
"""
@time           : 2021/9/21 下午11:48
@author         : liuning
@file           : elapsed_time.py
@description    : ...
"""
import datetime
import logging

def elapsed_time(func):
    """
    elapsed time of function
    :param func:
    :return:
    """

    def wrapper(*args, **kw):
        start_time = datetime.datetime.now()
        res = func(*args, **kw)
        over_time = datetime.datetime.now()
        etime = (over_time - start_time).total_seconds()
        logging.info('Elapsed time: current function <{0}> is {1} s'.format(func.__name__, etime))
        return res

    return wrapper