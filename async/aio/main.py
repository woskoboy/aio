import asyncio


@asyncio.coroutine
def do_any(name, time):
    yield from asyncio.sleep(time)
    print('Task №{} finished after {} seconds'.format(name, time))


def main():
    loop = asyncio.get_event_loop()
    coros = [do_any(i, i * 2) for i in range(3)]

    """ asyncio.wait - сопрограмма (сопр.ф-я),
        кот. завершится, когда завершатся все переданные ей coro или Future.
        Обертывает каждую coro объектом Task. 
        Возвращает объект-сопограмму (генератор)"""
    wait_coros = asyncio.wait(coros)

    """ Для управ-я сопр-й передаем её этой ф-ии.  
        Она обертывает полученный объект объектом Task
        Под капотом управляет coro|Future|Task(объектом wait_coros) с пом. yield from """
    r, _ = loop.run_until_complete(wait_coros)  # крутит цикл пока сопрограмма wait_coros не завершится.
    # r - множество завершенных Future-объектов; _ - множество незавершенных

    loop.close()


main()
