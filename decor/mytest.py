def f_float(f_string):
    def tmp_f(*args):
        res = f_string(*args)
        return float(res)
    return tmp_f


def f_string(f):
    def tmp_s(*args):
        dig = f(*args)
        return str(dig)
    return tmp_s


# @f_float
@f_string
def f(dig):
    print('link to ', f.__name__)
    return dig


res = f(78)
print(type(res), res)

