# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
"""
Asyncio class to Initialize, add and run the tasks

Example:
$ python test001.py

Notes:
- Break task from larger task to collection of subtasks
- Subtasks run asynchronously
- switching between subtasks is called context switch
- context switch is done through yield
- yielding is done through gevent.sleep
"""

import gevent

def dothis():
    """
    Sleep for a minute
    """
    print('Start in dothis')
    gevent.sleep(0)
    print('In dothis again')

def dothat():
    """
    Sleep for a minute
    """
    print('Start in dothat')
    gevent.sleep(0)
    print('In dothat again')

gevent.joinall([
    gevent.spawn(dothis),
    gevent.spawn(dothat)
])
