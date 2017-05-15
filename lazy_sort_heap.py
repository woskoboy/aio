"""
Пример ленивой сортировки. heapq.heapify по месту делает из списка кучу за
линейное время,а heapq.heappop извлекает за тем верхний элемент.
"""

import heapq


def lazy_sort(iterable):
    lst = list(iterable)
    heapq.heapify(lst)
    while lst:
        yield heapq.heappop(lst)


string_ = "".join([c for c in lazy_sort(u"абракадабра")])
print(string_)
