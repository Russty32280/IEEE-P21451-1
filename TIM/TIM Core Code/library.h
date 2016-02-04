
#ifndef _LIBRARY_H_
#define _LIBRARY_H_

/** @mainpage Embedded Library
 *
 * @section getting_started Getting Started With Using the Library
 * To use this library:
 * - add the desired modules (.c files) to your project and include the
 * corresponding header files (.h files) in system.h (you must create system.h).
 * - add the \ include directory to the compilers include directories
 * - add the \ hal \ hal_includes directory to the compilers include directories
 * - add the \ hal \ processor_family \ processor_number directory to the
 * compilers include directories
 * - enjoy
 *
 * For example to make a simple project which says "Hello World" every 10
 * seconds you would add the following c files to your project:
 * - buffer.c (used by the UART module)
 * - buffer_printf.c (optional - used by the UART module if you use UART_printf)
 * - charReceiverList.c (used by the UART module)
 * - hal_uart.c (found in the hal \ processor_family \ processor_number folder
 * - list.c (used by the task management module)
 * - task.c
 * - timing.c (used by the task management module)
 * - uart.c
 *
 * Your system.h may look something like the following:
 * @code
#ifndef _SYSTEM_H_
#define _SYSTEM_H_

// include the library header
#include "library.h"
// include list of modules used
#include "task.h"
#include "timing.h"
#include "list.h"
#include "buffer.h"
#include "buffer_printf.h"
#include "charReceiverList.h"
#include "itemBuffer.h"
#include "uart.h"

//hint: the MSP430F5529 uses UART1 for the builtin MSP Application UART1 virtual COM port
#define USE_UART2

// hint: the default clock for the MSP430F5529 is 1048576
// the default clock for the PIC32MX is set by configuration bits
#define FCPU     8000000L
// if peripheral clock is slower than main clock change it here
#define PERIPHERAL_CLOCK FCPU

#endif // _SYSTEM_H_
@endcode
 *
 * The main for this project may look something like this:
@code
#include "library.h"
#include "system.h"
// define which uart channel to use
#define UART_CHANNEL 2
void hello_world(void) {
    UART_Printf(UART_CHANNEL, "Hello World\r\n");
}
int32_t main(void)
{
    // do any device specific configuration here
    // SYSTEMConfig(FCPU, SYS_CFG_ALL); // config clock for PIC32
	// WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer for MSP430

    Timing_Init(); // initialize the timing module first
    Task_Init(); // initialize task management module next
    UART_Init(UART_CHANNEL);
	// enable interrupts after modules using interrupts have been initialized
	EnableInterrupts();
    Task_Schedule(hello_world, 0, 10000, 10000);
    while(1) SystemTick();
}
@endcode
 *
 */
#include "hal_general.h"

#endif // _LIBRARY_H_
