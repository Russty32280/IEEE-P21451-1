/** @file
 * @defgroup receiverlist Receiver List
 * @ingroup data_strucutre
 *
 * The @c char Receiver List module provides a simple way of keeping
 * a list of character receivers and processing a single character
 * through the receivers.
 *
 * This module was developed as a helper to the @ref uart UART Module
 * but it has use in any situation where multiple moldules may want
 * to process characters which are received.
 *
 * @author Anthony Merlino
 * @author Michael Muhlbaier
 *
 * @{
 */

#ifndef _CHAR_RECEIVER_LIST_H_
#define _CHAR_RECEIVER_LIST_H_

#include <stdint.h>
#include <stdbool.h>

/**
 * @todo Alex A. Document this datatype (when done change this line to "@todo MM check <your names> documentation"
 */
typedef void(*charReceiver_t)(char);

/**
 * @todo Atharva A. Document this structure (when done change this line to "@todo MM check <your names> documentation"
 */
typedef struct charReceiverList_t{
	uint16_t max_size; ///< max_size
	uint16_t size; ///< size
	charReceiver_t *receivers; ///< receivers
} charReceiverList_t;

/**
 *
 * @param rList
 * @param receiver_array
 * @param max_size
 *
 * @todo Dan B. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void CharReceiverList_Init(charReceiverList_t* rList, charReceiver_t* receiver_array, uint16_t max_size);

/**
 * 
 * @param rList
 * @param receiver
 * 
 * @todo Kate C. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void CharReceiverList_Add(charReceiverList_t* rList, charReceiver_t receiver);

/**
 *
 * @param rList
 * @param receiver
 *
 * @todo Matthew D. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void CharReceiverList_Remove(charReceiverList_t* rList, charReceiver_t receiver);

/**
 * 
 * @param rList
 * @param c
 * 
 * @todo Victor C. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void CharReceiverList_Run(charReceiverList_t* rList, char c);

/** @} */
#endif // _CHAR_RECEIVER_LIST_H_
