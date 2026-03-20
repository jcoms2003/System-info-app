import tkinter as tk
import psutil
import time

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = memory.used / (1024**3)  # GB
    memory_total = memory.total / (1024**3)  # GB
    
    temps = psutil.sensors_temperatures()
    cpu_temp = "N/A"
    if 'coretemp' in temps:
        cpu_temp = f"{temps['coretemp'][0].current}°C"
    elif 'cpu_thermal' in temps:
        cpu_temp = f"{temps['cpu_thermal'][0].current}°C"
    
    return f"CPU Usage: {cpu_percent}%\nMemory: {memory_used:.2f}GB / {memory_total:.2f}GB ({memory_percent}%)\nCPU Temp: {cpu_temp}"

def update_info():
    info_label.config(text=get_system_info())
    root.after(1000, update_info)  # Update every 5 seconds

root = tk.Tk()
root.title("System Monitor")

info_label = tk.Label(root, text="Loading...", font=("Arial", 12), justify=tk.LEFT)
info_label.pack(padx=20, pady=20)

update_info()
root.mainloop()