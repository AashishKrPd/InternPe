# importing required modules
from tkinter import Tk, Label, PhotoImage, Frame
from time import strftime
from os import path

# Getting Relative path for exe file 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)

# Creating Root window 
root = Tk()

# Setting up title, background and dimension
root.title("Indian Clock - (GMT + 5:30)")
root.config(background="black")
root.geometry("700x300")

# Adding Icon on top left of title
ico = PhotoImage(file=resource_path('clock.png'))
root.iconphoto(False, ico) 

# Creating a new Frame inside root window
frame1 = Frame(root, width=200, height=100, bg="lightblue")
frame1.grid(row=0, column=0, padx=50, pady=50)

# variable to hold the color for AM/PM 
color = "red"

def time():
    """
    takes no argument and extract hr, min, sec and AM/PM and update it to labels
    """
    stringTime = strftime("%H %M %S %p")
    hr, min, sec, ap = tuple(stringTime.split())
    
    # conveting from 24-hr format to 12-hr format and updating color of AM/PM
    if int(hr)>12:
        hr = str(int(hr)-12) #if 13-12 = 1
        if len(hr) == 1:
            hr='0'+hr # 1 to 01
        color = "red"
    else:
        color = "green"
    
    # Updating label to display correct time 
    h.config(text=hr)
    m.config(text=min)
    s.config(text=sec)
    a.config(text=" "+ap, foreground=color)
    
    # after each 1000ms=1s call time funtion 
    a.after(1000, time) 
    

# Label that hold value for hour
h = Label(frame1, font=('ds-digital', 80), background="black", foreground="cyan")
h.grid(row=1, column=1)


# Label that hold value for minute
m = Label(frame1, font=('ds-digital', 80), background="black", foreground="cyan")
m.grid(row=1, column=3)

# Label that hold value for second
s = Label(frame1, font=('ds-digital', 80), background="black", foreground="cyan")
s.grid(row=1, column=5)

# Label that hold value for AM/PM
a = Label(frame1, font=('ds-digital', 80), background="black", foreground=color)
a.grid(row=1, column=6)

# add colons (:) in between hr and min
fc = Label(frame1, text=":", font=('ds-digital', 80), background="black", foreground="brown")
fc.grid(row=1, column=2)

sc = Label(frame1, text=":", font=('ds-digital', 80), background="black", foreground="brown")
sc.grid(row=1, column=4)

# caling time function for the first time 
time()

# make sure the frame move and be in center of the windows and running loop
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop()

