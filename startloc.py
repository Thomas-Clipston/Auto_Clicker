import mouse
from time import sleep
import tkinter as tk

#Moves mouse to correct position and begins the process of clicking on the specific intervals
def start_clicker(window,Entry_box, Interval_Entrybox,sec_var):
    stopper = Entry_box.get()
    window.withdraw()
    Interval = Interval_Entrybox.get()
    i = 0
    if (Interval != "" and stopper != ""):
        while i < int(stopper):
            if(sec_var.get() == 1):
                sleep(int(Interval)*60)
                mouse.move(x,y)
                mouse.click('left')
                i = i+1
            else:
                sleep(int(Interval))
                mouse.move(x,y)
                mouse.click('left')
                i = i+1
    window.deiconify()


#finds the x and y cordinates of the mouses current position
def location(window):
    global x,y
    window.withdraw()
    while 1>0:
        if mouse.is_pressed("left") == True:
            window.deiconify()
            pos = list(mouse.get_position())
            x = pos[0]
            y = pos[1]
            return None


