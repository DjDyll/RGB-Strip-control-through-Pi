>>>>>>>>>>>>>>>>>>>>>>

#!/usr/bin/env python
 
import time
import os
 
STEP = 100
DELAY = 0.5
 
def pwm(pin, power):	
	power = power / 100.0
	cmd = "echo " + str(pin) + "=" + str(power) + " > /dev/pi-blaster"
	os.system(cmd)
    time.sleep(DELAY)
 
while True:
	#Blue to Dark Blue
    for i in range(50, 100, 1):
            pwm(3,i)  

	#Dark Blut to Blue
    for i in range(100, 50, -1):
            pwm(3,i)

>>>>>>>>>>>>>>>>>>>>>>