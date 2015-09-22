#UDP
import serial
import time
import RPi.GPIO as GPIO
import sys
import logging
import getpass
import ads1x15_ex_singleended1 as ADC1
import sleekxmpp
## SPECIFIC TO MAX CHIP##
#from max31855 import MAX31855, MAX31855Error
from time import sleep


cs_pin = 18 #GPIO 24 /18
clock_pin = 16 #GPIO 23 /16
data_pin = 15 #GPIO 22 /15
units = "f"


GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setwarnings(False)

#####################################################
# UART function
def readlineCR(port):
	ch = port.read()
        rv = ""
        while ch != "!":
                rv += ch
		ch = port.read()
        return rv
#####################################################

#####################################################
# TIM init           #ttyAMA0         
UARTport = serial.Serial(
    "/dev/ttyAMA0",baudrate=9600, timeout =20.0) # baudrate=115200, timeout=20.0)
#####################################################
while True:
	GPIO.setwarnings(False)
	myMsg= readlineCR(UARTport)
	print myMsg
	if myMsg == 'PING':
		UARTport.write('PONG' +'!')
		print 'pong'

	if myMsg == 'FANON':
		GPIO.output(40,True)
		#UARTport.write('FAN ON!')
		#msg.reply("GPIO on").send()
	if myMsg == 'FANOFF':
		GPIO.output(40, False)
		#sleep(1)
		#UARTport.write('FAN OFF!')
		#msg.reply("GPIO off").send()
	if myMsg == 'LIGHTON':
        	GPIO.output(37, True)
        	#sleep(1)
		#UARTport.write('LIGHT ON!')
        #msg.reply("GPIO off").send()
    	if myMsg == 'LIGHTOFF':
        	GPIO.output(37, False)
        	#sleep(1)
		#UARTport.write('LIGHT OFF')
    	#if myMsg == 'TEMP':
	#	thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
	#	print(thermocouple.get())
	#	TEMP = str(thermocouple.get())
        	#sleep(1)
	#	UARTport.write(TEMP + '!')
        	#msg.reply("GPIO off").send()
	if myMsg == 'TEMP1':
		TEMP1= (ADC1.readADC()-.5) *100

		if TEMP1 > 25:
			TEMP1 = str(TEMP1)
			UARTport.write(TEMP1 + '!')
			UARTport.write('EVENT!')
			print TEMP1 + " EVENT!"
		else:
			TEMP1 = str(TEMP1)
			UARTport.write(TEMP1 + '!')
			print TEMP1
		
		#Single ended ADC
#to send something:
#UARTport.write('stuff')

#to recieve:
#myMsg = readlineCR(UARTport)

