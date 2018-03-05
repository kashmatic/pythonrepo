# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103
"""
Asyncio class to Initialize, add and run the tasks

Example:
$ python myasync.py

"""

import asyncio

class MyAsync():
    """
    Class to run asyncio tasks
    """

    def __init__(self):
        """
        Initialize an event loop with empty task list
        """
        self.loop = asyncio.get_event_loop()
        self.tasks = []

    def add(self, atask):
        """
        Add a tast to the loop

        Keywork arguments:
        aTask -- function call with parameters
        """
        self.tasks.append(asyncio.ensure_future(atask))

    def run(self):
        """
        Run the list of tasks and close the loop
        """
        self.loop.run_until_complete(asyncio.wait(self.tasks))
        self.loop.close()

if __name__ == "__main__":
    myasync = MyAsync()
    myasync.add(asyncio.sleep(2))
    myasync.run()
