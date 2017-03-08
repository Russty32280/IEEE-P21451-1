import smbus
import time
bus = smbus.SMBus(1)
TempHumidAddress = 0x40

def TempRead():
	rawtemp = bus.read_word_data(TempHumidAddress,0xE3)
	print int(rawtemp)*175.72/65536
	temp = (175.72*rawtemp)/65536 - 46.85
	return temp

while True:
	Temperature = TempRead()
	print Temperature
	time.sleep(1)
