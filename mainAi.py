#import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BCM)

#Ultrasonic distance sensor
class ultrasonicSensor:
    #Function that initalises the object
    def __init__(self, ID, trigger, echo):
        self.ID = ID
        self.trigger = trigger
        self.echo = echo

    #Function that displays the ID and trigger and echo pins of the object
    def displayInformation(self):
        print("ID: {}".format(self.ID))
        print("Trigger Pin: {}".format(self.trigger))
        print("Echo Pin: {}".format(self.echo))

    def getDistance(self):
        #Sets the trigger low (off)
        GPIO.output(self.trigger, False)

        #Sends out pulse 
        GPIO.output(self.trigger, True) 
        time.sleep(0.00001)                    
        GPIO.output(trigger, False)  

        #Gets and measure the length of the echo
        while GPIO.input(echo) == 0:
            pulseStart = time.time()

        while GPIO.input(echo) == 1:
            pulseEnd = time.time()

        pulseLength = pulseEnd - pulseStart
        
        distance = pulseLength * 17150

        return distance 
        
