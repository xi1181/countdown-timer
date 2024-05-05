from tkinter import Tk, StringVar, Entry, Button, messagebox
import time

def countdowntimer():
    try:
        user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning("Warning", "Invalid Input!")
        return
    while user_input > -1:
        mins = user_input // 60
        secs = user_input % 60
        hours = 0
        if mins > 60:
            hours = mins// 60
            mins = mins % 60

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if user_input == 0:
            messagebox.showinfo("Time Countdown", "Time Over")
        user_input -= 1
root = Tk()
root.geometry("400x300")
root.title("Countdown timer")
root.config(bg = '#345')

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")
hour_box = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = hour)
mins_box = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = minute)
secs_box = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = second)
hour_box.place(x=130, y=20)
mins_box.place(x=180, y=20)
secs_box.place(x=230, y=20)
btn = Button(root, text = "Start Countdown", command = countdowntimer)
btn.place(x=150, y=120)
root.mainloop()