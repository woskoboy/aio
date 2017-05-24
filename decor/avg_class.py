# class Saver:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __call__(self, *args, **kwargs):
#         self.a += 1
#         self.b += 1
#         print(self.__str__())
#
#     def __repr__(self):
#         return 'a: {} b: {}'.format(self.a, self.b)
#
# obj = Saver()
#
# obj()
# obj()
# obj()


class Averager:
    def __init__(self):
        self.values = []

    def __call__(self, val):
        self.values.append(val)
        total = sum(self.values)/len(self.values)
        print(total)

avg = Averager()
avg(10)
avg(11)
avg(12)
print(avg.values)
