import logging
import json
from threading import Thread
from driver.CarDriver import CarDriver


class ProcessHandler(Thread):
    def __init__(self, process_queue, message_server, ultron, jarvis):
        Thread.__init__(self)
        self.setName('ProcessHandler')
        self.active = True
        self.ultron = ultron
        self.jarvis = jarvis
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
                for message in messages[1].split('@'):
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
            logging.error(str(error))

    def process_json_action(self, json_action):
        message_type = json_action["messageType"]

        if message_type == "0":  # Start Driving
            """Start Driving"""
            self.jarvis.start_filming()
        elif message_type == "1":  # Movement
            CarDriver.process_movement(json_action["angle"], json_action["power"])
        elif message_type == "3":  # Auto Return
            self.jarvis.stop_filming()
            self.ultron.return_origin()
            pass
        elif message_type == "12":  # Sensors Values
            CarDriver.set_sensor_values(json_action["free_front_left"],
                                        json_action["free_front_right"],
                                        json_action["free_back_left"],
                                        json_action["free_back_right"])
        elif message_type == "13":  # Shutdown
            CarDriver.stop_forward()
        elif message_type == "14":  # Shutdown
            CarDriver.stop_backward()
