#include "system.h"
#ifndef _TIMING_H_
#error "timing.h must be included in system.h"
#endif
#include <stdint.h>

volatile tint_t time, rollover_time;

/*************************************
 * HAL Function Declarations
 *************************************/
void hal_timing_Init(void);

#define TimingISR() time++

/* Including the hal_timing.c file here allows the ISR defined in that module
 * to have access to the time variable without extern-ing it.  It allows the ISR
 * to not have to make a function call. */
#include "hal_timing.c"

void Timing_Init(void) {
    // use flag so module only gets initialized once
    static uint8_t init_flag = 0;
    if(init_flag) return;
    time = 0;
    rollover_time = TIME_MAX;
    hal_Timing_Init();
    init_flag = 1;
}

uint32_t TimeNow(void) {
    return time;
}

uint32_t TimeSince(tint_t t) {
    if (time >= t) {
        return (time - t);
    } else {
        // The time variable has rolled over
        return (time + (1 + (rollover_time - t)));
    }
}

void DelayMs(tint_t delay) {
    uint32_t temp;

    temp = TimeNow();
    while (TimeSince(temp) <= delay) {
        Nop();
    }
}

void Timing_Roll(void) {
    rollover_time = time;
    time = 0;
}
