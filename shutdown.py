#!/usr/bin/python
# Short PIN 37, 39 to shutdown

import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if not GPIO.input(26):
        os.system("/sbin/shutdown -h now")
        break
    time.sleep(1)
