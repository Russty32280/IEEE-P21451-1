/*
 * TIM_Template.c
 *
 *  Created on: Dec 23, 2015
 *      Author: Russty32280
 */


#include <stdint.h>
#include <string.h>
#include <strings.h>
#include "macros.h"
#include "system.h"
#include "library.h"
#include "random_int.h"

#define UART_CHANNEL 1



char receive_buffer[RECEIVE_MAX_LENGTH];


static void UARTCharReceive(char c);
static void ParseMSG(char * Message);
static void FunctionSelect(char * FunctionID, char * ChannelID);


void TIM_Init(void){
    UART_Init(UART_CHANNEL);
	UART_RegisterReceiver(1, UARTCharReceive);
	MetaTEDSInit(); // This function is located in TIM.h

}



void UARTCharReceive(char c) {
	static int length;
	static int i = 0;
	static int j = 0;
	static int write_status = 0;

	//Only if we recieve a $ we will consider the communcation to start.

	if (c =='$'){
		length = 0;
		while (i<=RECEIVE_MAX_LENGTH){
			receive_buffer[i] = 0;
			i++;
		}
		write_status = 1;
	}

	//If we recieve a carriage return, then we take the message and pass it to the parsing function
	else if (c == '\r'){
		receive_buffer[length+1] = '\r';
		ParseMSG(receive_buffer);
		for (j=0; j<=RECEIVE_MAX_LENGTH; j++){
			receive_buffer[j]=0;
		}
		write_status = 0;
	}

	//So long as we have recieved a start character, we take in each character and append it to our message.
	else{
		if (write_status == 1){
			receive_buffer[length] = c;
			length++;
		}
	}
}


void ParseMSG(char * Message){
	volatile int I = 0;
	volatile int J = 0;
	static char PlaceHolder[3];
	static char PlaceHolder2[3];
	static char FuncID[3];
	//Only ever expected to have 255 functionIDs.
	static char ChanID[3];
	static int CommaOffset;
	//We need to commonize the way the function and channel ids are passed into other functions.
	for (I=0; I<=3; I++){
		if (Message[I] == ','){
			if (I==1){
				FuncID[0] = '0';
				FuncID[1] = '0';
				FuncID[2] = PlaceHolder[0];
				CommaOffset = 1;
			}
			else if (I==2){
				FuncID[0] = '0';
				FuncID[1] = PlaceHolder[0];
				FuncID[2] = PlaceHolder[1];
				CommaOffset = 2;
			}
			else if (I==3){
				FuncID[0] = PlaceHolder[0];
				FuncID[1] = PlaceHolder[1];
				FuncID[2] = PlaceHolder[2];
				CommaOffset = 3;
			}
		}
		else{
			PlaceHolder[I] = Message[I];
		}
	}

	for (J=0; J<=4; J++){
		UART_Printf(UART_CHANNEL, "%c", Message[CommaOffset + 1 + J]);
		if (Message[CommaOffset+1+J] == '\r'){
			if (J==2){
				ChanID[0] = '0';
				ChanID[1] = '0';
				ChanID[2] = PlaceHolder2[0];
			}
			else if (J==3){
				ChanID[0] = '0';
				ChanID[1] = PlaceHolder2[0];
				ChanID[2] = PlaceHolder2[1];
			}
			else if (J==4){
				ChanID[0] = PlaceHolder2[0];
				ChanID[1] = PlaceHolder2[1];
				ChanID[2] = PlaceHolder2[2];
			}
		}
		else{
			PlaceHolder2[J] = Message[CommaOffset + 1 + J];
		}
	}
	UART_Printf(UART_CHANNEL, "Function ID:");
	UART_Printf(UART_CHANNEL, FuncID);
	UART_Printf(UART_CHANNEL, "\r\n Channel ID:");
	UART_Printf(UART_CHANNEL, ChanID);
	FunctionSelect(FuncID, ChanID);
}


/*
 * All of these functions need to be defined in the TIM.c file for the specific TIM.
 */


void FunctionSelect(char * FunctionID, char * ChannelID){
	int IsGlobal;
	IsGlobal = strcmp(ChannelID, "000");
	UART_Printf(UART_CHANNEL, "IsGlobal: %d\r\n", IsGlobal);

	if(strcmp(FunctionID, "000") == 0){
		if(IsGlobal == 0){
			UART_Printf(UART_CHANNEL, "Writing Global Transducer\r\n");
		}
		else{
			UART_Printf(UART_CHANNEL, "Writing Transducer Channel: %s\r\n", ChannelID);
			WriteChannelTransducerData(ChannelID, random_int(0,100));
		}
	}

	if(strcmp(FunctionID, "128") == 0){
		if(IsGlobal == 0){
			UART_Printf(UART_CHANNEL, "Reading Global Transducer\r\n");
		}
		else{
			UART_Printf(UART_CHANNEL, "Reading Transducer Channel: %s\r\n", ChannelID);
			UART_Printf(UART_CHANNEL, "Data From Transducer %s : %d", ChannelID, ReadChannelTransducerData(ChannelID));
		}
	}

	if(strcmp(FunctionID, "160") == 0){
		if(IsGlobal == 0){
			//ReadMETA-Teds
			UART_Printf(UART_CHANNEL, "Going to read Meta-TEDS\r\n");
			ReadMetaTEDS();
		}
		else{
			UART_Printf(UART_CHANNEL, "Reading Channel TEDS for Channel %s\r\n", ChannelID);
		}
	}
	else if(strcmp(FunctionID, "161") == 0){
		if(IsGlobal == 0){
			UART_Printf(UART_CHANNEL, "Reading Meta-Identification TEDS\r\n");
		}
		else{
			UART_Printf(UART_CHANNEL, "Reading Channel Identification TEDS for Channel %s\r\n", ChannelID);
		}
	}
}
