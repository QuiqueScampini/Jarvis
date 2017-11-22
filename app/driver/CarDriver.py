from error.JarvisException import JarvisException
from gpio.JarvisGpioDriver import JarvisGpioDriver


class CarDriver:

    message_server = None

    free_front_left = False
    free_front_right = False

    free_back_left = False
    free_back_right = False

    backward = 1100
    forward = 1600
    brake_speed = 1300
    stop_speed = 1500

    middle_direction = 1350
    turn_dif = 250

    @classmethod
    def process_movement(cls, angle, speed):
        cls.process_direction_move(angle)
        cls.process_speed_move(speed)

    @classmethod
    def stop_forward(cls):
        JarvisGpioDriver.set_speed(cls.brake_speed)

    @classmethod
    def stop_backward(cls):
        JarvisGpioDriver.set_speed(cls.stop_speed)

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
        if 15 > speed > -15:
            return cls.stop_speed
        elif speed > 0:
            return cls.get_gpio_speed_with_parameters(cls.free_front_left,
                                                      cls.free_front_right,
                                                      cls.forward,
                                                      1)
        else:
            return cls.get_gpio_speed_with_parameters(cls.free_back_left,
                                                      cls.free_back_right,
                                                      cls.backward,
                                                      3)

    @classmethod
    def get_gpio_speed_with_parameters(cls, left_free_way, right_free_way, gpio_value, base_sensor):
        if left_free_way and right_free_way:
            return gpio_value

        cls.send_message_obstacle_detected(base_sensor)
        return cls.stop_speed

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
        return int(cls.middle_direction + ((cls.turn_dif * angle) / 100))
    """End direction Shit methods"""

    @classmethod
    def send_message_obstacle_detected(cls, sensor):
        cls.message_server.send_message(cls.obstacle_detected_message(sensor))
        pass

    @classmethod
    def obstacle_detected_message(cls, sensor_id):
        return '{"messageType": 6, "side": ' + str(sensor_id) + '}@'

    @classmethod
    def set_sensor_values(cls, free_front_left, free_front_right, free_back_left, free_back_right):
        cls.free_front_left = free_front_left
        cls.free_front_right = free_front_right
        cls.free_back_left = free_back_left
        cls.free_back_right = free_back_right

        speed = JarvisGpioDriver.get_speed()
        if speed == cls.forward and (not cls.free_front_left or not cls.free_front_right):
            cls.stop_forward()
        if speed == cls.backward and (not cls.free_back_left or not cls.free_back_right):
            cls.stop_backward()
