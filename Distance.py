import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)
trig=11
echo=13
print ("Distance Measurement In Progress")

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


pulse_duration=0
pulse_end  = 0
pulse_start = 0
pulse_end1  = 0

GPIO.output(trig, False)
print ("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(trig,True)
time.sleep(0.00001)
GPIO.output(trig,False)
#pulse_end0 = pulse_end1

while GPIO.input(echo) == 0:
  pulse_begin = time.time()
while GPIO.input(echo) == 1:
  pulse_end1 = time.time()
  

pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150   
#distance = round(distance, 2)


GPIO.cleanup()
print ("Distance: ",distance,"cm")