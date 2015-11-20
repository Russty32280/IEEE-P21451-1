#----------------------------- Server Implementation ----------------------#
# This is a rehash of the original implementation file "testrydo1.py" which utilizes
# functions from the P21451-1 Standard. Most code is copied from that original file.

import sleekxmpp
import sys
import os
import logging
import getpass
from optparse import OptionParser
import serial
import time
import warnings
# import P21451dash1


warnings.filterwarnings("ignore", category=SyntaxWarning)

#--------- Global Variables -------------

# The old code utilized a hardcoded value for these values.
# We need to be able to dynamically receive these values.

#**************************************
# OLD CODE

# global ServerID
# ServerID = '1'

# global ClientID
# ClientID = 'client1@jahschwa.com'

# global ServerName
# ServerName = 'Server1'

# global ServerIP
# ServerIP = 'xxx'

# global ClientIDGroup
# ClientIDGroup = 'xxx'

# global NumTIM
# NumTIM = '1'

# global TIMID
# TIMID = '1'

# global numofTransducerChannel
# numofTransducerChannel = '3'

# global TransducerChannelID
# TransducerChannelID = '[1,2,3]'

# global NCAPID
# NCAPID = '1'
#***************************************

# New Method

# For now this should stay hardcoded, however we will look into how to automate this name.
global NCAPServerID
NCAPServerID = 'NCAP1'

global NCAPClientID
NCAPClientID = '0'
NCAPClientID = NCAPServerRegister()

# This code needs to be implemented in the Identification Services File
#while NCAPClientID == '0'
#	time.sleep(1)
#	print "Looking for Clients"
#	(insert code to send request to clients)
#	if response == '1' # We got an actual response from a client
#		NCAPClientID = Response_from_Client
#		print "Connected to Client: " NCAPClientID


#####################################################
# 
def Parse(string,delim,stop):

    parsedString = string.split(stop)
    parsedString = parsedString[0].split(delim)
    parseNum = len(parsedString)

    return parsedString
#####################################################









#################################################
#				XMPP SEND
#################################################
def xmpp_send(toAddr,myMsg,**key):
    type = 'Normal'
    if ('type' in key):
        type = key['type']
    if type == 'Normal':
        xmpp.send_message(
            mto=toAddr,mbody=myMsg,mtype='chat')
    elif type == 'All':
        toAddr = 'P21451'
        xmpp.send_message(
            mto=toAddr,mbody=myMsg,mtype='groupchat')




###################################################
#				TIM Initialization
###################################################

# This function should return something like XML or objects which we can reference.
TIMs = NCAPTIMDiscover();
# From this information, we can import information about each TIM and save it.
for n <= TIMs(1)
	



