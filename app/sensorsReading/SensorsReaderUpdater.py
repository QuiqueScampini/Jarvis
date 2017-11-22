from threading import Thread
import json
from driver.CarDriver import CarDriver


class SensorsReaderUpdater(Thread):

    def __init__(self, sensors_reader_queue, process_queue):
        Thread.__init__(self)
        self.setName('SensorsReaderUpdater')
        self.sensors_reader_queue = sensors_reader_queue
        self.process_queue = process_queue
        self.active = True

    def run(self):
        while self.active:
            messages = self.sensors_reader_queue.get(True)
            if messages:
                for message in messages.split('@'):
                    if message:
                        self.process_message(message)

    def process_message(self, message):
        try:
            self.process_json_action(json.loads(message))
        except Exception as error:
            pass

    def process_json_action(self, json_action):
        CarDriver.set_sensor_values(json_action["free_front_left"],
                                    json_action["free_front_right"],
                                    json_action["free_back_left"],
                                    json_action["free_back_right"],
                                    self.process_queue)

    def stop(self):
        self.active = False
