import logging
from threading import Thread
from time import sleep
from model.gpio.JarvisGpio import JarvisGpio
from model.util.Constant import Constant
from model.util.JarvisManager import JarvisManager


class CollisionDetector(Thread):

    distance_to_stop = 0.5
    can_go_forward = True
    can_go_backward = True

    def __init__(self):
        Thread.__init__(self)
        self.setName('CollisionDetector')
        self.active = True

    def run(self):
        while self.active:
            logging.info('Detecting collisions and shit')
            actual_speed = JarvisGpio.get_speed()
            CollisionDetector.can_go_forward = self.get_movement_feasibility(self.get_left_front_distance(),
                                                                             self.get_right_front_distance(),
                                                                             self.moving_forward(actual_speed))
            CollisionDetector.can_go_backward = self.get_movement_feasibility(self.get_back_distance(),
                                                                              self.moving_backward(actual_speed))
            sleep(0.1)
        pass

    def stop(self):
        self.active = False

    @staticmethod
    def stop_message():
        return '{"messageType": 12}'

    @staticmethod
    def get_left_front_distance():
        return JarvisGpio.get_left_front_distance()

    @staticmethod
    def get_right_front_distance():
            return JarvisGpio.get_right_front_distance()

    @staticmethod
    def get_left_back_distance():
        return JarvisGpio.get_left_back_distance()

    @staticmethod
    def get_right_back_distance():
        return JarvisGpio.get_right_back_distance()

    @staticmethod
    def moving_forward(actual_speed):
        return actual_speed >= Constant.min_forward

    @staticmethod
    def moving_backward(actual_speed):
        return actual_speed <= Constant.min_backward

    def get_movement_feasibility(self, left_distance, right_distance, moving_that_way):
        if left_distance < CollisionDetector.distance_to_stop or \
                        right_distance < CollisionDetector.distance_to_stop:
            if moving_that_way:
                JarvisManager.add_to_process_queue(self.stop_message())
            return False
        else:
            return True
