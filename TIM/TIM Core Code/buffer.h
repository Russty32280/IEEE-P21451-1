//x comments which begin with //x are for beginner student information only
//x these comments would normally not be required

//x in every .h file it is recommended to use the following pattern:
//x 1. at the top check if a special flag is set (recommended _FILENAME_H_)
//x 2. if not define the flag
//x 3. put a matching endif at the end of the file
//x this will avoid many errors and issues if you ever include a .h file twice
//x since the second time it is included the flag _FILENAME_H_ will be defined
//x thus the contents of the file will be ignored
#ifndef _BUFFER_H_
#define _BUFFER_H_

//x include any standard headers which will be required by the module here
#include <stdint.h>
#include <stdbool.h>
//x include headers for dependent modules or any other headers required here

//x the following is a doxygen comment block. Read doxygen documentation for more
//x details
/** @file
 * @defgroup buffer FIFO Byte Buffer
 * @ingroup data_strucutre
 * 
 * This module implements a software FIFO buffer of bytes. It provides 
 * methods Push() and Pop() to add and remove bytes from the buffer.
 *
 * The user is responsible for allocating the structure used to manage the buffer,
 * buffer_t, as well as the actual byte array which will be used to implement the buffer.
 * These are then passed to BufferInit() which must be called prior to any attempts 
 * to Push or Pop.
 *
 * There is also a PushData() method which allows multiple bytes to be added to the buffer
 * at once.
 *
 * An alternative to this FIFO byte buffer is the Item Buffer module which works the same
 * except with items of any size instead of being limited to bytes only.
 *
 * @author Michael Muhlbaier
 * @author Anthony Merlino
 *
 * @version 0.1 Initial implementation
 * @version 1.0 Made Push and Pop interrupt safe
 * @version 1.1 Added PushData
 * @version 1.2 Added and corrected documentation, removed include "system.h"
 * @{
 */


/** data structure to hold the required information for each buffer
*/
typedef struct {
	uint16_t size; /**< size is the number of items in the buffer >*/
    uint16_t max_size; /**< max_size is the length of the buffer array provided by the user >*/
	char *front; /**< pointer to first item in buffer >*/
	char *rear; /**< pointer to next open position in the buffer >*/
	char *buffer_start; /**< buffer start location in memory >*/
	char *buffer_end; /**< buffer end location in memory (buffer_start + max_size) >*/
	void (*Callback)(void * buf); /**< Push callback, useful if buffer is used
		for communications, does not need to be used/set, initializes to 0>*/
	//x the input to the Callback should be a buffer_t pointer; however, buffer_t
	//x has not been defined thus the pointer is cast as a void pointer.
} buffer_t;

/** Push will add one item, data, to the FIFO buffer
 * 
 * Push will add one item to the rear of the data buffer then increment (and
 * wrap is needed) the rear. If the buffer is full it will overwrite the data
 * at the front of the buffer and increment the front.
 * 
 * BufferInit() must be used to initialize the buffer prior to calling Push and
 * passing it a pointer to the buffer.
 * 
 * @param buffer Pointer to the buffer_t data structure holding the buffer info
 * @param data char data to be added to the rear of the FIFO buffer
 * 
 * @warning Push is only interrupt safe if EnableInterrupts() and DisableInterrupts()
 * are defined by hal_general.h
 */
void Push(buffer_t *buffer, char data);

/** Pop will return one item from the front of the FIFO buffer
 * 
 * Pop will return the item at the front of the FIFO buffer then increment (and
 * wrap as needed) the front. If the buffer is empty it will return 0.
 * 
 * BufferInit() must be used to initialize the buffer prior to calling Pop and
 * passing it a pointer to the buffer.
 * 
 * @param buffer Pointer to the buffer_t data structure holding the buffer info
 * @return Data of type char from the front of the buffer
 * 
 * @warning is only interrupt safe if EnableInterrupts() and DisableInterrupts()
 * are defined by hal_general.h
 */
char Pop(buffer_t *buffer);

/** GetSize returns the number of items in the FIFO buffer
 * 
 * BufferInit() should be used to initialize the buffer otherwise the return
 * value will be meaningless
 * 
 * @param buffer Pointer to the buffer_t data structure holding the buffer info
 * @return Number of items in the buffer
 */
uint16_t GetSize(buffer_t *buffer);

/** Initialize a FIFO buffer
 * 
 * Example code:
 * @code
 * #define TX_BUFFER_LENGTH 512
 * buffer_t tx; // transmit buffer
 * char tx_buffer_array[TX_BUFFER_LENGTH]
 * ...
 * BufferInit(&tx, &tx_buffer_array[0], TX_BUFFER_LENGTH);
 * @endcode
 * 
 * @param buffer Pointer to the buffer_t data structure to be initialized
 * @param data_array Array of char data to implement the actual buffer
 * @param max_size Maximum size of the buffer (should be the same length as the
 * array)
 */
void BufferInit(buffer_t *buffer, char *data_array, uint16_t max_size);

/** Set Callback function for buffer to be called after items are Push'd to the buffer
 *
 * The callback function will be called after anything is Push'd to
 * the buffer. The function will be called with a pointer to the buffer which had an item pushed
 * onto it.
 *
 * Example:
 * @code
 * void TxCallback(buffer_t * buf);
 * #define TX_BUFFER_LENGTH 512
 * buffer_t tx; // transmit buffer
 * char tx_buffer_array[TX_BUFFER_LENGTH]
 * ...
 * BufferInit(&tx, &tx_buffer_array[0], TX_BUFFER_LENGTH);
 * BufferSetCallback(&tx, TxCallback);
 * ...
 * void TxCallback(buffer_t * buf) {
 * 		SET_UART_TX_IE();
 * }
 * @endcode
 * This example is useful for a uC which has a hardware Tx interrupt flag which is set
 * whenever there is room in the hardware Tx FIFO buffer. When done transmitting the
 * interrupt must be disabled to avoid getting stuck in the ISR. When data needs to be
 * sent the interrupt must be enabled again, thus the need for the callback.
 *
 * Another usage could be to handle received data on a receive buffer.
 *
 * @warning many applications may use the Push method in a ISR which means the Callback
 * would be called from a ISR. Thus care should be taken to ensure callbacks are both
 * fast and interrupt safe
 *
 * @param buffer Pointer to the buffer_t data structure whose callback function is to be set
 * @param Callback Function pointer to a callback function with no return value  and a
 * 	buffer_t pointer input.
 */
void BufferSetCallback(buffer_t * buffer, void (*Callback)(buffer_t * buffer));

/** Clear/remove the callback function for 'buffer'
 *
 * @param buffer Pointer to the buffer_t data structure whose callback function is to be cleared
 */
void BufferClearCallback(buffer_t * buffer);

/** Push a array of data to the buffer
 *
 * @warning PushData will disable interrupts while writing to the buffer. If
 * length is long this could interfere with time sensitive ISRs. Consider using
 * Push() if this is an issue.
 *
 * PushData will add an array of items to the rear of the data buffer and increment
 * (and wrap if needed) the rear. If the buffer does not have room none of the data
 * will be pushed to the buffer.
 *
 * BufferInit() must be used to initialize the buffer prior to calling PushData and
 * passing it a pointer to the buffer.
 *
 * @param buffer Pointer to the buffer_t data structure holding the buffer info
 * @param data char pointer to data array to be added to the rear of the FIFO buffer
 * @param length the number of items in the data array
 * @return 0 if succeeded, 1 if no room in buffer
 */
char PushData(buffer_t * buffer, char * data, uint16_t length);

#define BUFFER_PUSH_FAILED 1 ///< push failed (return value of PushData() )
#define BUFFER_PUSH_SUCCEEDED 0 ///< push succeeded (return value of PushData() )

//x this is a special doxygen command to end a grouping of doxygen comment blocks
/** @} */

//x when a #endif compiler directive is not immediately after the matching #if...
//x then it is recommended to add a comment to indicate which #if it pairs with
#endif // _BUFFER_H_
//x some compilers will produce warnings if there is no blank newline at the end of a file
