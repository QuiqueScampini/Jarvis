from threading import Thread
from queue import Queue
import time
import logging
import json

from model.driver import CarDriver
from model.util import JarvisManager


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
                if message:
                    self.process_message(message)
                    logging.debug('Getting ' + str(message) + ' : ' + str(self.process_queue.qsize()) + ' items in queue')
            time.sleep(0.2)

    def stop(self):
        self.active = False

    def process_message(self, message):

        try:
            json_action = json.loads(message)
        except Exception as error:
            JarvisManager.message_server.send_message('{"messageType": 9,"message": "mensaje","stackTrace": "'
                                                      + str(error) + '"}')
            return

        message_type = json_action["messageType"]

        if message_type == "1":
            logging.info('Move Car')
            self.process_movement(json_action)
        elif message_type == "6":
            logging.info('Llego 6')
        pass

    def process_movement(self, json_action):
        CarDriver.CarDriver.move_car(json_action)
        pass
