import tkinter as tk
from tkinter import ttk

# Main Dashboard Window
root = tk.Tk()
root.title("Pi-top ATV Dashboard")
root.geometry("800x480")  # Size of the Pi-top screen

# Frame for Engine Stats
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=0, column=0)

# Engine RPM Label
rpm_label = ttk.Label(frame1, text="Engine RPM: 0", font=("Helvetica", 18))
rpm_label.grid(row=0, column=0, pady=10)

# Engine Temperature Label
temp_label = ttk.Label(frame1, text="Engine Temperature: 0°C", font=("Helvetica", 18))
temp_label.grid(row=1, column=0, pady=10)

# Control Buttons
def crank_engine():
    # This would call the GPIO control script to start the engine
    print("Cranking Engine...")

crank_button = ttk.Button(frame1, text="Crank Engine", command=crank_engine)
crank_button.grid(row=2, column=0, pady=20)

# Start the Dashboard
root.mainloop()
