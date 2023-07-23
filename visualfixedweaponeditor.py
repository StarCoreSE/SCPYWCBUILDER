import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import re

# Root window
root = tk.Tk()
root.title("Fixed Weapon Editor")

# Function to read the current values from the configuration file
def read_current_values(file_path):
    # Open file and read the contents
    with open(file_path, 'r') as f:
        contents = f.read()

    # Find the values using regular expressions
    rate_of_fire = re.search(r'RateOfFire = (\d+)', contents)
    reload_time = re.search(r'ReloadTime = (\d+)', contents)
    deviate_shot_angle = re.search(r'DeviateShotAngle = ([\d.]+)', contents)

    # Update the slider variables with the found values
    if rate_of_fire:
        rate_of_fire_var.set(int(rate_of_fire.group(1)))
    else:
        messagebox.showwarning("Warning", "Rate of Fire value not found in the file.")
    if reload_time:
        reload_time_var.set(int(reload_time.group(1)))
    else:
        messagebox.showwarning("Warning", "Reload Time value not found in the file.")
    if deviate_shot_angle:
        deviate_shot_angle_var.set(deviate_shot_angle.group(1))
    else:
        messagebox.showwarning("Warning", "Deviate Shot Angle value not found in the file.")

# Function to validate decimal input in entry fields
def validate_decimal_input(var, index, value, action):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Variables to store values
rate_of_fire_var = tk.IntVar(value=500)
reload_time_var = tk.IntVar(value=360)
deviate_shot_angle_var = tk.StringVar(value='0.15')

# Function to open file selector and read the selected file
def open_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Fixed Weapon Config File", filetypes=(("CS files", "*.cs"), ("All files", "*.*")))
    if file_path:
        selected_file_path = file_path
        read_current_values(file_path)

        # Update text box
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('1.0', open(file_path).read())
        text.config(state='disabled')

# Button to open file selector
open_button = ttk.Button(root, text="Open Fixed Weapon Config File", command=open_file)
open_button.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

# Read current values from the default configuration file
default_file_path = 'testfixedweaponconfig.cs'
read_current_values(default_file_path)
selected_file_path = default_file_path

# String variables for label text
rate_of_fire_str = tk.StringVar(value=f'RateOfFire = {rate_of_fire_var.get()}')
reload_time_str = tk.StringVar(value=f'ReloadTime = {reload_time_var.get()}')
deviate_shot_angle_str = tk.StringVar(value=f'DeviateShotAngle = {deviate_shot_angle_var.get()}')

# Labels for sliders and deviate shot angle
rate_of_fire_label = tk.Label(root, textvariable=rate_of_fire_str)
reload_time_label = tk.Label(root, textvariable=reload_time_str)
deviate_shot_angle_label = tk.Label(root, textvariable=deviate_shot_angle_str)

# Slider widgets
rate_of_fire_slider = ttk.Scale(root, from_=1, to=1200, variable=rate_of_fire_var, orient=tk.HORIZONTAL)
reload_time_slider = ttk.Scale(root, from_=1, to=3600, variable=reload_time_var, orient=tk.HORIZONTAL)

# Deviate shot angle entry field
deviate_shot_angle_entry = ttk.Entry(root, textvariable=deviate_shot_angle_var, validate='key')
deviate_shot_angle_entry['validatecommand'] = (root.register(validate_decimal_input), '%v', '%i', '%P', '%d')

# Function to update labels when sliders change
def update_rate_of_fire(event):
    rate_of_fire_str.set(f'RateOfFire = {rate_of_fire_var.get()}')

def update_reload_time(event):
    reload_time_str.set(f'ReloadTime = {reload_time_var.get()}')

# Bind slider motion to update functions
rate_of_fire_slider.bind("<Motion>", update_rate_of_fire)
reload_time_slider.bind("<Motion>", update_reload_time)

# Function to increment slider by one using mouse wheel
def increment_slider(event):
    if event.delta > 0:
        event.widget.set(event.widget.get() + 1)
    elif event.delta < 0:
        event.widget.set(event.widget.get() - 1)

    # Update labels in real-time
    update_rate_of_fire(event)
    update_reload_time(event)

# Bind mouse wheel event to sliders
rate_of_fire_slider.bind("<MouseWheel>", increment_slider)
reload_time_slider.bind("<MouseWheel>", increment_slider)

# Pack labels, sliders, and entry fields using grid layout
rate_of_fire_label.grid(row=1, column=0, padx=10, pady=5)
rate_of_fire_slider.grid(row=2, column=0, padx=10, pady=5)

reload_time_label.grid(row=1, column=1, padx=10, pady=5)
reload_time_slider.grid(row=2, column=1, padx=10, pady=5)

deviate_shot_angle_label.grid(row=1, column=2, padx=10, pady=5)
deviate_shot_angle_entry.grid(row=2, column=2, padx=10, pady=5)

# Save button click handler
def save_config():
    # Get current values
    rate_of_fire = rate_of_fire_var.get()
    reload_time = reload_time_var.get()
    deviate_shot_angle = deviate_shot_angle_var.get()

    # Add the 'f' suffix to deviate_shot_angle
    deviate_shot_angle = f"{deviate_shot_angle}f"
    deviate_shot_angle_var.set(deviate_shot_angle)

    # Open file and modify
    with open(selected_file_path, 'r') as f:
        contents = re.sub(r'RateOfFire = \d+,', f'RateOfFire = {rate_of_fire},', f.read())
        contents = re.sub(r'ReloadTime = \d+,', f'ReloadTime = {reload_time},', contents)
        contents = re.sub(r'DeviateShotAngle = [\d.f]+,', f'DeviateShotAngle = {deviate_shot_angle},', contents)

    # Save changes
    with open(selected_file_path, 'w') as f:
        f.write(contents)

    # Update text box
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('1.0', open(selected_file_path).read())
    text.config(state='disabled')

# Save button
button = tk.Button(root, text="Save", command=save_config)
button.grid(row=3, column=0, columnspan=5, padx=10, pady=5)

# Text box
text = tk.Text(root)
text.grid(row=4, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")
text.insert('1.0', open(default_file_path).read())
text.config(state='disabled')

# Configure grid weights to make the text box expand when the window is resized
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.grid_rowconfigure(4, weight=1)

root.mainloop()
