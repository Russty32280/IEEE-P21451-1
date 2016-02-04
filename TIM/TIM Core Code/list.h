/**
 * @defgroup list List Module
 * @ingroup data_strucutre
 * 
 * @todo fill in the main comment block
 * @{
 */

#ifndef _LIST_H_
#define _LIST_H_

#include <stdint.h>

/**
 * @todo Victor C. Document this typedef (when done change this line to "@todo MM check <your names> documentation"
 */
typedef uint8_t(*sort_fn_t)(void*, void*);

/**
 * @todo Josh Hass Document this typedef (when done change this line to "@todo MM check <your names> documentation"
 */
typedef uint8_t(*identify_fn_t)(void*, void*);

/**
 * @todo Matthew D. Document this struct (when done change this line to "@todo MM check <your names> documentation"
 */
typedef struct list_link_t {
    void* item_ptr; ///< item_ptr
    struct list_link_t* next; ///< next
    struct list_link_t* previous; ///< previous
} list_link_t;

/**
 * @todo Jacob H. Document this struct (when done change this line to "@todo MM check <your names> documentation"
 */
typedef struct list_t {
    list_link_t* first; ///< first
    list_link_t* last; ///< last
    uint16_t length; ///< length
    uint16_t array_length; ///< array_length
    list_link_t* links; ///< links
    uint16_t* item_array; ///< item_array
    uint16_t item_size; ///< item_size
    sort_fn_t sort_fn; ///< sort_fn
    identify_fn_t identify_fn; ///< identify_fn
    // the following overhead members are only needed
    // to make the list module faster
    list_link_t * working[2]; ///< working
    list_link_t * unlinked[2]; ///< unlinked
    list_link_t * unused[2]; ///< unused
} list_t;

/**
 *
 * @param list
 * @param item_size
 * @param item_array
 * @param item_array_length
 * @param link_array
 *
 * @todo Austin H. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void List_Init(list_t* list, uint16_t item_size, void* item_array, uint16_t item_array_length, list_link_t* link_array);

/**
 *
 * @param list
 * @param sort_fn
 *
 * @todo Lee H. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_SetSortFunction(list_t* list, uint8_t(*sort_fn)(void* a, void* b));

/**
 *
 * @param list
 * @param identify_fn
 *
 * @todo Eric J. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_SetIdentifyFunction(list_t* list, uint8_t(*identify_fn)(void* identifier, void* item));

/**
 *
 * @param list
 * @param item
 * @return
 *
 * @todo Josh K. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void* List_AddAndLink(list_t* list, void* item);

/**
 *
 * @param list
 * @param item
 * @return
 *
 * @todo Joseph L. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void* List_Add(list_t* list, void* item);

/** @brief List_AddIndirect is used to obtain a valid position for which an item can be saved to.
 *
 * List_AddIndirect gets an unused link using GetUnusedLink. If unused link is available, function will update pointers
 * to unlinked items and update working links. If no unused links are available, return a null pointer
 *
 * @param list - Pointer to list that an item needs to be added to
 * @return Returns a null pointer if there is no room in list.
 * Otherwise returns item_ptr in the first unused link
 *
 */
void* List_AddIndirect(list_t* list);

/**
 *
 * @param list
 *
 * @todo James R. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void List_Link(list_t* list);

/**
 *
 * @param list
 *
 * @todo Andrew R. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void List_ResortFirst(list_t* list);

/**
 *
 * @param list
 *
 * @todo Chris R. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void List_ResortLast(list_t* list);

/**
 *
 * @param list
 * @param item
 *
 * @todo Jon W. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
// not interrupt safe
void List_LinkItem(list_t* list, void* item);

/**
 *
 * @param list
 * @return
 *
 * @todo Josh W. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void* List_GetFirst(list_t* list);

/**
 *
 * @param list
 * @return
 *
 * @todo TJ G. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void* List_GetLast(list_t* list);

/**
 *
 * @param list
 * @param item
 * @return
 *
 * @todo TJ G. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void* List_GetNext(list_t* list, void* item);

/**
 *
 * @param list
 * @param identifier
 * @return
 *
 * @todo George L. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void* List_GetItem(list_t* list, void* identifier);

/**
 *
 * @param list
 *
 * @todo George L. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_RemoveFirst(list_t* list);

/**
 *
 * @param list
 *
 * @todo Matthew M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_RemoveLast(list_t* list);

/**
 *
 * @param list
 * @param item
 *
 * @todo Matthew M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_Remove(list_t* list, void* item);

/**
 *
 * @param list
 *
 * @todo Anthony M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_RemoveAll(list_t* list);

/**
 *
 * @param list
 * @param item
 *
 * @todo Anthony M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_UnlinkItem(list_t* list, void* item);

/**
 *
 * @param list
 *
 * @todo Tom M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_UnlinkFirst(list_t* list);

/**
 *
 * @param list
 *
 * @todo Tom M. Document this function (when done change this line to "@todo MM check <your names> documentation"
 */
void List_UnlinkLast(list_t* list);

/// @}

#endif //_LIST_H_
