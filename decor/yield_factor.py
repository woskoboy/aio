class Fact:
    def __init__(self, n):
        self.n = n
        self.res = 1

    def __iter__(self):
        while self.n:
            yield self.res
            self.res *= self.n
            self.n -= 1

res = [i for i in Fact(5)]
print(res)


# def f():
#     vals = 1
#     while True:
#         n = yield vals
#         vals *= n
#
# f = f()
# next(f)
# res = [f.send(i) for i in range(1, 6)]
# print(res)


# def initze(func):
#     f = func()
#     next(f)
#     return f
#
#
# @initze
# def calc():
#     values = 1
#     while True:
#         n = yield
#         if n is None:
#             break
#         values *= n
#     return values
#
#
# def fact(n):
#     for i in range(1, n+1):
#         calc.send(i)
#     try:
#         calc.send(None)
#     except StopIteration as e:
#         print(e.value)
#
# fact(45000)

