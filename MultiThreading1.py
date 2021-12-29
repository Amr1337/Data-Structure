import threading
from threading import Thread
import time


def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):

    th = Thread(target=sleepMe, args=(i,))
    th.start()

print(threading.active_count())