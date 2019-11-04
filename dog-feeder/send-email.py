import smtplib
from email.MIMEText import MIMEText
import socket


socket.setdefaulttimeout(None)
HOST = "smtp.gmail.com"
PORT = "587"
sender= "" # insert email address here
password = "" # insert password here
receiver= "" # insert recipient email address here

msg = MIMEText("Hello World")

msg['Subject'] = 'Subject - Hello World'
msg['From'] = sender
msg['To'] = receiver

server = smtplib.SMTP()
server.connect(HOST, PORT)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver, msg.as_string())
server.close()

