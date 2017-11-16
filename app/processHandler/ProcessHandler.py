import logging
import json
from threading import Thread
from driver.CarDriver import CarDriver


class ProcessHandler(Thread):
    def __init__(self, process_queue, message_server):
        Thread.__init__(self)
        self.setName('ProcessHandler')
        self.active = True
        self.process_queue = process_queue
        self.message_server = message_server
        CarDriver.message_server = message_server

    def run(self):
        logging.info('Start handling messages')
        while self.active:
            logging.info('Waiting Message')
            messages = self.process_queue.get(True)
            if messages:
                logging.info('Processing messages')
                for message in messages.split('@'):
                    if message:
                        self.process_message(message)
                logging.debug('Getting ' + str(messages)
                              + ' : '
                              + str(self.process_queue.qsize())
                              + ' items in queue')

    def stop(self):
        self.active = False

    def process_message(self, message):
        try:
            self.process_json_action(json.loads(message))
        except Exception as error:
            logging.error('{"messageType": 9,"message": ' + message + ' ,"stackTrace": "'
                          + str(error) + '"}')

    @staticmethod
    def process_json_action(json_action):
        message_type = json_action["messageType"]

        if message_type == "1":
            """Movement"""
            CarDriver.process_movement(json["angle"], json["power"])
        elif message_type == 12:
            """Stop"""
            logging.info('The mother fucker told me to stop')
            CarDriver.stop()
        elif message_type == 13:
            logging.info('Message 13')
            CarDriver.set_sensor_values(json["front_left"], json["front_right"], json["back_left"], json["back_right"])
