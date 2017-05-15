from queue import Queue
from itertools import cycle

import time
from threading import Thread

'''Экземпляры Queue уже имеют все нужные блокировки,
поэтому они могут безопасно стать общими
для любого количества потоков.'''


def client(queue, name):
    while True:
        val = queue.get()
        print('Client {} get value: {}'.format(name, val))
        if not val:
            queue.put(val)
            break


class Provider:

    def __init__(self, queue, data):
        self.queue = queue
        self.data = data

    def set_data(self, val):
        self.queue.put(val)

    def generate_data(self):
        while True:
            try:
                val = next(self.data)
                self.set_data(val)
                print('Provider put value: ', val)
                time.sleep(0.2)
            except StopIteration:
                pass

# q = Queue()
# data = cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, 11, 12])
#
# p = Provider(q, data)
# Thread(target=p.generate_data).start()
#
# Thread(target=client, args=(q, 'A')).start()
# Thread(target=client, args=(q, 'B')).start()




