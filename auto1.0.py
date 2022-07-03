from time import sleep
import tkinter as tk
import mouse
from tkinter import ttk



window = tk.Tk()
window.title("Autlcicker 1.0")
window.geometry("200x200")
window.resizable(False,False)

#using global varibles because tkinter command returns are not assebile
x = 0 
y = 0

#finds the x and y cordinates of the mouses current position
def location():
    window.withdraw()
    global x,y
    while 1>0:
        if mouse.is_pressed("left") == True:
            window.deiconify()
            pos = list(mouse.get_position())
            x = pos[0]
            y = pos[1]
            return None
            
#Moves mouse to correct position and begins the process of clicking on the specific intervals
def start_clicker(Entry_box, Interval_Entrybox):
    stopper = Entry_box.get()
    Interval = Interval_Entrybox.get()
    i = 0
    while i < int(stopper):
        sleep(int(Interval))
        mouse.move(x,y)
        mouse.click('left')
        i = i+1
        



def main():
    #basic input
    entry_time_label = tk.Label(text="Time",font=("Ariel",10))
    Entry_time = tk.Entry()

    entry_interval_label = tk.Label(text="Interval",font=("Ariel",10))
    Entry_interval = tk.Entry()

    time_label = tk.Label(text="Auto_Clicker",font=("Ariel",10))
    #Buttons for seconds or for minutes
    seconds = tk.Checkbutton(text="Seconds")
    minutes = tk.Checkbutton(text="Minutes")
    #Buttons for placement/start of mouse during autoclicker
    Location = tk.Button(text="Set Location",command=location)
    start = tk.Button(text = "Start",command= lambda: start_clicker(Entry_time,Entry_interval))



    #Placeing the objects down

    time_label.grid(row=0,column=0,pady=10,padx=60,sticky="W")
    
    Entry_time.grid(row=1,column=0,sticky="W",padx=60)
    entry_time_label.grid(row=1,column=0,sticky="W")
    
    minutes.grid(row=2,column=0,pady=10,sticky="W",padx=80)
    seconds.grid(row=2,column=0,pady=10,sticky="W")

    entry_interval_label.grid(row=3,column=0,sticky="W")
    Entry_interval.grid(row=3,column=0,sticky="W",padx=60)

    Location.grid(row=4,column=0,sticky="W",pady=20,padx=80)
    start.grid(row=4,column=0,sticky="W",pady=20,padx=40)

    window.mainloop()
       

if __name__ == "__main__":
    main()