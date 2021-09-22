# err_reraise.py
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

"""result:

Traceback (most recent call last):
  File "/Users/liuning/project/python_learn/debug/err_reraise.py", line 18, in <module>
    bar()
  File "/Users/liuning/project/python_learn/debug/err_reraise.py", line 12, in bar
    foo('0')
  File "/Users/liuning/project/python_learn/debug/err_reraise.py", line 6, in foo
    raise ValueError('invalid value: %s' % s)
ValueError: invalid value: 0

"""
