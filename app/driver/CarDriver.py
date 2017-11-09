from gpio.JarvisGpioDriver import JarvisGpioDriver


class CarDriver:

    backward = 1100
    forward = 1600
    brake = 1300
    stop = 1500

    middle_direction = 1350
    turn_dif = 250

    @classmethod
    def process_movement(cls, angle, speed):
        cls.process_direction_move(angle)
        cls.process_speed_move(speed)

    @classmethod
    def stop(cls):
        JarvisGpioDriver.set_speed(cls.brake)

    @classmethod
    def get_property(cls, json, json_property):
        return json[json_property]

    """Start Speed Shit methods"""
    @classmethod
    def process_speed_move(cls, speed):
        cls.validate_new_speed(speed)
        JarvisGpioDriver.set_speed(cls.get_gpio_speed(speed))

    """Received speed is checked to be between -100 and 100"""
    @classmethod
    def validate_new_speed(cls, speed):
        if not(speed in range(-100, 101)):
            raise JarvisException('New speed ' + str(speed) + ' out of range [-100, 100]')

    @classmethod
    def get_gpio_speed(cls, speed):
        if 10 > speed > -10:
            return Constant.stop_speed
        elif speed > 0:
            return cls.get_gpio_speed_with_parameters(CollisionDetector.free_front_left,
                                                      CollisionDetector.free_front_right,
                                                      Constant.min_forward,
                                                      1,
                                                      speed)
        else:
            return cls.get_gpio_speed_with_parameters(CollisionDetector.free_back_left,
                                                      CollisionDetector.free_back_right,
                                                      Constant.min_backward,
                                                      3,
                                                      speed)

    @classmethod
    def get_gpio_speed_with_parameters(cls, left_free_way, right_free_way, base_gpio_value, base_sensor, speed):
        if not left_free_way:
            CollisionDetector.inform_imposibility_to_move(base_sensor)
            return Constant.stop_speed
        if not right_free_way:
            CollisionDetector.inform_imposibility_to_move(base_sensor + 1)
            return Constant.stop_speed

        return int(base_gpio_value + (Constant.speed_multiplier * speed))
    """End Speed Shit methods"""

    """Start direction Shit methods"""
    @classmethod
    def process_direction_move(cls, angle):
        cls.validate_direction(angle)
        JarvisGpioDriver.set_direction(cls.get_gpio_direction(angle))

    @classmethod
    def validate_direction(cls, angle):
        if not (angle in range(-100, 101)):
            raise JarvisException('Turn Value ' + str(angle) + ' out of range [-100, 100]')

    @classmethod
    def get_gpio_direction(cls, angle):
        return int(Constant.middle_direction + ((Constant.turn_dif * angle) / 100))
    """End direction Shit methods"""

    @classmethod
    def send_message_obstacle_detected(cls, direction_base_sensor):
        pass
