# import asyncio


def sub_gen():
    total = 0
    avg = None
    ind = 0
    while True:
        val = yield
        if val is None:
            break
        total += val
        ind += 1
        avg = total / ind
    return avg


def delegate_gen():
    # yield from проглотит StopIteration
    #  и достанет из него value
    avg = yield from sub_gen()
    print(avg)


# декоратор не занимается инициализацией
# @asyncio.coroutine
def main():
    deleg = delegate_gen()
    next(deleg)
    deleg.send(10)
    deleg.send(30)
    deleg.send(50)
    deleg.send(None)


try:
    main()
except StopIteration as e:
    print('StopIteration')

# main()  # StopIteration

# # run_until_complete проглатывает StopIteration,
# # если main() - корутина (@asyncio.coroutine)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()




