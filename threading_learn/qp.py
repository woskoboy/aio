from heapq import heappop, heappush
from threading import Thread, Condition

import time

from threading_learn.q import Provider, client


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0
        self.cv = Condition()

    def put(self, val):
        """ used of provider to put data of the queue"""
        priority, item = val
        with self.cv:
            heappush(self.queue, (-priority, self.count, item))
            self.count += 1
            self.cv.notify()

    def get(self):
        """used of client to get data from the queue"""
        with self.cv:
            while not self.queue:
                self.cv.wait()
            return heappop(self.queue)[-1]

items = [(4, 'C'), (-5, 'G'), (8, 'A'), (3, 'D'),
         (-1, 'F'), (3, 'E'), (-7, 'H'), (6, 'B'), (19, 'HIGH')]

pq = PriorityQueue()

p = Provider(pq, iter(items))
Thread(target=p.generate_data).start()
time.sleep(5)

Thread(target=client, args=(pq, 'clientA')).start()
Thread(target=client, args=(pq, 'clientB')).start()
Thread(target=client, args=(pq, 'clientC')).start()




