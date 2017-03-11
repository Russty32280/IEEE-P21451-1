#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)

LEDADDRESS = 0x67

bus.write_byte_data(LEDADDRESS, 0x06, 0x01)
bus.write_byte_data(LEDADDRESS, 0x07, 0x01)
bus.write_byte_data(LEDADDRESS, 0x08, 0x01)
bus.write_byte_data(LEDADDRESS, 0x09, 0x01)
time.sleep(3)
bus.write_byte_data(LEDADDRESS, 0x06, 0x00)
bus.write_byte_data(LEDADDRESS, 0x07, 0x00)
bus.write_byte_data(LEDADDRESS, 0x08, 0x00)
bus.write_byte_data(LEDADDRESS, 0x09, 0x00)

