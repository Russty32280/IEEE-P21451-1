#-------------------------------------- 7.3 TEDS Access Services----------------------------------------------#
# Server TEDS Access Services - CSD - Created: 03/31/2015 - Modified: 05/19/2015

int ServerID = '1';

def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == ‘732’
         ReadTransducerChannelTEDServices()
     elif msg[0] == ‘7312’
         ReadWriteTransducerChannelTEDSServices()

def ReadTransducerChannelTEDSservices
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

        #Message to be sent to the TIm
        TimMSG = '732,' + ChannelID

        #Sending request to TIM
         UART_send(timId,ChannelId,TimMSG)
         TEDS1 =  UART_Rec(TIMId,ChannelId) # Receives the TED information
                
        reply = '0,' +TEDS1
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)


def WriteTransducerChannelTEDSServices
    if msg[1] == ncapID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        transducerChannelTEDS = msg[5] #Data to be written to TIM

        # Message sent to the TIM
        TimMSG = '7312,' + ChannelId + ',' + transducerChannelTEDS

        #Writing data to TIM
         UART_send(timId,ChannelId,TimMSG)
         TEDS1 =  UART_Rec(timId,ChannelId)
           
        #Sends reply message once writing functions have been sent. 1 for errors and 0 for no error
        reply = '0,' +TEDS1
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)
