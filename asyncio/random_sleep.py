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
    number = random.randint(0, 10)
    print("GO SLEEP for {}".format(number))
    await custom_sleep(number)
    print("SLEPT for {}".format(number))

if __name__ == "__main__":
    startTime = time.time()

    aMultiTask = MyAsync()
    aMultiTask.add(factorial())
    aMultiTask.add(factorial())
    aMultiTask.run()

    endTime = time.time()
    print("TOTAL time: {}".format(endTime - startTime))
