#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(*args):
    for arg in args:
        print(arg)


f(1, 2, 3, 4, 5)


def f2(**kwargs):
    for arg in kwargs:
        print(arg, kwargs[arg])


f2(a=1, b=2, c=3)
