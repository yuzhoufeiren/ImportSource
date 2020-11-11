import gevent
from gevent import monkey
import time

monkey.patch_all()

def test1(temp):

    time.sleep(0.001)
    print(temp)

def test2(temp):
    time.sleep(0.001)
    print(temp)

gevent.joinall([
    gevent.spawn(test1, "slw1.txt"),
    gevent.spawn(test2, "slw2.txt")
,
])