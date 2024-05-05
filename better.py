from tkinter import Tk, StringVar, Spinbox, Button, messagebox, Frame
import time
 
stop_countdown = False
def countdowntimer():
    global stop_countdown
    try:
        userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        messagebox.showerror("Error", "Invalid Input")
        return
    reset_btn.config(state="disabled")
    hourbox.config(state="disabled")
    minutebox.config(state="disabled")
    secondbox.config(state="disabled")
    while userinput > -1:
        if stop_countdown:
            break
        mins, secs = divmod(userinput, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
 
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
 
        root.update()
        time.sleep(1)
 
        if userinput == 0:
            messagebox.showinfo("Countdown Timer", "Time's up!")
            reset_btn.config(state="normal")
            hourbox.config(state="normal")
            minutebox.config(state="normal")
            secondbox.config(state="normal")
        userinput -= 1
 
def stop_timer():
    global stop_countdown
    stop_countdown = True
    reset_btn.config(state="normal")
    hourbox.config(state="normal")
    minutebox.config(state="normal")
    secondbox.config(state="normal")
 
def reset_timer():
    global stop_countdown
    hour.set("00")
    minute.set("00")
    second.set("00")
 
root = Tk()
root.geometry("400x300")
root.title("Countdown Timer")
root.config(bg="#345")
 
frame = Frame(root)
frame.pack(expand=True)
 
hour = StringVar()
minute = StringVar()
second = StringVar()
 
hour.set("00")
minute.set("00")
second.set("00")
 
hourbox = Spinbox(frame, from_=0, to=23, width=3, font=("Arial", 18), textvariable=hour, disabledbackground="grey", disabledforeground="black")
minutebox = Spinbox(frame, from_=0, to=59, width=3, font=("Arial", 18), textvariable=minute, disabledbackground="grey", disabledforeground="black")
secondbox = Spinbox(frame, from_=0, to=59, width=3, font=("Arial", 18), textvariable=second, disabledbackground="grey", disabledforeground="black")
 
hourbox.grid(row=0, column=0, padx=10, pady=10)
minutebox.grid(row=0, column=1, padx=10, pady=10)
secondbox.grid(row=0, column=2, padx=10, pady=10)
 
start_btn = Button(frame, text="Start Countdown", command=countdowntimer)
start_btn.grid(row=1, column=0, padx=10, pady=10)
 
stop_btn = Button(frame, text="Stop Countdown", command=stop_timer)
stop_btn.grid(row=1, column=1, padx=10, pady=10)
 
reset_btn = Button(frame, text="Reset Countdown", command=reset_timer)
reset_btn.grid(row=1, column=2, padx=10, pady=10)
 
root.mainloop()