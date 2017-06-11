import weakref


class Watcher:
    instances = weakref.WeakSet()

    def __init__(self):
        self.__class__.instances.add(self)

a = Watcher()
b = Watcher()
c = Watcher()
print(list(Watcher.instances))
c = 1
a = 2
print(list(Watcher.instances))

# class Cheese:
#     def __init__(self, kind):
#         self.kind = kind
#
#     def __repr__(self):
#         return 'Cheese %s' % self.kind
#
# catalog = [
#     Cheese('Red'),
#     Cheese('Green'),
#     Cheese('Blue'),
# ]
#
# stock = weakref.WeakValueDictionary()
# for cheese in catalog:
#     stock[cheese.kind] = cheese
#
# print(list(stock.items()))
# del catalog
# del cheese
# print(list(stock.items()))
