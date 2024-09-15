import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
from playsound import playsound

def check_alarm():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time.get():
            play_alarm()
            break
        time.sleep(1)

def play_alarm():
    playsound(alarm_tone.get())
    snooze_option = messagebox.askyesno("Alarm", "Do you want to snooze?")
    if snooze_option:
        time.sleep(300)  
        playsound(alarm_tone.get())

def set_alarm():
    alarm_thread = threading.Thread(target=check_alarm)
    alarm_thread.start()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.get()} with tone {alarm_tone.get()}")

root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Alarm Time (HH:MM:SS):").grid(row=0, column=0, padx=10, pady=10)
alarm_time = tk.Entry(root)
alarm_time.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Alarm Tone (File Path):").grid(row=1, column=0, padx=10, pady=10)
alarm_tone = tk.Entry(root)
alarm_tone.grid(row=1, column=1, padx=10, pady=10)

set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
