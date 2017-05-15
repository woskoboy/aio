""" slots """
# class User:
#     __slots__ = ['name', 'last_name', 'age']
#
#     def __init__(self, name, lname, age):
#         self.name = name
#         self.last_name = lname
#         self.age = age
#
# u1 = User('Vasya', 'Pupkin', 32)
# u2 = User('Tolya', 'Pupkin', 22)
# u3 = User('Jenya', 'Kim', 45)
#
# u2.age = 100
# print(u2.age)

""" sorted max min """
# from heapq import nlargest
#
# portfolio = [
#     {'name': 'GOOG', 'shares': 50},
#     {'name': 'YHOO', 'shares': 75},
#     {'name': 'AOL', 'shares': 20},
#     {'name': 'SCOX', 'shares': 65}
# ]
#
# sdic = sorted(portfolio, key=lambda itm: itm['shares'])
# print(sdic)
#
# m = min(portfolio, key=lambda itm: itm['shares'])
# print(m)
#
# print(nlargest(2, portfolio, key=lambda itm: itm['shares']))
#
# sdic = sorted(portfolio, key=lambda itm: itm['shares'])
# print(sdic[-2:])

""" date """

# import re
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# pat = re.compile(r'(\d+)/(\d+)/(\d+)')
# g = (d.groups() for d in pat.finditer(text))
# print(list(g))


""" missing key """

# class Subdict(dict):
#
#     def __missing__(self, key):
#         return key
#
# s = '{who} have {n} friends?'
# print(s.format_map(Subdict(who='we')))

""" revers """

# class ReversCounter:
#     """Reversed Counter"""
#
#     def __init__(self, begin, end, step):
#         self._begin = begin
#         self._end = end
#         self._step = step
#
#     def __iter__(self):
#         while self._begin < self._end:
#             yield self._begin
#             self._begin += self._step
#
#     def __reversed__(self):
#         while self._begin < self._end:
#             yield self._end
#             self._end -= self._step
#
# rc = ReversCounter(0, 10, 0.5)
# print(list(reversed(rc)))

""" объект-генератор с дополнительным
    состоянием (атрибут с тек. историей)"""

# from collections import deque
#
# class linehistory:
#
#     def __init__(self, lines, histlen=3):
#         self.lines = lines
#         self.history = deque(maxlen=histlen)
#
#     def __iter__(self):
#         for lineno, line in enumerate(self.lines, 1):
#             self.history.append((lineno, line))
#             yield line
#
#     def clear(self):
#         self.history.clear()
#
# with open('book.txt') as f:
#     lines = linehistory(f)
#     for line in lines:
#         if 'python' in line:
#             for lineno, hline in lines.history:
#                 print('{}:{}'.format(lineno, hline), end='')

""" drop lines"""
# with open('book.txt') as f:
#     lines = (line for line in f if not line.startswith('#'))
#     for line in lines:
#         print(line, end='')

""" отобразить слова к строкам,
    где они встречаются """

# from collections import defaultdict
#
# result = defaultdict(list)
# with open('book.txt') as f:
#     for inx, line in enumerate(f, 1):
#         for word in line.split():
#             result[word].append(inx)
#
# print(result, end='')

""" """
fname = 'first_name'
lname = 'last_name'
d = {}
d[fname, lname] = 'Vasya Pupkin'
print(d)

