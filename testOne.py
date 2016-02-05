import RPi.GPIO as GPIO                    
import time                                
GPIO.setmode(GPIO.BCM)

#Defines the pines
frontRight = 2
backRight = 3
frontLeft = 17 #Pin four not working for some reson 
backLeft = 5
buzzer = 6
trigger = 7
echo = 8

for i in range(2, 12):
    GPIO.setup(i,GPIO.OUT)                 

GPIO.setup(17,GPIO.OUT)  

while True:
    print("LEDs Motors ")
    GPIO.output(frontRight, True)
    time.sleep(0.5)
    GPIO.output(backRight, True)
    time.sleep(0.5)
    GPIO.output(frontLeft, True)
    time.sleep(0.5)
    GPIO.output(backLeft, True)
    time.sleep(0.5)
    GPIO.output(frontRight, False)
    time.sleep(0.5)
    GPIO.output(backRight, False)
    time.sleep(0.5)
    GPIO.output(frontLeft, False)
    time.sleep(0.5)
    GPIO.output(backLeft, False)
    time.sleep(0.5)

    print("Buzzer")
    GPIO.output(buzzer, True)
    time.sleep(0.5)
    GPIO.output(buzzer, False)

    print("LED weapons ")
