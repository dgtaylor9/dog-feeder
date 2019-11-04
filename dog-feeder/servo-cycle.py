import pigpio
import time
import RPi.GPIO as GPIO

#Definitions
servoPowerPin = 17 # pin 11: to transistor base: "power switch"
servoControlPin = 18 # pin 12 = GPIO 18 with PWM functionality
left = 700	# ms: Min servo pulse width
right = 2300	# ms: Max servo pulse width

#setup
connection = pigpio.pi()
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPowerPin, GPIO.OUT, initial=GPIO.HIGH)  #Power on

#Start left
connection.set_servo_pulsewidth(servoControlPin, left) #0 degrees
print("Servo {} {} micro pulses".format(servoControlPin, left))
time.sleep(1)
        
#Go Right
connection.set_servo_pulsewidth(servoControlPin, right) #120 degrees
print("Servo {} {} micro pulses".format(servoControlPin, right))
time.sleep(1)

#Return left
connection.set_servo_pulsewidth(servoControlPin, left) #0 degrees
print("Servo {} {} micro pulses".format(servoControlPin, left))
time.sleep(1)

#cleanup        
GPIO.output(servoPowerPin, GPIO.LOW) # Power off the transitor/servo
GPIO.cleanup()
connection.stop()
