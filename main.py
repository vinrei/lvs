import tkinter as tk
from tkinter import messagebox

def on_submit():
    event_type = event_type_entry.get()
    image_filename = image_filename_entry.get()

    # Display the inputs (or you can process them as needed)
    messagebox.showinfo("Submitted", f"Event Type: {event_type}\nImage Filename: {image_filename}")

# Create the main window
root = tk.Tk()
root.title("Simple Security System UI")

# Event Type Label and Entry
event_type_label = tk.Label(root, text="Event Type:")
event_type_label.grid(row=0, column=0, padx=10, pady=10)

event_type_entry = tk.Entry(root, width=30)
event_type_entry.grid(row=0, column=1, padx=10, pady=10)

# Image Filename Label and Entry
image_filename_label = tk.Label(root, text="Image Filename:")
image_filename_label.grid(row=1, column=0, padx=10, pady=10)

image_filename_entry = tk.Entry(root, width=30)
image_filename_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
