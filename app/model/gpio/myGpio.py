
def start_gpio():
    print("Started")


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
