import time
from .JarvisGpio import JarvisGpio


class JarvisGpioSensors(JarvisGpio):

    front_Echo_Left_Pin = 19
    front_Trig_Left_Pin = 26

    front_Echo_Right_Pin = 17
    front_Trig_Right_Pin = 4

    back_Trig_Left_Pin = 16
    back_Echo_Left_Pin = 20

    back_Trig_Right_Pin = 23
    back_Echo_Right_Pin = 24

    @classmethod
    def get_front_left_distance(cls):
        return cls.get_distance(cls.front_Echo_Left_Pin, cls.front_Trig_Left_Pin)

    @classmethod
    def get_front_right_distance(cls):
        return cls.get_distance(cls.front_Echo_Right_Pin, cls.front_Trig_Right_Pin)

    @classmethod
    def get_back_left_distance(cls):
        return cls.get_distance(cls.back_Echo_Left_Pin, cls.back_Trig_Left_Pin)

    @classmethod
    def get_back_right_distance(cls):
        return cls.get_distance(cls.back_Echo_Right_Pin, cls.back_Trig_Right_Pin)

    @classmethod
    def get_distance(cls, echo_pin, trigger_pin):
        cls.gpio.write(trigger_pin, 1)
        time.sleep(0.00001)
        cls.gpio.write(trigger_pin, 0)
        start = time.time()
        stop = start + 1
        timeout = start
        while cls.gpio.read(echo_pin) == 0 and (time.time() - timeout) < 0.3:
            start = time.time()
        while cls.gpio.read(echo_pin) == 1 and (time.time() - timeout) < 0.3:
            stop = time.time()
        elapsed = stop-start
        distance = (elapsed * 34300)/2
        distance = round(distance, 2)
        return distance
