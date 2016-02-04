/*! \file TIM1.h
	\brief User/Manufacturer defined file tuned specifically for the Transducer used.

	\details A user who wishes to utilize the TIM Architecture laai out in the TIM_CORE files
	must have this file located inside the compilers file system upon building. This file
	has the templates for each of the core functions as laid out by the  IEEE P24151-2 standard.
	By utilizing this approach to implementation, the end-user only has to modify small amount of code,
	whilst leaving the core functionality alone. All function names as laid out in this file MUST
	remain the same, as these functions are called by the TIM_CORE.

	\author Russell Trafford
	\date 12/15/2015

 */


#ifndef TIM1_H_
#define TIM1_H_

/*! \fn void MetaTEDSInit(void)
	\brief Initializes the MetaTEDS in RAM for use by the NCAP.

	\warning All current values are arbitrary! Please refer to P21451-2 for proper value ranges.
	\todo Implement Flash Memory read/write so that changes are saved between power cycles.
 */

/*! \fn int ReadChannelTransducerData(char * ChannelID)
	\brief Reads the data from a specific channel.
	\param ChannelID The channel number in the form of "XXX", where X is a char from 0-9. ad XXX ranges from "000" - "255"
	\warning Current implementation only produces a random number when asked for data.
	\todo  Implement a proper sensor and produce readings for it.

 */

/*! \fn void WriteChannelTransducerData(char * ChannelID, int WriteData)
	\brief Writes data to a specific channel.
	\param ChannelID The channel number in the form "XXX", where X is a char from 0-9 and XXX ranges from "000"- "255"
	\param WriteData Data to be written to the specific transducer.

	\warning Currently not implemented in TIM_CORE.
	\todo Find in the standard how WriteData needs to be formatted (if at all).
 */

/*! \fn void ReadMetaTEDS(void)
	\brief Returns the content of the current verson of the MetaTEDS in RAM

	Currently this function is implemented using UART_Printf.
	\todo Find a more efficient way of returning the MetaTEDS back to the NCAP.
 */


void MetaTEDSInit(void);
int ReadChannelTransducerData(char * ChannelID);
void WriteChannelTransducerData(char * ChannelID, int WriteData);
void ReadMetaTEDS(void);

#endif /* TIM1_H_ */
