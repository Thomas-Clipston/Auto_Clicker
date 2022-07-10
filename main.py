import tkinter as tk
from click import command
import startloc

window = tk.Tk()
window.title("Autlcicker 1.0")
window.geometry("210x210")
window.resizable(False,False)

#using global varibles because tkinter command returns are not assebile
x = 0 
y = 0

def main():
    #check buttons varibles for checking and unchecking
    sec_var = tk.IntVar()

    #basic input
    entry_time_label = tk.Label(text="#Clicks",font=("Ariel",10))
    Entry_time = tk.Entry()

    entry_interval_label = tk.Label(text="Interval",font=("Ariel",10))
    Entry_interval = tk.Entry()

    time_label = tk.Label(text="Auto_Clicker",font=("Ariel",10))
    #Buttons for seconds or for minutes 
    seconds = tk.Checkbutton(text="Unchecked for seconds, checked\nfor minutes", variable=sec_var,justify="left")

    #Buttons for placement/start of mouse during autoclicker
    Location = tk.Button(text="Set Location",command= lambda: startloc.location(window))
    start = tk.Button(text = "Start",command= lambda: startloc.start_clicker(window,Entry_time,Entry_interval,sec_var))



    #Placeing the objects down
    time_label.grid(row=0,column=0,pady=10,padx=60,sticky="W")
    
    Entry_time.grid(row=1,column=0,sticky="W",padx=60)
    entry_time_label.grid(row=1,column=0,sticky="W")
    
    seconds.grid(row=3,column=0,sticky="W")

    entry_interval_label.grid(row=2,column=0,sticky="W",pady=10)
    Entry_interval.grid(row=2,column=0,sticky="W",padx=60)

    Location.grid(row=4,column=0,sticky="W",padx=80,pady=10)
    start.grid(row=4,column=0,sticky="W",padx=40)

    
    #Main loop and constant running functions
    
    window.mainloop()
       

if __name__ == "__main__":
    main()