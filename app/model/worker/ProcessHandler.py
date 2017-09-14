from queue import Queue
from threading import Thread


class ProcessHandler(Thread):
    process_queue = Queue()

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Start handling messages")
