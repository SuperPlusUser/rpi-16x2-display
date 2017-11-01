
# -*- coding: utf-8 -*-
"""
16x2 I2C Display
Version 1.0.0
DELOARTS Research Inc.
Philip Delorenzo
02.05.2016

This script interacts with an 16x2 display wired on the I2C bus on the Raspberry Pi.
It prints the IP address of the Raspberry.
"""
import lcd
from time import sleep
from subprocess import *

def runCMD(cmd):
    com = Popen(cmd, shell=True, stdout=PIPE)
    shellOutput = com.communicate()
    return shellOutput[0]

if __name__ == "__main__":
    cmdIP = "ip addr show eth0 | grep inet |awk '{print $2}' | cut -d/ -f1"
    strIP = runCMD(cmdIP)

    lcd.init()
    lcd.printString("IP Address:", lcd.line1)
    lcd.printString(strIP.split('\n')[0], lcd.line2)
    sleep(15)
    lcd.clear()
    lcd.setBacklightOff()