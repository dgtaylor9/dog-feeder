import pigpio
import time
import RPi.GPIO as GPIO
import datetime
import smtplib
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import socket
from picamera import PiCamera

# define constants for email sending
HOST = "smtp.gmail.com"
PORT = "587"
sender= "" # insert email address here
password = "" # insert password here
receiver= "" # insert recipient email address here
photoFile = "DogFeeder/crate_photo.jpg"

def send_email(subject, body):
   socket.setdefaulttimeout(None)

   msg = MIMEMultipart()

   msg['Subject'] = subject 
   msg['From'] = sender
   msg['To'] = receiver

   text = MIMEText(body)
   msg.attach(text)

   img_data = open(photoFile, 'rb').read()
   image = MIMEImage(img_data, name=photoFile)
   msg.attach(image)
   
   server = smtplib.SMTP()
   server.connect(HOST, PORT)
   server.starttls()
   server.login(sender,password)
   server.sendmail(sender,receiver, msg.as_string())
   server.close()
   return;

def take_photo():
   try:
      camera = PiCamera()
      camera.resolution = (1024, 768)
      camera.start_preview()
      time.sleep(2)
      camera.capture(photoFile)
   finally:
      camera.stop_preview()
      camera.close()


print("Feeding started at {}".format(datetime.datetime.now().isoformat()))

try:
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

   #Take a photo
   take_photo()

   # Send success email
   send_email("Dog Fed Successfully!", "The mongrel is fat and happy. :-)")

except Exception as e:
   # Send failure email
   print("FAILURE: " + str(e))
   send_email("FAILURE Feeding Dog!", "The mongrel is sad and hungry. :-(\nException: " + str(e)) 
