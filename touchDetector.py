import RPi.GPIO as GPIO
state = False
from gpiozero import Buzzer
buzzer=Buzzer(16)
import smtplib


SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='testiotprojects@gmail.com'
GMAIL_PASSWORD = 'Tigers@TU!'

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

def button_callback(channel):
    state = GPIO.input(channel)
    
    if(state ==0):
        print("Button released")
        buzzer.on()
        sender = Emailer()
        sendTo = 'testiotprojects@gmail.com'
        emailSubject = "touch detected"
        emailContent = "Somebody touch the sensor in the lab"

        sender.sendmail(sendTo, emailSubject, emailContent)
    else:
        print("button pressed")
        #buzzer.value(0)
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(13,GPIO.BOTH, callback=button_callback)
message = input("Press enter to quit\n\n")
GPIO.cleanup()