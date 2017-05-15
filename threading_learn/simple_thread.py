from threading import Thread
import time


class Counter:
    def __init__(self):
        self.finished = False

    def run(self, n):
        while not self.finished and n > 0:
            print('T-minus %s' % n)
            time.sleep(1)
            n -= 1

    def terminate(self):
        self.finished = True


c = Counter()
t = Thread(target=c.run, args=(5,))
t.start()

# time.sleep(2)
# c.terminate()

# def counter(n):
# 	while n > 0:
# 		print('T-minus %s' % n)
# 		time.sleep(1)
# 		n -= 1


# t = Thread(target=counter, args=(10,))
# t.start()

# print('hello')
# print('World')
# time.sleep(0.5)
# print('tyrty')
