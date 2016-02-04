#include "system.h"
#ifndef _ITEMBUFFER_H_
#error "Please include itemBuffer.h in system.h"
#endif

bool PushItem(item_buffer_t *buffer, uint16_t *data) {
	BlockInterrupts();
	// calculate the size available in the buffer and make sure there is enough room for the item
	// if not then abort and return false
    uint16_t sizeAvailable = buffer->buffer_end - buffer->buffer_start + 1 - (buffer->size * buffer->item_size);
	if(sizeAvailable >= buffer->item_size ) {
		// push data onto rear location and increment rear
		int i;
		for(i = 0; i < buffer->item_size; i++){
			*buffer->rear++ = *(data + i);
			// check to make sure rear isn't past the end of the buffer
			if(buffer->rear > buffer->buffer_end) buffer->rear = buffer->buffer_start;
		}
		buffer->size++;

		if(buffer->Callback) buffer->Callback(buffer);
	}else {
		RestoreInterrupts();
		return false;
	}

	RestoreInterrupts();
	return true;
}

void PopItem(item_buffer_t *buffer, uint16_t *data) {
	BlockInterrupts();
	int i;
	if(buffer->size == 0) { RestoreInterrupts(); return; }
	for(i = 0; i < buffer->item_size; i++){
		*data++ = *buffer->front;
		buffer->front++;
		if(buffer->front > buffer->buffer_end) buffer->front = buffer->buffer_start;
	}
	buffer->size--;
	RestoreInterrupts();
}

uint16_t ItemBufferGetSize(item_buffer_t *buffer) {
	return buffer->size;
}

void ItemBufferInit(item_buffer_t *buffer, uint16_t *data_array, uint16_t max_size, uint8_t item_size) {
	buffer->buffer_start = data_array;
	buffer->front = data_array;
	buffer->rear = data_array;
	buffer->buffer_end = data_array + (max_size * item_size) - 1;
	buffer->size = 0;
	buffer->item_size = item_size;
	buffer->Callback = 0;
}

void ItemBufferSetCallback(item_buffer_t * buffer, void (*Callback)(item_buffer_t * buffer)) {
	buffer->Callback = (void (*)(void *))Callback; // cast callback to void pointer
}

void ItemBufferClearCallback(item_buffer_t * buffer) { buffer->Callback = 0; }
