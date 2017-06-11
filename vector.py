from array import array

import math


class Vector2D:

    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        """ благодаря этому можем распаковывать *self"""
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        """ сравниваем как кортежи """
        return tuple(self) == tuple(other)

    def __abs__(self):
        """ длина вектора от начала координат до точки x,y: sqrt(x*x+y*y) """
        return math.hypot(*self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __str__(self):
        return str(tuple(self))

    def __bool__(self):
        """ True при длине вектора отличной от нуля"""
        return bool(abs(self))

    def __repr__(self):
        """ Vector2D(x,y) """
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    @classmethod
    def frombytes(cls, octets):
        """ читаем typecode из первого байта; 
        из двоичной посл-ти октетов создаем объект memoryview
        и приводим его к типу typecode"""
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)


v1 = Vector2D(4, 3)
print(bool(v1))
