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

#### NEW TIM ANNOUNCEMENT

## 7411: Subscribe A New TIM Service
# When a TIM is plugged in (powered up?), TIM sends TIM Announcement to NCAP. NCAP should report this new TIM to NCAP Client.
# Also NCAP Client should subscribe a new TIM addition service.
#	Request:
#		uInt16 ncapID (NCAP ID)
#		TimeDuration timeout
#		_String aNewTIMSubscriber (NCAP Client)
#	Response:
#		UInt8 errorCode
#		_String aNewTIMPublisher (NCAP)
#		UInt16 subscriptionID



## 7412: Announce A New TIM
#	Request:
#		UInt16 ncapID
#		UInt16 newTIMID
#		_String aNewTIMPublisher (NCAP)
#		UInt16 subscriptionID
#		TimeInstance timAnnouncementTime
#		_String newTIMDescription (New TIM Name)



#### TIM Departure Announcement Service

## 7421: Subscribe A TIM Departure Service
# When a TIM is disconnected, TIM sends TIM departure announcement to NCAP.
# NCAP should report this departed TIM to NCAP Client.
# NCAP client should also subscribe a TIM departure service.
#	Request:
#		UInt16 ncapID
#		TimeDuration timeout
#		_String aDepartureTIMSubscriber
#	Response:
#		UInt8 errorCode
#		_String aDepartureTIMPublisher
#		UInt16 subscriptionID



## 7422: Announce A Departed TIM
# Request:
#		UInt16 ncapID
#		UInt16 newTIMID
#		UInt16 subscriptionID
#		_String aDepartedTIMPublisher
#		TimeInstance timAnnouncementTime
#		_String departedTIMDescription



#### Sensor Alert Service

## 7431: Subscribe Sensor Alert Service
# Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16 channelID
#		StringArray minMaxThreshold
#		_String sensorAlertSubscriber
# Response:
#		UInt8 status
#		_String sensorAlertPublisher
#		UInt16 subscriptionID



## 7432: Notify Sensor Alert
#	Request:
#		UInt16 ncapID
#		UInt16 timeID
#		UInt channelID
#		Argument transducerData
#		_String sensorAlertPublisher
#		UInt16 sensorAlertID
#		UInt16 subscriptionID
#		TimeInstance alertTime
#		CAPMsg	sensorAlertMsg



#### Sensor Alert Service From Multiple Channels of one TIM

## 7441: Subscribe Sensor Network
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16Array channelIds
#		StringArray minMaxThresholds
#		_String sensorAlertSubscriber
#	Response:
#		UInt8 errorCode
#		_String sensorAlertPublisher
#		UInt16 subscriptionID



## 7442: Notify Sensor Alert
#	Request:
#		UInt16 ncapID
#		UInt16 timeID
#		UInt16 channelID
#		_String transducerData
#		_String sensorAlertPublisher
#		UInt16 sensorAlertID
#		UInt16 subscriptionID
#		TimeInstance alertTime
#		CAPMsg sensorAlertMsg



#### SENSOR ALERT SERVICE from Multiple Channels of Multiple TIMs

## 7451: Subscribe Sensor Alert Service
#	Request:
#		UInt16 ncapID
#		UInt16Array timIDs
#		UInt16Array channelNumbersOfTIMs
#		UInt16Array channelIds
#		StringArray minMaxThresholds_String sensorAlertSubscriber
#	Response:
#		UInt8 errorCode
#		_String sensorAlertPublisher
#		UInt16 subscriptionID



## 7452: Notify Sensor Alert
#	Request:
#		UInt16 ncapID
#		UInt16 timeID
#		UInt16 channelID
#		Argument transducerData
#		_String sensorAlertPublisher
#		UInt16 sensorAlertID
#		UInt16 subscriptionID
#		TimeInstance alertTime
#		CAPMsg sensorAlertMsg



#### Setup Sensor Alert Thresholds

## 7461: Service for One Channel of One TIM
#	Request:
#		UInt16 ncapID
#		UInt16Array timIDs
#		UInt16 channelID
#		TimeDuration timeout
#		_String MinValue
#		_String MaxValue
#	Response:
#		UInt16 errorCode



## 7462: Service for Multiple Channels of One TIM
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16Array channelIDs
#		TimeDuration timeout
#		_StringArray MinValueArray
#		_StringArray MaxValueArray
#	Response:
#		UInt16 errorCode



## 7463: Service for Multiple Channels of Multiple TIMs
#	Request:
#		UInt16 ncapID
#		UInt16Array timID
#		UInt16Array channelIDs
#		TimeDuration timeout
#		_StringArray MinValueArray
#		_StringArray MaxValueArray
#	Response:
#		UInt16 errorCode



def NotifySensorAlert:
    Alert =  UART_Rec(TIMID,)
    TIMAlert = Parse(Alert',', ';')
    Data = TIMAlert[0]
    AlertType = TIMAlert[1]
    reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' + Data + ',' + Subscriber+ ',' + SubscriptionID  +',' + AlertType     
    xmpp_send(Subscriber,reply)

#-----------------END--------------------------------
