/**
 * @defgroup uart UART Module
 * @file uart.h
 *
 *  Created on: Mar 12, 2014
 *      Author: Michael Muhlbaier
 *  Updated on: Feb 7, 2015
 *      Author: Anthony Merlino
 * @{
 */

#ifndef _UART_H_
#define _UART_H_

#include <stdint.h>
#include <stdbool.h>
#include "charReceiverList.h"

/** Initialize UART module
 *
 * Example usage:
 * @code
 * UART_Init(UART0_CHANNEL);
 * @endcode
 *
 * @param channel - The channel of UART to be used.  Macros for these should be defined in the 
 * HAL of the specific device.  
 */
void UART_Init(uint8_t channel);

void UART_WriteByte(uint8_t channel, char c);
void UART_Write(uint8_t channel, char * data, uint16_t length);
void UART_Printf(uint8_t channel, char * str,...);
void UART_vprintf(uint8_t channel, char * str, va_list vars);
uint8_t UART_IsTransmitting(uint8_t channel);

void UART_Tick(void);
void UART_RegisterReceiver(uint8_t channel, charReceiver_t fn);
void UART_UnregisterReceiver(uint8_t channel, charReceiver_t fn);

/** @}*/
#endif /* _UART_H_ */
