import webiopi
import datetime
import time
import os
import random

GPIO = webiopi.GPIO

a_fwd=14
a_bwd=15
b_fwd=18
b_bwd=23
t=0.54
t1=1.83
def setup():

	
	GPIO.setFunction(a_fwd,GPIO.OUT)
	GPIO.setFunction(a_bwd,GPIO.OUT)
	GPIO.setFunction(b_fwd,GPIO.OUT)
	GPIO.setFunction(b_bwd,GPIO.OUT)

	GPIO.digitalWrite(a_fwd,GPIO.LOW)
	GPIO.digitalWrite(a_bwd,GPIO.LOW)
	GPIO.digitalWrite(b_fwd,GPIO.LOW)
	GPIO.digitalWrite(b_bwd,GPIO.LOW)

def loop():
    webiopi.sleep(5)

def destroy():

    GPIO.setFunction(a_fwd, GPIO.IN)
    GPIO.setFunction(a_bwd, GPIO.IN)
    GPIO.setFunction(b_fwd, GPIO.IN)
    GPIO.setFunction(b_bwd, GPIO.IN)

@webiopi.macro
def MoveLeft():
    Stop()
    r=('/home/pi/left/img'+str(random.randrange(0,1000,1))+'.jpg')
    os.system('fswebcam -r 320x240 -S 8 '+r)
    GPIO.digitalWrite(a_bwd,GPIO.HIGH)
    GPIO.digitalWrite(b_fwd,GPIO.HIGH)
    time.sleep(t)
    Stop()
@webiopi.macro
def MoveRight():
    Stop()
    r=('/home/pi/right/img'+str(random.randrange(0,1000,1))+'.jpg')
    os.system('fswebcam -r 320x240 -S 8 '+r)
    GPIO.digitalWrite(a_fwd, GPIO.HIGH)
    GPIO.digitalWrite(b_bwd, GPIO.HIGH)
    time.sleep(t)
    Stop()
@webiopi.macro
def MoveForward():
    Stop()
    r=('/home/pi/forward/img'+str(random.randrange(0,1000,1))+'.jpg')
    os.system('fswebcam -r 320x240 -S 8 '+r)
    GPIO.digitalWrite(a_fwd, GPIO.HIGH)
    GPIO.digitalWrite(b_fwd, GPIO.HIGH)
    time.sleep(t1)
    Stop()
@webiopi.macro
def MoveBackward():
    Stop()
    GPIO.digitalWrite(a_bwd, GPIO.HIGH)
    GPIO.digitalWrite(b_bwd, GPIO.HIGH)
    time.sleep(t1)
    Stop()
@webiopi.macro
def Stop():
    GPIO.digitalWrite(a_fwd, GPIO.LOW)
    GPIO.digitalWrite(a_bwd, GPIO.LOW)
    GPIO.digitalWrite(b_fwd, GPIO.LOW)
    GPIO.digitalWrite(b_bwd, GPIO.LOW)
