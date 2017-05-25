from decor.decorater import clock


@clock
def factorial(n):
    print(factorial.__name__)  # clocked
    # теперь вызов factorial(n-1) на самом деле вызывает clocked(n-1)
    return 1 if n < 2 else n*factorial(n-1)  # снова проваливаемся в clocked

print('result: ', factorial(5))

