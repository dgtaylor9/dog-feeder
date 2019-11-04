import pigpio
import time
import RPi.GPIO as GPIO
import datetime

print("Feeding started at {}".format(datetime.datetime.now().isoformat()))

servoPowerPin = 17 # pin 11: to transistor base: "power switch"
servoControlPin = 18 # pin 12 = GPIO 18 with PWM functionality

connection = pigpio.pi()
left = 700
right = 2300
middle = (right - left) / 2 + left

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPowerPin, GPIO.OUT, initial=GPIO.HIGH)  #Power on

#Start left
connection.set_servo_pulsewidth(servoControlPin, left) #0 degrees
print("Servo {} {} micro pulses".format(servoControlPin, left))
time.sleep(2)
     
#Go Right
connection.set_servo_pulsewidth(servoControlPin, right) #120 degrees
print("Servo {} {} micro pulses".format(servoControlPin, right))
time.sleep(2)

#Return left
connection.set_servo_pulsewidth(servoControlPin, left) #0 degrees
print("Servo {} {} micro pulses".format(servoControlPin, left))
time.sleep(2)

#cleanup        
GPIO.output(servoPowerPin, GPIO.LOW) # Power off the transitor/servo
GPIO.cleanup()
connection.stop()
print("Feeding completed at {}".format(datetime.datetime.now().isoformat()))
