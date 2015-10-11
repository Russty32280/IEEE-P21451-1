#--------------------- Shared TIM Services ----------------------#

# 10/11/2015
# Russell Trafford
# This file (skeleton for now) will contain the "Back end" of the NCAP which communicates with the
# TIMS. This should contain a method to store, edit, and delete TIM profiles, a function which can be used for
# sending a formatted string to and from a TIM, as well as other funcitonality to be determined.

# We will for now keep the ServerID as a global variable declared at the beginning, however we will need a
# method to not only set this value from the client, but also an easy way to pull in this value into other
# files.




## TIM_Send
# This function will send a formatted string, @param TIM_Message , to a corresponding TIM which is presumed
# to be registered and underneath this NCAP.
# TIM_Send will return the received message (as a formatted string) from the TIM.
#
# Example Usage (From Transducer Access Services):
# SampleData = TIM_Send(TIMID, ChannelID, '721')

def TIM_Send(TIM_ID, Channel_ID, TIM_Message)
	# This references a saved list of registered TIMs and looks for the corresponding method of communication.
	# TIM_Roster will return an integer which denotes the following communication style:
	#	(0) ERROR, Possibly not registered
	#	(1)	I2C
	#	(2) SPI
	#	(3) UART
	#	(4) 1-Wire
	#	(5) 802.11
	#	(6) ZigBee
	#	(7) BlueTooth
	#	(8) BlueTooth, LE
	# ** More to be determined from the Standard**
	# ** Numbers are subject to change based on fluctuations in the standard**
	# Users of this code can add more functionality if their application needs it (ex. NRF24L01)
	TIM_Comm = TIM_Roster(TIM_ID, Channel_ID)
	
	if TIM_Comm == 0
		reply = 'ERROR: TIM communication style not registered'
	elif TIM_Comm == 1
		reply = I2C_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 2
		reply = SPI_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 3
		reply = UART_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 4
		reply = OneWire_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 5
		reply = WiFi_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 6
		reply = ZigBee_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 7
		reply = BlueTooth_Send(TIM_ID, Channel_ID, TIM_Message)
	elif TIM_Comm == 8
		reply = BlueToothLE_Send(TIM_ID, Channel_ID, TIM_Message)
	else
		reply = 'ERROR: TIM_Comm out of range. Verify correct registration with TIM_ID, Channel_ID'

	
