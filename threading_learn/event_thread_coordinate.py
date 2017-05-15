from threading import Thread, Event
import time


def counter_down(n, evt):
	while n > 0:
		evt.wait()
		print('T-down %s' % n)
		time.sleep(1)
		n -= 1

def counter_up(n, evt):
	i = 0
	while i < n:
		i += 1
		evt.wait()
		print('T-up %s' % i)
		time.sleep(1)
		

evt = Event()

t1 = Thread(target=counter_up, args=(5,evt))
t1.start()

t2 = Thread(target=counter_down, args=(5, evt))
t2.start()

time.sleep(4)
evt.set()