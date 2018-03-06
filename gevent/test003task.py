# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
"""
Asyncio class to Initialize, add and run the tasks

Example:
$ python test003task.py

Notes:
- non-deterministic task
- means output is not guaranteed to give same result for same input
"""

import random
import gevent

def task(num):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2)*0.01)
    print('Task {} done'.format(num))

def doasync():
    """
    Create a list of tasks and run it

    Notes:
    - gevent.spawn wraps a given function inside of a greenlet thread
    - gevent.joinall blocks current program to run all greenlets
    - gevent.joinall waits for all the greenlets to terminate
    """
    alltasks = []
    for i in range(10):
        alltasks.append(gevent.spawn(task, i))
    gevent.joinall(alltasks)

doasync()
