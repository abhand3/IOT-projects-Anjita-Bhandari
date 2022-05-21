#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor
import smtplib

pir = MotionSensor(4)

SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='' //your email
GMAIL_PASSWORD = '' //password

#Create class to send an email
class Emailer:
	def sendmail(self, recipient,  subject, content):
		#Creating the headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
			"To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()

		#Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

		#Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
def callback(channel):
        if GPIO.input(channel):
               # print ("Sound Detected!")
            sender = Emailer()
            sendTo = '' //email
            emailSubject = "Sound detected"
            emailContent = "Sound detected in the lab"

            sender.sendmail(sendTo, emailSubject, emailContent)
            print ("Sound Detected!")
        else:
            if pir.wait_for_motion(1):
                print ("motion Detected!")
            else:
                print ("motion not Detected!")     
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
        time.sleep(1)
