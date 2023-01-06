import tkinter as tk
from tkinter import messagebox




# Create a window
window = tk.Tk()
window.title("Project Pogo")
window.geometry("300x200")

# Create a function to download the files
def download_files():
  # Show a message box asking the user to confirm the download
  result = messagebox.askyesno("Confirm Download", "Do you want to download the files for Project Pogo?")
  
  # If the user clicks "Yes", show a message saying the download was successful
  if result:
    messagebox.showinfo("Success", "The files for Project Pogo have been downloaded!")
  # If the user clicks "No", show a message saying the download was cancelled
  else:
    messagebox.showinfo("Cancelled", "The download was cancelled.")

# Create a download button
download_button = tk.Button(text=f"Download Files associated for {projectName}", command=download_files)
download_button.pack()

# Run the main loop
window.mainloop()
