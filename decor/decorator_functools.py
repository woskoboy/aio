import time
# import functools


def clock(func):

    def clocked(*args):
        name = func.__name__ + ', '.join(repr(arg) for arg in args)
        start = time.time()
        result = func(*args)
        stop = time.time() - start
        msg = ' function: {} time: {:.10f} result: {}'.format(name, stop, result)
        print(msg)
        return result

    return clocked


# @clock
# def factorial(n):
#     return 1 if n < 2 else n*factorial(n-1)
#
# print(factorial(5))
