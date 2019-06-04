
import datetime as dt
import time
import os
import sys
import serial
import binascii
from serial import Serial

baud = 115200
estimatedByteNum = (115200*0.8)
difference = 0

ser = serial.Serial('COM11', baud)
ser.flushInput()
ser.flushOutput()

filepath = time.strftime("%Y%m%d-%H%M%S") + ".txt"
wordsList = 0
numLines = 0
numWords = 0
numChars = 0

timeStart = dt.datetime.now()
timeEnd = dt.datetime.now() + dt.timedelta(0,1)
timeAct = dt.datetime.now()
file=open(filepath, "a+")
bytesToRead = 0
ser.flushInput()
ser.flushOutput()
while (timeAct < timeEnd):
	bytesToRead = 0
	bytesToRead = ser.inWaiting()
	if(bytesToRead > 0):
		buffer = ser.read(bytesToRead)
		file.write(buffer.decode("ascii"))
		ser.flushInput()
		ser.flushOutput()
	timeAct = dt.datetime.now()
	
file.close()
		
with open(filepath, "r") as file:
	for line in file:
		wordsList = line.split()
		numLines += 1
		numWords += len(wordsList)
		numChars += len(line)

difference = (numChars - estimatedByteNum)

with open("measures.txt", "a+") as file:
	file.write(str(numChars))
	file.write("\n")
	
print(difference)
print ("********** STATISTICS **********")
print ("Lines: %i\nWords: %i\nCharacters: %i" % (numLines, numWords, numChars))
print("Check byte num: %i" % (os.path.getsize(filepath) - numLines))
print("Time between start and end: %s" % str(timeAct - timeStart))
print ("**********************************")




