def clock(func):

    def clocked(val):       # возникла рекурсия, т.к. func вызывает clocked
        result = func(val)  # продолжаем проваливаться пока не вернется результат (равный 1),

        print(result)       # тогда он будет напечатан
        return result       # и передан выше (где умножен на n и передан еще выше в вызвавшаю функцию и т.д.)

    return clocked
