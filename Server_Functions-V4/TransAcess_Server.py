#-------------------------------------- 7.2 Transducer Access Services----------------------------------------------#
# Server Transducer Access Services - CSD - Created: 03/24/2015 - Modified: 05/19/2015

int ServerID = '1';

def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == '7211'
         ReadTransducerSampleDataFromAChannelofTIM()
    elif msg[0] == '7212'
         ReadTransducerBlockDataFromAChannelofTIM()
    elif msg[0] == '7213'
         ReadTransducerSampleDataFromMultipleChannelsofTIM()
    elif msg[0] == '7214'
         ReadTransducerBlockDataFromMultipleChannelsofTIM()
    elif msg[0] == '7215'
         ReadTransducerSampleDataFromMultipleChannelsofMultipleTIM()
    elif msg[0] == '7216'
         ReadTransducerBlockDataFromMultipleChannelsofMultiplesTIM()
    elif msg[0] == '7217'
         WriteTransducerSampleDataFromMultipleChannelsofTIM()
	#elif msg[0] == '7218'
		#WriteTransducerBlockDataFromMultipleChannelsOfATIM()
	#elif msg[0] == '7219'
		#WriteTransducerSampleDataFromAChannelOfATIM()
	#elif msg[0] == '7220'
		#WriteTransducerBlockDataFromAChannelOfATIM()
	#elif msg[0] == '7221'
		#WriteTransducerSampleDataFromMultipleChannelsOfMultipleTIMs()
	#elif msg[0] == '7222'
		#WriteTransducerBlockDataFromMultipleChannelsOfMultipleTIMs()
	#elif msg[0] == '7223'
		#ReadTransducerBlockDataFromAChannelOfATIM()
	#elif msg[0] == '7224'
		#ReadTransducerStreamDataFromAChannelOfATIM()
	#elif msg[0] == '7225'
		#ReadTransducerBlockDataFromMultipleChannelsOfATIM()
	#elif msg[0] == '7226'
		#ReadTransducerBlockDataFromMultipleChannelOfMultipleTIMs()

		


# Reading Transducer sample data from a single channel of single TIM

## ReadTransducerSampleDataFromAChannelofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16 channelId
#               TimeDuration timeout
#               UInt8 samplingMode
#
#Response:
#               UInt16 errorCode
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16 channelId
#               _String transducerSampleData
 def ReadTransducerSampleDataFromAChannelofTIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

		
		# This part needs to be replaced with a TIMSend which has a Channel Input
		#
		#	TIM_Send(TIMID, ChannelID, '721')
		#	SampleData = TIM_Recieve(TIMID, ChannelID);
		#
        #Polling TIM for data
        if ChannelID == 1
            UART_send(TIMID,Channel1,'721')
            SampleData =  UART_Rec(TIMID,Channel1);
        elif ChannelID == 2
             UART_send(TIMID,Channel2,'721')
             SampleData =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End 


# Reading Transducer block data from a single channel of single TIM

## ReadTransducerBlockDataFromAChannelofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16 channelId
#               TimeDuration timeout
#               UInt8 samplingMode
#		UInt32 numberOfSamples
#		TimeInstance startTime
#
#Response:
#               UInt16 errorCode
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16 channelId
#               StringArray transducerBlockData
 def ReadTransducerBlockDataFromAChannelofTIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        NumSample = msg[5]
        SampleInterval = msg[6]
        StartTime = msg[7]

        TimMSG = '722,' + NumSample + ',' SampleInterval + ',' StartTime
        
        #Poling TIM for data
        if ChannelID == 1
            UART_send(TIMID,Channel1,TimMSG)
            SampleData =  UART_Rec(TIMID,Channel1);
        elif ChannelID == 2
             UART_send(TIMID,Channel2,TimMSG)
             SampleData =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End

# Reading Transducer sample data from a multiple channels of single TIM

## ReadTransducerSampleDataFromMultipleChannelsofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16Array channelIds
#               TimeDuration timeout
#               UInt8 samplingMode
#
#Response:
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16Arrays channelIds
#               StringArray transducerBlockDatas
 def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

        #Poling TIM for data
         UART_send(TIMID,Channel1,'723')
         SampleData1 =  UART_Rec(TIMID,Channel1);
         UART_send(TIMID,Channel2,'723')
         SampleData2 =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData1 + ',' + SampleData2
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End 

# Reading Transducer block data from a multiple channels of single TIM

## ReadTransducerBlockDataFromMultipleChannelsofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16Array channelIds
#               TimeDuration timeout
#               UInt32 numberOfSamples
#		TimeInterval sampleInterval
#		TimeInterval startTime
#
#Response:
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16Arrays channelIds
#               StringArray transducerBlockDatas
 def ReadTransducerBlockDataFromMultipleChannelsofTIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        NumSample = msg[5]
        SampleInterval = msg[6]
        StartTime = msg[7]

        TimMSG = '724,' + NumSample + ',' SampleInterval + ',' StartTime
        
        #Poling TIM for data
         UART_send(TIMID,Channel1,TimMSG)
         SampleData1 =  UART_Rec(TIMID,Channel1);
         UART_send(TIMID,Channel2,TimMSG)
         SampleData2 =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData1 + ',' + SampleData2
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End 


# Reading Transducer sample data from a multiple channels of multiple TIMs

## ReadTransducerSampleDataFromMultipleChannelsofMultipleTIMs
#
#Request:
#               UInt16 timIds
#               UInt16 ncapId
#		UInt16Array numberOfChannelsOfTIM
#               UInt16Array channelIds
#               TimeDuration timeout
#               UInt8 samplingMode
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16Array timeIDs
#		UInt16 numberOfChannelsOfTIM
#               UInt16Arrays channelIds
#               StringArray transducerSampleDatas
 def ReadTransducerSampleDataFromMultipleChannelsofMultipleTIMs(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

        #Poling TIM for data
         UART_send(TIM1,Channel1,'725')
         SampleData1 =  UART_Rec(TIMID,Channel1);
         UART_send(TIM1,Channel2,'725')
         SampleData2 =  UART_Rec(TIMID,Channel2);

         UART_send(TIM2,Channel1,'725')
         SampleData3 =  UART_Rec(TIMID,Channel1);
         UART_send(TIM2,Channel2,'725')
         SampleData4 =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData1 + ',' + SampleData2 + ',' SampleData3 + ',' + SampleData4
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End         

# Reading Transducer block data from a multiple channels of multiples TIM

## ReadTransducerBlockDataFromMultipleChannelsofMultipleTIMs
#
#Request:
#               UInt16 timIds
#               UInt16 ncapId
#		UInt16Array numberOfChannelsOfTIM
#               UInt16Array channelIds
#               TimeDuration timeout
#               UInt32 numberOfSample
#		TimeInterval sampleInterval
#		TimeInterval startTime
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16Array timeIDs
#		UInt16 numberOfChannelsOfTIM
#               UInt16Arrays channelIds
#               StringArray transducerBlockDatas
 def ReadTransducerBlockDataFromMultipleChannelsofMultipleTIMs(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        NumSample = msg[5]
        SampleInterval = msg[6]
        StartTime = msg[7]

        TimMSG = '726,' + NumSample + ',' SampleInterval + ',' StartTime
        
        #Poling TIM for data
         UART_send(TIM1,Channel1,TimMSG)
         SampleData1 =  UART_Rec(TIMID,Channel1)
         UART_send(TIM1,Channel2,TimMSG)
         SampleData2 =  UART_Rec(TIMID,Channel2)

         UART_send(TIM2,Channel1,TimMSG)
         SampleData3 =  UART_Rec(TIMID,Channel1);
         UART_send(TIM2,Channel2,TimMSG)
         SampleData4 =  UART_Rec(TIMID,Channel2);
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID + ',' SampleData1 + ',' + SampleData2 + ',' SampleData3 + ',' + SampleData4
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)

#End


## WriteTransducerSampleDataToAChannelofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16 channelId
#               TimeDuration timeout
#               UInt8 samplingMode
#		String dataValue ??
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16 channelId


## WriteTransducerBlockDataToAChannelofTIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16 channelId
#               TimeDuration timeout
#               UInt32 numberOfSamples
#		TimeInterval sampleInterval
#		TimeInstance startTime
#		String dataValue ??
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16 channelId



# Writing Transducer Sample data from a single channels of a TIM

## WriteTransducerSampleDataToMultipleChannelsOfATIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16Arrays channelIds
#               TimeDuration timeout
#               UInt8 samplingMode
#		String transducerSampleDatas
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16Array channelIds
def WriteTransducerSampleDataToMultipleChannelsOfATIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        Sampling Mode = msg[5]
        Data = msg[6]

        TimMSG = '727,' + Data
        
        #Sending TIM data to be written to a channel
         UART_send(TIMID,ChannelID,TimMSG)
        
        reply = '0,' + ServerID +',' TIMID + ',' + ChannelID 
        xmpp_send(ClientID,reply)
    else
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)



## WriteTransducerBlockDataToMultipleChannelsOfATIM
#
#Request:
#               UInt16 ncapId
#               UInt16 timId
#               UInt16Arrays channelIds
#               TimeDuration timeout
#               UInt32 numberOfSamples
#		TimeInterval sampleInterval
#		TimeInterval startTime
#
#Response:
#               UInt16 ncapId
#               UInt16 timeID
#               UInt16Array channelIds
#		StringArray transducerBlockDatas


## WriteTransducerSampleDataToMultipleChannelsOfMultipleTIMs
#
#Request:
#               UInt16 ncapId
#               UInt16Array timIds
#               UInt16Arrays numberOfChannelsOfTIM
#		UInt16Array channelIds
#               TimeDuration timeout
#               UInt8 samplingMode
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16Arrays timeIDs
#		UInt16Array numberOfChannelsOfTIM
#               UInt16Array channelIds



## WriteTransducerBlockDataToMultipleChannelsOfMultipleTIMs
#
#Request:
#               UInt16 ncapId
#               UInt16Array timIds
#               UInt16Arrays numberOfChannelsOfTIM
#		UInt16Array channelIds
#               TimeDuration timeout
#               UInt32 numberOfSamples
#		TimeInterval sampleInterval
#		TimeInterval startTime
#		StringArray transducerBlockDatas
#
#Response:
#		UInt16 errorcode
#               UInt16 ncapId
#               UInt16Arrays timeIDs
#		UInt16Array numberOfChannelsOfTIM
#               UInt16Array channelIds

#End 