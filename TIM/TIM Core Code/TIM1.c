/*
 * TIM1.c
 *
 *  Created on: Dec 23, 2015
 *      Author: Russty32280
 */

#include "library.h"
#include "system.h"
#include "TIM_Core.h"
#include "random_int.h"
#include <string.h>
#include <strings.h>

struct ChannelData{
	int Chan1;
	int Chan2;
	int Chan3;
};

struct ChannelData ChanData;


META_TEDS MTEDS;
//struct CHANNEL_TEDS;


void MetaTEDSInit(void){
	/*
	 * These are filler values. You would need to look on datasheets to determine these
	 */
	MTEDS.MetaTEDSLength = 1000; //!<
	MTEDS.IEEE1451WGNum = 2;
	MTEDS.TEDSVersionNum = 1;
	strcpy(MTEDS.GloballyUID , "abcdefghij");
	MTEDS.CH0IndCalExtKey = 20;
	MTEDS.CH0IndDataExtKey = 10;
	MTEDS.CH0TEDSExtKey = 10;
	MTEDS.CH0EUAppKey = 11;
	MTEDS.WCChanDataLen = 12;
	MTEDS.WCChanDataRep = 13;
	MTEDS.CH0WrTEDSLen = 100;
	MTEDS.TWU = 1;
	MTEDS.TGWS = 2;
	MTEDS.TGRS = 3;
	MTEDS.TWSP = 4;
	MTEDS.TWWUT = 5;
	MTEDS.CRT = 6;
	MTEDS.THS = 7;
	MTEDS.TLAT = 8;
	MTEDS.TTH = 9;
	MTEDS.TOH = 10;
	MTEDS.MDR = 11;
	MTEDS.ChanGroupLen = 12;
	MTEDS.NumChanGroup = 13;
	MTEDS.MTChecksum = 14;
}


int ReadChannelTransducerData(char * ChannelID){
	int Data;
	if(strcmp(ChannelID, "001") == 0){
		ChanData.Chan1 = random_int(0,100);
		Data = ChanData.Chan1;
	}
	else if (strcmp(ChannelID, "002") == 0){
		Data = ChanData.Chan2;
	}
	return Data;
}

void WriteChannelTransducerData(char * ChannelID, int WriteData){

	if(strcmp(ChannelID, "002")==0){
		ChanData.Chan2 = WriteData;
	}
}


void ReadMetaTEDS(void){
	/*
	 * Unfortunately this is the only way i can think of doing this.
	 * Every element is separated by a comma and in order based on
	 * the -2 standard.
	 */
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.MetaTEDSLength);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.IEEE1451WGNum);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.TEDSVersionNum);
	UART_Printf(UART_CHANNEL, "%s,", MTEDS.GloballyUID);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.CH0IndCalExtKey);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.CH0IndDataExtKey);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.CH0TEDSExtKey);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.CH0EUAppKey);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.WCChanDataLen);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.WCChanDataRep);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.CH0WrTEDSLen);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TWU);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TGWS);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TGRS);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TWSP);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TWWUT);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.CRT);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.THS);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TLAT);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TTH);
	UART_Printf(UART_CHANNEL, "%f,", MTEDS.TOH);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.MDR);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.ChanGroupLen);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.NumChanGroup);
	UART_Printf(UART_CHANNEL, "%d,", MTEDS.MTChecksum);
	UART_Printf(UART_CHANNEL, "\r\n");
}
