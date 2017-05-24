import functools
from operator import itemgetter, attrgetter, mul
from collections import namedtuple

res = functools.reduce(lambda a, b: a * b, range(1, 6))
# print(res)

data = [
    ('RU', 'Russia', 'r', (36, 45)),
    ('JN', 'Japanise', 'j', (87, 44)),
    ('CN', 'China', 'c', (68, 78)),
    ('US', 'USA', 'u', (63, 91)),
]

MStation = namedtuple('MStation', 'code letter coord name')
Coord = namedtuple('Coord', 'lat lon')
metro = []
for code, name, letter, (lat, lon) in data:
    metro.append(MStation(
        code=code, letter=letter, name=name, coord=Coord(lat=lat, lon=lon)))

""" сортировка станций по выбранному атрибуту """
for station in sorted(metro, key=attrgetter('coord.lon')):
    print(station)

"""сортировка кортежей по n-ому элементу"""
sd = sorted(data, key=itemgetter(1))
print(sd)
'''выборка элементов из кортежей'''
ig = itemgetter(0, 3)
for city in data:
    code, (l, lat) = ig(city)
    print(code, l, lat)

mulon = functools.partial(mul, 3)
res = map(mulon, range(1, 10))
print(list(res))


def getme(a, *c):
    for n in c:
        a *= n
    print(a)


values = [i for i in range(3, 6)]
getme(1, 2, *values)
# or
new_getme = functools.partial(getme, 1)
vals = [n for n in range(2, 6)]
new_getme(*vals)

# def anyfunc(arg):
#   a = 1
#   b = 'str'
#   return b
#
# class A:
#   pass
#
# print(set(dir(anyfunc))-set(dir(A())))

# def fact(n):
#   r  = k = 1
#   while k < n:
#        r = r * (k+1)
#        k+=1
#   return r
#
# print(fact(5))

# def factorial(n):
#   return 1 if n < 2 else n*factorial(n-1)
# print(factorial(5))


# '''factorial recurse'''
# class MyException(Exception):
#   def __init__(self, val):
#       self.value = val


# def fact(res, n):
#   if n <= 1:
#       raise MyException(res) from Exception
#   n -= 1
#   fact(n*res, n)

# try:
#   fact(1, 6)
# except MyException as e:
#   print('result', e.value)

# '''factorial yield'''

# def fac():
#   values = 1
#   while True:
#       n = yield
#       if n == None:
#           break
#       values *= n
#   return values

# fun = fac()
# next(fun)
# for i in range(5,1,-1):
#   fun.send(i)

# try:
#   fun.send(None)
# except Exception as e:
#   print('result', e.value)



# CONST = 10

# last_count = 5495
# count = 5450

# urls = []

# dif_count = last_count - count
# if dif_count < CONST:
#   urls.append((dif_count,0))
# else:
#   k, o = divmod(dif_count, CONST)
#   for offset in range(k):
#       urls.append((CONST,CONST*offset))
#   urls.append((o, CONST*k))

# print(urls)

# from collections import namedtuple

# ranks = [i for i in range(2,11)]+list('JQKA')
# suits = 'krest vini romb love'.split()

# Card = namedtuple('Card','rank suit')

# class Deck:
#   def __init__(self):
#       self.__cards = [Card(rank, suit) for suit in suits for rank in ranks]

#   def __getitem__(self, pos):
#       return self.__cards[pos]

#   def __len__(self):
#       return len(self.__cards)


# deck = Deck()

# s_priority = dict(vini=3,love=2,romb=1, krest=0)

# def high(card):
#   k = len(s_priority)
#   r_priority = ranks.index(card.rank)
#   return r_priority*k+s_priority[card.suit]

# for card in sorted(deck, key=high):
#   print(card)

# print(len(deck))
