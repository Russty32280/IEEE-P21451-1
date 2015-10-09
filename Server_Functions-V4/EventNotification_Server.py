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

		 
		 

## 751: Read TIM Configuration
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt tIMConfig
# Please see the standard for READ TIM configuration Returns



## 752: Write TIM Configuration
#	Request:
#		UInt16 ncapId
#		UInt16 timId
#		TimeDuration timeout
#		UInt8 tIMConfig
#	Response:
#		UInt8 errorCode
# Please see standard for WRITE TIM configuration Returns



## 753: Read Packet Loss Rate
# This function is dependent on packet loss monitoring/actual packet sending
# Returns the rate at which packet communication is flagged as incomplete.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt16packetLossRate



## 754: Read Link Utilization
# Reads the theoretical percentage usage of the TIM's communication link.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#	Response:
#		UInt16 LinkUtilization (Data Throughput Utilization)



## 755: Read TIM Utilization
# Returns the percentage usage of the TIM processor and its throughput
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#	Response:
#		UInt16 TIMUtilization (Hardware Throughput)



## 756: Read Latency
# Returns the speed communication takes place.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#	Response:
#		TimeDuration latency



## 757: Read Measurement Update Interval (Trigger Services)
# Read the timing of a pre-existing trigger
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt16 measurementUpdateInterval



## 758: Read TIM Fault Diagnostics
# Read a desired TIM's Fault Flags
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt16Array TIMFaultDiagnostics



## 759: Read TIM Health
# Read is the Health of a desired TIM. Health is a quantized value that can clue in if the TIM is bound for failure
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt16 TIMHealth



## 7510: Read Maintenance Due
# Read the set maintenance date of a TIM
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		uInt16 daysUntilMaintenanceDue



## 7511: Write Maintenance Due
# Set the number of days until the next service should be carried out for a desired TIM
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16 daysUntilMaintenanceDue
#		TimeDuration timeout
#	Response:
#		UInt16 errorCode



## 7512: Read Measurement Accuracy
# Read the expected percent error of a specific reading
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		Float32measurementUncertainty



## 7513: Write TIM Self Test Result:
# Initiates a self-test of a TIM. Upon completion of self-test, TIM responds with a report of the outcome of the diagnostics.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt8 TIMSelfTestResult



## 7514: Read TIM Reference Test
# TIM uses desired reference to carry out calibration readings.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16 reference (what reference TIM is using for test)
#	Response:
#		UInt16 TIMReferenceTest



## 7515: Read TIM Location
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		TimeDuration timeout
#	Response:
#		UInt16Array TIMLocation



## 7516: Write Calibrate TIM
# Using calibration arrays, TIM is calibrated from the software side.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16Array TIMParametersA
#		UInt16Array TIMParametersB
#		UInt16Array TIMParametersC
#	Response:
#		UInt16 writeSuccess (was TIM written to)



## 7517: Read Calibrate TIM
# Using Calibration Arrays, TIM is calibrate from the software side.
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#	Response:
#		UInt16Array TIMParametersA
#		UInt16Array TIMParametersB
#		UInt16Array TIMParametersC



## 7518: Write Time Sync TIM
# Synchronizes TIM using timeSyncParameters
#	Request:
#		UInt16 ncapID
#		UInt16 timID
#		UInt16array timeSyncParameters (see the standard)
#	Response:
#		UInt16 writeSuccess (was TIM written to)




		 
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
