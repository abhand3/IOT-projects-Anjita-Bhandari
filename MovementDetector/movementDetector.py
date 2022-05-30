import RPi.GPIO as GPIO
import time
#GPIO SETUP
import smtplib

SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='' //YOUR EMAIL
GMAIL_PASSWORD = '' //YOUR EMAIL PASSWORD

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

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
def callback(channel):
        if GPIO.input(channel):
                print ("Movement Detected!")
                sender = Emailer()
                sendTo = '' //EMAIL
                emailSubject = "Movement detected"
                emailContent = "Movement detected in the lab"
        
                sender.sendmail(sendTo, emailSubject, emailContent)
        else:
                print ("Movement Detected!")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
        time.sleep(1)
