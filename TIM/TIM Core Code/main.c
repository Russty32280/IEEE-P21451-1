#include <msp430.h> 

#include "library.h"
#include "system.h"

#define UART_CHANNEL 1

int32_t main(void){
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer

    Timing_Init();
    Task_Init();
    TIM_Init();
//    Task_Schedule(TIM_Init,0,0,0);
//    TIM_Init();
//  Flash_Init();
//    Task_Schedule(hello_world, 0, 1000, 1000);


    EnableInterrupts();
    while(1) SystemTick();
}
