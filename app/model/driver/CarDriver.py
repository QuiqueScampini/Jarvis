from model.driver.CollisionDetector import CollisionDetector
from model.gpio.JarvisGpio import JarvisGpio
from model.error.JarvisException import JarvisException
from model.util.Constant import Constant


class CarDriver:

    @classmethod
    def process_movement(cls, movement_json):
        cls.process_direction_move(cls.get_property(movement_json, 'angle'))
        cls.process_speed_move(cls.get_property(movement_json, 'power'))

    @classmethod
    def stop(cls):
        JarvisGpio.set_speed(Constant.stop_speed)
        pass

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
            return Constant.stop_speed
        elif speed > 0:
            return cls.get_gpio_speed(CollisionDetector.can_go_forward, Constant.min_forward, speed)
        else:
            return cls.get_gpio_speed(CollisionDetector.can_go_backward, Constant.min_backward, speed)

    @classmethod
    def get_gpio_speed(cls, collision_detected, base_gpio_value, speed):
        if collision_detected:
            return int(base_gpio_value + (Constant.speed_multiplier * speed))
        else:
            return Constant.stop_speed
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
        return int(Constant.middle_direction + ((Constant.turn_dif * angle) / 100))
    """End direction Shit methods"""
