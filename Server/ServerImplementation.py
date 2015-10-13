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

# New Skeleton Code

# For now this should stay hardcoded, however we will look into how to automate this name.
global NCAPServerID
NCAPServerID = 'NCAP1'

global NCAPClientID
NCAPClientID = '0'
NCAPClientID = NCAPServerRegister()

# This code needs to be implemented in the Identifcation Services File
#while NCAPClientID == '0'
#	time.sleep(1)
#	print "Looking for Clients"
#	(insert code to send request to clients)
#	if response == '1' # We got an actual response from a client
#		NCAPClientID = Response_from_Client
#		print "Connected to Client: " NCAPClientID


