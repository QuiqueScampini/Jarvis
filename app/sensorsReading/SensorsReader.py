from time import sleep
from multiprocessing import Process
from gpio.JarvisGpioSensors import JarvisGpioSensors


class SensorsReader(Process):

    def __init__(self, process_queue):
        Process.__init__(self)
        self.active = True
        self.distance_to_stop = 60
        self.process_queue = process_queue

    def run(self):
        while self.active:
            self.process_queue.put(self.feasibility_message())
            sleep(0.1)

    def stop(self):
        self.active = False

    def feasibility_message(self):
        return '{"messageType": 13' + \
               ', "front_left": ' + str(self.front_left()).lower() + \
               ', "front_right": ' + str(self.front_right()).lower() + \
               ', "back_left": ' + str(self.back_left()).lower() + \
               ', "back_right": ' + str(self.back_right()).lower() + \
               '}@'

    def front_left(self):
        return JarvisGpioSensors.get_front_left_distance() < self.distance_to_stop

    def front_right(self):
        return JarvisGpioSensors.get_front_right_distance() < self.distance_to_stop

    def back_left(self):
        return JarvisGpioSensors.get_back_left_distance() < self.distance_to_stop

    def back_right(self):
        return JarvisGpioSensors.get_back_right_distance() < self.distance_to_stop
