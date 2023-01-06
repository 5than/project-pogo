import tkinter as tk
import json
import subprocess
from tkinter import messagebox

# Read the JSON file
with open("logins.json", "r") as f:
  data = json.load(f)

# Create a dictionary of usernames and passwords
credentials = {user["username"]: user["password"] for user in data}

# Create a window
window = tk.Tk()
window.title("Login System")
window.geometry("300x200")

# Create a function to verify the login credentials
def verify_login():
  # Read the username and password from the entry widgets
  username = username_entry.get()
  password = password_entry.get()
  
  # Check if the username and password match a valid username and password
  if username in credentials and credentials[username] == password:
    # If the login is successful, close the login window and open main.py
    window.destroy()
    subprocess.run(["python", "main.py"])
  else:
    # If the login is unsuccessful, show an error message
    messagebox.showerror("Error", "Invalid username or password")

# Create a label for the username
username_label = tk.Label(text="Username:")
username_label.pack()

# Create an entry widget for the username
username_entry = tk.Entry()
username_entry.pack()

# Create a label for the password
password_label = tk.Label(text="Password:")
password_label.pack()

# Create an entry widget for the password
password_entry = tk.Entry(show="*")
password_entry.pack()

# Create a login button
login_button = tk.Button(text="Login", command=verify_login)
login_button.pack()

# Run the main loop
window.mainloop()
