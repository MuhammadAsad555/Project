import time
import threading
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from plyer import notification

def calculate_water_glasses(weight_kg):
    liters = weight_kg * 0.035
    glasses = round(liters / 0.25)
    return glasses

def remind_user(name):
    message = f"Hey {name}, drink water!"
    notification.notify(
        title="Drink Water Reminder",
        message=message,
        timeout=10
    )

def start_reminder():
    name = name_var.get().strip()
    try:
        weight = float(weight_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for weight.")
        return

    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return

    glasses_needed = calculate_water_glasses(weight)
    result_label.config(text=f"{name}, you should drink about {glasses_needed} glasses today.")

    # Start reminder thread
    def reminder_loop():
        while True:
            remind_user(name)
            time.sleep(60 * 60)  # 1 hour

    threading.Thread(target=reminder_loop, daemon=True).start()

# GUI Setup
app = Tk()
app.title("Hydration Reminder")
app.geometry("300x250")

Label(app, text="Enter your name:").pack(pady=5)
name_var = StringVar()
Entry(app, textvariable=name_var).pack(pady=5)

Label(app, text="Enter your weight (kg):").pack(pady=5)
weight_var = StringVar()
Entry(app, textvariable=weight_var).pack(pady=5)

Button(app, text="Start Reminder", command=start_reminder).pack(pady=10)

result_label = Label(app, text="", fg="blue")
result_label.pack(pady=10)

app.mainloop()
