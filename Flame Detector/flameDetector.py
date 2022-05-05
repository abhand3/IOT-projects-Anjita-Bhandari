import RPi.GPIO as GPIO
import time
state = False
from gpiozero import Buzzer
buzzer=Buzzer(16)
import smtplib

SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='testiotprojects@gmail.com'
GMAIL_PASSWORD = 'Tigers@TU!'

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

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    state = GPIO.input(channel)
    
    if(state ==0):
        print("flame detected")
        buzzer.on()
        sender = Emailer()
        sendTo = 'testiotprojects@gmail.com'
        emailSubject = "flame detected"
        emailContent = "flame detected in the lab"
        
        sender.sendmail(sendTo, emailSubject, emailContent)
    else:
        buzzer.off()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)