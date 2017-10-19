import logging
import pigpio
import time


class JarvisGpio:

    gpio_manager = pigpio.pi()
    #gpio_manager = pigpio.pi('192.168.0.15')
    speed_Pin = 18
    direction_Pin = 14

    front_Echo_Left_Pin = 19
    front_Trig_Left_Pin = 26

    front_Echo_Right_Pin = 3
    front_Trig_Right_Pin = 4

    back_Trig_Left_Pin = 16
    back_Echo_Left_Pin = 20

    back_Trig_Right_Pin = 23
    back_Echo_Right_Pin = 24

    @classmethod
    def set_speed(cls, new_speed):
        cls.set_servo_value(new_speed, cls.speed_Pin)

    @classmethod
    def get_speed(cls):
        return cls.get_servo_value(cls.speed_Pin)

    @classmethod
    def set_direction(cls, new_turn):
        cls.set_servo_value(new_turn, cls.direction_Pin)

    @classmethod
    def get_direction(cls):
        return cls.get_servo_value(cls.direction_Pin)

    @classmethod
    def set_servo_value(cls, value, pin):
        logging.info('Setting Value ' + str(value) + ' to pin ' + str(pin))
        cls.gpio_manager.set_servo_pulsewidth(pin, value)

    @classmethod
    def get_servo_value(cls, pin):
        try:
            return cls.gpio_manager.get_servo_pulsewidth(pin)
        except Exception:
            return 0

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
        cls.gpio_manager.write(trigger_pin, 1)
        time.sleep(0.00001)
        cls.gpio_manager.write(trigger_pin, 0)
        start = time.time()
        stop = start + 1
        timeout = start
        while cls.gpio_manager.read(echo_pin) == 0 and (time.time() - timeout) < 0.3:
            start = time.time()
        while cls.gpio_manager.read(echo_pin) == 1 and (time.time() - timeout) < 0.3:
            stop = time.time()
        elapsed = stop-start
        distance = (elapsed * 34300)/2
        distance = round(distance, 2)
        logging.info('Distance:' + str(distance) + ' Trig:' + str(trigger_pin) + ' Echo:' + str(echo_pin))
        return distance
