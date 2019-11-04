import RPi.GPIO as GPIO
import time

servoControlPin = 12 #GPIO 18 with PWM functionality

GPIO.setmode(GPIO.BOARD) #use the pin numbers on the board
GPIO.setup(servoControlPin, GPIO.OUT) #set the pin to send controls to the servo on

frequencyHertz = 50
pwm = GPIO.PWM(servoControlPin, frequencyHertz)

leftPosition = 0.9 #num of milliseconds of pulse width for minimum position
rightPosition = 2.1 #num of milliseconds of pulse width for maximum position
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

positionList = [leftPosition, rightPosition]

# results in 20ms per cycle
msPerCycle = 1000 / frequencyHertz

#start it at the middle position
dutyCyclePercentage = middlePosition * 100 / msPerCycle
pwm.start(dutyCyclePercentage)
print 'Position: ' + str(middlePosition)
print 'Duty Cycle: ' + str(dutyCyclePercentage)
print ''

try:
    time.sleep(5)
    for i in range(3):
        for position in positionList:
            # calculate the percentage of "on time" in each 20ms cycle
            dutyCyclePercentage = position * 100 / msPerCycle

            print 'Position: ' + str(position)
            print 'Duty Cycle: ' + str(dutyCyclePercentage)
            print ''

            pwm.ChangeDutyCycle(dutyCyclePercentage)
            time.sleep(5) #duration servo remains in position

    pwm.stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
