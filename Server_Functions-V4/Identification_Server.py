#-------------------------------------- 7.1 Identification Services----------------------------------------------#
# P21451-1-4 functions - Server_identifcation - Created: 3/3/2015 - Modified: 05/19/2015

#Identifcation services

#------ Global Variables--------------------------
global ServerID
ServerID = '1'

global ServerName
ServerName = 'Server1'

global ServerIP
ServerIP = 'xxx'

global ClientIDGroup
ClientIDGroup = '

global NumTIM
NumTIM = '1'

global TIMID
TIMID = '1'

global numofTransducerChannel
numofTransducerChannel = '3'

global TransducerChannelID
TransducerChannelID = '[1,2,3]'

#--------------------------------------------------------

def Server_init
    NCAPServerRegister()

def Server_down
    NCAPServerUnRegister()    
	
def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == '713'
         NCAPServerDiscover()
    elif msg[0] == '714'
         NCAPTIMDiscovery()
    elif msg[0] == '715'
         NCAPTransducerDiscovery()
    elif msg[0] == '716'
         NCAPClientJoin()
    elif msg[0] == '717'
         NCAPClientUnJoin()

		 
# NCAPServerRegister Service 
# NCAP registers to NCAP Client to join a network, when it is powered up.
# Request:	
#		UInt16 ncapId
#		_String ncapName
#		_String ncapIPAddress		 
def NCAPServerRegister
    msg = '711,' + ServerID + ',' + ServerName + ',' + ServerIP
    xmpp_send(ClientIDGroup, msg,type = 'All')


# NCAPServerUnRegister Service
# NCAP unregisters to NCAP Client to leave network, when 
#	it is powered down.
# Request:
#		UInt16 ncapId
def NCAPServerUnRegister
    msg = '712,' + ServerID 
    xmpp_send(ClientIDGroup, msg,type = 'All')

	
# NCAPTIMRegister is missing in Standard and Code
# NCAPTransducerRegister is missing in Standard and Code	


# NCAPServerDiscover Service
# NCAP client discovery all NCAPs having registered it.
# Request: 
#		UInt16 ncapClientId
# Response:
#		UInt16 errorCode
#		UInt16 ncapId 
def NCAPServerDiscover(msg)
    ClientID == msg[1]
      reply = '0,' + ServerID
      xmpp_send(ClientID,reply)


# NCAPTIMDiscover Service
# NCAP client discovers all TIMs having registered to the 
#	specific NCAP.
# Request:
#		UInt16 ncapId
# Response:
#		UInt16 errorCode
#		UInt16 numOfTIM
#		UInt16Array timIds
def NCAPTIMDiscover(msg)
    if msg[1] == ClientID
      reply = '0,' + NumTIM + ',' + TIMID
      xmpp_send(ClientID,reply)
    else
        reply = '1'  
        xmpp_send(ClientID,reply)    

		
# NCAPTransducerDiscover Service
# NCAP client discovers all transducerChannels of the TIM
#	of the NCAP.
# Request:
# 		UInt16 ncapId
#		UInt16 timId
# Response: 
#		UInt16 errorCode
# 		UInt16 ncapId
# 		UInt16 timId
#		UInt16 numOfTransducerChannels
# 		UInt16Array transducerChannelIds
def NCAPTransducerDiscovery(msg)
    if msg[1] == ClientID
      reply = '0,' + ServerID + ',' + TIMID + ',' + numofTransducerChannel + ',' + TransducerChannelID
      xmpp_send(ClientID,reply)
    else
        reply = '1'  
        xmpp_send(ClientID,reply)    


# NCAPClientJoin is missing from Standard and not defined in the Code
# NCAPClientUnJoin is missing from Standard and not defined in the Code

    
