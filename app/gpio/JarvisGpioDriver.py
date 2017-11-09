from JarvisGpio import JarvisGpio


class JarvisGpioDriver(JarvisGpio):

    speed_Pin = 18
    direction_Pin = 14

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
