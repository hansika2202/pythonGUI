import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 48), bg="black", fg="white")
label.pack(pady=20)

update_time()
root.mainloop()