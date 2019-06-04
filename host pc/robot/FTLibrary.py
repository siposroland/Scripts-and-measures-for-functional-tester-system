
import os
import sys
import serial
from serial import Serial

def stm_send(stm, text):
    stm.reset_input_buffer()
    stm.write(text)
    stm.flush()

def hub_is_connected:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*MHUB$")
	while (1): 
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "HUB1" in bAscii:
			return True
		if "HUB0" in bAscii:
			return False
	ser.flushInput()
	ser.flushOutput()

def	digital_io_is_connected:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*MDIO$")
	while (1):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "DIO1" in bAscii:
			return True
		if "DIO0" in bAscii:
			return False
	ser.flushInput()
	ser.flushOutput()

def	analog_io_is_connected:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*MAIO$")
	while (1):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "AIO1" in bAscii:
			return True
		if "AIO0" in bAscii:
			return False
	ser.flushInput()
	ser.flushOutput()

def	analog_io_is_connected:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*MAIO$")
	while (1):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "AIO1" in bAscii:
			return True
		if "AIO0" in bAscii:
			return False
	ser.flushInput()
	ser.flushOutput()

def	data_is_ok:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*DDAT$")
	while (1):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		bAscii = buffer.decode("ascii")
		if "P0" in bAscii:
			return True
		if "*" in bAscii:
			return False
	ser.flushInput()
	ser.flushOutput()

def	enable_timer:
	ser = serial.Serial('COM5', 115200)
	stm_send(ser, "*MTIMEN$")
	return True
