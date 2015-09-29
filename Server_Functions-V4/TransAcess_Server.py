#-------------------------------------- 7.2 Transducer Access Services----------------------------------------------#
# Server Transducer Access Services - CSD - Created: 03/24/2015 - Modified: 05/19/2015

int ServerID = '1';

def Server_main

    msg = Parse(rawmsg,',', ';')

    if msg[0] == '721'
         ReadTransducerSampleDataFromAChannelofTIM()
    elif msg[0] == '722'
         ReadTransducerBlockDataFromAChannelofTIM()
    elif msg[0] == '723'
         ReadTransducerSampleDataFromMultipleChannelsofTIM()
    elif msg[0] == '724'
         ReadTransducerBlockDataFromMultipleChannelsofTIM()
    elif msg[0] == '725'
         ReadTransducerSampleDataFromMultipleChannelsofMultipleTIM()
    elif msg[0] == '726'
         ReadTransducerBlockDataFromMultipleChannelsofMultiplesTIM()
    elif msg[0] == '727'
         WriteTransducerSampleDataFromMultipleChannelsofTIM()
	#elif msg[0] == '728'
		#WriteTransducerBlockDataFromMultipleChannelsOfATIM()
	#elif msg[0] == '729'
		#WriteTransducerSampleDataFromAChannelOfATIM()
	#elif msg[0] == '730'
		#WriteTransducerBlockDataFromAChannelOfATIM()
	#elif msg[0] == '731'
		#WriteTransducerSampleDataFromMultipleChannelsOfMultipleTIMs()
	#elif msg[0] == '732'
		#WriteTransducerBlockDataFromMultipleChannelsOfMultipleTIMs()

# Reading Transducer sample data from a single channel of single TIM
 def ReadTransducerSampleDataFromAChannelofTIM(msg)
    if msg[1] == ServerID
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

        #Poling TIM for data
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
 def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg)
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
 def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg)
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
 def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg)
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


# Writing Transducer Sample data from a single channels of a TIM
 def WriteTransducerSampleDataFromMultipleChannelsofTIM(msg)
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

#End 
