/*
 * uart.c
 *
 *  Created on: Mar 12, 2014
 *      Author: Michael Muhlbaier
 *  Updated on: Feb 7, 2015
 *      Author: Anthony Merlino
 */

#include "system.h"
#ifndef _UART_H_
#error "uart.h must be included in system.h"
#endif
#ifndef _BUFFER_PRINTF_H_
#warning "To use UART_printf(): include buffer_printf.h in system.h and buffer_printf.c must be in your project"
#endif
#ifndef _BUFFER_H_
#error "include buffer.h in system.h and buffer.c must be in your project"
#endif


void UART_Tx_Start(uint8_t channel);

/**************************************
 * Hardware Abstraction Layer Includes
 *************************************/
#include "hal_uart.h"

/**************************************
 * Default Macros
 *************************************/
#ifndef UART_BAUD
#define UART_BAUD 115200
#endif
#define NUM_RECEIVERS 2
#ifndef UART_TX_BUFFER_LENGTH
#define UART_TX_BUFFER_LENGTH 128
#endif
#ifndef UART_RX_BUFFER_LENGTH
#define UART_RX_BUFFER_LENGTH 32
#endif
#ifndef UART_MAX_CHARS_PER_CALL
#define UART_MAX_CHARS_PER_CALL 20
#endif

#ifdef USE_UART7
    #ifndef UART7_BAUD
        #define UART7_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART7_RECEIVERS
        #define NUM_UART7_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART7_RX_BUFFER_LENGTH
        #define UART7_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART7_TX_BUFFER_LENGTH
        #define UART7_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx7, tx7;
    char tx_buffer_array7[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array7[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList7;
    charReceiver_t receiver_array7[NUM_UART7_RECEIVERS];
#endif
#ifdef USE_UART6
    #ifndef UART6_BAUD
        #define UART6_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART6_RECEIVERS
        #define NUM_UART6_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART6_RX_BUFFER_LENGTH
        #define UART6_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART6_TX_BUFFER_LENGTH
        #define UART6_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx6, tx6;
    char tx_buffer_array6[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array6[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList6;
    charReceiver_t receiver_array6[NUM_UART6_RECEIVERS];
#endif
#ifdef USE_UART5
    #ifndef UART5_BAUD
        #define UART5_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART5_RECEIVERS
        #define NUM_UART5_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART5_RX_BUFFER_LENGTH
        #define UART5_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART5_TX_BUFFER_LENGTH
        #define UART5_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx5, tx5;
    char tx_buffer_array5[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array5[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList5;
    charReceiver_t receiver_array5[NUM_UART5_RECEIVERS];
#endif
#ifdef USE_UART4
    #ifndef UART4_BAUD
        #define UART4_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART4_RECEIVERS
        #define NUM_UART4_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART4_RX_BUFFER_LENGTH
        #define UART4_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART4_TX_BUFFER_LENGTH
        #define UART4_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx4, tx4;
    char tx_buffer_array4[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array4[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList4;
    charReceiver_t receiver_array4[NUM_UART4_RECEIVERS];
#endif
#ifdef USE_UART3
    #ifndef UART3_BAUD
        #define UART3_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART3_RECEIVERS
        #define NUM_UART3_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART3_RX_BUFFER_LENGTH
        #define UART3_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART3_TX_BUFFER_LENGTH
        #define UART3_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx3, tx3;
    char tx_buffer_array3[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array3[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList3;
    charReceiver_t receiver_array3[NUM_UART3_RECEIVERS];
#endif
#ifdef USE_UART2
    #ifndef UART2_BAUD
        #define UART2_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART2_RECEIVERS
        #define NUM_UART2_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART2_RX_BUFFER_LENGTH
        #define UART2_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART2_TX_BUFFER_LENGTH
        #define UART2_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx2, tx2;
    char tx_buffer_array2[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array2[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList2;
    charReceiver_t receiver_array2[NUM_UART2_RECEIVERS];
#endif
#ifdef USE_UART1
    #ifndef UART1_BAUD
        #define UART1_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART1_RECEIVERS
        #define NUM_UART1_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART1_RX_BUFFER_LENGTH
        #define UART1_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART1_TX_BUFFER_LENGTH
        #define UART1_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx1, tx1;
    char tx_buffer_array1[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array1[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList1;
    charReceiver_t receiver_array1[NUM_UART1_RECEIVERS];
#endif
#ifdef USE_UART0
    #ifndef UART0_BAUD
        #define UART0_BAUD UART_BAUD
    #endif
    #ifndef NUM_UART0_RECEIVERS
        #define NUM_UART0_RECEIVERS NUM_RECEIVERS
    #endif
    #ifndef UART0_RX_BUFFER_LENGTH
        #define UART0_RX_BUFFER_LENGTH UART_RX_BUFFER_LENGTH
    #endif
    #ifndef UART0_TX_BUFFER_LENGTH
        #define UART0_TX_BUFFER_LENGTH UART_TX_BUFFER_LENGTH
    #endif
    buffer_t rx0, tx0;
    char tx_buffer_array0[UART_TX_BUFFER_LENGTH];
    char rx_buffer_array0[UART_RX_BUFFER_LENGTH];
    charReceiverList_t receiverList0;
    charReceiver_t receiver_array0[NUM_UART0_RECEIVERS];
#endif

#ifdef USE_UART7
    #define NUM_UARTS 8
#elif defined USE_UART6
    #define NUM_UARTS 7
#elif defined USE_UART5
    #define NUM_UARTS 6
#elif defined USE_UART4
    #define NUM_UARTS 5
#elif defined USE_UART3
    #define NUM_UARTS 4
#elif defined USE_UART2
    #define NUM_UARTS 3
#elif defined USE_UART1
    #define NUM_UARTS 2
#elif defined USE_UART0
    #define NUM_UARTS 1
#else
#error No UARTS used, remove this file from project
#endif

struct {
    buffer_t * rx;
    buffer_t * tx;
    charReceiverList_t * receiverList;
} uart[NUM_UARTS];

uint8_t rx_flags;

void UART_Init(uint8_t channel) {
    // use flag so init calls to Timing_Init and Task_Init get called only once
    static uint8_t init_flag = 0;

    rx_flags = 0;

    switch(channel){
#ifdef USE_UART0
        case 0:
            hal_UART_Init(channel, UART0_BAUD);
            BufferInit(&rx0, &rx_buffer_array0[0], UART0_RX_BUFFER_LENGTH);
            BufferInit(&tx0, &tx_buffer_array0[0], UART0_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList0, &receiver_array0[0], NUM_UART0_RECEIVERS);
            uart[0].rx = &rx0;
            uart[0].tx = &tx0;
            uart[0].receiverList = &receiverList0;
            break;
#endif
#ifdef USE_UART1
        case 1:
            hal_UART_Init(channel, UART1_BAUD);
            BufferInit(&rx1, &rx_buffer_array1[0], UART1_RX_BUFFER_LENGTH);
            BufferInit(&tx1, &tx_buffer_array1[0], UART1_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList1, &receiver_array1[0], NUM_UART1_RECEIVERS);
            uart[1].rx = &rx1;
            uart[1].tx = &tx1;
            uart[1].receiverList = &receiverList1;
            break;
#endif
#ifdef USE_UART2
        case 2:
            hal_UART_Init(channel, UART2_BAUD);
            BufferInit(&rx2, &rx_buffer_array2[0], UART2_RX_BUFFER_LENGTH);
            BufferInit(&tx2, &tx_buffer_array2[0], UART2_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList2, &receiver_array2[0], NUM_UART2_RECEIVERS);
            uart[2].rx = &rx2;
            uart[2].tx = &tx2;
            uart[2].receiverList = &receiverList2;
            break;
#endif
#ifdef USE_UART3
        case 3:
            hal_UART_Init(channel, UART3_BAUD);
            BufferInit(&rx3, &rx_buffer_array3[0], UART3_RX_BUFFER_LENGTH);
            BufferInit(&tx3, &tx_buffer_array3[0], UART3_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList3, &receiver_array3[0], NUM_UART3_RECEIVERS);
            uart[3].rx = &rx3;
            uart[3].tx = &tx3;
            uart[3].receiverList = &receiverList3;
            break;
#endif
#ifdef USE_UART4
        case 4:
            hal_UART_Init(channel, UART4_BAUD);
            BufferInit(&rx4, &rx_buffer_array4[0], UART4_RX_BUFFER_LENGTH);
            BufferInit(&tx4, &tx_buffer_array4[0], UART4_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList4, &receiver_array4[0], NUM_UART4_RECEIVERS);
            uart[4].rx = &rx4;
            uart[4].tx = &tx4;
            uart[4].receiverList = &receiverList4;
            break;
#endif
#ifdef USE_UART5
        case 5:
            hal_UART_Init(channel, UART5_BAUD);
            BufferInit(&rx5, &rx_buffer_array5[0], UART5_RX_BUFFER_LENGTH);
            BufferInit(&tx5, &tx_buffer_array5[0], UART5_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList5, &receiver_array5[0], NUM_UART5_RECEIVERS);
            uart[5].rx = &rx5;
            uart[5].tx = &tx5;
            uart[5].receiverList = &receiverList5;
            break;
#endif
#ifdef USE_UART6
        case 6:
            hal_UART_Init(channel, UART6_BAUD);
            BufferInit(&rx6, &rx_buffer_array6[0], UART6_RX_BUFFER_LENGTH);
            BufferInit(&tx6, &tx_buffer_array6[0], UART6_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList6, &receiver_array6[0], NUM_UART6_RECEIVERS);
            uart[6].rx = &rx6;
            uart[6].tx = &tx6;
            uart[6].receiverList = &receiverList6;
            break;
#endif
#ifdef USE_UART7
        case 7:
            hal_UART_Init(channel, UART7_BAUD);
            BufferInit(&rx7, &rx_buffer_array7[0], UART7_RX_BUFFER_LENGTH);
            BufferInit(&tx7, &tx_buffer_array7[0], UART7_TX_BUFFER_LENGTH);
            CharReceiverList_Init(&receiverList7, &receiver_array7[0], NUM_UART7_RECEIVERS);
            uart[7].rx = &rx7;
            uart[7].tx = &tx7;
            uart[7].receiverList = &receiverList7;
            break;
#endif
    }

#ifdef _TASK_H_
    #ifndef UART_TICK_OVERRIDE
        // if the Task Management Module is being used then schedule
        // the UART_Tick to happen every ms
        if(init_flag == 0) {
            // make sure the task manager is initialized
            Task_Init();
            Task_Schedule(UART_Tick,0,1,1);
        }
    #endif
#endif
    init_flag = 1;
}

void UART_Tick(void){
    char c;
    volatile unsigned int i;
    volatile unsigned int b;

    if(rx_flags != 0){
        for(i = 0; i < NUM_UARTS; i++){
            if(rx_flags & (1 << i)){
                // clear the flag
                rx_flags &= ~(1 << i);
                b = GetSize(uart[i].rx);
                if(b > UART_MAX_CHARS_PER_CALL) b = UART_MAX_CHARS_PER_CALL;
                while(b--){
                    c = Pop(uart[i].rx);
                    CharReceiverList_Run(uart[i].receiverList, c);
                }
            }
        }
    }
}


void UART_Tx_Handler(uint8_t channel){
    while(hal_UART_SpaceAvailable(channel)) {
        if(GetSize(uart[channel].tx)){
            hal_UART_TxChar(channel, Pop(uart[channel].tx));
        } else {
            hal_UART_DisableTxInterrupt(channel);
            break;
        }
    }
}

void UART_Tx_Start(uint8_t channel){
    while(hal_UART_SpaceAvailable(channel)) {
        if(GetSize(uart[channel].tx)){
            hal_UART_TxChar(channel,Pop(uart[channel].tx));
        } else {
            return;
        }
    }
    hal_UART_EnableTxInterrupt(channel);
}

void UART_Rx_Handler(uint8_t channel) {
    while(hal_UART_DataAvailable(channel)) {
        Push(uart[channel].rx, hal_UART_RxChar(channel));
        rx_flags |= (1 << channel);
    }
}
 
void UART_WriteByte(uint8_t channel, char data) {
    if(channel >= NUM_UARTS) return;
    Push(uart[channel].tx, data);
    UART_Tx_Start(channel);
}

void UART_Write(uint8_t channel, char * data, uint16_t length) {
    if(channel >= NUM_UARTS) return;
    PushData(uart[channel].tx, data, length);
    UART_Tx_Start(channel);
}

void UART_Printf(uint8_t channel, char * str,...){
    // variable argument list type
    va_list vars;
    // initialize the variable argument list pointer by specifying the
    // input argument immediately preceding the variable list
    va_start(vars, str);
    // this module could be used without buffer_printf if this one function is
    // not used. Flag added to make it easy to not require buffer_printf
#ifdef _BUFFER_PRINTF_H_
    Push_vprintf(uart[channel].tx, str, vars);
#endif
    va_end(vars);
    UART_Tx_Start(channel);
}

void UART_vprintf(uint8_t channel, char * str, va_list vars) {
    if(channel >= NUM_UARTS) return;
    Push_vprintf(uart[channel].tx, str, vars);
    UART_Tx_Start(channel);
}

void UART_RegisterReceiver(uint8_t channel, charReceiver_t fn){
    if(channel >= NUM_UARTS) return;
    CharReceiverList_Add(uart[channel].receiverList, fn);
}

void UART_UnregisterReceiver(uint8_t channel, charReceiver_t fn){
    if(channel >= NUM_UARTS) return;
    CharReceiverList_Remove(uart[channel].receiverList, fn);
}

uint8_t UART_IsTransmitting(uint8_t channel) {
    if(channel >= NUM_UARTS) return 0;
    return GetSize(uart[channel].tx);
}
