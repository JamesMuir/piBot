import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

trigger = 7                                #Associate pin 23 to TRIG
echo = 8                                   #Associate pin 24 to ECHO

print("Distance measurement in progress")

GPIO.setup(trigger,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(echo,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(trigger, False)                 #Set TRIG as LOW
  print("Waitng For Sensor To Settle")
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(trigger, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(trigger, False)                 #Set TRIG as LOW

  while GPIO.input(echo)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(echo)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print("Distance:",distance,"cm") #Print distance 
  else:
    print("Out Of Range")                  #display out of range
