
import datetime as dt
import time
import os
import sys
import serial
from serial import Serial

def stm_send(stm, text):
    stm.reset_input_buffer()
    stm.write(text)
    stm.flush()

print ("********** RTC SYNC **********")
baud = 115200

ser = serial.Serial('COM5', baud)

timeStart = dt.datetime.now()
ser.flushInput()
ser.flushOutput()

endFlag = 1
timeAct = dt.datetime.now()


msg = "*SYNC" + str(timeAct) + "$"
arr = bytes(msg, 'utf-8')
stm_send(ser, arr)

while (endFlag):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "DELAY" in bAscii:
			timeAct = dt.datetime.now()
			msg = "*DLYR" + str(timeAct) + "$"
			arr = bytes(msg, 'utf-8')
			stm_send(ser, arr)
			endFlag = 0
	ser.flushInput()
	ser.flushOutput()

print("Time synchronisation ok at %s." % str(timeAct))
print ("**********************************")




