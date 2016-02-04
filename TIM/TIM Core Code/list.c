#include "system.h"
#ifndef _LIST_H_
#error "list.h must be included in system.h"
#endif

#define NULL_LINK 0
#define UNUSED_LINK (list_link_t*)1
#define PENDING_LINK (list_link_t*)2
#define LINK_IN_USE (list_link_t*)3
// helper macro
#define IsLinkValid(link) (link > LINK_IN_USE)

#define ERROR_NO_ROOM_IN_LIST 1
#define ERROR_ITEM_NOT_FOUND 2
#define ERROR_INVALID_LINK 3

// helper functions
static list_link_t* GetUnusedLink(list_t* list);
static list_link_t* FindUnusedLink(list_t* list);
static void Link(list_t* list, list_link_t* link);
static void Unlink(list_t* list, list_link_t* link);
static list_link_t* FindLinkByItem(list_t* list, void* item);
#define UpdateWorkingLinks(list, link)    list->working[1] = list->working[0]; \
                                    list->working[0] = link;
#define List_Error(error)

void List_Init(list_t* list, uint16_t item_size, void* item_array,
        uint16_t item_array_length, list_link_t* link_array) {
    list->links = link_array;
    list->item_array = item_array;
    list->item_size = item_size;
    list->array_length = item_array_length;
    list->length = 0;
    list->first = NULL_LINK;
    list->last = NULL_LINK;
    list->sort_fn = 0;
    list->identify_fn = 0;
    list->working[0] = NULL_LINK;
    list->working[1] = NULL_LINK;
    list->unlinked[0] = NULL_LINK;
    list->unlinked[1] = NULL_LINK;
    list->unused[0] = &link_array[0];
    list->unused[1] = &link_array[1];
    // initialize all link pointers to point to the items
    // and initialize the next and previous links to UNUSED / NULL
    uint16_t i;
    uint8_t* item_ptr;
    item_ptr = item_array;
    for (i = 0; i < item_array_length; i++) {
        link_array[i].item_ptr = item_ptr;
        link_array[i].next = UNUSED_LINK;
        item_ptr += item_size;
    }
}

void List_SetSortFunction(list_t* list, uint8_t(*sort_fn)(void* a, void* b)) {
    list->sort_fn = sort_fn;
}

void List_SetIdentifyFunction(list_t* list,
        uint8_t(*identify_fn)(void* identifier, void* item)) {
    list->identify_fn = identify_fn;
}

void* List_AddAndLink(list_t* list, void* item) {
    // use add indirect to get a pointer to where to put the item
    list_link_t* link = NULL_LINK;
    link = GetUnusedLink(list);
    if (link == NULL_LINK) {
        List_Error(ERROR_NO_ROOM_IN_LIST);
        return 0;
    }
    // now we have a pointer to the item so move the data to the item in the list
    memcpy(link->item_ptr, item, list->item_size);
    // link into the list
    Link(list, link);
    UpdateWorkingLinks(list, link);
    return link->item_ptr;
}

void* List_Add(list_t* list, void* item) {
    void* item_ptr;
    // use add indirect to get a pointer to where to put the item
    item_ptr = List_AddIndirect(list);
    if (item_ptr == 0) {
        List_Error(ERROR_NO_ROOM_IN_LIST);
        return 0;
    }
    // now we have a pointer to the item so move the data to the item in the list
    memcpy(item_ptr, item, list->item_size);
    return item_ptr;
}

void* List_AddIndirect(list_t* list) {
    list_link_t* link = 0;
    link = GetUnusedLink(list);
    if (link == 0) {
        List_Error(ERROR_NO_ROOM_IN_LIST);
        return 0;
    }
    // update the pointers to the unlinked items
    // if the unlinked pointers are both used then indicate so by setting
    // unlinked[1] to PENDING_LINK
    BlockInterrupts();
    if (list->unlinked[1] == 0) {
        list->unlinked[1] = list->unlinked[0];
        list->unlinked[0] = link;
    } else list->unlinked[1] = PENDING_LINK;
    RestoreInterrupts();
    // update the working pointers so linking can happen fast
    UpdateWorkingLinks(list, link);
    return link->item_ptr;
}

void List_Link(list_t* list) {
    // if there aren't too many unlinked then we will have pointers to them all
    if (list->unlinked[1] != PENDING_LINK) {
        if (list->unlinked[0]) Link(list, list->unlinked[0]);
        if (list->unlinked[1]) Link(list, list->unlinked[1]);
    } else {
        // otherwise we need to search the entire list for items to link
        uint16_t i;
        for (i = 0; i < list->array_length; i++) {
            if (list->links[i].next == PENDING_LINK) {
                Link(list, &list->links[i]);
            }
        }
    }
    list->unlinked[0] = 0;
    list->unlinked[1] = 0;
}

void List_ResortFirst(list_t* list) {
    list_link_t* link;
    // remove from list
    link = list->first;
    list->first = link->next;
    if(list->first) list->first->previous = NULL_LINK;
    // decrement length since Link will increment length
    list->length--;
    Link(list, link);
    UpdateWorkingLinks(list, link);
}

void List_ResortLast(list_t* list) {
    list_link_t* link;
    // remove from list
    link = list->last;
    list->last = link->previous;
    if(list->last) list->last->next = NULL_LINK;
    // decrement length since Link will increment length
    list->length--;
    Link(list, link);
    UpdateWorkingLinks(list, link);
}

void List_LinkItem(list_t* list, void* item) {
    list_link_t* link;
    // try to find the item using the unlinked links
    link = list->unlinked[0];
    if(link) {
        if(link->item_ptr == item) {
            Link(list, link);
            BlockInterrupts();
            if(list->unlinked[1] != PENDING_LINK) {
                list->unlinked[0] = list->unlinked[1];
                list->unlinked[1] = 0;
            }
            RestoreInterrupts();
            return;
        }
        link = list->unlinked[1];
        if(link != PENDING_LINK && link != 0) {
            if(link->item_ptr == item) {
                Link(list, link);
                BlockInterrupts();
                if(list->unlinked[0] != PENDING_LINK)
                list->unlinked[1] = 0;
                RestoreInterrupts();
                return;
            }
        }
    }
    link = FindLinkByItem(list, item);
    if(link) {
        // if the link has not be unlinked then unlink
        if(link->next != LINK_IN_USE) Unlink(list, link);
        Link(list, link);
    }else List_Error(ERROR_ITEM_NOT_FOUND);
}

void* List_GetFirst(list_t* list) {
    return (list->first) ? (list->first->item_ptr) : 0;
}

void* List_GetLast(list_t* list) {
    return (list->last) ? (list->last->item_ptr) : 0;
}

void* List_GetNext(list_t* list, void* item) {
    list_link_t* link;
    link = FindLinkByItem(list, item);
    if(IsLinkValid(link->next)) return link->next->item_ptr;
    else {
        List_Error(ERROR_ITEM_NOT_FOUND);
        return 0;
    }
}

void* List_GetItem(list_t* list, void* identifier) {
    list_link_t* link;
    // make sure there is a identify function registered
    if(list->identify_fn == 0) return 0;
    // check the working links then traverse the list
    link = list->working[0];
    if(link) {
        if(link->next != PENDING_LINK && link->next != UNUSED_LINK) {
            if(list->identify_fn(identifier, link->item_ptr)) return link->item_ptr;
        }
    }
    link = list->working[1];
    if(link) {
        if(link->next != PENDING_LINK && link->next != UNUSED_LINK) {
            if(list->identify_fn(identifier, link->item_ptr)) return link->item_ptr;
        }
    }
    // the item was not one of the recent working links so traverse the list
    link = list->first;
    while(IsLinkValid(link)) {
        if(list->identify_fn(identifier, link->item_ptr)) {
            UpdateWorkingLinks(list, link);
            return link->item_ptr;
        }link = link->next;
    }
    return 0;
}

void List_RemoveFirst(list_t* list) {
    list_link_t* link;
    link = list->first;
    Unlink(list, link);
    link->next = UNUSED_LINK;
}

void List_RemoveLast(list_t* list) {
    list_link_t* link;
    link = list->last;
    Unlink(list, link);
    link->next = UNUSED_LINK;
}

void List_Remove(list_t* list, void* item) {
    list_link_t* link;
    link = FindLinkByItem(list, item);
    if(link) {
        Unlink(list, link);
        link->next = UNUSED_LINK;
    }else List_Error(ERROR_ITEM_NOT_FOUND);
}

void List_RemoveAll(list_t* list) {
    list->length = 0;
    list->first = NULL_LINK;
    list->last = NULL_LINK;
    list->working[0] = NULL_LINK;
    list->working[1] = NULL_LINK;
    list->unlinked[0] = NULL_LINK;
    list->unlinked[1] = NULL_LINK;
    list->unused[0] = &list->links[0];
    list->unused[1] = &list->links[1];
    // initialize all link pointers to point to the items
    // and initialize the next and previous links to UNUSED / NULL
    uint16_t i;
    for (i = 0; i < list->array_length; i++) {
        list->links[i].next = UNUSED_LINK;
    }
}

void List_UnlinkItem(list_t* list, void* item) {
    list_link_t* link;
    link = FindLinkByItem(list, item);
    if(link) {
        Unlink(list, link);
    }else List_Error(ERROR_ITEM_NOT_FOUND);
}

void List_UnlinkFirst(list_t* list) {
    list_link_t* link;
    link = list->first;
    if(link) {
        Unlink(list, link);
    }else List_Error(ERROR_ITEM_NOT_FOUND);
}

void List_UnlinkLast(list_t* list) {
    list_link_t* link;
    link = list->last;
    if(link) {
        Unlink(list, link);
    }else List_Error(ERROR_ITEM_NOT_FOUND);
}

void Link(list_t* list, list_link_t* link) {
    // if the list is empty then put this item on the front
    if(list->first == 0) {
        BlockInterrupts();
        list->first = link;
        list->last = link;
        link->next = NULL_LINK;
        link->previous = NULL_LINK;
        list->length++;
        RestoreInterrupts();
        return;
    }
    if(list->sort_fn) {
        list_link_t* current;
        current = list->first;
        // see if this task will be linked into the first position
        if(list->sort_fn(link->item_ptr, current->item_ptr)) {
            BlockInterrupts();
            list->first->previous = link;
            link->next = list->first;
            link->previous = NULL_LINK;
            list->first = link;
            list->length++;
            RestoreInterrupts();
            return;
        }
        while(current) {
            if(list->sort_fn(link->item_ptr, current->item_ptr)) {
                BlockInterrupts();
                link->previous = current->previous;
                link->next = current;
                current->previous->next = link;
                current->previous = link;
                list->length++;
                RestoreInterrupts();
                return;
            }
            current = current->next;
        }
    }
    // if there is no sort then link the item to the end (last) of the list
    // same if we traversed the entire list and didn't find where it went yet
    BlockInterrupts();
    link->previous = list->last;
    if(list->last) {
        list->last->next = link;
    }else list->first = link;
    list->last = link;
    link->next = NULL_LINK;
    list->length++;
    RestoreInterrupts();
}

void Unlink(list_t* list, list_link_t* link) {
    if(!IsLinkValid(link) || link->next == LINK_IN_USE) {
        List_Error(ERROR_INVALID_LINK);
        return;
    }
    UpdateWorkingLinks(list, link);
    BlockInterrupts();
    if(link == list->first) {
        list->first = link->next;
        if(list->first == NULL_LINK) {
            list->last = NULL_LINK;
            list->length = 0;
        }else {
            list->first->previous = NULL_LINK;
            list->length--;
        }
        link->next = LINK_IN_USE;
        RestoreInterrupts();
        return;
    }
    if(link == list->last) {
        list->last = link->previous;
        if(list->last == NULL_LINK) {
            list->first = NULL_LINK;
            list->length = 0;
        }else {
            list->last->next = NULL_LINK;
            list->length--;
        }
        link->next = LINK_IN_USE;
        RestoreInterrupts();
        return;
    }
    link->previous->next = link->next;
    link->next->previous = link->previous;
    link->next = LINK_IN_USE;
    list->length--;
    RestoreInterrupts();
    return;
}

list_link_t* FindLinkByItem(list_t* list, void* item) {
    list_link_t* link;
    // try searching the working links
    link = list->working[0];
    if(link) {
        if(link->item_ptr == item) {
            UpdateWorkingLinks(list, link);
            return link;
        }
    }
    link = list->working[1];
    if(link) {
        if(link->item_ptr == item) {
            UpdateWorkingLinks(list, link);
            return link;
        }
    }
    // calculate item link
    // index is ((item address) - (item array base)) / (item size)
    uint16_t index;
    /// @warning index calculation will break on systems that are not byte addressable
    index = ((uint8_t *)item - (uint8_t*)list->item_array) / list->item_size;
    if(index >= list->array_length) return 0;
    else return &list->links[index];
}

list_link_t* GetUnusedLink(list_t* list) {
    // block interrupts and find an available item slot
    list_link_t* link = 0;
    BlockInterrupts();
    if (list->unused[0] != 0) {
        link = list->unused[0];
        list->unused[0] = 0;
    } else if (list->unused[1] != 0) {
        link = list->unused[1];
        list->unused[1] = 0;
    }
    if (link == 0) link = FindUnusedLink(list);
    if (link == 0) {
        RestoreInterrupts();
        return 0;
    }
    link->next = PENDING_LINK;
    RestoreInterrupts();
    return link;
}

list_link_t* FindUnusedLink(list_t* list) {
    // initialize to 1 so the search starts at index 2 (remember 2 unused links
    // are exist at first)
    static uint16_t i = 1;
    uint16_t start;
    // start the search at the location after the last search ended
    start = ++i;
    // search from i (from the last found link + 1) to the end
    for (/*nothing here*/; i < list->array_length; i++) {
        if(list->links[i].next == UNUSED_LINK) return &list->links[i];
    }
    // search from 0 to start
    for (i = 0; i < start; i++) {
        if(list->links[i].next == UNUSED_LINK) return &list->links[i];
    }
    List_Error(ERROR_NO_ROOM_IN_LIST);
    return 0;
}
