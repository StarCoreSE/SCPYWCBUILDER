import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import re

# Root window
root = tk.Tk()
root.title("Weapon Editor")
root.geometry("600x400")

selected_file_path = ""
weapon_mode = "Fixed"  # Default mode is "Fixed"

def read_current_values(file_path):
    # Open file and read the contents
    with open(file_path, 'r') as f:
        contents = f.read()

    # Check if the file contains "WeaponDefinition"
    if "new WeaponDefinition" not in contents:
        messagebox.showwarning("Warning", "The selected file is not a valid weapon file.")
        return

    # Check if the config file has AzimuthPartId = "None"
    is_fixed_weapon = "AzimuthPartId = \"None\"" in contents

    # Update the weapon mode label based on the config type
    if is_fixed_weapon:
        set_fixed_mode()
    else:
        set_turret_mode()

    # Find the values using regular expressions
    rate_of_fire = re.search(r'RateOfFire = (\d+)', contents)
    reload_time = re.search(r'ReloadTime = (\d+)', contents)
    deviate_shot_angle = re.search(r'DeviateShotAngle = ([\d.]+)', contents)

    # Update the slider variables with the found values
    if rate_of_fire:
        rate_of_fire_var.set(int(rate_of_fire.group(1)))
    if reload_time:
        reload_time_var.set(int(reload_time.group(1)))
    if deviate_shot_angle:
        deviate_shot_angle_var.set(deviate_shot_angle.group(1))

    # Update the mode label text and color
    mode_label.config(text="Weapon Mode: Fixed Weapon Config" if is_fixed_weapon else "Weapon Mode: Turret Weapon Config", foreground="red" if is_fixed_weapon else "blue")

def set_fixed_mode():
    global weapon_mode
    weapon_mode = "Fixed"
    mode_label.config(text="Weapon Mode: Fixed", foreground="red")
    rate_of_fire_slider.config(from_=1, to=3600)
    reload_time_slider.config(from_=1, to=3600)
    deviate_shot_angle_entry.config(validate='key')
    # Remove the RotateRate and ElevateRate widgets from the GUI
    rotate_rate_label.grid_remove()
    elevate_rate_label.grid_remove()
    rotate_rate_entry.grid_remove()
    elevate_rate_entry.grid_remove()

def set_turret_mode():
    global weapon_mode
    weapon_mode = "Turret"
    mode_label.config(text="Weapon Mode: Turret", foreground="blue")
    rate_of_fire_slider.config(from_=1, to=3600)  # Customize the range as needed
    reload_time_slider.config(from_=1, to=3600)  # Customize the range as needed
    deviate_shot_angle_entry.config(validate='key', validatecommand=(root.register(validate_decimal_input), '%v', '%i', '%P', '%d'))
    # Add the RotateRate and ElevateRate widgets back to the GUI with padding
    rotate_rate_label.grid(row=5, column=0, padx=10, pady=5)
    elevate_rate_label.grid(row=5, column=1, padx=10, pady=5)
    rotate_rate_entry.grid(row=6, column=0, padx=10, pady=5)
    elevate_rate_entry.grid(row=6, column=1, padx=10, pady=5)



# Function to validate decimal input in entry fields
def validate_decimal_input(var, index, value, action):
    try:
        float(value)
        return True
    except ValueError:
        return False

def switch_weapon_mode():
    if weapon_mode == "Fixed":
        set_turret_mode()
    else:
        set_fixed_mode()

# Toggle button to switch between Fixed and Turret modes
toggle_button = ttk.Button(root, text="Switch Mode", command=lambda: switch_weapon_mode())
toggle_button.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

# Label to display the current weapon mode
mode_label = ttk.Label(root, text="Weapon Mode: Fixed", foreground="black")
mode_label.grid(row=1, column=0, columnspan=5, padx=10, pady=5)


# Variables to store values
rate_of_fire_var = tk.IntVar(value=1)
reload_time_var = tk.IntVar(value=1)
deviate_shot_angle_var = tk.StringVar(value=1)


# Variables to store values
rotate_rate_var = tk.StringVar(value="0.005f")
elevate_rate_var = tk.StringVar(value="0.005f")

# Insert an additional row between the labels and the entry fields for RotateRate and ElevateRate
tk.Label(root).grid(row=4)  # Empty label for padding


# Labels for RotateRate and ElevateRate
rotate_rate_label = tk.Label(root, text="RotateRate:")
elevate_rate_label = tk.Label(root, text="ElevateRate:")

# Entry fields for RotateRate and ElevateRate
rotate_rate_entry = ttk.Entry(root, textvariable=rotate_rate_var, validate='key')
elevate_rate_entry = ttk.Entry(root, textvariable=elevate_rate_var, validate='key')
rotate_rate_entry['validatecommand'] = elevate_rate_entry['validatecommand'] = (root.register(validate_decimal_input), '%v', '%i', '%P', '%d')


# Function to open file selector and read the selected file
def open_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Fixed Weapon Config File", filetypes=(("CS files", "*.cs"), ("All files", "*.*")))
    if file_path:
        selected_file_path = file_path

        # Check if the file is a valid weapon file
        with open(file_path, 'r') as f:
            contents = f.read()
            if "new WeaponDefinition" not in contents or "WeaponDefinition" not in contents:
                messagebox.showwarning("Warning", "The selected file is not a valid weapon file.")
                return

        read_current_values(file_path)

        # Update text box
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('1.0', open(file_path).read())
        text.config(state='disabled')


# Button to open file selector
open_button = ttk.Button(root, text="Open Weapon Config File", command=open_file)
open_button.grid(row=0, column=0, columnspan=5, padx=10, pady=5)



# String variables for label text
rate_of_fire_str = tk.StringVar(value=f'RateOfFire = {rate_of_fire_var.get()}')
reload_time_str = tk.StringVar(value=f'ReloadTime = {reload_time_var.get()}')
deviate_shot_angle_str = tk.StringVar(value=f'DeviateShotAngle = {deviate_shot_angle_var.get()}')
rotate_rate_str = tk.StringVar(value=f'RotateRate = {rotate_rate_var.get()}')
elevate_rate_str = tk.StringVar(value=f'ElevateRate = {elevate_rate_var.get()}')



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

def update_deviate_shot_angle_label(event=None):
    deviate_shot_angle_str.set(f'DeviateShotAngle = {deviate_shot_angle_var.get()}')

def update_rotate_rate_label(event=None):
    rotate_rate_str.set(f'RotateRate = {rotate_rate_var.get()}')

def update_elevate_rate_label(event=None):
    elevate_rate_str.set(f'ElevateRate = {elevate_rate_var.get()}')

rotate_rate_entry.bind("<FocusOut>", update_rotate_rate_label)
elevate_rate_entry.bind("<FocusOut>", update_elevate_rate_label)



# Bind events to update labels
rate_of_fire_slider.bind("<Motion>", update_rate_of_fire)
reload_time_slider.bind("<Motion>", update_reload_time)
deviate_shot_angle_entry.bind("<FocusOut>", update_deviate_shot_angle_label)

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
rate_of_fire_label.grid(row=2, column=0, padx=10, pady=5)
rate_of_fire_slider.grid(row=3, column=0, padx=10, pady=5)

reload_time_label.grid(row=2, column=1, padx=10, pady=5)
reload_time_slider.grid(row=3, column=1, padx=10, pady=5)

deviate_shot_angle_label.grid(row=2, column=2, padx=10, pady=5)
deviate_shot_angle_entry.grid(row=3, column=2, padx=10, pady=5)

def save_config():
    # Get current values
    rate_of_fire = rate_of_fire_var.get()
    reload_time = reload_time_var.get()
    deviate_shot_angle = deviate_shot_angle_var.get()
    rotate_rate = rotate_rate_var.get()
    elevate_rate = elevate_rate_var.get()

    # Add the 'f' suffix to deviate_shot_angle, rotate_rate, and elevate_rate if they don't have one
    if not deviate_shot_angle.endswith("f"):
        deviate_shot_angle = f"{deviate_shot_angle}f"
    if not rotate_rate.endswith("f"):
        rotate_rate = f"{rotate_rate}f"
    if not elevate_rate.endswith("f"):
        elevate_rate = f"{elevate_rate}f"

    deviate_shot_angle_var.set(deviate_shot_angle)
    rotate_rate_var.set(rotate_rate)
    elevate_rate_var.set(elevate_rate)

    # Open file and modify
    with open(selected_file_path, 'r') as f:
        contents = re.sub(r'DeviateShotAngle = [\d.f]+,', f'DeviateShotAngle = {deviate_shot_angle},', f.read())
        contents = re.sub(r'RotateRate = [\d.f]+,', f'RotateRate = {rotate_rate},', contents)
        contents = re.sub(r'ElevateRate = [\d.f]+,', f'ElevateRate = {elevate_rate},', contents)

    # Save changes
    with open(selected_file_path, 'w') as f:
        f.write(contents)

    # Update DeviateShotAngle, RotateRate, and ElevateRate labels
    update_deviate_shot_angle_label()
    update_rotate_rate_label()
    update_elevate_rate_label()

    # Update text box
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('1.0', open(selected_file_path).read())
    text.config(state='disabled')


# Save button
button = tk.Button(root, text="Save", command=save_config)
button.grid(row=8, column=1, columnspan=1, padx=0, pady=0)  # Span 2 columns instead of 3, align to the right

# Text box
text = tk.Text(root)
text.grid(row=9, column=0, columnspan=3, padx=10, pady=5)  # Span 2 columns instead of 3
if selected_file_path:
    text.insert('1.0', open(selected_file_path).read())
text.config(state='disabled')

# Configure grid weights to make the text box expand when the window is resized
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()