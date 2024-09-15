import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

reminders = {}

def show_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_str = cal.formatmonth(year, month)
    text_area.delete(1.0, tk.END)  
    text_area.insert(tk.INSERT, cal_str)

def add_reminder():
    date = reminder_date.get()
    note = reminder_note.get()
    if date and note:
        reminders[date] = note
        messagebox.showinfo("Reminder Set", f"Reminder set for {date}: {note}")
    else:
        messagebox.showwarning("Input Error", "Please enter both date and reminder note.")

def show_reminders():
    reminder_list.delete(0, tk.END)  
    for date, note in reminders.items():
        reminder_list.insert(tk.END, f"{date}: {note}")


root = tk.Tk()
root.title("Calendar and Reminder App")

text_area = tk.Text(root, height=10, width=40)
text_area.grid(row=0, column=0, padx=10, pady=10)

# Date and note entry
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.W, padx=10)
reminder_date = tk.Entry(root)
reminder_date.grid(row=1, column=1, padx=10)

tk.Label(root, text="Reminder Note:").grid(row=2, column=0, sticky=tk.W, padx=10)
reminder_note = tk.Entry(root)
reminder_note.grid(row=2, column=1, padx=10)

# Add reminder button
add_button = tk.Button(root, text="Add Reminder", command=add_reminder)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Show reminders button
show_button = tk.Button(root, text="Show Reminders", command=show_reminders)
show_button.grid(row=4, column=0, columnspan=2, pady=10)

# Reminder list display
reminder_list = tk.Listbox(root, width=40, height=10)
reminder_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Set the current month's calendar
now = datetime.now()
show_calendar(now.year, now.month)

# Run the application
root.mainloop()
