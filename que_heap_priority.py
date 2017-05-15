""" Элемент с наименьшим значением всегда находится
в позиции с индексом 0. Это свойство может с успехом быть
 задействовано в приложениях, где особенно частый доступ
  необходим к наименьшему элементу, но полную сортировку
   проводить накладно."""

""" Метод heappop() всегда возвращает «наименьший» элемент,
 что является ключом к тому, чтобы заставить очередь удалять
  правильные элементы"""

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)  # [-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())


"""
# импорт двух функций очереди под именами,
 принятыми в данной статье

from heapq import heappush as insert, heappop as extract_maximum

pq = []  # инициализация списка

# вставка в очередь элемента "p" с индексом 0 и приоритетом 4

insert(pq, (4, 0, "p"))
insert(pq, (2, 1, "e"))
insert(pq, (3, 2, "a"))
insert(pq, (1, 3, "h"))

# вывод четырёх элементов в порядке возрастания приоритетов

print(extract_maximum(pq)[-1] + extract_maximum(pq)[-1] + extract_maximum(pq)[-1] + extract_maximum(pq)[-1])
"""