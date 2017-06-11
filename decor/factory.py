def factory(active=True):
    """ Фабрика возвращает настоящий декоратор,
     применяемый к оригинальной функции"""
    def decorate(func):
        """ декоратор возвращает ф-ю: 
        либо оригин-ю либо новую - декорированную """
        def new_func(*args):
            res = func(*args)
            return float(res)

        if active:
            return new_func  # работаем с новой ф-ей
        else:
            return func  # либо всё с той же

    return decorate


@factory(active=False)
def f(n):
    return n

print(f(37))
