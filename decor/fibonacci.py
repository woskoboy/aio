from decor.decorator_functools import clock
from functools import lru_cache

""" lru_cache кэширует результаты
    предыдущих вызовов функции:
    избегаем повторного вычисления с теми же аргументами.
    (из кэша вытесняются те элементы к кот. давно не было обращений)
"""


@lru_cache()
@clock
def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(30))
