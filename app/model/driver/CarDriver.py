from model.driver.CollisionDetector import CollisionDetector
from model.gpio.JarvisGpio import JarvisGpio
from model.error.JarvisException import JarvisException


class CarDriver:

    min_backward = 1100
    #max_backward = 700
    min_forward = 1600
    #max_forward = 2000
    speed_multiplier = 4
    #brake_speed = 1300
    stop_speed = 1500

    #max_left = 1100
    middle = 1350
    #max_right = 1600
    turn_dif = 250

    @classmethod
    def process_movement(cls, movement_json):
        cls.process_direction_move(cls.get_property(movement_json, 'angle'))
        cls.process_speed_move(cls.get_property(movement_json, 'power'))

    @classmethod
    def get_property(cls, json, json_property):
        return json[json_property]

    """Start Speed Shit methods"""
    @classmethod
    def process_speed_move(cls, speed):
        cls.validate_new_speed(speed)
        JarvisGpio.set_speed(cls.get_gpio_speed(speed))

    """Received speed is checked to be between -100 and 100"""
    @classmethod
    def validate_new_speed(cls, speed):
        if not(speed in range(-100, 101)):
            raise JarvisException('New speed ' + str(speed) + ' out of range [-100, 100]')

    @classmethod
    def get_gpio_speed(cls, speed):
        if speed == 0:
            return cls.stop_speed
        elif speed > 0:
            return cls.get_gpio_speed(CollisionDetector.can_go_forward, cls.min_forward, speed)
        else:
            return cls.get_gpio_speed(CollisionDetector.can_go_backward, cls.min_backward, speed)

    @classmethod
    def get_gpio_speed(cls, collision_detected, base_gpio_value, speed):
        if collision_detected:
            return int(base_gpio_value + (cls.speed_multiplier * speed))
        else:
            return cls.stop_speed
    """End Speed Shit methods"""

    """Start direction Shit methods"""
    @classmethod
    def process_direction_move(cls, angle):
        cls.validate_direction(angle)
        JarvisGpio.set_direction(cls.get_gpio_direction(angle))

    @classmethod
    def validate_direction(cls, angle):
        if not (angle in range(-100, 101)):
            raise JarvisException('Turn Value ' + str(angle) + ' out of range [-100, 100]')

    @classmethod
    def get_gpio_direction(cls, angle):
        return int(cls.middle + ((cls.turn_dif * angle) / 100))
    """End direction Shit methods"""


