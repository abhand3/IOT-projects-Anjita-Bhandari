import RPi.GPIO as GPIO
import time
import smtplib

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

GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 13
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print ("Calibrating.....")
time.sleep(2)

print ("Place the object......")

object = True
pulse_start1 = time.time()
pulse_end1 = time.time()
pulse_duration1 = pulse_end1 - pulse_start1
distance1 = pulse_duration1 * 17150
distance1 = round(distance1+1.15, 1)

try:
    while object:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)

       while GPIO.input(ECHO)==0:
          pulse_start = time.time()

       while GPIO.input(ECHO)==1:
          pulse_end = time.time()

       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150

       distance = round(distance+1.15, 1)
       
       dist2 = None
  
       if distance<=20 and distance>=5:
          print ("distance:",distance,"cm")
          i=1
          dist2 = distance
          if(distance!=distance1):
            sender = Emailer()
            sendTo = '' //email
            emailSubject = "Distance Calculator"
            emailContent = "Distance is" + str(distance)

            sender.sendmail(sendTo, emailSubject, emailContent)
            distance1= distance
          
       if distance>20 and i==1:
          print ("place the object....")
          i=0
       time.sleep(2)



except KeyboardInterrupt:
     GPIO.cleanup()
