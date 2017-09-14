from threading import Thread
from queue import Queue
import time
import logging


class ProcessHandler(Thread):

    val = None
    active = None
    process_queue = Queue()

    def __init__(self, val):
        Thread.__init__(self)
        self.setName('ProcessHandler')
        self.val = val
        self.active = True

    def run(self):
        logging.info('Start handling messages')
        while self.active:
            if not self.process_queue.empty():
                message = self.process_queue.get()
                logging.debug('Getting ' + str(message) + ' : ' + str(self.process_queue.qsize()) + ' items in queue')
            time.sleep(1)

    def stop(self):
        self.active = False
