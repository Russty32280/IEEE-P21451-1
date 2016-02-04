#include <msp430.h>
#include <stdint.h>
#include "hal_uart.h"
#include "system.h"

#define UART0 0
#define UART1 1

void hal_UART_Init(uint8_t channel, uint32_t baud){
	
	switch(channel){
		case UART0:
			P3SEL |= BIT3 + BIT4;
			hal_UART_Disable(channel);
			UCA0CTL1 = UCSSEL_2;
			UCA0BR0 = FCPU / baud;
			UCA0BR1 = FCPU / baud / 256;
			UCA0MCTL = ((FCPU*8) / baud - (FCPU / baud) * 8) << 1;
			hal_UART_Enable(channel);
			break;
		case UART1:
			P4SEL |= BIT4 + BIT5;
			hal_UART_Disable(channel);
			UCA1CTL1 = UCSSEL_2;
			UCA1BR0 = FCPU / baud;
			UCA1BR1 = FCPU / baud / 256;
			UCA1MCTL = ((FCPU*8) / baud - (FCPU / baud) * 8) << 1;
			hal_UART_Enable(channel);
			break;
	}
	hal_UART_EnableTxInterrupt(channel);
	hal_UART_EnableRxInterrupt(channel);
}

void hal_UART_Enable(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0CTL1 &= ~(UCSWRST);
			break;
		case UART1:
			UCA1CTL1 &= ~(UCSWRST);
			break;
		default:
			return;
	}
}

void hal_UART_Disable(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0CTL1 |= UCSWRST;
			break;
		case UART1:
			UCA1CTL1 |= UCSWRST;
			break;
		default:
			return;
	}
}

void hal_UART_EnableRxInterrupt(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IE |= UCRXIE;
			break;
		case UART1:
			UCA1IE |= UCRXIE;
			break;
		default:
			return;
	}
}

void hal_UART_EnableTxInterrupt(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IE |= UCTXIE;
			break;
		case UART1:
			UCA1IE |= UCTXIE;
			break;
		default:
			return;
	}
}

void hal_UART_DisableRxInterrupt(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IE &= ~UCRXIE;
			break;
		case UART1:
			UCA1IE &= ~UCRXIE;
			break;
		default:
			return;
	}
}

void hal_UART_DisableTxInterrupt(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IE &= ~UCTXIE;
			break;
		case UART1:
			UCA1IE &= ~UCTXIE;
			break;
		default:
			return;
	}
}

void hal_UART_TxChar(uint8_t channel, char c){
	switch(channel){
		case UART0:
			UCA0TXBUF = c;
			break;
		case UART1:
			UCA1TXBUF = c;
			break;
		default:
			return;
	}
}

char hal_UART_RxChar(uint8_t channel){
	switch(channel){
		case UART0:
			return UCA0RXBUF;
		case UART1:
			return UCA1RXBUF;
		default:
			return 0;
	}
}

void hal_UART_ClearTxIF(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IFG &= ~UCTXIFG;
			break;
		case UART1:
			UCA1IFG &= ~UCTXIFG;
			break;
		default:
			return;
	}
}

void hal_UART_ClearRxIF(uint8_t channel){
	switch(channel){
		case UART0:
			UCA0IFG &= ~UCRXIFG;
			break;
		case UART1:
			UCA1IFG &= ~UCRXIFG;
			break;
		default:
			return;
	}
}

uint8_t hal_UART_DataAvailable(uint8_t channel){
	switch(channel){
		case UART0:
			return (UCA0IFG & UCRXIFG);
		case UART1:
			return (UCA1IFG & UCRXIFG);
		default:
			return 0;
	}
}

uint8_t hal_UART_SpaceAvailable(uint8_t channel){
	switch(channel){
		case UART0:
			return (UCA0IFG & UCTXIFG);
		case UART1:
			return (UCA1IFG & UCTXIFG);
		default:
			return 0;
	}
}

#pragma vector=USCI_A0_VECTOR
__interrupt void _UART0_ISR(void){
	UART_Rx_Handler(UART0);
	hal_UART_ClearRxIF(UART0);
	UART_Tx_Handler(UART0);
}

#pragma vector=USCI_A1_VECTOR
__interrupt void _UART1_ISR(void){
	UART_Rx_Handler(UART1);
	hal_UART_ClearRxIF(UART1);
	UART_Tx_Handler(UART1);
}
