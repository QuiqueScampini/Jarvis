import logging
from model.gpio.JarvisGpio import JarvisGpio
from model.error.JarvisException import JarvisException


class CarDriver:

    speed_step = 40
    min_backward = 1100
    brake_speed = 1300
    stop_speed = 1500
    min_forward = 1600

    # TODO Maybe Not necessary
    max_forward = 2000
    max_backward = 700

    max_left = 1000

    max_right = 1700

    @classmethod
    def process_movement(cls,movement_json):
        logging.info('Move Car')
        CarDriver.set_angle(cls.get_property(movement_json, 'angle'))
        CarDriver.process_speed_move(cls.get_property(movement_json, 'power'))

    @classmethod
    def get_property(cls, json, json_property):
        return json[json_property]

    """Start Speed Shit methods"""
    @classmethod
    def process_speed_move(cls, speed):
        cls.validate_new_speed(speed)
        new_speed = cls.get_gpio_speed(speed)

        if cls.get_speed() != new_speed:
            JarvisGpio.set_speed(speed)
            logging.info('New Speed' + speed)
        else:
            logging.info('Not necessary to change Speed')
        pass

    """Received speed is checked to be between -100 and 100"""
    @classmethod
    def validate_new_speed(cls, speed):
        if speed in range(-100, 100):
            raise JarvisException('New speed ' + str(speed) + ' out of range [-100, 100]')

    @classmethod
    def get_gpio_speed(cls, speed):
        if speed == 0:
            return cls.stop_speed

        base_speed = cls.min_forward if speed > 0 else cls.min_backward
        return base_speed + int(speed/10) * cls.speed_step

    @classmethod
    def get_speed(cls):
        return JarvisGpio.get_speed()

    """End Speed Shit methods"""

    """Start direction Shit methods"""

    @classmethod
    def set_angle(cls, angle):
        JarvisGpio.set_direction(angle)
        logging.info('Turning ' + angle)

    """End direction Shit methods"""
