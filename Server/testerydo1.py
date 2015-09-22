'''python XMPP_NCAP_Server.py -j test@grandline.terracrypt.net -p test'''
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

#------ Global Variables--------------------------
global ServerID
ServerID = '1'

global ClientID
ClientID = 'client1@jahschwa.com'

global ServerName
ServerName = 'Server1'

global ServerIP
ServerIP = 'xxx'

global ClientIDGroup
ClientIDGroup = 'xxx'

global NumTIM
NumTIM = '1'

global TIMID
TIMID = '1'

global numofTransducerChannel
numofTransducerChannel = '3'

global TransducerChannelID
TransducerChannelID = '[1,2,3]'

global NCAPID
NCAPID = '1'


#####################################################
# UART function
def readlineCR(port):
        ch = port.read()
        rv = ''
        while (ch!='!') & (ch!=''):
                
                rv += ch
                ch = port.read()
                
        return rv
#####################################################


#####################################################
# uart stuff
def UART_send(TIMID,ChannelID,TIMmsg):
    
    if ChannelID == '1':
        A = 'LIGHT'
    elif ChannelID == '2':
        A = 'FAN'
    
    if TIMmsg == '721':
        UARTport.write('TEMP1!')
    elif TIMmsg == '727,0':
        B = 'OFF!'
        UARTport.write(A + B)
    elif TIMmsg == '727,1':
        B = 'ON!'
        UARTport.write(A + B)

def UART_Rec(timid,timchannel):
    myMsg = readlineCR(UARTport)
    return myMsg
#####################################################



#####################################################
# xmpp send function
def xmpp_send(toAddr,myMsg,**key):
    type = 'Normal'
    if ('type' in key):
        type = key['type']
    if type == 'Normal':
        xmpp.send_message(
            mto=toAddr,mbody=myMsg,mtype='chat')
    elif type == 'All':
        toAddr = 'P21451'
        xmpp.send_message(
            mto=toAddr,mbody=myMsg,mtype='groupchat')
#####################################################


#####################################################
# TIM init        
global UARTport
UARTport = serial.Serial(
        "/dev/ttyAMA0", baudrate=9600, timeout= 0.25)

tim_on = False
print '\n\nWaiting for TIM...\n'
myMsg = 'None'
UARTport.flushInput()
UARTport.write('!PING!')
myMsg = readlineCR(UARTport)

if myMsg == 'PONG':
        tim_on = True
        print 'TIM Connected!\n\n'
else:
        print 'TIM Not Found!\n\n'
    
UARTport.flushInput()
UARTport.write('FANOFF!')
UARTport.write('LIGHTOFF!')

'''global fState
global lState
fState = 0
lState = 0'''
#####################################################


#####################################################
# 
if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input
#####################################################


#####################################################
# 
def Parse(string,delim,stop):

    parsedString = string.split(stop)
    parsedString = parsedString[0].split(delim)
    parseNum = len(parsedString)

    return parsedString
#####################################################


#####################################################
# Reading Transducer sample data from a single channel of single TIM
def ReadTransducerSampleDataFromAChannelofTIM(msg):
    if msg[1] == ServerID:
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]

        #Polling TIM for data
        if ChannelID == '1':
            UART_send(TIMID,'1','721')
            SampleData =  UART_Rec(TIMID,'1')
        
        elif ChannelID == '2':
            UART_send(TIMID,'2','721')
            SampleData =  UART_Rec(TIMID,'2')
        
    elif ChannelID == '3':
        UART_send(TIMID,'3','721')
        SampleData =  UART_Rec(TIMID,'3')
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)
    
        
    reply = '0,'+ServerID+','+TIMID+','+ChannelID+','+SampleData
    xmpp_send(ClientID,reply)
    
    print SampleData
    event = UART_Rec(TIMID,'event')
    if event == 'EVENT':
        print 'Whoop!'
        xmpp_send(ClientID,event+',6,6,6;')



# Reading Transducer block data from a single channel of single TIM
'''def ReadTransducerBlockDataFromAChannelofTIM(msg):
    if msg[1] == ServerID:
        msg[2] = TIMID
        msg[3] = ChannelID
        msg[4] = Timeout
        msg[5] = NumSample
        msg[6] = SampleInterval
        msg[7] = StartTime

        TimMSG = '722,' + NumSample + ','+ SampleInterval + ','+ StartTime
        
        #Poling TIM for data
        if ChannelID == 1:
        UART_send(TIMID,Channel1,TimMSG)
        SampleData =  UART_Rec(TIMID,Channel1)
        elif ChannelID == 2:
        UART_send(TIMID,Channel2,TimMSG)
        SampleData =  UART_Rec(TIMID,Channel2)
        
        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID + ','+ SampleData
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)'''


# Reading Transducer sample data from a multiple channels of single TIM
'''def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg):
    if msg[1] == ServerID:
        msg[2] = TIMID
        msg[3] = ChannelIDs
        msg[4] = Timeout

        #Polling TIM for data
        UART_send(TIMID,Channel1,'723')
        SampleData1 =  UART_Rec(TIMID,Channel1)
        UART_send(TIMID,Channel2,'723')
        SampleData2 =  UART_Rec(TIMID,Channel2)

        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID + ','+ SampleData1 + ',' + SampleData2
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)'''


# Reading Transducer block data from a multiple channels of single TIM
'''def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg):
    if msg[1] == ServerID:
        msg[2] = TIMID
        msg[3] = ChannelIDs
        msg[4] = Timeout
        msg[5] = NumSample
        msg[6] = SampleInterval
        msg[7] = StartTime

        TimMSG = '724,' + NumSample + ','+ SampleInterval + ','+ StartTime

        #Poling TIM for data
        UART_send(TIMID,Channel1,TimMSG)
        SampleData1 =  UART_Rec(TIMID,Channel1)
        UART_send(TIMID,Channel2,TimMSG)
        SampleData2 =  UART_Rec(TIMID,Channel2)

        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID + ','+ SampleData1 + ',' + SampleData2
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply) '''


# Reading Transducer sample data from a multiple channels of multiple TIMs
'''def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg):
    if msg[1] == ServerID:
        msg[2] = TIMIDs
        msg[3] = ChannelIDs
        msg[4] = Timeout

        #Poling TIM for data
        UART_send(TIM1,Channel1,'725')
        SampleData1 =  UART_Rec(TIMID,Channel1)
        UART_send(TIM1,Channel2,'725')
        SampleData2 =  UART_Rec(TIMID,Channel2)

        UART_send(TIM2,Channel1,'725')
        SampleData3 =  UART_Rec(TIMID,Channel1)
        UART_send(TIM2,Channel2,'725')
        SampleData4 =  UART_Rec(TIMID,Channel2)

        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID + ','+SampleData1 + ',' + SampleData2 + ','+ SampleData3 + ',' + SampleData4
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)'''

         

# Reading Transducer block data from a multiple channels of multiples TIM
'''def ReadTransducerSampleDataFromMultipleChannelsofTIM(msg):
    if msg[1] == ServerID:
        msg[2] = TIMIDs
        msg[3] = ChannelIDs
        msg[4] = Timeout
        msg[5] = NumSample
        msg[6] = SampleInterval
        msg[7] = StartTime

        TimMSG = '726,' + NumSample + ','+ SampleInterval + ','+ StartTime
        
        #Poling TIM for data
        UART_send(TIM1,Channel1,TimMSG)
        SampleData1 =  UART_Rec(TIMID,Channel1)
        UART_send(TIM1,Channel2,TimMSG)
        SampleData2 =  UART_Rec(TIMID,Channel2)

        UART_send(TIM2,Channel1,TimMSG)
        SampleData3 =  UART_Rec(TIMID,Channel1)
        UART_send(TIM2,Channel2,TimMSG)
        SampleData4 =  UART_Rec(TIMID,Channel2)
        
        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID +','+ SampleData1 + ',' + SampleData2 + ','+ SampleData3 + ',' + SampleData4
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)'''


# Writing Transducer Sample data from a single channels of a TIM
def WriteTransducerSampleDataFromMultipleChannelsofTIM(msg):
    if msg[1] == ServerID:
        TIMID = msg[2]
        ChannelID = msg[3]
        Timeout = msg[4]
        Sampling_Mode = msg[5]
        Data = msg[6]

        TimMSG = '727,' + Data
        
        #Poling TIM for data
        UART_send(TIMID,ChannelID,TimMSG)
        
        reply = '0,' + ServerID +','+ TIMID + ',' + ChannelID 
        xmpp_send(ClientID,reply)
    else:
        reply = '1,' + ServerID  
        xmpp_send(ClientID,reply)


def Server_Main(rawmsg):
    UARTport.flushInput()
    msg = Parse(rawmsg,',', ';')

    if msg[0] == '721':
        ReadTransducerSampleDataFromAChannelofTIM(msg)
    elif msg[0] == '722':
        ReadTransducerBlockDataFromAChannelofTIM(msg)
    elif msg[0] == '723':
        ReadTransducerSampleDataFromMultipleChannelsofTIM(msg)
    elif msg[0] == '724':
        ReadTransducerBlockDataFromMultipleChannelsofTIM(msg)
    elif msg[0] == '725':
        ReadTransducerSampleDataFromMultipleChannelsofMultipleTIM(msg)
    elif msg[0] == '726':
        ReadTransducerBlockDataFromMultipleChannelsofMultiplesTIM(msg)
    elif msg[0] == '727':
        WriteTransducerSampleDataFromMultipleChannelsofTIM(msg)





#####################################################
# xmpp class   
class NCAPserver(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, room, nick):
        
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        
        self.room = room
        self.nick = nick
        
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)
        self.add_event_handler("groupchat_message", self.muc_message)
        self.add_event_handler("muc::%s::got_online" % self.room, self.muc_online)

    def start(self, event):
        
        self.send_presence()
        self.get_roster()
        ## self.plugin['xep_0045'].joinMUC(self.room,self.nick,wait=True)

    def message(self, msg):
        
        stringy = str(msg['body'])
        recStr = str(msg['from'])
        recStr = Parse(recStr,'@','/')
        print recStr[0] + ':\t\t\t' + stringy
        
        if (stringy == 'Q') or (stringy == 'q'):
            raise SystemExit
        if (stringy == 'R') or (stringy == 'r'):
            os.system('sudo reboot')

            
        Server_Main(stringy+';')
        
    def muc_message(self, msg):
        if msg['mucnick'] != self.nick and self.nick in msg['body']:
            self.send_message(mto=msg['from'].bare,
                mbody= "I heard that, %s." % msg['mucnick'],
                mtype='groupchat')
    
    def muc_online(self, presence):
        if presence['muc']['nick'] != self.nick:
            self.send_message(mto=presence['from'].bare,
                mbody="Hello, %s %s" % (presence['muc']['role'],
                presence['muc']['nick']), mtype='groupchat')
#####################################################


if __name__ == '__main__':

    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
        action='store_const', dest='loglevel',
        const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
        action='store_const', dest='loglevel',
        const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
        action='store_const', dest='loglevel',
        const=5, default=logging.INFO)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
        help="JID to use")
    optp.add_option("-p", "--password", dest="password",
        help="password to use")
    optp.add_option("-r", "--room", dest="room",
        help="room for one more?")
    optp.add_option("-n", "--nick", dest="nick",
        help="nick at nite!")
    
    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    if opts.jid is None:
        opts.jid = 'server1@jahschwa.com'
    
    if opts.password is None:
        opts.password = 'Password1'
    
    if opts.room is None:
        opts.room = 'P21451@conference.grandline.terracrypt.net'
        
    if opts.nick is None:
        opts.nick = 'P21451'

    xmpp = NCAPserver(opts.jid, opts.password, opts.room, opts.nick)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0004') # Data Forms
    xmpp.register_plugin('xep_0060') # PubSub
    xmpp.register_plugin('xep_0199') # XMPP Ping
    xmpp.register_plugin('xep_0045') # MUC plugin

    if xmpp.connect():
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")
