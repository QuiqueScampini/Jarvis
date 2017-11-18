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
            sleep(0.2)

    def stop(self):
        self.active = False

    def feasibility_message(self):
        return '{"messageType": "12"' + \
               ', "free_front_left": ' + str(self.free_front_left()).lower() + \
               ', "free_front_right": ' + str(self.free_front_right()).lower() + \
               ', "free_back_left": ' + str(self.free_back_left()).lower() + \
               ', "free_back_right": ' + str(self.free_back_right()).lower() + \
               '}@'

    def free_front_left(self):
        return JarvisGpioSensors.get_front_left_distance() > self.distance_to_stop

    def free_front_right(self):
        return JarvisGpioSensors.get_front_right_distance() > self.distance_to_stop

    def free_back_left(self):
        return JarvisGpioSensors.get_back_left_distance() > self.distance_to_stop

    def free_back_right(self):
        return JarvisGpioSensors.get_back_right_distance() > self.distance_to_stop
