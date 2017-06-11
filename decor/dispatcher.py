from collections import abc
import numbers
from functools import singledispatch


@singledispatch
def base_handler(obj):
    content = repr(obj)
    return 'Something object: {}'.format(content)


@base_handler.register(str)
def _(text):
    return 'String: %s' % text


@base_handler.register(numbers.Integral)
def _(digitals):
    return 'Digitals: {}'.format(digitals*10)


@base_handler.register(abc.MutableSequence)
@base_handler.register(tuple)
def _(seq):
    items = ', '.join(base_handler(it) for it in seq)
    return items


def func():
    pass

print(base_handler('hello'))
print(base_handler([0, ('hi', ['li', 1]), func]))
