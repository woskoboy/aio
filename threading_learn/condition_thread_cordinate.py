from threading import Thread, Condition
import time


class PTimer(object):
    def __init__(self, n):
        self._condition = Condition()
        self._interval = n
        self._flag = 0

    def run(self):
        """ ждёт интервал и хватает замок;
        инвертирует флаг, извещает остальных и отпускает замок"""
        while True:
            time.sleep(self._interval)
            with self._condition:
                self._flag ^= 1
                self._condition.notify_all()

    def start(self):
        t = Thread(target=self.run)
        t.start()

    def wait_notify(self):
        """ захват замка """
        with self._condition:
            last_flag = self._flag
            while last_flag == self._flag:
                self._condition.wait()


ptimer = PTimer(3)
ptimer.start()


def counter_down(n):
    while n > 0:
        # evt.wait()
        ptimer.wait_notify()
        print('T-down %s' % n)
        time.sleep(1)
        n -= 1


def counter_up(end):
    n = 0
    while n < end:
        n += 1
        # evt.wait()
        ptimer.wait_notify()
        print('T-up %s' % n)
        time.sleep(1)


Thread(target=counter_down, args=(5,)).start()
Thread(target=counter_up, args=(5,)).start()
