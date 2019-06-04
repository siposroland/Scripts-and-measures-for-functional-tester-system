
import datetime as dt
import matplotlib.animation as animation
import time
import threading
import tkinter
from tkinter import *
from tkinter import ttk
import serial
from serial import Serial
from random import randint
import numpy as np
import matplotlib.pyplot as plt
gui = Tk()
gui.title("Functional Tester Interface")
s = serial.Serial('COM11', 115200)
text = Text(width = 65, height = 5)


import subprocess
import webbrowser
import sys

def doNothing():
    print("nothing")

def create_window():
    window = Tk()    


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)




def callback():
    print ("click!")

def create_window():
    window = tk.Toplevel(gui)

	
frame = Frame(gui, bg='black', width=350, height=40)
frame.pack(fill='x')
v = StringVar()
button1 = Button(frame, text='MANUAL TRIGGER', command = "create_window")
button1.pack(side='left', padx=0)
button2 = Button(frame, text='SET ANALOG', command = "create_window")
button2.pack(side='left', padx=0)
button3 = Button(frame, text='SET DIGITAL')
button3.pack(side='left', padx=0)
button4 = Button(frame, text='TOGGLE TIMER', command = "create_window")
button4.pack(side='left', padx=0)
button5 = Button(frame, text='ADD TRIGGER EVENT', command = "create_window")
button5.pack(side='left', padx=0)	
w = Canvas(gui, width=500, height=300)
w.pack()

actual = 200
actual2 = 200
actual3 = 200
time = 220
def get_data():
    """This function serves the purpose of collecting data from the serial object and storing 
    the filtered data into a global variable.
    The function has been put into a thread since the serial event is a blocking function.
    """
    global actual
    global actual2
    global actual3
    global time
    global w
    while(1):   
        try:
            serial_data = s.readline()
            data = serial_data.decode("utf-8").split(" ")
            #print (data)
            if data[0] == 'I0' or data[0] == 'O0':
                if data[1] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p0p0,fill=pin)
                if data[2] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p0p1,fill=pin)
                if data[3] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p0p2,fill=pin)
                if data[4] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p0p3,fill=pin)
            if data[0] == 'I1' or data[0] == 'O1':
                if data[1] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p1p0,fill=pin)
                if data[2] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p1p1,fill=pin)
                if data[3] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p1p2,fill=pin)
                if data[4] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p1p3,fill=pin)
            if data[0] == 'I2' or data[0] == 'O2':
                if data[1] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p2p0,fill=pin)
                if data[2] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p2p1,fill=pin)
                if data[3] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p2p2,fill=pin)
                if data[4] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p2p3,fill=pin)
            if data[0] == 'I3' or data[0] == 'O3':
                if data[1] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p3p0,fill=pin)
                if data[2] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p3p1,fill=pin)
                if data[3] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p3p2,fill=pin)
                if data[4] == '1':			
                    pin = "green"
                else:
                    pin = "red"
                w.itemconfigure(p3p3,fill=pin)
            if data[0] == 'ADC0:':
                act = round((((1022+randint(0, 10))/2048)*3.3), 1)
                w.itemconfigure(adc0, text = str(act) + " V")
                step3 = int(round((-1*int(act)/2048)*50))+ 80
                moved3 = step3 - actual3
                actual3 = actual3 + moved3
                w.move(ov3,1,moved3)
            if data[2] == 'ADC1:':
                w.itemconfigure(adc1, text = str(round(((int(data[3])/2048)*3.3),2)) + " V")
                step2 = int(round((-1*int(data[3])/2048)*50))+ 80
                moved2 = step2 - actual2
                actual2 = actual2 + moved2
                w.move(ov2,1,moved2)
            if data[4] == 'DAC0:':
                w.itemconfigure(dac0, text = str(round(((int(data[5])/2048)*3.3),2)) + " V")
                step = int(round((-1*int(data[5])/2048)*50))+ 80
                moved = step - actual
                actual = actual + moved
                w.move(ov,1,moved)
                time = time + 1
            if (time == (220 + 230)):
                time = 220
                w.move(ov,-230,0)
                w.move(ov2,-230,0)
                w.move(ov3,-230,0)
                #w.coords(line, scaled)
                #for i in ov:
                    #w.move(ov[50], 10, 10)   #  for x += 10
                    #idx = i - 41
                    #print (ov[199])
                    #if (idx < 199):
                     #   w.coords(ov[idx], w.coords(ov[idx] + 1))
                #w.coords(ov[199], start_width+idx, data[5]/100, start_width+5+idx,data[5]/100+1)
				
			
			
        
        except TypeError:
            pass

start_width = 220
end_width = 450
start_height = 180
end_height = 20
w.create_line(220,180,450,180, width=2)
w.create_line(220,180,450,180, width=2)
w.create_line(220,180,220,20,  width=2)
w.create_line(215,25,220,20,  width=2)
w.create_text(270,40,fill="green", font="Consolas 10 bold", text="DAC0 channel")
w.create_text(270,30,fill="blue", font="Consolas 10 bold", text="ADC1 channel")
w.create_text(270,20,fill="red", font="Consolas 10 bold", text="ADC0 channel")
w.create_line(220,130,450,130, width=2, dash=(2, 4))
w.create_text(200,130,fill="black",font="Consolas 10 bold", text="0V")
w.create_text(180,35,fill="black",font="Consolas 10 bold", text="Voltage")
w.create_line(225,25,220,20,  width=2)
w.create_line(445,175,450,180, width=2)
w.create_line(445,185,450,180, width=2)
w.create_line(220,75,450,75, width=2, dash=(2, 4))
w.create_text(200,75,fill="black",font="Consolas 10 bold", text="3.3V")
w.create_text(445,200,fill="black",font="Consolas 10 bold", text="Time")


actual = start_height-80
actual2 = start_height-80
actual3 = start_height-50
ov = w.create_oval(200, start_height-30, 200+5, start_height-35, fill="green")
ov2 = w.create_oval(200, start_height-30, 200+5, start_height-35, fill="blue")
ov3 = w.create_oval(200, start_height-30, 200+5, start_height-35, fill="red")
#for i in range(50):	
#    ov.append (w.create_oval(start_width+i, start_height-30, start_width+2*i, start_height-31, fill="green"))
	


#line = w.create_line(scaled2, fill='black', smooth=1)			
#for xs,ys in scaled:
#	w.create_oval(x-6,y-6c,x+6,y+6, width=1,outline='black', fill='SkyBlue2')

width = 50
height = 30
size = 10
add=20
w.create_text(width+32,height-15,fill="black",font="Consolas 12 bold", text="DIGITAL IO Module")
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT0")
p0p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p0p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p0p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p0p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

height = 50
width = 50
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT1")
p1p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p1p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p1p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p1p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

height = 70
width = 50
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT2")
p2p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p2p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p2p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p2p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

height = 90
width = 50
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT3")
p3p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p3p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p3p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p3p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

height = 110
width = 50
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT4")
p4p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p4p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p4p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p4p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

height = 130
width = 50
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="PORT5")
p5p0 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p5p1 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p5p2 = w.create_rectangle(width, height, width+size, height+size, fill="red")
width = width + add
p5p3 = w.create_rectangle(width, height, width+size, height+size, fill="red")

width = 50
height = 180
size = 10
add=20
w.create_text(width+32,height-15,fill="black",font="Consolas 12 bold", text="ANALOG IO Module")

width = 50
height = 180
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="ADC0")
adc0 = w.create_text(width+25,height + 5,fill="black",font="Consolas 10 bold", text="0")

width = 50
height = 200
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="ADC1")
adc1 = w.create_text(width+25,height + 5,fill="black",font="Consolas 10 bold", text="0")

width = 50
height = 220
w.create_text(width-25,height + 5,fill="black",font="Consolas 10 bold", text="DAC0")
dac0 = w.create_text(width+25,height + 5,fill="black",font="Consolas 10 bold", text="0")
dac0Type = w.create_text(width+90,height + 5,fill="black",font="Consolas 10 bold", text="sinus")



gui.geometry('480x300')
t1 = threading.Thread(target = get_data)
t1.daemon = True
t1.start()
gui.mainloop()






