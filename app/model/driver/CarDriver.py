from model.gpio.JarvisGpio import JarvisGpio
import logging

class CarDriver:

    @staticmethod
    def move_car(movement_json):
        CarDriver.__set_angle(movement_json["angle"])
        CarDriver.__set_speed(movement_json["power"])

    @staticmethod
    def __set_speed(speed):
        JarvisGpio.set_speed(CarDriver.get_gpio_speed(speed))
        logging.info('New Speed' + speed)

    @staticmethod
    def __set_angle(angle):
        JarvisGpio.set_direction(CarDriver.get_gpio_direction(angle))
        logging.info('Turning ' + angle)

    @classmethod
    def get_gpio_speed(cls, speed):
        return (speed*500)/100 + 1500

    @classmethod
    def get_gpio_direction(cls, angle):
        return (angle*500)/100 + 1500
