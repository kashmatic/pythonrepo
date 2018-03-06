# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
"""
Asyncio example to sleep for random time

Example:
$ python random_sleep.py

"""

import asyncio
import time
import random

from myasync import MyAsync

async def custom_sleep(number):
    """
    Sleep for a given amount of time
    """
    # print('SLEEP {}'.format(datetime.now()))
    await asyncio.sleep(number)

async def factorial():
    """
    Randomly get a number to sleep
    """
    number = random.randint(0, 5)
    print("GO SLEEP for {}".format(number))
    await custom_sleep(number)
    print("SLEPT for {}".format(number))

if __name__ == "__main__":
    startTime = time.time()

    aMultiTask = MyAsync()
    # for i in range(0, 5):
    aMultiTask.add(factorial())
    # aMultiTask.addlist([factorial(), factorial(), factorial()])
    aMultiTask.run()

    print("TOTAL time: {}".format(time.time() - startTime))
