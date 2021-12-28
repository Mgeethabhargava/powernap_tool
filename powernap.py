from time import strftime
from tkinter import *
from tkinter import filedialog
import datetime
import time
from pygame import mixer
from tkinter import messagebox as mb

root = Tk()
root.title("Power-Napper Notification")
root.geometry("900x900")
root.config(background = "white")
global label_file_explorer

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    # print(alarmtime)
    if filename:
        if alarmtime!="::":
            alarmclock(alarmtime)
    else:
        mb.showwarning('Warning', 'ringtone is not selected')

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        # print(time_now)
        if time_now==alarmtime:
            Wakeup = Label(root, font=("arial", 20, "bold"), text="wakeup! wakeup! wakeup", bg="DodgerBlue2", fg="white").grid(row=6, columnspan=3)
            # print("wakeup!")
            mixer.init()
            mixer.music.load(filename)
            mixer.music.play()
            break

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
    if filename:
        pass
    else:
        mb.showwarning('Warning', 'ringtone is not selected')
        # mb.showinfo('No', 'Quit has been cancelled')

def stopalarm():
    if mb.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    # print("successfully stopped")


# Create a File Explorer label
greet = Label(root,font = ("arial", 20, "bold"),text = "Please select a ringtone for alarm").grid(row = 1, columnspan = 3)
greet = Label(root,font = ("arial", 20, "bold"),text = "and type time as hh:mm:ss").grid(row = 2, columnspan = 3)
hrs = StringVar()
mins = StringVar()
secs = StringVar()
hrbtn = Entry(root, textvariable=hrs,width=5,font = ('arial', 15, 'bold'))
hrbtn.grid(row=5,column=0)
minbtn=Entry(root, textvariable=mins,width=5,font = ("arial", 15, "bold")).grid(row=5,column=1)
secbtn= Entry(root, textvariable=secs, width=5,font = ("arial", 15, "bold")).grid(row=5,column=2)
button_explore = Button(root,text = "Browse Files",command = browseFiles).grid(row=8,column=1)
setbtn = Button(root, text="Set Alarm", command=setalarm, bg="DodgerBlue2", fg="white",font = ("arial", 15, "bold")).grid(row=15,column=0)
stopbtn = Button(root, text="Stop Alarm", command= stopalarm, bg="DodgerBlue1", fg="white",font = ("arial", 15, "bold")).grid(row=15, column=2, columnspan=2)
# timeleft = Label(root, font=('arial', 20, 'bold'))
# timeleft.grid()
center_window(500, 400)
root.protocol("WM_DELETE_WINDOW", stopalarm)
root.mainloop()
