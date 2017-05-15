import threading

cv = threading.Condition()


class Item:
    """Класс-контейнер для элементов, которые будут потребляться
    в потоках"""

    def __init__(self):
        self._items = []

    def is_available(self):
        return len(self._items) > 0

    def get(self):
        return self._items.pop()

    def make(self, i):
        self._items.append(i)


item = Item()


def consume():
    """Потребление очередного элемента (с ожиданием его появления)"""
    cv.acquire()
    while not item.is_available():
        cv.wait()
    it = item.get()
    cv.release()
    return it


def consumer():
    while True:
        print(consume())


def produce(i):
    """Занесение нового элемента в контейнер и оповещение потоков"""
    cv.acquire()
    item.make(i)
    cv.notify()
    cv.release()


p1 = threading.Thread(target=consumer, name="t1")
p1.setDaemon(True)
p2 = threading.Thread(target=consumer, name="t2")
p2.setDaemon(True)
p1.start()
p2.start()
produce("ITEM1")
produce("ITEM2")
produce("ITEM3")
produce("ITEM4")
p1.join()
p2.join()
