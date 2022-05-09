<h1>Description</h1>
<p>This is a touch detector project built on Raspberry Pi that detects touch when we pressed the sensor and released it. This also makes a sound through a buzzer when the touch sensor is pressed. This is assuming you have a working interface for your raspberry pi. This specific tutorial mounts the Raspberry Pi and uses Thonny IDE to run the code.</p>

GitHub Link: https://github.com/abhand3/IOT-projects-Anjita-Bhandari/blob/main/touchDetector.py

<h2>Materials Needed</h2>
<h3>Hardware<h3>
1 Raspberry Pi</br>
1 Breadboard </br>
1 Touch module </br>
1 Buzzer </br>
5 Male-to-Male cables (any color) <br>

<p>Note: the color of the cables do not matter, they just make things easier! Hardware Connection Setup</p>

1.	Mount the Raspberry Pi GPIO extension board in the breadboard</br>
2.	Connect the touch module to the breadboard with the Raspberry Pi using the 3 Male-to-Male.</br>
3.	Here I connected the male to male wire with the wires comes with touch module</br>

Cable Connections
Cable Color	Touch module Connection	GIPO Extension Connection
Black	GND	GND
Red	VCC	3V
Yellow	S	GPIO13

4.	Buzzer connection:
Cable Color	Buzzer Connection	GIPO Extension Connection
Red	Positive	GPIO16
blue	Negative	GND

 <h3>Follow the picture if you need:</h3>
 <img src="https://user-images.githubusercontent.com/88409698/167430707-1266239e-eed0-4f88-a9c9-1c208e5aaa81.png">
 <h3>Software Instructions</h3>
1.	Open Thonny IDE and change to the Raspberry Pi (python 3.7.3) interpreter on the bottom right hand corner.
2.	Click Plus sign and copy paste the code (from flameDetector.py) and save it or 
Download the file from GitHub and save it.
3.	Modify the email part as needed( for example, you can change the email and password to email you have (Line 10 and Line 11) and email address in Line 41.
4.	Run the program. If all goes well, when you run the program everything should work fine. 


