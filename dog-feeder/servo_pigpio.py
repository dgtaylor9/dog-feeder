import pigpio
import time

servoControlPin = 18 # pin 12 = GPIO 18 with PWM functionality

connection = pigpio.pi()
left = 700
right = 2300
middle = (right - left) / 2 + left

try:
    while True:
        connection.set_servo_pulsewidth(servoControlPin, left) #0 degrees
        print("Servo {} {} micro pulses".format(servoControlPin, left))
        time.sleep(5)
        
##        connection.set_servo_pulsewidth(servoControlPin, middle) #90 degrees
##        print("Servo {} {} micro pulses".format(servoControlPin, middle))
##        time.sleep(1)
        
        connection.set_servo_pulsewidth(servoControlPin, right) #180 degrees
        print("Servo {} {} micro pulses".format(servoControlPin, right))
        time.sleep(5)
        
##        connection.set_servo_pulsewidth(servoControlPin, middle) #90 degrees
##        print("Servo {} {} micro pulses".format(servoControlPin, middle))
##        time.sleep(1)
        
except KeyboardInterrupt:
    connection.set_servo_pulsewidth(servoControlPin, 0);

connection.stop()
