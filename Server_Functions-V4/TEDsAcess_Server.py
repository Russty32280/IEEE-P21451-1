#-------------------------------------- 7.3 TEDS Access Services----------------------------------------------#
# Server TEDS Access Services - CSD - Created: 03/31/2015 - Modified: 05/19/2015

int ServerID = '1';

def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == ‘732’
         ReadTransducerChannelTEDServices()
     elif msg[0] == ‘7312’
         ReadWriteTransducerChannelTEDSServices()
		 


		 
## 731: Read TIM MetaTEDS
#
# Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#
# Response:
#		UInt16 errorCode
#		UInt16 StringArray timMetaTEDS		 
	
	

## 732: Read Transducer Channel TEDS services
#
# Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16 channelID
#		TimeDuration timeout
#
# Response:
#		UInt16 errorCode
#		StringArray transducerChannelTEDS

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

		
		
		
## 733: Read User Transducer Name 
# 
# Request:
#		UInt16 ncapID
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray userTranducerNameTEDS



## 734: Read 1451Dot5 802Dot11 PhyTEDS
# 
# Request:
#		UInt16 ncapID
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray 1451.5Dot802Dot11PhyTEDS



## 735: Read 1451Dot5 BlueTooth PhyTEDS
# 
# Request:
#		UInt16 ncapID
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray 1451Dot5BlueToothPhyTEDS



## 736: Read 1451Dot5 ZigBee PhyTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray 1451Dot5ZigBeePhyTEDS



## 737: Read 1451Dot5 6LowPAN PhyTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray 1451Dot56LowPANPhyTEDS



## 738: Read 1451Dot2 PhyTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray 1451Dot2PhyTEDS



## 739: Read TIM MetaIdTEDS service
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		ArgumentArray timMetaIdTEDS



## 7310: Read Transducer Channel MetaIdTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		UInt16 channelId 
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		out ArgumentArray tranducerChannelIdTEDS



## 7311: Read TIM GeoLocationTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# Response:
#		UInt16 errorCode
# 		StringArray timGeoLocationTEDS



## 7312: Write TIM MetaTEDS
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		UInt16 StringArray timMetaTEDS
# Response:
#		UInt16 errorCode	
		


## 7313: Write Transducer ChannelTEDS Services
# 
# Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16 channelID
#		TimeDuration timeout
#		StringArray transducerChannelTEDS
# Response:
# 		UInt16 errorCode
	
def WriteTransducerChannelTEDSServices
    #
	if msg[1] == ncapID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        transducerChannelTEDS = msg[5] #Data to be written to TIM

        # Message sent to the TIM
        TimMSG = '7312,' + ChannelId + ',' + transducerChannelTEDS

        #Writing data to TIM
		"""This should ultimately be replaced with a "Universal" function which can write to the TIM Regardless of 
         the method which is used to communicate with it (UART, I2C, etc.)
		 """
		 UART_send(timId,ChannelId,TimMSG)
         TEDS1 =  UART_Rec(timId,ChannelId)
           
        #Sends reply message once writing functions have been sent. 1 for errors and 0 for no error
        reply = '0,' +TEDS1
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

		
## 7314: Write User Transducer NameTEDS 
# 
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray userTranducerNameTEDS
# Response:
#		UInt16 errorCode



## 7315: Write 1451Dot5 802Dot11 PhyTEDS 
# WriteIEEE 14541.5-802.11 (tedsType = 13, RadioType=0)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray userTranducerNameTEDS
# Response:
#		UInt16 errorCode



## 7316: Write 1451Dot5 BlueTooth PhyTEDS 
# WriteIEEE 1451.5-BlueTooth (tedsType = 13, RadioType=1)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray 1451Dot5BlueToothPhyTEDS
# Response:
#		UInt16 errorCode



## 7317: Write 1451Dot5 ZigBee PhyTEDS 
# WriteIEEE 1451.5-ZigBee (tedsType = 13, RadioType=2)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray 1451Dot5ZigBeePhyTEDS
# Response:
#		UInt16 errorCode



## 7318: Write 1451Dot5 6LowPAN PhyTEDS  
# WriteIEEE 1451.5-6LWPAN (tedsType = 13, RadioType=3)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray 1451Dot56LowPANPhyTEDS
# Response:
#		UInt16 errorCode



## 7319: Write 1451Dot2 PhyTEDS  
# WriteIEEE 1451.2 (tedsType = 13, serialType=1,2,3,4,5)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		StringArray 1451Dot2PhyTEDS
# Response:
#		UInt16 errorCode



#Optional:

## 7320: Write TIM MetaIdTEDS service  
# WriteTIM MetaID TEDS Service (tedsType=1)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
# 		ArgumentArray timMetaIdTEDS
# Response:
#		UInt16 errorCode



## 7321: Write Transducer Channel MetaId TEDS  
# WriteTransducerChannel MetaID TEDS Service    ( tedsType=1)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		UInt16 channelId 
#		TimeDuration timeout
# 		out ArgumentArray tranducerChannelIdTEDS
# Response:
#		UInt16 errorCode



## 7322: Write TIM GeoLocationTEDS service  
# WriteTIM GeoLocation TEDS Web service: (tedsType=14)
# Request:
#		UInt16 ncapId
#		UInt16 timId
#		UInt16 channelId 
#		TimeDuration timeout
# 		StringArray timGeoLocationTEDS
# Response:
#		UInt16 errorCode