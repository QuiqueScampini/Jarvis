import time
import logging
import json
from threading import Thread
from queue import Queue
from model.driver.CarDriver import CarDriver


class ProcessHandler(Thread):

    val = None
    active = None
    process_queue = Queue()

    def __init__(self):
        Thread.__init__(self)
        self.setName('ProcessHandler')
        self.active = True

    def run(self):
        logging.info('Start handling messages')
        while self.active:
            if not self.process_queue.empty():
                """TODO El True en get hace que sea bloqueante
                message = self.process_queue.get(True)"""
                message = self.process_queue.get()
                if message:
                    self.process_message(message)
                    logging.debug('Getting ' + str(message)
                                             + ' : '
                                             + str(self.process_queue.qsize())
                                             + ' items in queue')
            time.sleep(0.2)

    def stop(self):
        self.active = False

    def add_to_queue(self, message_str):
        self.process_queue.put(message_str)

    def process_message(self, message):
        try:
            json_action = json.loads(message)
        except Exception as error:
            JarvisManager.send_message('{"messageType": 9,"message": "mensaje","stackTrace": "'
                                       + str(error) + '"}')
            return

        message_type = json_action["messageType"]

        if message_type == "1":
            CarDriver.process_movement(json_action)
        elif message_type == "6":
            logging.info('Llego 6')
        pass
