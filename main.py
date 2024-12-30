import logging
import tkinter as tk
from tkinter import messagebox

from camera import take_picture
from storage import EventStorage

# Configure the logging settings
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# User has submitted a new event
def on_submit():
    event_type = event_type_entry.get()
    image_filename = image_filename_entry.get()

    event_storage.save_to_file(event_type, image_filename)
    messagebox.showinfo("Submitted", f"Event Type: {event_type}\nImage Filename: {image_filename}")
    logger.info(f"Event was added") # do not include PII in the logs

def on_picture_requested():
    result = take_picture()
    if result:
        image_filename_entry.insert(0, result)

# Initialise application
logger.info("Application started")
event_storage = EventStorage()
event_storage.read_existing_events()

# Create the main window
root = tk.Tk()
root.title("Simple Security System UI")

# Event Type Label and Entry
event_type_label = tk.Label(root, text="Event Type:")
event_type_label.grid(row=0, column=0, padx=10, pady=10)

event_type_entry = tk.Entry(root, width=50)
event_type_entry.grid(row=0, column=1, padx=10, pady=10)

# Image Filename Label and Entry
image_filename_label = tk.Label(root, text="Image Filename:")
image_filename_label.grid(row=2, column=0, padx=10, pady=10)

image_filename_entry = tk.Entry(root, width=50)
image_filename_entry.grid(row=2, column=1, padx=10, pady=10)

# Take picture button
picture_button = tk.Button(root, text="Take Picture - press 's' in popup", command=on_picture_requested)
picture_button.grid(row=1, column=0, columnspan=2, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
