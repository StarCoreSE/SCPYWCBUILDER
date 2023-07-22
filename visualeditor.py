import tkinter as tk
from tkinter import ttk
import os
import re

# Root window
root = tk.Tk()
root.title("Ammo Editor")

# Function to read the current values from the configuration file
def read_current_values():
    # Open file and read the contents
    with open('testconfig.cs', 'r') as f:
        contents = f.read()

    # Find the values using regular expressions
    damage = re.search(r'BaseDamage = (\d+)', contents)
    max_traj = re.search(r'MaxTrajectory = (\d+)', contents)
    desired_speed = re.search(r'DesiredSpeed = (\d+)', contents)
    color = re.search(r'Color = Color\(red: (\d+), green: (\d+), blue: (\w+), alpha: (\d+)\)', contents)

    # Update the slider variables with the found values
    if damage:
        damage_var.set(int(damage.group(1)))
    if max_traj:
        max_traj_var.set(int(max_traj.group(1)))
    if desired_speed:
        desired_speed_var.set(int(desired_speed.group(1)))
    if color:
        color_red_var.set(color.group(1))
        color_green_var.set(color.group(2))
        color_blue_var.set(color.group(3))
        color_alpha_var.set(color.group(4))

# Function to validate integer input in entry fields
def validate_integer_input(var, index, value, action):
    if value.isdigit() or (value == "" and action == "1"):  # Allow empty string when deleting
        return True
    return False

# Function to update the color preview
def update_color_preview():
    red = min(max(int(color_red_var.get()), 0), 255)
    green = min(max(int(color_green_var.get()), 0), 255)
    blue = min(max(int(color_blue_var.get()), 0), 255)
    color_preview_canvas.config(bg=f'#{red:02x}{green:02x}{blue:02x}')


# Variables to store values
damage_var = tk.IntVar(value=100)
max_traj_var = tk.IntVar(value=300)
desired_speed_var = tk.IntVar(value=50)
color_red_var = tk.StringVar(value='5')
color_green_var = tk.StringVar(value='2')
color_blue_var = tk.StringVar(value='1')
color_alpha_var = tk.StringVar(value='1')

# Read current values from the configuration file
read_current_values()

# String variables for label text
damage_str = tk.StringVar(value=f'Damage = {damage_var.get()}')
max_traj_str = tk.StringVar(value=f'Max Trajectory = {max_traj_var.get()}')
desired_speed_str = tk.StringVar(value=f'Desired Speed = {desired_speed_var.get()}')
color_str = tk.StringVar(value=f'Color = Color(red: {color_red_var.get()}, green: {color_green_var.get()}, blue: {color_blue_var.get()}, alpha: {color_alpha_var.get()})')

# Labels for sliders and color
damage_label = tk.Label(root, textvariable=damage_str)
max_traj_label = tk.Label(root, textvariable=max_traj_str)
desired_speed_label = tk.Label(root, textvariable=desired_speed_str)
color_label = tk.Label(root, textvariable=color_str)

# Slider widgets
damage_slider = ttk.Scale(root, from_=1, to=10000, variable=damage_var, orient=tk.HORIZONTAL)
max_traj_slider = ttk.Scale(root, from_=1, to=10000, variable=max_traj_var, orient=tk.HORIZONTAL)
desired_speed_slider = ttk.Scale(root, from_=1, to=10000, variable=desired_speed_var, orient=tk.HORIZONTAL)

# Color entry boxes
color_entry_label = tk.Label(root, text="R, G, B:")
color_red_entry = ttk.Entry(root, textvariable=color_red_var, width=5, validate='key')
color_red_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_red_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_red_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_green_entry = ttk.Entry(root, textvariable=color_green_var, width=5, validate='key')
color_green_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_green_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_green_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_blue_entry = ttk.Entry(root, textvariable=color_blue_var, width=5, validate='key')
color_blue_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_blue_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_blue_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_alpha_label = tk.Label(root, text="Alpha:")
color_alpha_entry = ttk.Entry(root, textvariable=color_alpha_var, width=5, validate='key')
color_alpha_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_alpha_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_alpha_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

# Function to update labels when sliders change
def update_damage(event):
    damage_str.set(f'Damage = {damage_var.get()}')

def update_max_traj(event):
    max_traj_str.set(f'Max Trajectory = {max_traj_var.get()}')

def update_desired_speed(event):
    desired_speed_str.set(f'Desired Speed = {desired_speed_var.get()}')

# Bind slider motion to update functions
damage_slider.bind("<ButtonRelease>", update_damage)
max_traj_slider.bind("<ButtonRelease>", update_max_traj)
desired_speed_slider.bind("<ButtonRelease>", update_desired_speed)

# Pack labels and sliders using grid layout
damage_label.grid(row=0, column=0, padx=10, pady=5)
damage_slider.grid(row=1, column=0, padx=10, pady=5)

max_traj_label.grid(row=0, column=1, padx=10, pady=5)
max_traj_slider.grid(row=1, column=1, padx=10, pady=5)

desired_speed_label.grid(row=0, column=2, padx=10, pady=5)
desired_speed_slider.grid(row=1, column=2, padx=10, pady=5)

color_label.grid(row=0, column=3, padx=10, pady=5)
color_entry_label.grid(row=1, column=3, padx=10, pady=5)
color_red_entry.grid(row=1, column=4, padx=2, pady=5)
color_green_entry.grid(row=1, column=5, padx=2, pady=5)
color_blue_entry.grid(row=1, column=6, padx=2, pady=5)

color_alpha_label.grid(row=2, column=3, padx=10, pady=5)
color_alpha_entry.grid(row=2, column=4, padx=2, pady=5)

# Color preview canvas
color_preview_label = tk.Label(root, text="Color Preview:")
color_preview_canvas = tk.Canvas(root, width=30, height=30, bg='white')
color_preview_label.grid(row=2, column=5, padx=10, pady=5)
color_preview_canvas.grid(row=2, column=6, padx=2, pady=5)

# Save button click handler
def save_config():

    # Get current values
    damage = damage_var.get()
    max_traj = max_traj_var.get()
    desired_speed = desired_speed_var.get()
    color_red = color_red_var.get()
    color_green = color_green_var.get()
    color_blue = color_blue_var.get()
    color_alpha = color_alpha_var.get()

    # Format the color string
    color_str.set(f'Color = Color(red: {color_red}, green: {color_green}, blue: {color_blue}, alpha: {color_alpha})')

    # Open file and modify
    with open('testconfig.cs', 'r') as f:
        contents = re.sub('BaseDamage = [0-9]*,', f'BaseDamage = {damage},', f.read())
        contents = re.sub('MaxTrajectory = [0-9]*,', f'MaxTrajectory = {max_traj},', contents)
        contents = re.sub('DesiredSpeed = [0-9]*,', f'DesiredSpeed = {desired_speed},', contents)
        contents = re.sub('Color = Color\(red: [0-9a-z]*,', f'Color = Color(red: {color_red},', contents)
        contents = re.sub('green: [0-9a-z]*,', f'green: {color_green},', contents)
        contents = re.sub('blue: [0-9a-z]*,', f'blue: {color_blue},', contents)
        contents = re.sub('alpha: [0-9]*\),', f'alpha: {color_alpha}),', contents)

    # Save changes
    with open('testconfig.cs', 'w') as f:
        f.write(contents)

    # Update text box
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('1.0', open('testconfig.cs').read())
    text.config(state='disabled')


# Save button
button = tk.Button(root, text="Save", command=save_config)
button.grid(row=3, column=0, columnspan=7, padx=10, pady=5)

# Text box
text = tk.Text(root)
text.grid(row=4, column=0, columnspan=7, padx=10, pady=5, sticky="nsew")
text.insert('1.0', open('testconfig.cs').read())
text.config(state='disabled')

# Configure grid weights to make the text box expand when the window is resized
for i in range(7):
    root.grid_columnconfigure(i, weight=1)

root.grid_rowconfigure(4, weight=1)

root.mainloop()