import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering

frontRight = 2
backRight = 3
frontLeft = 17 #Pin four not working for some reson 
backLeft = 5
trigger = 7                                #Associate pin 23 to TRIG
echo = 8                                   #Associate pin 24 to ECHO

print("Distance measurement in progress")

GPIO.setup(trigger,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(echo,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(frontRight,GPIO.OUT)
GPIO.setup(backRight,GPIO.OUT)
GPIO.setup(frontLeft,GPIO.OUT)
GPIO.setup(backLeft,GPIO.OUT) 

def getDistance():
       
    GPIO.output(trigger, False)                 #Set TRIG as LOW
    print("Waitng For Sensor To Settle")
    time.sleep(0.5)                            #Delay of 2 seconds

    GPIO.output(trigger, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(trigger, False)                 #Set TRIG as LOW

    while GPIO.input(echo)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(echo)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance

    if distance > 2 and distance < 400:      #Check whether the distance is within range
        print("Distance:",distance,"cm") #Print distance 
    else:
        print("Out Of Range")                  #display out of range

    return distance
    
while True:
    #Keeps the LEDs lit as long as the distance between the sensor and wall is more than 5cm
    distance = getDistance()
    if distance > 5:
        GPIO.output(frontRight, True)
        GPIO.output(backRight, True)
        GPIO.output(frontLeft, True)
        GPIO.output(backLeft, True)  
    else:
        GPIO.output(frontRight, False)
        GPIO.output(backRight, False)
        GPIO.output(frontLeft, False)
        GPIO.output(backLeft, False)  
