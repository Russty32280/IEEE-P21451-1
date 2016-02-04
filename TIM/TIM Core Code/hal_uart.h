
 /**
 * @defgroup hal_uart HAL UART Module
 * @ingroup uart
 * @file hal_uart.h
 *
 *  Created on: Feb 8, 2015
 *      Author: Anthony Merlino
 * @todo Anthony Merlino document this
 * @{
 */

#ifndef _HAL_UART_H_
#define _HAL_UART_H_

void UART_Tx_Handler(uint8_t channel);
void UART_Rx_Handler(uint8_t channel);

void hal_UART_Init(uint8_t channel, uint32_t baud);

void hal_UART_Enable(uint8_t channel);
void hal_UART_Disable(uint8_t channel);

uint8_t hal_UART_SpaceAvailable(uint8_t channel);
uint8_t hal_UART_DataAvailable(uint8_t channel);

void hal_UART_ClearRxIF(uint8_t channel);
void hal_UART_ClearTxIF(uint8_t channel);
void hal_UART_EnableRxInterrupt(uint8_t channel);
void hal_UART_EnableTxInterrupt(uint8_t channel);
void hal_UART_DisableRxInterrupt(uint8_t channel);
void hal_UART_DisableTxInterrupt(uint8_t channel);

char hal_UART_RxChar(uint8_t channel);
void hal_UART_TxChar(uint8_t channel, char c);
 
/** @}*/
#endif /* _HAL_UART_H_ */
