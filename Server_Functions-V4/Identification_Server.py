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
         NCAPServerDisocery()
    elif msg[0] == '714'
         NCAPTIMDiscovery()
    elif msg[0] == '715'
         NCAPTransducerDiscovery()
    elif msg[0] == '716'
         NCAPClientJoin()
    elif msg[0] == '717'
         NCAPClientUnJoin()

def NCAPServerRegister
    msg = '711,' + ServerID + ',' + ServerName + ',' + ServerIP
    xmpp_send(ClientIDGroup, msg,type = 'All')

def NCAPServerUnRegister
    msg = '712,' + ServerID 
    xmpp_send(ClientIDGroup, msg,type = 'All')

def NCAPServerDiscovery(msg)
    ClientID == msg[1]
      reply = '0,' + ServerID
      xmpp_send(ClientID,reply)

def NCAPTIMDiscovery(msg)
    if msg[1] == ClientID
      reply = '0,' + NumTIM + ',' + TIMID
      xmpp_send(ClientID,reply)
    else
        reply = '1'  
        xmpp_send(ClientID,reply)    

def NCAPTransducerDiscovery(msg)
    if msg[1] == ClientID
      reply = '0,' + ServerID + ',' + TIMID + ',' + numofTransducerChannel + ',' + TransducerChannelID
      xmpp_send(ClientID,reply)
    else
        reply = '1'  
        xmpp_send(ClientID,reply)    


    
