import logging
import pigpio


class JarvisGpio:

    gpio = pigpio.pi()

    @classmethod
    def set_servo_value(cls, value, pin):
        logging.info('Setting Value ' + str(value) + ' to pin ' + str(pin))
        cls.gpio.set_servo_pulsewidth(pin, value)

    @classmethod
    def get_servo_value(cls, pin):
        try:
            return cls.gpio.get_servo_pulsewidth(pin)
        except Exception:
            return 0
