#-------------------------------------- 7.4 Event Notification Services----------------------------------------------#
# Server Event Notification Services - CSD - Created: 04/28/2015 - Modified: 05/19/2015




#------ Global Variables--------------------------
global ServerID
ServerID = '1'

global ServerName
ServerName = 'Server1'

global ServerIP
ServerIP = 'xxx'

global ClientID
ClientID = '1'

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
#-----------------------------------------------

def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == '743'
         SubscribeSensorAlert(msg)

# Client Subscribes to a Sensor Alerts-----------------
 def ReadTransducerSampleDataFromAChannelofTIM(msg):
    if msg[1] == ServerID
        TIMID = msg[2] 
        ChannelID= msg[3] 
        Threshold = msg[4]  
        Subscriber = msg[5]
        
        SubscriptionID = 1;
        
        reply = '0,' + ServerID +',' SubscriptionID      
        xmpp_send(ClientID,reply)
#-----------------END------------------------------

def NotifySensorAlert:
    Alert =  UART_Rec(TIMID,)
    TIMAlert = Parse(Alert',', ';')
    Data = TIMAlert[0]
    AlertType = TIMAlert[1]
    reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' + Data + ',' + Subscriber+ ',' + SubscriptionID  +',' + AlertType     
    xmpp_send(Subscriber,reply)

#-----------------END--------------------------------
