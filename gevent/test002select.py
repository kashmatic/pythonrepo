# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
"""
Asyncio class to Initialize, add and run the tasks

Example:
$ python test002select.py

Notes:
- select() blocking call that polls the current greenlet
- select(<input>, <output>, <error>, <timeout>)
- for network and IO bound functions
- greenlet is a lightweight coroutine
"""

import time
import gevent
from gevent import select

start = time.time()

## function to get the time run
tic = lambda: 'at {:1.1f} seconds'.format(time.time() - start)

def dothis():
    """
    Wait for I/O operation
    """
    print('Start in dothis at {}'.format(tic()))
    select.select([], [], [], 2)
    print('In dothis again at {}'.format(tic()))

def dothat():
    """
    Wait for I/O operation
    """
    print('Start in dothat at {}'.format(tic()))
    select.select([], [], [], 2)
    print('In dothat again at {}'.format(tic()))

def onethis():
    """
    Do anything
    """
    print("one this at {}".format(tic()))
    gevent.sleep()

gevent.joinall([
    gevent.spawn(dothis),
    gevent.spawn(dothat),
    gevent.spawn(onethis),
])
