import tkinter as tk
from tkinter import messagebox
import threading
import time

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder Application")
        self.root.geometry("300x200")

        # Variables to store reminder time and message
        self.reminder_message = tk.StringVar()
        self.reminder_interval = tk.IntVar()

        # UI Elements
        tk.Label(root, text="Reminder Message:").pack(pady=5)
        tk.Entry(root, textvariable=self.reminder_message).pack(pady=5)

        tk.Label(root, text="Interval (seconds):").pack(pady=5)
        tk.Entry(root, textvariable=self.reminder_interval).pack(pady=5)

        tk.Button(root, text="Start Reminder", command=self.start_reminder).pack(pady=10)
        tk.Button(root, text="Quit", command=root.quit).pack(pady=5)

    def show_reminder(self):
        while self.running:
            messagebox.showinfo("Reminder", self.reminder_message.get())
            time.sleep(self.reminder_interval.get())

    def start_reminder(self):
        if self.reminder_message.get() and self.reminder_interval.get() > 0:
            self.running = True
            reminder_thread = threading.Thread(target=self.show_reminder, daemon=True)
            reminder_thread.start()
        else:
            messagebox.showerror("Error", "Please enter a valid message and interval.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
