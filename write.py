#!/usr/bin/env python2
"""
This is just a quick and dirty implementation of the protocol described here:
https://www.triades.net/13-geek/13-serial-protocol-for-a-chinese-rfid-125khz-reader-writer.html
This is probably public domain
No warranty
"""

BEEP_TIME = 30
LED_GREEN = 2
LED_RED = 1

import sys
import serial
from time import sleep

from common import *
#import common

if __name__=="__main__":
    device = serial.Serial("/dev/ttyUSB0", 38400)
    #printResponse(info(device))

#    for i in range(3):
#        #test some beeping nd blinking
#        beep(device, BEEP_TIME)
#        led(device, LED_RED)
#        sleep(0.2)

    print "writing card..."
    response = readTag(device)
    i = 0
    while 0!=ord(response[1][0]):
        #This commented line will write 11 22 33 44 55 to a card
        response = writeTag(device, sys.argv[1])
        response = readTag(device)
        led(device, LED_GREEN)
        i+=1
    beep(device, BEEP_TIME)
    printResponse(response)
    sleep(0.3)

