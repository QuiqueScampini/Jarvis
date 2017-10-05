import pigpio


class JarvisGpio:

    #gpio_manager = pigpio.pi()
    gpio_manager = None
    speed_Pin = 15
    direction_Pin = 14

    front_Echo_Left_Pin = 19
    front_Trig_Left_Pin = 26

    back_Echo_Left_Pin = 16
    back_Trig_Left_Pin = 20

    front_Echo_Right_Pin = 27
    front_Trig_Right_Pin = 22

    back_Echo_Right_Pin = 23
    back_Trig_Right_Pin = 24

    @classmethod
    def set_speed(cls, new_speed):
        cls.set_servo_value(new_speed, cls.speed_Pin)

    @classmethod
    def get_speed(cls):
        cls.get_servo_value(cls.speed_Pin)

    @classmethod
    def set_direction(cls, angle):
        direction_value = cls.get_gpio_direction(angle)
        if direction_value > cls.max_left:
            direction_value = cls.max_left
        elif direction_value < cls.max_right:
            direction_value = cls.max_right
        cls.set_servo_value(direction_value, cls.direction_Pin)

    @classmethod
    def set_servo_value(cls, value, pin):
        cls.gpio_manager.set_servo_pulsewidth(pin, value)

    @classmethod
    def get_servo_value(cls, pin):
        cls.gpio_manager.get_servo_pulsewidth(pin)

    @classmethod
    def get_gpio_direction(cls, angle):
        return (angle*500)/100 + 1500

"""
Para los sensores
pi.set_mode( 4, pigpio.INPUT)  # GPIO  4 as input
pi.set_mode(17, pigpio.OUTPUT) # GPIO 17 as output
pi.set_mode(24, pigpio.ALT2)   # GPIO 24 as ALT2
pi1.write(4, 0) # set local Pi's GPIO 4 low
pi2.write(4, 1) # set tom's GPIO 4 to high

pi.set_servo_pulsewidth(17, 0)    # off
pi.set_servo_pulsewidth(17, 1000) # safe anti-clockwise
pi.set_servo_pulsewidth(17, 1500) # centre
pi.set_servo_pulsewidth(17, 2000) # safe clockwise

CUANDO CIERRO HACER UN 
    gpio_manager.stop()
    
import RPi.GPIO as GPIO
import time

GPIO_OUT=14
GPIO_DIRECTION=18

Car_Max_Right=5.6			# 190 mv
Car_Normal_Direction=8.79	# 290 mv
Car_Max_Left=11.7			# 390 mv

#Inicializamos lo global, luego se envuelve en una clase
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_DIRECTION,GPIO.OUT)
GPIO.setup(GPIO_OUT,GPIO.OUT)
directionObject=GPIO.PWM(GPIO_DIRECTION,50)


def getDutyCycle(newVoltaje):
	#receives a newVoltaje in mV and transform it to GPIO DutyCycle
	# 33 mv -> 1%
	# x mv	-> x/33
	newDutyCycle=newVoltaje/33
	
	if newDutyCycle < Car_Max_Right:
		newDutyCycle=Car_Max_Right
	elif newDutyCycle > Car_Max_Left:
		newDutyCycle=Car_Max_Left
	
	return newDutyCycle

def startDirection():
	directionObject.start(Car_Normal_Direction)
	
def stopDirection():
	directionObject.stop()
	
def changeDirection(newVoltaje):
	newDutyCycle=float("{0:.2f}".format(getDutyCycle(float(newVoltaje))))
	directionObject.ChangeDutyCycle(newDutyCycle)
	print "Duty Cycle Change to ", newDutyCycle, " with Voltaje", newVoltaje

def on():
	print "LED on"
	GPIO.output(GPIO_OUT,GPIO.HIGH)

def off():
	print "LED off"
	GPIO.output(GPIO_OUT,GPIO.LOW)"""
