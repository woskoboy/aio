class Deco:
    def __call__(self, func):
        def deco(*args):
            res = func(*args)
            return type(res), res
        return deco


@Deco()
def f(val):
    return val

print(*f(5))

