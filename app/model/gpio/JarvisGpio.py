#import pigpio


class JarvisGpio:

    #gpio_manager = pigpio.pi()
    speed_Pin = 18
    direction_Pin = 17

    front_Echo_Left_Pin = 19
    front_Trig_Left_Pin = 26

    back_Echo_Left_Pin = 16
    back_Trig_Left_Pin =20

    front_Echo_Right_Pin = 19
    front_Trig_Right_Pin = 26

    back_Echo_Right_Pin = 16
    back_Trig_Right_Pin =20

    max_speed = 2000
    min_speed = 700

    max_left = 2000
    max_right = 1000

    @classmethod
    def set_speed(cls, speed_value):
        if speed_value > cls.max_speed:
            speed_value = cls.max_speed
        elif speed_value < cls.min_speed:
            speed_value = cls.min_speed
        cls.set_servo_value(speed_value, cls.speed_Pin)

    @classmethod
    def set_direction(cls, direction_value):
        if direction_value > cls.max_left:
            direction_value = cls.max_left
        elif direction_value < cls.max_right:
            direction_value = cls.max_right
        cls.set_servo_value(direction_value, cls.direction_Pin)

    @classmethod
    def set_servo_value(cls,value,pin):
        cls.speed_Pin
        #cls.gpio_manager.set_servo_pulsewidth(pin, value)

"""import RPi.GPIO as GPIO
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
