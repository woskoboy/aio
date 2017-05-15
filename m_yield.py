def cor(a):
    print("Coroutine started with a = ", a)
    b = yield a
    print('Coroutine received b = ', b)
    c = yield a + b
    print('Coroutine received c = ', c)

my_cor = cor(10)

print(next(my_cor))

print(my_cor.send(20))
print(my_cor.send(99))


