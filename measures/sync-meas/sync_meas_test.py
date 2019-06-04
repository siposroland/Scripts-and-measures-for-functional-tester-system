
import datetime as dt
import time
import os
import sys
import serial
import binascii
from serial import Serial
from time import mktime

baud = 115200

ser = serial.Serial('COM5', baud)
ser.flushInput()
ser.flushOutput()

def write_read(s, msg):
    s.write(msg)
    s.flush()
    line = s.readline()
    return line.encode('ascii')

def save_os_time():
    tim = dt.datetime.now()
    stamp = tim.timestamp()
    sec = int(((stamp / 1e4) % 1) * 1e4)
    msec = ((int((stamp % 1)*1e3)) / 1e3)
    os_time = (sec + msec)
    print ("OS Time: %.3f" % os_time)
    with open("measures.txt", "a+") as file:
        file.write(str(os_time))
        file.write("\n")

def save_main_time(times):
    timdt = mktime(times)
    #stamp = timdt.timestamp()
    sec = int(((timdt / 1e4) % 1) * 1e4)
    msec = ((int((timdt % 1)*1e3)) / 1e3)
    main_time = (sec + msec)
    print ("Main Time: %.3f" % main_time)
    with open("measures.txt", "a+") as file:
        file.write(str(main_time))
        file.write("\n")

print ("********** SYNC MEAS **********")
save_os_time()
msg = "*GETT$"
ans = write_read(ser, msg.encode('ascii'))
data = ans.decode("utf-8").split(",")
year = 0
month = 0
day = 0
hour = 0
min = 0
sec = 0
msec = 0
print (data[0])
if data[0] == 'TIME':
    if int(data[1]) < 10: 
        year = '0' + str(data[1]) 
    else:
        year = str(data[1]) 
    month = str(data[2])
    day = str(data[3])
    hour = str(data[4])
    min = str(data[5])
    sec = str(data[6])
    msec = str(data[7])
    timestamp = time.strptime(day + '/' + month + '/' + year + ' ' + hour +':' + min +':' + sec +'.' + msec, '%d/%m/%y %H:%M:%S.%f')
    save_main_time(timestamp)
print ("**********************************")




