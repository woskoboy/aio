data = dict(
    man=[75, 78, 84, 95],
    woman=[45, 39, 62])


def subgen_average():
    total = 0
    ind = 0
    avg = None
    while True:
        val = yield
        if val is None:
            break
        total += val
        ind += 1
        avg = total/ind
    return avg


def gen(result, key):
    while True:
        result[key] = yield from subgen_average()


def client():
    result = {}

    for key, weights in data.items():
        delegate = gen(result, key)
        next(delegate)
        for weight in weights:
            delegate.send(weight)
        delegate.send(None)

    print(result)


if __name__ == '__main__':
    client()
