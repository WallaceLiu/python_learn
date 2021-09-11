# -*- coding: utf-8 -*-
"""
@time           : 2021/9/11 下午12:15
@author         : liuning
@file           : wordcount.py
@description    : ...
"""
from toolz import comp, frequencies, partial


def stem(word):
    """ Stem word to primitive form """
    return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")


wordcount = comp(frequencies, partial(map, stem), str.split)

if __name__ == '__main__':
    print(wordcount("This cat jumped over this other cat!"))
    # prints {'this': 2, 'cat': 2, 'jumped': 1, 'over': 1, 'other': 1}
