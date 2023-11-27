from customtkinter import *
import playsound
import time
from PIL import Image, ImageTk

app = CTk()
app.title("Timer")
app.geometry("400x600")
app.resizable(False,False)

heading= CTkLabel(app,text="Timer App", font=("Helvetica" ,30 ), text_color="#ea3458")
heading.pack(pady=10)

CTkLabel(app, text="Current Time:", font=("Helvetica" ,25 ), text_color="white" ).place(x=65, y=70)

def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    ct.configure(text=clock_time)
    ct.after(1000, clock)

ct = CTkLabel(app, text="", font=("Helvetica", 25))
ct.place(x=220, y=70)
clock()

hrs = StringVar()
CTkEntry(app, textvariable=hrs, width=70, font=("Helvetica", 50)).place(x=30, y=155)
hrs.set("00")

min = StringVar()
CTkEntry(app, textvariable=min, width=70, font=("Helvetica", 50)).place(x=150, y=155)
min.set("00")


secs = StringVar()
CTkEntry(app, textvariable=secs, width=70, font=("Helvetica", 50)).place(x=270, y=155)
secs.set("00")

ho = CTkLabel(app, text="Hours", font=("Helvetica", 12)).place(x=30, y=220)
mi = CTkLabel(app, text="Mins", font=("Helvetica", 12)).place(x=150, y=220)
se = CTkLabel(app, text="Secs", font=("Helvetica", 12)).place(x=270, y=220)



def timer():
    times = int(hrs.get())*3600 + int(min.get())*60+int(secs.get())

    while times > -1:
        minute, second = (times//60, times %60)

        hour = 0
        if minute>60:
            hour,minute = (minute//60, minute%60)

        secs.set(second)
        min.set(minute)
        hrs.set(hour)


        app.update()
        time.sleep(1)

        if times == 0:
            playsound.playsound("Ringtone.mp3")
            secs.set("00")
            min.set("00")
            hrs.set("00")

        times -= 1


def brush():
    hrs.set("00")
    min.set("02")
    secs.set("00")

def face():
    hrs.set("00")
    min.set("15")
    secs.set("00")

def meditate():
    hrs.set("00")
    min.set("10")
    secs.set("00")

def cancel():
    hrs.set("00")
    min.set("00")
    secs.set("00")
    

image_button = CTkButton(app, text="Brush\n00:02:00",font=("Helvetica", 15), fg_color="#000", corner_radius=50, width=60,command=brush)
button = CTkButton(app, text="Face Mask\n00:15:00",font=("Helvetica", 15), fg_color="#000", corner_radius=50, width=60, command=face)
btn = CTkButton(app, text="Meditate\n00:10:00",font=("Helvetica", 15), fg_color="#000", corner_radius=50, width=60,command=meditate )
image_button.place(x=35, y=300)
button.place(x=155, y=300)
btn.place(x=275, y=300)

button = CTkButton(app, text="Start", fg_color="#ea3458", width=150, height=40, font=("Helvetica", 20), command=timer)

button2 = CTkButton(app, text="Cancel", fg_color="#ea3458", width=150, height=40, font=("Helvetica", 20), command=cancel)
button2.pack(side=BOTTOM)
button.pack(padx=5, pady=30, side=BOTTOM)
app.mainloop()