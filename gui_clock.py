from tkinter import *
import time
from playsound import playsound

root = Tk()
root.title("Digital Clock with Timer")
root.geometry("600x400")

t = 0

def set_timer():
    global t
    t = t + int(e1.get()) * 60
    return t

def countdown():
    global t
    if t > 0:
        label1.config(text=t)
        t = t -1
        label1.after(1000, countdown)
        time.sleep(.05)
    elif t == 0:
        print("end")
        label1.config(text="BREAK TIME")
        return playsound('tng_chirp_clean.mp3')

def clock():
    date = time.strftime("%x")
    day = time.strftime("%a")
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    clock_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    date_label.config(text=day + " " + date)
    clock_label.after(1000, clock)


clock_label = Label(root, text="", font="Helvetica, 56", fg="red", bg="black")
clock_label.pack(pady=20)

date_label = Label(root, text="", font="Helvetica, 42", fg="white", bg="black")
date_label.pack(pady=20)

label1 = Label(root, font="Helvetica, 32")
label1.pack()

e1 = Entry(root, textvariable="helvetica")
e1.pack()

b1 = Button(root, text="Set Timer", width=20, command=set_timer)
b1.pack()

b2 = Button(root, text="Start", width=20, command=countdown)
b2.pack()

clock()

root.mainloop()
