import tkinter as tk
from tkinter import messagebox

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Dummy credentials
    valid_username = "admin"
    valid_password = "12345"

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Function to toggle password visibility
def toggle_password():
    if check_var.get():
        entry_password.config(show="")  # Show password
    else:
        entry_password.config(show="*")  # Hide password

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x250")

# Create widgets
label_title = tk.Label(root, text="Login", font=("Arial", 16, "bold"))
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Password is hidden by default

# Show password checkbox
check_var = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(
    root, text="Show Password", variable=check_var, command=toggle_password
)

button_login = tk.Button(root, text="Login", command=validate_login)

# Arrange widgets in the window
label_title.pack(pady=10)
label_username.pack(pady=5)
entry_username.pack(pady=5)
label_password.pack(pady=5)
entry_password.pack(pady=5)
checkbox_show_password.pack(pady=5)
button_login.pack(pady=10)

# Start the event loop
root.mainloop()
