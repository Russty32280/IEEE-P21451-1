/*
 * buffer_printf.c
 *
 *  Created on: Mar 11, 2014
 *      Author: Michael
 */
#include "system.h"
#ifndef _BUFFER_PRINTF_H_
#error "buffer_printf.h must be included in system.h"
#endif
#ifndef _BUFFER_H_
#error "include buffer.h in system.h and buffer.c must be in your project"
#endif

#include <stdarg.h>

void Push_printf(buffer_t * buf, char * str, ...) {
    // variable argument list type
    va_list vars;
    // initialize the variable argument list pointer by specifying the
    // input argument immediately preceding the variable list
    va_start(vars, str);
    Push_vprintf(buf, str, vars);
    va_end(vars);
}

void Push_vprintf(buffer_t * buf, char * str, va_list vars) {
    char escape = 0;
    while (*str != 0) {
        if (*str == '%' && !escape) {
            switch (*(str + 1)) {
                case 0:
                    str++;
                    continue;
                case 'b':
                    // Function declared in Paterson_midterm.h/.c
                    PushBinary16(buf, va_arg(vars, unsigned int));
                    str += 2;
                    continue;
                case 'c': // char
                    // to be implemented by everyone else
#ifdef __XC32__
                    Push(buf, va_arg(vars, int));
#else
                    Push(buf, va_arg(vars, char));
#endif
                    str += 2;
                    continue;
                case 'd':
                    // Capo
                    // use va_arg to ge the next variable of length int
                    Push_int16(buf, va_arg(vars, int));
                    str += 2;
                    continue;
                case 'e':
                case 'f':
                case 'g': // scientific notation of float
                    // Jehandad
                    PushFloat(buf, va_arg(vars, double));
                    str += 2;
                    continue;
                case 'l':
                    Push_int32(buf, va_arg(vars, int32_t));
                    str += 2;
                    continue;
                case 's': // string
                    // Cecere / Paterson
                    PushStr(buf, va_arg(vars, char *));
                    str += 2;
                    continue;
                case 'u':
                    // use va_arg to ge the next variable of length int
                    Push_uint16(buf, va_arg(vars, unsigned int));
                    str += 2;
                    continue;
                case 'x': // hex
                    // Jake
                    PushHex(buf, va_arg(vars, int));
                    str += 2;
                    continue;
                default:
                    // if the character following the % was not "special"
                    // then we will print the % and whatever follows it
                    break;
            }
        }
        //escape = (*str == '\\') ? 1 : 0;
        //Push(buf,*str++);
        if (*str == '\\' && *(str + 1) == '%') {
            str++;
            escape = 1;
        } else {
            Push(buf, *str++);
            escape = 0;
        }
    }

}

void Push_uint16(buffer_t * buf, uint16_t x) {
    char num[6];
    unsigned int i = 0;
    do {
        num[i] = (x % 10) + '0';
        x /= 10;
        i++;
    } while (x);
    do {
        Push(buf, num[--i]);
    } while (i);
}

void PushBinary16(buffer_t * buf, uint16_t x) {
    uint16_t i;
    for (i = 0; i < 16; i++) {
        Push(buf, (x & 0x0001) ? '1' : '0');
        x >>= 1;
    }
}

void Push_int16(buffer_t * buf, int16_t x) {
    if (x < 0) {
        Push(buf, '-');
        x = -x;
    }
    Push_uint16(buf, x);
}

void Push_int32(buffer_t * buf, int32_t x) {
    if (x < 0) {
        Push(buf, '-');
        x = -x;
    }
    Push_uint32(buf, x);
}

void Push_uint32(buffer_t * buf, uint32_t x) {
    char num[10];
    unsigned int i = 0;
    do {
        num[i] = (x % 10) + '0';
        x /= 10;
        i++;
    } while (x);
    do {
        Push(buf, num[--i]);
    } while (i);
}

void PushStr(buffer_t * buf, char * str) {
    do {
        Push(buf, *str);
    } while (*str++ != 0);
}

void PushHex(buffer_t *buf, uint16_t x) {
    volatile unsigned int y;
    char num[4];
    unsigned int i = 0;
    for (i = 0; i < 4; i++) {
        y = x - ((x >> 4) << 4); // x % 16
        num[i] = (y >= 10) ? (y + 0x37) : (y + 0x30);
        x >>= 4; // x / 16
    } //while(x);

    do {
        Push(buf, num[--i]);
    } while (i);
}

void PushFloat(buffer_t * buf, float x) {
    int i;
    long l;
    // for now just print 0.000 format
    i = x;
    Push_int16(buf, i);
    l = (x * 1000);
    l = l - i * 1000;
    Push(buf, '.');
    if (l < 100) Push(buf, '0');
    if (l < 10) Push(buf, '0');
    if (l == 0) Push(buf, '0');
    else Push_uint16(buf, l & 0xFFFF);
}
